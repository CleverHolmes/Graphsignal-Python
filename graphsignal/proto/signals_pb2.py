# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: signals.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rsignals.proto\x12\x13graphsignal.signals\"]\n\rUploadRequest\x12\x39\n\x0eworker_signals\x18\x01 \x03(\x0b\x32!.graphsignal.signals.WorkerSignal\x12\x11\n\tupload_ms\x18\x02 \x01(\x04\"\x10\n\x0eUploadResponse\"\xb7\x01\n\x0cSignalRecord\x12\x0f\n\x07\x64\x61ta_id\x18\x01 \x01(\t\x12\x15\n\rdeployment_id\x18\x07 \x01(\t\x12\x13\n\x0b\x65ndpoint_id\x18\x02 \x01(\t\x12\x38\n\rworker_signal\x18\x04 \x01(\x0b\x32!.graphsignal.signals.WorkerSignal\x12\x1a\n\x12\x64\x61ta_retention_sec\x18\x05 \x01(\x04\x12\x14\n\x0ctime_skew_ms\x18\x06 \x01(\x12\"\xfd\x08\n\x0cWorkerSignal\x12\x11\n\tworker_id\x18\x1c \x01(\t\x12\x11\n\tsignal_id\x18\x30 \x01(\t\x12\x17\n\x0f\x64\x65ployment_name\x18\x35 \x01(\t\x12\x15\n\rendpoint_name\x18\x01 \x01(\t\x12\x10\n\x08start_us\x18\x05 \x01(\x04\x12\x0e\n\x06\x65nd_us\x18\x06 \x01(\x04\x12\x34\n\x0bsignal_type\x18\x31 \x01(\x0e\x32\x1f.graphsignal.signals.SignalType\x12&\n\x04tags\x18- \x03(\x0b\x32\x18.graphsignal.signals.Tag\x12*\n\x06params\x18; \x03(\x0b\x32\x1a.graphsignal.signals.Param\x12\x38\n\rtrace_metrics\x18\x33 \x01(\x0b\x32!.graphsignal.signals.TraceMetrics\x12\x35\n\x0c\x64\x61ta_metrics\x18\x34 \x03(\x0b\x32\x1f.graphsignal.signals.DataMetric\x12\x36\n\x0ctrace_sample\x18\x37 \x01(\x0b\x32 .graphsignal.signals.TraceSample\x12\x32\n\nexceptions\x18/ \x03(\x0b\x32\x1e.graphsignal.signals.Exception\x12<\n\ralloc_summary\x18< \x03(\x0b\x32%.graphsignal.signals.MemoryAllocation\x12\x30\n\nop_profile\x18= \x03(\x0b\x32\x1c.graphsignal.signals.OpStats\x12\x38\n\x0ekernel_profile\x18> \x03(\x0b\x32 .graphsignal.signals.KernelStats\x12\x34\n\x0c\x64\x61ta_profile\x18\x32 \x03(\x0b\x32\x1e.graphsignal.signals.DataStats\x12\x31\n\troot_span\x18? \x01(\x0b\x32\x1e.graphsignal.signals.TraceSpan\x12\x32\n\nmodel_info\x18& \x01(\x0b\x32\x1e.graphsignal.signals.ModelInfo\x12\x36\n\nframeworks\x18$ \x03(\x0b\x32\".graphsignal.signals.FrameworkInfo\x12\x36\n\x0c\x64\x65vice_usage\x18\x12 \x03(\x0b\x32 .graphsignal.signals.DeviceUsage\x12\x32\n\nnode_usage\x18\x19 \x01(\x0b\x32\x1e.graphsignal.signals.NodeUsage\x12\x38\n\rprocess_usage\x18\x1a \x01(\x0b\x32!.graphsignal.signals.ProcessUsage\x12\x32\n\nagent_info\x18# \x01(\x0b\x32\x1e.graphsignal.signals.AgentInfo\x12\x35\n\x0c\x61gent_errors\x18\x07 \x03(\x0b\x32\x1f.graphsignal.signals.AgentError\"9\n\x03Tag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x16\n\x0eis_trace_level\x18\x03 \x01(\x08\"<\n\x05Param\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x16\n\x0eis_trace_level\x18\x03 \x01(\x08\"\xfe\x01\n\x06Metric\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.graphsignal.signals.Metric.MetricType\x12\x0f\n\x05gauge\x18\x02 \x01(\x01H\x00\x12:\n\treservoir\x18\x03 \x01(\x0b\x32%.graphsignal.signals.Metric.ReservoirH\x00\x1a\x1b\n\tReservoir\x12\x0e\n\x06values\x18\x01 \x03(\x01\"J\n\nMetricType\x12\x14\n\x10UNDEFINED_METRIC\x10\x00\x12\x10\n\x0cGAUGE_METRIC\x10\x01\x12\x14\n\x10RESERVOIR_METRIC\x10\x02\x42\x08\n\x06values\"\xa6\x01\n\x0cTraceMetrics\x12/\n\nlatency_us\x18\x01 \x01(\x0b\x32\x1b.graphsignal.signals.Metric\x12/\n\ncall_count\x18\x04 \x01(\x0b\x32\x1b.graphsignal.signals.Metric\x12\x34\n\x0f\x65xception_count\x18\x05 \x01(\x0b\x32\x1b.graphsignal.signals.Metric\"a\n\nDataMetric\x12\x11\n\tdata_name\x18\x01 \x01(\t\x12\x13\n\x0bmetric_name\x18\x02 \x01(\t\x12+\n\x06metric\x18\x04 \x01(\x0b\x32\x1b.graphsignal.signals.Metric\"f\n\x0bTraceSample\x12\x12\n\nlatency_us\x18\x02 \x01(\x04\x12\x1a\n\x12thread_cpu_time_us\x18\x03 \x01(\x04\x12\x12\n\nis_ensured\x18\x04 \x01(\x08\x12\x13\n\x0bis_profiled\x18\x05 \x01(\x08\"\x96\x01\n\tTraceSpan\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08start_ns\x18\x02 \x01(\x04\x12\x0e\n\x06\x65nd_ns\x18\x03 \x01(\x04\x12\x15\n\rhas_exception\x18\x04 \x01(\x08\x12-\n\x05spans\x18\x05 \x03(\x0b\x32\x1e.graphsignal.signals.TraceSpan\x12\x13\n\x0bis_endpoint\x18\x06 \x01(\x08\"C\n\tException\x12\x10\n\x08\x65xc_type\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x0bstack_trace\x18\x03 \x01(\t\"5\n\x06SemVer\x12\r\n\x05major\x18\x01 \x01(\x05\x12\r\n\x05minor\x18\x02 \x01(\x05\x12\r\n\x05patch\x18\x03 \x01(\x05\"\xc2\x02\n\x10MemoryAllocation\x12K\n\x0e\x61llocator_type\x18\x01 \x01(\x0e\x32\x33.graphsignal.signals.MemoryAllocation.AllocatorType\x12\x12\n\ndevice_idx\x18\x02 \x01(\x04\x12\x16\n\x0e\x61llocated_size\x18\x03 \x01(\x04\x12\x15\n\rreserved_size\x18\x04 \x01(\x04\x12\x12\n\nfreed_size\x18\x05 \x01(\x04\x12\x17\n\x0fnum_allocations\x18\x06 \x01(\x04\x12\x19\n\x11num_alloc_retries\x18\x07 \x01(\x04\x12\x10\n\x08num_ooms\x18\x08 \x01(\x04\"D\n\rAllocatorType\x12\x17\n\x13UNDEFINED_ALLOCATOR\x10\x00\x12\x1a\n\x16PYTORCH_CUDA_ALLOCATOR\x10\x01\"\xcd\x03\n\x07OpStats\x12\x34\n\x07op_type\x18\x01 \x01(\x0e\x32#.graphsignal.signals.OpStats.OpType\x12\x0f\n\x07op_name\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x04\x12\x14\n\x0chost_time_ns\x18\x04 \x01(\x04\x12\x19\n\x11self_host_time_ns\x18\x05 \x01(\x04\x12\x1e\n\x16self_host_time_percent\x18\x06 \x01(\x01\x12\x16\n\x0e\x64\x65vice_time_ns\x18\x07 \x01(\x04\x12\x1b\n\x13self_device_time_ns\x18\x08 \x01(\x04\x12\x13\n\x0bhost_memory\x18\t \x01(\x04\x12\x18\n\x10self_host_memory\x18\n \x01(\x04\x12\x15\n\rdevice_memory\x18\x0b \x01(\x04\x12\x1a\n\x12self_device_memory\x18\x0c \x01(\x04\x12\x11\n\tdata_size\x18\r \x01(\x04\x12\x14\n\x0c\x64\x61ta_per_sec\x18\x0e \x01(\x01\x12\r\n\x05\x66lops\x18\x0f \x01(\x04\"L\n\x06OpType\x12\x10\n\x0cUNDEFINED_OP\x10\x00\x12\r\n\tPYTHON_OP\x10\x01\x12\x0e\n\nPYTORCH_OP\x10\x02\x12\x11\n\rCOLLECTIVE_OP\x10\x03\"k\n\x0bKernelStats\x12\x12\n\ndevice_idx\x18\x01 \x01(\x04\x12\x0f\n\x07op_name\x18\x02 \x01(\t\x12\x13\n\x0bkernel_name\x18\x03 \x01(\t\x12\r\n\x05\x63ount\x18\x04 \x01(\x04\x12\x13\n\x0b\x64uration_ns\x18\x05 \x01(\x04\"\xa4\x01\n\tDataStats\x12\x11\n\tdata_name\x18\x01 \x01(\t\x12\x11\n\tdata_type\x18\x02 \x01(\t\x12\r\n\x05shape\x18\x04 \x03(\x04\x12\x38\n\x06\x63ounts\x18\x05 \x03(\x0b\x32(.graphsignal.signals.DataStats.DataCount\x1a(\n\tDataCount\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x04\"O\n\tModelInfo\x12\x14\n\x0cmodel_format\x18\x04 \x01(\t\x12\x12\n\nmodel_name\x18\x03 \x01(\t\x12\x18\n\x10model_size_bytes\x18\x02 \x01(\x04\"\xbd\x01\n\rFrameworkInfo\x12\x0c\n\x04name\x18\x04 \x01(\t\x12,\n\x07version\x18\x02 \x01(\x0b\x32\x1b.graphsignal.signals.SemVer\x12\x41\n\x06params\x18\x03 \x03(\x0b\x32\x31.graphsignal.signals.FrameworkInfo.FrameworkParam\x1a-\n\x0e\x46rameworkParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xca\x05\n\x0b\x44\x65viceUsage\x12@\n\x0b\x64\x65vice_type\x18\x0b \x01(\x0e\x32+.graphsignal.signals.DeviceUsage.DeviceType\x12\x12\n\ndevice_idx\x18\x15 \x01(\x04\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\x12\x14\n\x0c\x61rchitecture\x18\x11 \x01(\t\x12\x37\n\x12\x63ompute_capability\x18\x0f \x01(\x0b\x32\x1b.graphsignal.signals.SemVer\x12\x11\n\tmem_total\x18\x03 \x01(\x04\x12\x10\n\x08mem_used\x18\x04 \x01(\x04\x12\x10\n\x08mem_free\x18\x05 \x01(\x04\x12\x14\n\x0cmem_reserved\x18\x13 \x01(\x04\x12\x1f\n\x17gpu_utilization_percent\x18\x06 \x01(\x01\x12\x1a\n\x12mem_access_percent\x18\x10 \x01(\x01\x12\x1a\n\x12pcie_throughput_tx\x18\r \x01(\x01\x12\x1a\n\x12pcie_throughput_rx\x18\x0e \x01(\x01\x12&\n\x1envlink_throughput_data_tx_kibs\x18\x17 \x01(\x01\x12&\n\x1envlink_throughput_data_rx_kibs\x18\x18 \x01(\x01\x12\x12\n\ngpu_temp_c\x18\x08 \x01(\x01\x12\x15\n\rpower_usage_w\x18\t \x01(\x01\x12\x19\n\x11\x66\x61n_speed_percent\x18\n \x01(\x01\x12\x1f\n\x17mxu_utilization_percent\x18\x0c \x01(\x01\x12:\n\tprocesses\x18\x14 \x03(\x0b\x32\'.graphsignal.signals.DeviceProcessUsage\"9\n\nDeviceType\x12\x19\n\x15\x44\x45VICE_TYPE_UNDEFINED\x10\x00\x12\x07\n\x03GPU\x10\x02\x12\x07\n\x03TPU\x10\x03\"i\n\x12\x44\x65viceProcessUsage\x12\x0b\n\x03pid\x18\x01 \x01(\x04\x12\x17\n\x0fgpu_instance_id\x18\x02 \x01(\x04\x12\x1b\n\x13\x63ompute_instance_id\x18\x03 \x01(\x04\x12\x10\n\x08mem_used\x18\x04 \x01(\x04\"\x93\x03\n\x0cProcessUsage\x12\x0b\n\x03pid\x18\x13 \x01(\x04\x12\x0c\n\x04rank\x18\x14 \x01(\x04\x12\x10\n\x08has_rank\x18\x15 \x01(\x08\x12\x12\n\nlocal_rank\x18\x16 \x01(\x04\x12\x16\n\x0ehas_local_rank\x18\x17 \x01(\x08\x12\x10\n\x08start_ms\x18\x0e \x01(\x04\x12\x10\n\x08\x63pu_name\x18\x10 \x01(\t\x12\x19\n\x11\x63pu_usage_percent\x18\x01 \x01(\x01\x12\x0f\n\x07max_rss\x18\x02 \x01(\x04\x12\x13\n\x0b\x63urrent_rss\x18\x03 \x01(\x04\x12\x0f\n\x07vm_size\x18\x04 \x01(\x04\x12:\n\x07runtime\x18\x06 \x01(\x0e\x32).graphsignal.signals.ProcessUsage.Runtime\x12\x34\n\x0fruntime_version\x18\x07 \x01(\x0b\x32\x1b.graphsignal.signals.SemVer\x12\x14\n\x0cruntime_impl\x18\x08 \x01(\t\",\n\x07Runtime\x12\x15\n\x11RUNTIME_UNDEFINED\x10\x00\x12\n\n\x06PYTHON\x10\x01\"\xc6\x02\n\tNodeUsage\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x12\n\nip_address\x18\x07 \x01(\t\x12\x11\n\tnode_rank\x18\x0c \x01(\x04\x12\x15\n\rhas_node_rank\x18\r \x01(\x08\x12\x10\n\x08mem_used\x18\t \x01(\x04\x12\x11\n\tmem_total\x18\n \x01(\x04\x12\x10\n\x08platform\x18\x02 \x01(\t\x12\x0f\n\x07machine\x18\x03 \x01(\t\x12\x0f\n\x07os_name\x18\x04 \x01(\t\x12\x12\n\nos_version\x18\x05 \x01(\t\x12\x13\n\x0bnum_devices\x18\x06 \x01(\x05\x12:\n\x07\x64rivers\x18\x0b \x03(\x0b\x32).graphsignal.signals.NodeUsage.DriverInfo\x1a+\n\nDriverInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\xab\x01\n\tAgentInfo\x12<\n\nagent_type\x18\x01 \x01(\x0e\x32(.graphsignal.signals.AgentInfo.AgentType\x12,\n\x07version\x18\x03 \x01(\x0b\x32\x1b.graphsignal.signals.SemVer\"2\n\tAgentType\x12\x13\n\x0f\x41GENT_UNDEFINED\x10\x00\x12\x10\n\x0cPYTHON_AGENT\x10\x01\"2\n\nAgentError\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x13\n\x0bstack_trace\x18\x02 \x01(\t*\x95\x01\n\nSignalType\x12\x12\n\x0eUNKNOWN_SIGNAL\x10\x00\x12\x11\n\rSAMPLE_SIGNAL\x10\x01\x12\x14\n\x10\x45XCEPTION_SIGNAL\x10\x02\x12\x1a\n\x16LATENCY_OUTLIER_SIGNAL\x10\x04\x12\x19\n\x15MISSING_VALUES_SIGNAL\x10\x03\x12\x13\n\x0fSNAPSHOT_SIGNAL\x10\x05\x62\x06proto3')

