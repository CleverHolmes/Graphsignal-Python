import logging
import sys
import xgboost as xgb


import graphsignal
from graphsignal.recorders.base_recorder import BaseRecorder
from graphsignal.proto_utils import parse_semver
from graphsignal.proto import signals_pb2
from graphsignal.proto_utils import add_framework_param, add_driver

logger = logging.getLogger('graphsignal')

class XGBoostRecorder(BaseRecorder):
    def __init__(self):
        self._framework = None
        self._comm_info = None

    def setup(self):
        self._framework = signals_pb2.FrameworkInfo()
        self._framework.name = 'XGBoost'
        parse_semver(self._framework.version, xgb.__version__)

        for key, value in xgb.get_config().items():
            if isinstance(value, (bool, int, float, str)):
                add_framework_param(self._framework, key, value)

    def on_trace_start(self, proto, context, options):
        pass

    def on_trace_stop(self, proto, context, options):
        pass

    def on_trace_read(self, proto, context, options):
        if self._framework:
            proto.frameworks.append(self._framework)

    def on_metric_update(self):
        pass
