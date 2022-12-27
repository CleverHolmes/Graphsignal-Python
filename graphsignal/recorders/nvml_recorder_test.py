import unittest
import logging
import sys
from unittest.mock import patch, Mock
import torch
from google.protobuf.json_format import MessageToJson
import pprint
import time

import graphsignal
from graphsignal.proto import signals_pb2
from graphsignal.endpoint_trace import DEFAULT_OPTIONS
from graphsignal.recorders.nvml_recorder import NVMLRecorder

logger = logging.getLogger('graphsignal')


class NVMLRecorderTest(unittest.TestCase):
    def setUp(self):
        if len(logger.handlers) == 0:
            logger.addHandler(logging.StreamHandler(sys.stdout))
        graphsignal.configure(
            api_key='k1',
            deployment='d1',
            debug_mode=True)

    def tearDown(self):
        graphsignal.shutdown()

    def test_record(self):
        recorder = NVMLRecorder()
        recorder.setup()

        signal = signals_pb2.WorkerSignal()
        context = {}
        recorder.on_trace_start(signal, context, DEFAULT_OPTIONS)
        recorder.on_trace_stop(signal, context, DEFAULT_OPTIONS)
        recorder.on_trace_read(signal, context, DEFAULT_OPTIONS)

        model = torch.nn.Linear(1, 1)
        if torch.cuda.is_available():
            model = model.cuda()

        signal = signals_pb2.WorkerSignal()
        context = {}
        recorder.on_trace_start(signal, context, DEFAULT_OPTIONS)

        x = torch.arange(-50, 50, 0.00001).view(-1, 1)
        if torch.cuda.is_available():
            x = x.cuda()
        pred = model(x)

        signal = signals_pb2.WorkerSignal()
        recorder.on_trace_stop(signal, context, DEFAULT_OPTIONS)
        recorder.on_trace_read(signal, context, DEFAULT_OPTIONS)

        #pp = pprint.PrettyPrinter()
        #pp.pprint(MessageToJson(signal))

        if len(signal.device_usage) > 0:
            self.assertTrue(signal.node_usage.num_devices > 0)

            self.assertEqual(signal.node_usage.drivers[0].name, 'CUDA')
            self.assertIsNotNone(signal.node_usage.drivers[0].version)

            device_usage = signal.device_usage[0]
            self.assertEqual(device_usage.device_type, signals_pb2.DeviceUsage.DeviceType.GPU)
            self.assertNotEqual(device_usage.device_id, 0)
            self.assertNotEqual(device_usage.device_id, '')
            self.assertNotEqual(device_usage.device_name, '')
            self.assertNotEqual(device_usage.architecture, '')
            self.assertTrue(device_usage.compute_capability.major > 0)
            self.assertTrue(device_usage.mem_total > 0)
            self.assertTrue(device_usage.mem_used > 0)
            self.assertTrue(device_usage.mem_free > 0)
            self.assertTrue(device_usage.gpu_utilization_percent > 0)
            #self.assertTrue(device_usage.mem_access_percent > 0)
            self.assertTrue(device_usage.gpu_temp_c > 0)
            self.assertTrue(device_usage.power_usage_w > 0)
            #self.assertTrue(device_usage.fan_speed_percent > 0)
            self.assertTrue(device_usage.gpu_temp_c > 0)
            self.assertTrue(device_usage.power_usage_w > 0)