_SIGNALTYPE = DESCRIPTOR.enum_types_by_name['SignalType']
SignalType = enum_type_wrapper.EnumTypeWrapper(_SIGNALTYPE)
UNKNOWN_SIGNAL = 0
SAMPLE_SIGNAL = 1
EXCEPTION_SIGNAL = 2
LATENCY_OUTLIER_SIGNAL = 4
MISSING_VALUES_SIGNAL = 3
SNAPSHOT_SIGNAL = 5


_UPLOADREQUEST = DESCRIPTOR.message_types_by_name['UploadRequest']
_UPLOADRESPONSE = DESCRIPTOR.message_types_by_name['UploadResponse']
_SIGNALRECORD = DESCRIPTOR.message_types_by_name['SignalRecord']
_WORKERSIGNAL = DESCRIPTOR.message_types_by_name['WorkerSignal']
_TAG = DESCRIPTOR.message_types_by_name['Tag']
_PARAM = DESCRIPTOR.message_types_by_name['Param']
_METRIC = DESCRIPTOR.message_types_by_name['Metric']
_METRIC_RESERVOIR = _METRIC.nested_types_by_name['Reservoir']
_TRACEMETRICS = DESCRIPTOR.message_types_by_name['TraceMetrics']
_DATAMETRIC = DESCRIPTOR.message_types_by_name['DataMetric']
_TRACESAMPLE = DESCRIPTOR.message_types_by_name['TraceSample']
_TRACESPAN = DESCRIPTOR.message_types_by_name['TraceSpan']
_EXCEPTION = DESCRIPTOR.message_types_by_name['Exception']
_SEMVER = DESCRIPTOR.message_types_by_name['SemVer']
_MEMORYALLOCATION = DESCRIPTOR.message_types_by_name['MemoryAllocation']
_OPSTATS = DESCRIPTOR.message_types_by_name['OpStats']
_KERNELSTATS = DESCRIPTOR.message_types_by_name['KernelStats']
_DATASTATS = DESCRIPTOR.message_types_by_name['DataStats']
_DATASTATS_DATACOUNT = _DATASTATS.nested_types_by_name['DataCount']
_MODELINFO = DESCRIPTOR.message_types_by_name['ModelInfo']
_FRAMEWORKINFO = DESCRIPTOR.message_types_by_name['FrameworkInfo']
_FRAMEWORKINFO_FRAMEWORKPARAM = _FRAMEWORKINFO.nested_types_by_name['FrameworkParam']
_DEVICEUSAGE = DESCRIPTOR.message_types_by_name['DeviceUsage']
_DEVICEPROCESSUSAGE = DESCRIPTOR.message_types_by_name['DeviceProcessUsage']
_PROCESSUSAGE = DESCRIPTOR.message_types_by_name['ProcessUsage']
_NODEUSAGE = DESCRIPTOR.message_types_by_name['NodeUsage']
_NODEUSAGE_DRIVERINFO = _NODEUSAGE.nested_types_by_name['DriverInfo']
_AGENTINFO = DESCRIPTOR.message_types_by_name['AgentInfo']
_AGENTERROR = DESCRIPTOR.message_types_by_name['AgentError']
_METRIC_METRICTYPE = _METRIC.enum_types_by_name['MetricType']
_MEMORYALLOCATION_ALLOCATORTYPE = _MEMORYALLOCATION.enum_types_by_name['AllocatorType']
_OPSTATS_OPTYPE = _OPSTATS.enum_types_by_name['OpType']
_DEVICEUSAGE_DEVICETYPE = _DEVICEUSAGE.enum_types_by_name['DeviceType']
_PROCESSUSAGE_RUNTIME = _PROCESSUSAGE.enum_types_by_name['Runtime']
_AGENTINFO_AGENTTYPE = _AGENTINFO.enum_types_by_name['AgentType']
UploadRequest = _reflection.GeneratedProtocolMessageType('UploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADREQUEST,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.UploadRequest)
  })
