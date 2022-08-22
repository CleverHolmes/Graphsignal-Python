from typing import Any, Union, Optional
import time
import sys
import os
import logging
import threading
import uuid
import hashlib
import atexit

from graphsignal.version import __version__
from graphsignal.agent import Agent
from graphsignal.workload import Workload
from graphsignal.uploader import Uploader
from graphsignal.usage.process_reader import ProcessReader
from graphsignal.usage.nvml_reader import NvmlReader
from graphsignal.inference_span import InferenceSpan
from graphsignal import tracers
from graphsignal.proto import profiles_pb2

logger = logging.getLogger('graphsignal')

_agent = None


def _check_configured():
    global _agent
    if not _agent:
        raise ValueError(
            'Profiler not configured, call graphsignal.configure() first')


def _check_and_set_arg(
        name, value, is_str=False, is_int=False, is_bool=False, required=False, max_len=None):
    env_name = 'GRAPHSIGNAL_{0}'.format(name.upper())

    if not value and env_name in os.environ:
        value = os.environ[env_name]
        if value:
            if is_int:
                try:
                    value = int(value)
                except:
                    raise ValueError('configure: invalid format, expected integer: {0}'.format(name))
            elif is_bool:
                value = bool(value)

    if not value:
        if required:
            raise ValueError('configure: missing argument: {0}'.format(name))
    else:
        if is_str:
            if not isinstance(value, str):
                raise ValueError('configure: invalid format, expected string: {0}'.format(name))
            if max_len and len(value) > max_len:
                raise ValueError('configure: invalid format, string too long (>{0}): {1}'.format(name, max_len))
        elif is_int:
            if not isinstance(value, int):
                raise ValueError('configure: invalid format, expected integer: {0}'.format(name))
        elif is_bool:
            if not isinstance(value, bool):
                raise ValueError('configure: invalid format, expected boolean: {0}'.format(name))

    return value


def configure(
        api_key: Optional[str] = None,
        workload_name: Optional[str] = None,
        debug_mode: Optional[bool] = False,
        disable_op_profiler: Optional[bool] = False) -> None:
    global _agent

    if _agent:
        logger.warning('Profiler already configured')
        return

    debug_mode = _check_and_set_arg('debug_mode', debug_mode, is_bool=True)
    if debug_mode:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)
    api_key = _check_and_set_arg('api_key', api_key, is_str=True, required=True)
    workload_name = _check_and_set_arg('workload_name', workload_name,  is_str=True, max_len=50)
    disable_op_profiler = _check_and_set_arg('disable_op_profiler', disable_op_profiler, is_bool=True)

    _agent = Agent()
    _agent.worker_id = _uuid_sha1(size=12)
    _agent.api_key = api_key
    if workload_name:
        _agent.workload_name = workload_name
    _agent.disable_op_profiler = disable_op_profiler
    _agent.debug_mode = debug_mode
    _agent.uploader = Uploader()
    _agent.uploader.configure()
    _agent.process_reader = ProcessReader()
    _agent.process_reader.setup()
    _agent.nvml_reader = NvmlReader()
    _agent.nvml_reader.setup()

    _agent.workload = Workload()
    if workload_name:
        _agent.workload.workload_id = _sha1(workload_name, size=12)
    else:
        _agent.workload.workload_id = _sha1('', size=12)

    atexit.register(shutdown)

    logger.debug('Profiler configured')


def workload() -> Workload:
    _check_configured()

    return _agent.workload


def upload(block=False) -> None:
    _check_configured()

    _agent.workload.upload(block=block)


def shutdown() -> None:
    _check_configured()

    global _agent
    atexit.unregister(shutdown)
    _agent.workload.end(block=True)
    _agent.process_reader.shutdown()
    _agent.nvml_reader.shutdown()
    _agent = None

    logger.debug('Profiler shutdown')


def generate_uuid() -> None:
    return _uuid_sha1()    


def _sha1(text, size=-1):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(text.encode('utf-8'))
    return sha1_hash.hexdigest()[0:size]


def _uuid_sha1(size=-1):
    return _sha1(str(uuid.uuid4()), size)


__all__ = [
    '__version__',
    'configure',
    'workload',
    'upload',
    'shutdown',
    'generate_uuid',
    'tracers'
]