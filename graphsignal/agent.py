import logging
import sys
import time
import uuid
import hashlib
import importlib
import socket
import contextvars
import importlib.abc

from graphsignal import version
from graphsignal.uploader import Uploader
from graphsignal.metrics import MetricStore
from graphsignal.logs import LogStore
from graphsignal.proto import signals_pb2
from graphsignal.samplers.random_samples import RandomSampler
from graphsignal.samplers.latency_outliers import LatencyOutlierSampler
from graphsignal.samplers.missing_values import MissingValueSampler
from graphsignal.proto_utils import parse_semver

logger = logging.getLogger('graphsignal')


class GraphsignalTracerLogHandler(logging.Handler):
    def __init__(self, agent):
        super().__init__()
        self._agent = agent  

    def emit(self, record):
        try:
            log_tags = {'deployment': self._agent.deployment}
            if self._agent.hostname:
                log_tags['hostname'] = self._agent.hostname
            if self._agent.tags is not None:
                log_tags.update(self._agent.tags)

            exception = None
            if record.exc_info and isinstance(record.exc_info, tuple):
                exception = self.format(record)

            self._agent.log_store().log_tracer_message(
                tags=log_tags,
                level=record.levelname,
                message=record.getMessage(),
                exception=exception)
        except Exception:
            pass


RECORDER_SPECS = {
    '(default)': [
        ('graphsignal.recorders.cprofile_recorder', 'CProfileRecorder'),
        ('graphsignal.recorders.process_recorder', 'ProcessRecorder'),
        ('graphsignal.recorders.nvml_recorder', 'NVMLRecorder')],
    'torch': [
        ('graphsignal.recorders.pytorch_recorder', 'PyTorchRecorder'),
        ('graphsignal.recorders.kineto_recorder', 'KinetoRecorder')],
    'yappi': [('graphsignal.recorders.yappi_recorder', 'YappiRecorder')],
    'tensorflow': [('graphsignal.recorders.tensorflow_recorder', 'TensorFlowRecorder')],
    'jax': [('graphsignal.recorders.jax_recorder', 'JAXRecorder')],
    'onnxruntime': [('graphsignal.recorders.onnxruntime_recorder', 'ONNXRuntimeRecorder')],
    'deepspeed': [('graphsignal.recorders.deepspeed_recorder', 'DeepSpeedRecorder')],
    'openai': [('graphsignal.recorders.openai_recorder', 'OpenAIRecorder')],
    'langchain': [('graphsignal.recorders.langchain_recorder', 'LangChainRecorder')],
    'banana_dev': [('graphsignal.recorders.banana_recorder', 'BananaRecorder')],
    'autogpt.prompt': [('graphsignal.recorders.autogpt_recorder', 'AutoGPTRecorder')]
}

class SourceLoaderWrapper(importlib.abc.SourceLoader):
    def __init__(self, loader, agent):
        self._loader = loader
        self._agent = agent

    def create_module(self, spec):
        return self._loader.create_module(spec)

    def exec_module(self, module):
        self._loader.exec_module(module)
        try:
            self._agent.initialize_recorders_for_module(module.__name__)
        except Exception:
            logger.error('Error initializing recorders for module %s', module.__name__, exc_info=True)

    def load_module(self, fullname):
        self._loader.load_module(fullname)

    def get_data(self, path):
        return self._loader.get_data(path)

    def get_filename(self, fullname):
        return self._loader.get_filename(fullname)


class SupportedModuleFinder(importlib.abc.MetaPathFinder):
    def __init__(self, agent):
        self._agent = agent
        self._disabled = False

    def find_spec(self, fullname, path=None, target=None):
        if self._disabled:
            return None

        if fullname in RECORDER_SPECS:
            try:
                self._disabled = True
                spec = importlib.util.find_spec(fullname)
                if spec:
                    loader = importlib.util.find_spec(fullname).loader
                    if loader is not None and isinstance(loader, importlib.abc.SourceLoader):
                        return importlib.util.spec_from_loader(fullname, SourceLoaderWrapper(loader, self._agent))
            except Exception:
                logger.error('Error patching spec for module %s', fullname, exc_info=True)
            finally:
                self._disabled = False

        return None