_sym_db.RegisterMessage(UploadRequest)

UploadResponse = _reflection.GeneratedProtocolMessageType('UploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADRESPONSE,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.UploadResponse)
  })
_sym_db.RegisterMessage(UploadResponse)

SignalRecord = _reflection.GeneratedProtocolMessageType('SignalRecord', (_message.Message,), {
  'DESCRIPTOR' : _SIGNALRECORD,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.SignalRecord)
  })
_sym_db.RegisterMessage(SignalRecord)

WorkerSignal = _reflection.GeneratedProtocolMessageType('WorkerSignal', (_message.Message,), {
  'DESCRIPTOR' : _WORKERSIGNAL,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.WorkerSignal)
  })
_sym_db.RegisterMessage(WorkerSignal)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.Tag)
  })
_sym_db.RegisterMessage(Tag)

Param = _reflection.GeneratedProtocolMessageType('Param', (_message.Message,), {
  'DESCRIPTOR' : _PARAM,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.Param)
  })
_sym_db.RegisterMessage(Param)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {

  'Reservoir' : _reflection.GeneratedProtocolMessageType('Reservoir', (_message.Message,), {
    'DESCRIPTOR' : _METRIC_RESERVOIR,
    '__module__' : 'signals_pb2'
    # @@protoc_insertion_point(class_scope:graphsignal.signals.Metric.Reservoir)
    })
  ,
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.Metric)
  })
