
import unittest
import logging
import sys
import os
import json
import time
from unittest.mock import patch, Mock
from google.protobuf.json_format import MessageToJson
import pprint

import graphsignal
from graphsignal.recorders.instrumentation import patch_method, instrument_method
from graphsignal.uploader import Uploader

logger = logging.getLogger('graphsignal')


class Dummy:
    def __init__(self):
        pass

    def test(self, a, b, c=None):
        return a + 1

    def test_exc(self):
        raise Exception('exc1')

    def test_gen(self):
        for i in range(2):
            yield 'item' + str(i)


class RecorderUtilsTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        if len(logger.handlers) == 0:
            logger.addHandler(logging.StreamHandler(sys.stdout))
        graphsignal.configure(
            api_key='k1',
            deployment='d1',
            debug_mode=True)

    async def asyncTearDown(self):
        graphsignal.shutdown()

    @patch.object(Uploader, 'upload_signal')
    async def test_instrument_method(self, mocked_upload_signal):
        obj = Dummy()

        trace_func_called = False
        def trace_func(trace, args, kwargs, ret, exc):
            nonlocal trace_func_called
            trace_func_called = True

        instrument_method(obj, 'test', 'ep1', trace_func)

        obj.test(1, 2, c=3)

        signal = mocked_upload_signal.call_args[0][0]

        self.assertTrue(trace_func_called)
        self.assertEqual(signal.endpoint_name, 'ep1')

    @patch.object(Uploader, 'upload_signal')
    async def test_instrument_method_generator(self, mocked_upload_signal):
        obj = Dummy()

        trace_func_called = None
        def trace_func(trace, args, kwargs, ret, exc):
            nonlocal trace_func_called
            trace_func_called = True

        instrument_method(obj, 'test_gen', 'ep1', trace_func)

        for item in obj.test_gen():
            pass

        signal = mocked_upload_signal.call_args[0][0]

        self.assertTrue(trace_func_called)
        self.assertEqual(signal.endpoint_name, 'ep1')
        self.assertEqual(signal.root_span.spans[0].name, 'response')

    async def test_patch_method(self):
        obj = Dummy()

        before_func_called = False
        def before_func(args, kwargs):
            nonlocal before_func_called
            before_func_called = True
            self.assertEqual(args, (1, 2))
            self.assertEqual(kwargs, {'c': 3})
            return dict(d=1)

        after_func_called = False
        def after_func(args, kwargs, ret, exc, context):
            nonlocal after_func_called
            after_func_called = True
            self.assertEqual(args, (1, 2))
            self.assertEqual(kwargs, {'c': 3})
            self.assertEqual(ret, 2)
            self.assertIsNone(exc)
            self.assertEqual(context['d'], 1)

        self.assertTrue(patch_method(obj, 'test', before_func=before_func, after_func=after_func))

        obj.test(1, 2, c=3)

        self.assertTrue(before_func_called)
        self.assertTrue(after_func_called)

    async def test_patch_method_exc(self):
        obj = Dummy()

        after_func_called = False
        def after_func(args, kwargs, ret, exc, context):
            nonlocal after_func_called
            after_func_called = True
            self.assertEqual(str(exc), 'exc1')

        self.assertTrue(patch_method(obj, 'test_exc', after_func=after_func))

        with self.assertRaises(Exception) as context:
            obj.test_exc()

        self.assertTrue(after_func_called)

    async def test_patch_method_generator(self):
        obj = Dummy()

        yield_func_called = False
        def yield_func(idx, item, context):
            nonlocal yield_func_called
            yield_func_called = True
            if idx != -1:
                self.assertTrue(item in ('item0', 'item1'))

        self.assertTrue(patch_method(obj, 'test_gen', yield_func=yield_func))

        for item in obj.test_gen():
            pass

        self.assertTrue(yield_func_called)