class Agent:
    METRIC_READ_INTERVAL_SEC = 10
    METRIC_UPLOAD_INTERVAL_SEC = 20
    LOG_UPLOAD_INTERVAL_SEC = 20

    def __init__(
            self, 
            api_key=None, 
            api_url=None, 
            deployment=None, 
            tags=None, 
            auto_instrument=True, 
            record_data_samples=False, 
            upload_on_shutdown=True, 
            debug_mode=False):
        if debug_mode:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.WARNING)

        self.api_key = api_key
        if api_url:
            self.api_url = api_url
        else:
            self.api_url = 'https://signal-api.graphsignal.com'
        self.deployment = deployment
        self.tags = tags
        self.context_tags = None
        self.auto_instrument = auto_instrument
        self.record_data_samples = record_data_samples
        self.upload_on_shutdown = upload_on_shutdown
        self.debug_mode = debug_mode
        self.hostname = None
        try:
            self.hostname = socket.gethostname()
        except BaseException:
            logger.debug('Error reading hostname', exc_info=True)

        self._tracer_log_handler = None
        self._uploader = None
        self._metric_store = None
        self._log_store = None
        self._recorders = None
        self._random_samplers = None
        self._lo_samplers = None
        self._mv_samplers = None

        self._process_start_ms = int(time.time() * 1e3)

        self.last_metric_read_ts = 0
        self.last_metric_upload_ts = int(self._process_start_ms / 1e3)
        self.last_log_upload_ts = int(self._process_start_ms / 1e3)

    def setup(self):
        self._uploader = Uploader()
        self._uploader.setup()
        self._metric_store = MetricStore()
        self._log_store = LogStore()
        self._recorders = {}
        self._random_samplers = {}
        self._lo_samplers = {}
        self._mv_samplers = {}

        # initialize tracer log handler
        self._tracer_log_handler = GraphsignalTracerLogHandler(self)
        logger.addHandler(self._tracer_log_handler)

        # initialize context tags variable
        self.context_tags = contextvars.ContextVar('graphsignal_context_tags', default={})

        # initialize module wrappers
        self._module_finder = SupportedModuleFinder(self)
        sys.meta_path.insert(0, self._module_finder)

        # initialize default recorders and recorders for already loaded modules
        for module_name in RECORDER_SPECS.keys():
            if module_name == '(default)' or module_name in sys.modules:
                self.initialize_recorders_for_module(module_name)

    def shutdown(self):
        if self.upload_on_shutdown:
            if self._metric_store.has_unexported():
                metrics = self._metric_store.export()
                for metric in metrics:
                    self._uploader.upload_metric(metric)

            if self._log_store.has_unexported():
                entries = self._log_store.export()
                for entry in entries:
                    self._uploader.upload_log_entry(entry)

        for recorder in self.recorders():
            recorder.shutdown()

        self.upload(block=True)

        self._recorders = None
        self._metric_store = None
        self._log_store = None
        self._lo_samplers = None
        self._random_samplers = None
        self._mv_samplers = None
        self._uploader = None

        self.context_tags.set({})
        self.context_tags = None

        # remove module wrappers
        if self._module_finder in sys.meta_path:
            sys.meta_path.remove(self._module_finder)
        self._module_finder = None

        # remove tracer log handler
        logger.removeHandler(self._tracer_log_handler)
        self._tracer_log_handler = None

    def uploader(self):
        return self._uploader

    def initialize_recorders_for_module(self, module_name):
        # check already loaded
        if module_name in self._recorders:
            return

        # check if supported
        if module_name not in RECORDER_SPECS:
            return

        # load recorder
        logger.debug('Initializing recorder for module: %s', module_name)
        specs = RECORDER_SPECS[module_name]
        self._recorders[module_name] = []
        for spec in specs:
            try:
                recorder_module = importlib.import_module(spec[0])
                recorder_class = getattr(recorder_module, spec[1])
                recorder = recorder_class()
                recorder.setup()
                self._recorders[module_name].append(recorder)
            except Exception:
                logger.error('Failed to initialize recorder for module: %s', module_name, exc_info=True)

    def recorders(self):
        for recorder_list in self._recorders.values():
            for recorder in recorder_list:
                yield recorder

    def metric_store(self):
        return self._metric_store

    def log_store(self):
        return self._log_store

    def random_sampler(self, operation):
        if operation in self._random_samplers:
            return self._random_samplers[operation]
        else:
            random_sampler = self._random_samplers[operation] = RandomSampler()
            return random_sampler

    def lo_sampler(self, operation):
        if operation in self._lo_samplers:
            return self._lo_samplers[operation]
        else:
            lo_sampler = self._lo_samplers[operation] = LatencyOutlierSampler()
            return lo_sampler

    def mv_sampler(self, operation):
        if operation in self._mv_samplers:
            return self._mv_samplers[operation]
        else:
            lo_sampler = self._mv_samplers[operation] = MissingValueSampler()
            return lo_sampler

    def emit_trace_start(self, proto, context, options):
        last_exc = None
        for recorder in self.recorders():
            try:
                recorder.on_trace_start(proto, context, options)
            except Exception as exc:
                last_exc = exc
        if last_exc:
            raise last_exc

    def emit_trace_stop(self, proto, context, options):
        last_exc = None
        for recorder in self.recorders():
            try:
                recorder.on_trace_stop(proto, context, options)
            except Exception as exc:
                last_exc = exc
        if last_exc:
            raise last_exc

    def emit_trace_read(self, proto, context, options):
        last_exc = None
        for recorder in self.recorders():
            try:
                recorder.on_trace_read(proto, context, options)
            except Exception as exc:
                last_exc = exc
        if last_exc:
            raise last_exc

    def emit_metric_update(self):
        last_exc = None
        for recorder in self.recorders():
            try:
                recorder.on_metric_update()
            except Exception as exc:
                last_exc = exc
        if last_exc:
            raise last_exc

    def create_trace_proto(self):
        proto = signals_pb2.Trace()
        proto.trace_id = _uuid_sha1(size=12)
        proto.tracer_info.tracer_type = signals_pb2.TracerInfo.TracerType.PYTHON_TRACER
        parse_semver(proto.tracer_info.version, version.__version__)
        return proto

    def upload(self, block=False):
        if block:
            self._uploader.flush()
        else:
            self._uploader.flush_in_thread()

    def check_metric_read_interval(self, now=None):
        if now is None:
            now = time.time()
        return (self.last_metric_read_ts < now - Agent.METRIC_READ_INTERVAL_SEC)
    
    def set_metric_read(self, now=None):
        self.last_metric_read_ts = now if now else time.time()

    def check_metric_upload_interval(self, now=None):
        if now is None:
            now = time.time()
        return (self.last_metric_upload_ts < now - Agent.METRIC_UPLOAD_INTERVAL_SEC)

    def set_metric_upload(self, now=None):
        self.last_metric_upload_ts = now if now else time.time()

    def check_log_upload_interval(self, now=None):
        if now is None:
            now = time.time()
        return (self.last_log_upload_ts < now - Agent.LOG_UPLOAD_INTERVAL_SEC)

    def set_log_upload(self, now=None):
        self.last_log_upload_ts = now if now else time.time()

    def tick(self, block=False, now=None):
        if now is None:
            now = time.time()

        if self.check_metric_upload_interval(now):
            if self._metric_store.has_unexported():
                metrics = self._metric_store.export()
                for metric in metrics:
                    self.uploader().upload_metric(metric)
                self.set_metric_upload(now)

        if self.check_log_upload_interval(now):
            if self._log_store.has_unexported():
                entrys = self._log_store.export()
                for entry in entrys:
                    self.uploader().upload_log_entry(entry)
                self.set_log_upload(now)

        self.upload(block=False)


def _sha1(text, size=-1):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(text.encode('utf-8'))
    return sha1_hash.hexdigest()[0:size]


def _uuid_sha1(size=-1):
    return _sha1(str(uuid.uuid4()), size)