_sym_db.RegisterMessage(Metric)
_sym_db.RegisterMessage(Metric.Reservoir)

TraceMetrics = _reflection.GeneratedProtocolMessageType('TraceMetrics', (_message.Message,), {
  'DESCRIPTOR' : _TRACEMETRICS,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.TraceMetrics)
  })
_sym_db.RegisterMessage(TraceMetrics)

DataMetric = _reflection.GeneratedProtocolMessageType('DataMetric', (_message.Message,), {
  'DESCRIPTOR' : _DATAMETRIC,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.DataMetric)
  })
_sym_db.RegisterMessage(DataMetric)

TraceSample = _reflection.GeneratedProtocolMessageType('TraceSample', (_message.Message,), {
  'DESCRIPTOR' : _TRACESAMPLE,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.TraceSample)
  })
_sym_db.RegisterMessage(TraceSample)

TraceSpan = _reflection.GeneratedProtocolMessageType('TraceSpan', (_message.Message,), {
  'DESCRIPTOR' : _TRACESPAN,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.TraceSpan)
  })
_sym_db.RegisterMessage(TraceSpan)

Exception = _reflection.GeneratedProtocolMessageType('Exception', (_message.Message,), {
  'DESCRIPTOR' : _EXCEPTION,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.Exception)
  })
