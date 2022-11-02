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
from graphsignal.proto import signals_pb2
from graphsignal.uploader import Uploader

logger = logging.getLogger('graphsignal')


class JaxProfilerTest(unittest.TestCase):
    def setUp(self):
        if len(logger.handlers) == 0:
            logger.addHandler(logging.StreamHandler(sys.stdout))
        graphsignal.configure(
            api_key='k1',
            debug_mode=True)

    def tearDown(self):
        graphsignal.shutdown()

    def test_read_info(self):
        try:
            import jax
            import jax.numpy as jnp
            from jax import grad, jit, vmap
            from jax import random
        except ImportError:
            logger.info('Not testing JAX profiler, package not found.')
            return

        from graphsignal.profilers.jax import JaxProfiler

        profiler = JaxProfiler()
        signal = signals_pb2.WorkerSignal()
        profiler.read_info(signal)

        self.assertEqual(
            signal.frameworks[0].type,
            signals_pb2.FrameworkInfo.FrameworkType.JAX_FRAMEWORK)

    def test_start_stop(self):
        try:
            import jax
            import jax.numpy as jnp
            from jax import grad, jit, vmap
            from jax import random
        except ImportError:
            logger.info('Not testing JAX profiler, package not found.')
            return

        from graphsignal.profilers.jax import JaxProfiler

        profiler = JaxProfiler()
        signal = signals_pb2.WorkerSignal()
        profiler.start(signal)

        key = random.PRNGKey(0)
        x = random.normal(key, (10,))
        size = 100
        x = random.normal(key, (size, size), dtype=jnp.float32)
        jnp.dot(x, x.T).block_until_ready()

        profiler.stop(signal)

        pp = pprint.PrettyPrinter()
        pp.pprint(MessageToJson(signal))

        self.assertTrue(sum([op_stats.count for op_stats in signal.op_stats]) > 0)
        if jax.device_count() > 0:
            self.assertTrue(sum([op_stats.total_device_time_us for op_stats in signal.op_stats]) > 0)
            self.assertTrue(sum([op_stats.self_device_time_us for op_stats in signal.op_stats]) > 0)
        else:
            self.assertTrue(sum([op_stats.total_host_time_us for op_stats in signal.op_stats]) > 0)
            self.assertTrue(sum([op_stats.self_host_time_us for op_stats in signal.op_stats]) > 0)
        self.assertNotEqual(signal.trace_data, b'')
