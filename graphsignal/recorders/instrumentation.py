import logging
from functools import wraps
import asyncio
import types

import graphsignal

logger = logging.getLogger('graphsignal')


def instrument_method(obj, func_name, operation, trace_func, data_func=None):
    def before_func(args, kwargs):
        return dict(trace=graphsignal.start_trace(operation=operation))

    def after_func(args, kwargs, ret, exc, context):
        trace = context['trace']

        if not is_generator(ret) and not is_async_generator(ret):
            trace.measure()

        try:
            if exc is not None:
                trace.set_exception(exc)

            trace_func(trace, args, kwargs, ret, exc)
        except Exception as e:
            logger.debug('Error tracing %s', func_name, exc_info=True)

        if not is_generator(ret) and not is_async_generator(ret):
            trace.stop()

    def yield_func(stopped, item, context):
        trace = context['trace']

        if stopped:
            trace.stop()
        else:
            if data_func:
                data_func(trace, item)

    if not patch_method(obj, func_name, before_func=before_func, after_func=after_func, yield_func=yield_func):
        logger.debug('Cannot instrument %s.', operation)


def uninstrument_method(obj, func_name, operation):
    if not unpatch_method(obj, func_name):
        logger.debug('Cannot uninstrument %s.', operation)


def patch_method(obj, func_name, before_func=None, after_func=None, yield_func=None):
    if not hasattr(obj, func_name):
        return False

    func = getattr(obj, func_name)

    if hasattr(func, '__graphsignal_wrapped__'):
        return False

    if asyncio.iscoroutinefunction(func):
        if yield_func:
            async def async_generator_wrapper(gen, yield_func, context):
                async for item in gen:
                    try:
                        yield_func(False, item, context)
                    except:
                        logger.debug('Exception in yield_func', exc_info=True)
                    yield item
                yield_func(True, None, context)

        @wraps(func)
        async def wrapper(*args, **kwargs):
            context = None
            exc = None
            ret = None

            if before_func:
                try:
                    context = before_func(args, kwargs)
                except:
                    logger.debug('Exception in before_func', exc_info=True)

            try:
                ret = await func(*args, **kwargs)
            except BaseException as e:
                exc = e

            if after_func:
                try:
                    after_func(args, kwargs, ret, exc, context)
                except:
                    logger.debug('Exception in after_func', exc_info=True)

            if yield_func:
                try:
                    if is_async_generator(ret):
                        ret = async_generator_wrapper(ret, yield_func, context)
                except:
                    logger.debug('Exception in yield_func', exc_info=True)

            if exc:
                raise exc
            return ret
    else:
        if yield_func:
            def generator_wrapper(gen, yield_func, context):
                for item in gen:
                    try:
                        yield_func(False, item, context)
                    except:
                        logger.debug('Exception in yield_func', exc_info=True)
                    yield item
                yield_func(True, None, context)

        @wraps(func)
        def wrapper(*args, **kwargs):
            context = None
            exc = None
            ret = None

            if before_func:
                try:
                    context = before_func(args, kwargs)
                except:
                    logger.debug('Exception in before_func', exc_info=True)

            try:
                ret = func(*args, **kwargs)
            except BaseException as e:
                exc = e

            if after_func:
                try:
                    after_func(args, kwargs, ret, exc, context)
                except:
                    logger.debug('Exception in after_func', exc_info=True)

            if yield_func:
                try:
                    if is_generator(ret):
                        ret = generator_wrapper(ret, yield_func, context)
                except:
                    logger.debug('Exception in yield_func', exc_info=True)

            if exc:
                raise exc
            return ret

    setattr(wrapper, '__graphsignal_wrapped__', True)
    setattr(obj, func_name, wrapper)
    return True


def unpatch_method(obj, func_name):
    if not hasattr(obj, func_name):
        return False

    func = getattr(obj, func_name)

    if not hasattr(func, '__graphsignal_wrapped__'):
        return False

    if not hasattr(func, '__wrapped__'):
        return False
    
    setattr(obj, func_name, getattr(func, '__wrapped__'))
    return True


def is_generator(obj):
    return obj and isinstance(obj, types.GeneratorType)


def is_async_generator(obj):
    return obj and isinstance(obj, types.AsyncGeneratorType)


def read_args(args, kwargs, names):
    values = {}
    for name, arg in zip(names, args):
        values[name] = arg
    values.update(kwargs)
    return values