_sym_db.RegisterMessage(Exception)

SemVer = _reflection.GeneratedProtocolMessageType('SemVer', (_message.Message,), {
  'DESCRIPTOR' : _SEMVER,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.SemVer)
  })
_sym_db.RegisterMessage(SemVer)

MemoryAllocation = _reflection.GeneratedProtocolMessageType('MemoryAllocation', (_message.Message,), {
  'DESCRIPTOR' : _MEMORYALLOCATION,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.MemoryAllocation)
  })
_sym_db.RegisterMessage(MemoryAllocation)

OpStats = _reflection.GeneratedProtocolMessageType('OpStats', (_message.Message,), {
  'DESCRIPTOR' : _OPSTATS,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.OpStats)
  })
_sym_db.RegisterMessage(OpStats)

KernelStats = _reflection.GeneratedProtocolMessageType('KernelStats', (_message.Message,), {
  'DESCRIPTOR' : _KERNELSTATS,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.KernelStats)
  })
_sym_db.RegisterMessage(KernelStats)

DataStats = _reflection.GeneratedProtocolMessageType('DataStats', (_message.Message,), {

  'DataCount' : _reflection.GeneratedProtocolMessageType('DataCount', (_message.Message,), {
    'DESCRIPTOR' : _DATASTATS_DATACOUNT,
    '__module__' : 'signals_pb2'
    # @@protoc_insertion_point(class_scope:graphsignal.signals.DataStats.DataCount)
    })
  ,
  'DESCRIPTOR' : _DATASTATS,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.DataStats)
  })
