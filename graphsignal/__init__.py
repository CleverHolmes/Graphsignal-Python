from typing import Dict, Any, Union, Optional
import os
import logging
import atexit
import functools
import asyncio

from graphsignal.version import __version__
from graphsignal.agent import Agent
from graphsignal.traces import Trace, TraceOptions

logger = logging.getLogger('graphsignal')

_agent = None


def _check_configured():
    global _agent
    if not _agent:
        raise ValueError(
            'Agent not configured, call graphsignal.configure() first')


def _check_and_set_arg(
        name, value, is_str=False, is_int=False, is_bool=False, is_kv=False, required=False, max_len=None):
    env_name = 'GRAPHSIGNAL_{0}'.format(name.upper())

    if not value and env_name in os.environ:
        value = os.environ[env_name]
        if value:
            if is_str:
                if max_len and len(value) > max_len:
                    raise ValueError('configure: invalid format, expected string with max length {0}: {1}'.format(max_len, name))
            if is_int:
                try:
                    value = int(value)
                except:
                    raise ValueError('configure: invalid format, expected integer: {0}'.format(name))
            elif is_bool:
                value = bool(value)
            elif is_kv:
                try:
                    value = dict([el.strip(' ') for el in kv.split('=')] for kv in value.split(','))
                except:
                    raise ValueError('configure: invalid format, expected comma-separated key-value list (k1=v1,k2=v2): {0}'.format(name))

    if not value and required:
        raise ValueError('configure: missing argument: {0}'.format(name))

    return value


def configure(
        api_key: Optional[str] = None,
        api_url: Optional[str] = None,
        deployment: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        auto_instrument: Optional[bool] = True,
        upload_on_shutdown: Optional[bool] = True,
        debug_mode: Optional[bool] = False) -> None:
    global _agent

    if _agent:
        logger.warning('Agent already configured')
        return

    debug_mode = _check_and_set_arg('debug_mode', debug_mode, is_bool=True)
    if debug_mode:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)
    api_key = _check_and_set_arg('api_key', api_key, is_str=True, required=True)
    api_url = _check_and_set_arg('api_url', api_url, is_str=True, required=False)
    deployment = _check_and_set_arg('deployment', deployment, is_str=True, required=True)
    tags = _check_and_set_arg('tags', tags, is_kv=True, required=False)

    _agent = Agent(
        api_key=api_key,
        api_url=api_url,
        deployment=deployment,
        tags=tags,
        auto_instrument=auto_instrument,
        upload_on_shutdown=upload_on_shutdown,
        debug_mode=debug_mode)
    _agent.setup()

    atexit.register(shutdown)

    logger.debug('Agent configured')


def set_tag(key: str, value: str) -> None:
    _check_configured()

    if not key:
        raise ValueError('set_tag: key must be provided')
    if value is None:
        raise ValueError('set_tag: value must be provided')

    if _agent.tags is None:
        _agent.tags = {}

    if len(_agent.tags) > Trace.MAX_RUN_TAGS:
        raise ValueError('set_tag: too many tags (>{0})'.format(Trace.MAX_RUN_TAGS))

    _agent.tags[key] = value


def log_param(name: str, value: str) -> None:
    if not name:
        raise ValueError('set_param: name must be provided')
    if value is None:
        raise ValueError('set_param: value must be provided')

    if _agent.params is None:
        _agent.params = {}

    if len(_agent.params) > Trace.MAX_RUN_PARAMS:
        raise ValueError('set_param: too many params (>{0})'.format(Trace.MAX_RUN_PARAMS))

    _agent.params[name] = value


def set_context_tag(key: str, value: str) -> None:
    _check_configured()

    if not key:
        raise ValueError('set_context_tag: key must be provided')
    if value is None:
        raise ValueError('set_context_tag: value must be provided')

    tags = _agent.context_tags.get()
    if len(tags) > Trace.MAX_RUN_TAGS:
        raise ValueError('set_context_tag: too many tags (>{0})'.format(Trace.MAX_TRACE_TAGS))

    tags[key] = value
    _agent.context_tags.set(tags)


def start_trace(
        endpoint: str,
        tags: Optional[Dict[str, str]] = None,
        options: Optional[TraceOptions] = None) -> Trace:
    _check_configured()

    return Trace(endpoint=endpoint, tags=tags, options=options)


def trace_function(
        func=None, *,
        endpoint: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        options: Optional[TraceOptions] = None):
    if func is None:
        return functools.partial(trace_function, endpoint=endpoint, tags=tags, options=options)

    if endpoint is None:
        endpoint_or_name = func.__name__
    else:
        endpoint_or_name = endpoint

    if asyncio.iscoroutinefunction(func):
        @functools.wraps(func)
        async def tf_async_wrapper(*args, **kwargs):
            with start_trace(endpoint=endpoint_or_name, tags=tags, options=options):
                return await func(*args, **kwargs)
        return tf_async_wrapper
    else:
        @functools.wraps(func)
        def tf_wrapper(*args, **kwargs):
            with start_trace(endpoint=endpoint_or_name, tags=tags, options=options):
                return func(*args, **kwargs)
        return tf_wrapper


def upload(block=False) -> None:
    _check_configured()

    _agent.upload(block=block)


def shutdown() -> None:
    global _agent
    if not _agent:
        return

    atexit.unregister(shutdown)
    _agent.shutdown()
    _agent = None

    logger.debug('Agent shutdown')


__all__ = [
    '__version__',
    'configure',
    'upload',
    'shutdown',
    'start_trace',
    'function_trace',
    'Trace',
    'TraceOptions'
]