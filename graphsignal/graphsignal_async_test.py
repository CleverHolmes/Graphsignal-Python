import unittest
import logging
import sys
import os
import asyncio
from unittest.mock import patch, Mock

import graphsignal
from graphsignal.traces import Trace

logger = logging.getLogger('graphsignal')


class GraphsignalAsyncTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        if len(logger.handlers) == 0:
            logger.addHandler(logging.StreamHandler(sys.stdout))
        graphsignal.configure(
            api_key='k1',
            deployment='d1',
            upload_on_shutdown=False,
            debug_mode=True)

    async def asyncTearDown(self):
        graphsignal.shutdown()

    @patch.object(Trace, '_stop', return_value=None)
    @patch.object(Trace, '_start', return_value=None)
    async def test_start_trace(self, mocked_start, mocked_stop):
        async def test_func(p):
            return 1 + p

        with graphsignal.start_trace(endpoint='ep1'):
            ret = await test_func(12)
            self.assertEqual(ret, 13)

        mocked_start.assert_called_once()
        mocked_stop.assert_called_once()

    @patch.object(Trace, '_stop', return_value=None)
    @patch.object(Trace, '_start', return_value=None)
    async def test_trace_function(self, mocked_start, mocked_stop):
        @graphsignal.trace_function
        async def test_func(p):
            return 1 + p

        ret = await test_func(12)
        self.assertEqual(ret, 13)

        mocked_start.assert_called_once()
        mocked_stop.assert_called_once()

    @patch.object(Trace, '_stop', return_value=None)
    @patch.object(Trace, '_start', return_value=None)
    async def test_trace_function_with_args(self, mocked_start, mocked_stop):
        @graphsignal.trace_function(endpoint='ep1', tags=dict(t1='v1'))
        async def test_func(p):
            return 1 + p

        ret = await test_func(12)
        self.assertEqual(ret, 13)

        mocked_start.assert_called_once()
        mocked_stop.assert_called_once()