_sym_db.RegisterMessage(DataStats)
_sym_db.RegisterMessage(DataStats.DataCount)

ModelInfo = _reflection.GeneratedProtocolMessageType('ModelInfo', (_message.Message,), {
  'DESCRIPTOR' : _MODELINFO,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.ModelInfo)
  })
_sym_db.RegisterMessage(ModelInfo)

FrameworkInfo = _reflection.GeneratedProtocolMessageType('FrameworkInfo', (_message.Message,), {

  'FrameworkParam' : _reflection.GeneratedProtocolMessageType('FrameworkParam', (_message.Message,), {
    'DESCRIPTOR' : _FRAMEWORKINFO_FRAMEWORKPARAM,
    '__module__' : 'signals_pb2'
    # @@protoc_insertion_point(class_scope:graphsignal.signals.FrameworkInfo.FrameworkParam)
    })
  ,
  'DESCRIPTOR' : _FRAMEWORKINFO,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.FrameworkInfo)
  })
_sym_db.RegisterMessage(FrameworkInfo)
_sym_db.RegisterMessage(FrameworkInfo.FrameworkParam)

DeviceUsage = _reflection.GeneratedProtocolMessageType('DeviceUsage', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEUSAGE,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.DeviceUsage)
  })
_sym_db.RegisterMessage(DeviceUsage)

DeviceProcessUsage = _reflection.GeneratedProtocolMessageType('DeviceProcessUsage', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEPROCESSUSAGE,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.DeviceProcessUsage)
  })
_sym_db.RegisterMessage(DeviceProcessUsage)

ProcessUsage = _reflection.GeneratedProtocolMessageType('ProcessUsage', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSUSAGE,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.ProcessUsage)
  })
_sym_db.RegisterMessage(ProcessUsage)

NodeUsage = _reflection.GeneratedProtocolMessageType('NodeUsage', (_message.Message,), {

  'DriverInfo' : _reflection.GeneratedProtocolMessageType('DriverInfo', (_message.Message,), {
    'DESCRIPTOR' : _NODEUSAGE_DRIVERINFO,
    '__module__' : 'signals_pb2'
    # @@protoc_insertion_point(class_scope:graphsignal.signals.NodeUsage.DriverInfo)
    })
  ,
  'DESCRIPTOR' : _NODEUSAGE,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.NodeUsage)
  })
_sym_db.RegisterMessage(NodeUsage)
_sym_db.RegisterMessage(NodeUsage.DriverInfo)

AgentInfo = _reflection.GeneratedProtocolMessageType('AgentInfo', (_message.Message,), {
  'DESCRIPTOR' : _AGENTINFO,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.AgentInfo)
  })
_sym_db.RegisterMessage(AgentInfo)

AgentError = _reflection.GeneratedProtocolMessageType('AgentError', (_message.Message,), {
  'DESCRIPTOR' : _AGENTERROR,
  '__module__' : 'signals_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.signals.AgentError)
  })
_sym_db.RegisterMessage(AgentError)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SIGNALTYPE._serialized_start=5640
  _SIGNALTYPE._serialized_end=5789
  _UPLOADREQUEST._serialized_start=38
  _UPLOADREQUEST._serialized_end=131
  _UPLOADRESPONSE._serialized_start=133
  _UPLOADRESPONSE._serialized_end=149
  _SIGNALRECORD._serialized_start=152
  _SIGNALRECORD._serialized_end=335
  _WORKERSIGNAL._serialized_start=338
  _WORKERSIGNAL._serialized_end=1487
  _TAG._serialized_start=1489
  _TAG._serialized_end=1546
  _PARAM._serialized_start=1548
  _PARAM._serialized_end=1608
  _METRIC._serialized_start=1611
  _METRIC._serialized_end=1865
  _METRIC_RESERVOIR._serialized_start=1752
  _METRIC_RESERVOIR._serialized_end=1779
  _METRIC_METRICTYPE._serialized_start=1781
  _METRIC_METRICTYPE._serialized_end=1855
  _TRACEMETRICS._serialized_start=1868
  _TRACEMETRICS._serialized_end=2034
  _DATAMETRIC._serialized_start=2036
  _DATAMETRIC._serialized_end=2133
  _TRACESAMPLE._serialized_start=2135
  _TRACESAMPLE._serialized_end=2237
  _TRACESPAN._serialized_start=2240
  _TRACESPAN._serialized_end=2390
  _EXCEPTION._serialized_start=2392
  _EXCEPTION._serialized_end=2459
  _SEMVER._serialized_start=2461
  _SEMVER._serialized_end=2514
  _MEMORYALLOCATION._serialized_start=2517
  _MEMORYALLOCATION._serialized_end=2839
  _MEMORYALLOCATION_ALLOCATORTYPE._serialized_start=2771
  _MEMORYALLOCATION_ALLOCATORTYPE._serialized_end=2839
  _OPSTATS._serialized_start=2842
  _OPSTATS._serialized_end=3303
  _OPSTATS_OPTYPE._serialized_start=3227
  _OPSTATS_OPTYPE._serialized_end=3303
  _KERNELSTATS._serialized_start=3305
  _KERNELSTATS._serialized_end=3412
  _DATASTATS._serialized_start=3415
  _DATASTATS._serialized_end=3579
  _DATASTATS_DATACOUNT._serialized_start=3539
  _DATASTATS_DATACOUNT._serialized_end=3579
  _MODELINFO._serialized_start=3581
  _MODELINFO._serialized_end=3660
  _FRAMEWORKINFO._serialized_start=3663
  _FRAMEWORKINFO._serialized_end=3852
  _FRAMEWORKINFO_FRAMEWORKPARAM._serialized_start=3807
  _FRAMEWORKINFO_FRAMEWORKPARAM._serialized_end=3852
  _DEVICEUSAGE._serialized_start=3855
  _DEVICEUSAGE._serialized_end=4569
  _DEVICEUSAGE_DEVICETYPE._serialized_start=4512
  _DEVICEUSAGE_DEVICETYPE._serialized_end=4569
  _DEVICEPROCESSUSAGE._serialized_start=4571
  _DEVICEPROCESSUSAGE._serialized_end=4676
  _PROCESSUSAGE._serialized_start=4679
  _PROCESSUSAGE._serialized_end=5082
  _PROCESSUSAGE_RUNTIME._serialized_start=5038
  _PROCESSUSAGE_RUNTIME._serialized_end=5082
  _NODEUSAGE._serialized_start=5085
  _NODEUSAGE._serialized_end=5411
  _NODEUSAGE_DRIVERINFO._serialized_start=5368
  _NODEUSAGE_DRIVERINFO._serialized_end=5411
  _AGENTINFO._serialized_start=5414
  _AGENTINFO._serialized_end=5585
  _AGENTINFO_AGENTTYPE._serialized_start=5535
  _AGENTINFO_AGENTTYPE._serialized_end=5585
  _AGENTERROR._serialized_start=5587
  _AGENTERROR._serialized_end=5637
# @@protoc_insertion_point(module_scope)
