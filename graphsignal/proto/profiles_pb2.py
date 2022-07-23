# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profiles.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eprofiles.proto\x12\x14graphsignal.profiles\"X\n\rUploadRequest\x12\x34\n\x0bml_profiles\x18\x01 \x03(\x0b\x32\x1f.graphsignal.profiles.MLProfile\x12\x11\n\tupload_ms\x18\x02 \x01(\x04\"\x10\n\x0eUploadResponse\"\xb0\x01\n\rProfileRecord\x12\x0f\n\x07\x64\x61ta_id\x18\x01 \x01(\t\x12\x13\n\x0bworkload_id\x18\x02 \x01(\t\x12\x12\n\nprofile_id\x18\x03 \x01(\t\x12\x33\n\nml_profile\x18\x04 \x01(\x0b\x32\x1f.graphsignal.profiles.MLProfile\x12\x1a\n\x12\x64\x61ta_retention_sec\x18\x05 \x01(\x04\x12\x14\n\x0ctime_skew_ms\x18\x06 \x01(\x12\"\xa9\x07\n\tMLProfile\x12\x15\n\rworkload_name\x18\x01 \x01(\t\x12\x11\n\tworker_id\x18\x1c \x01(\t\x12\x0e\n\x06run_id\x18\x02 \x01(\t\x12\x14\n\x0crun_start_ms\x18\' \x01(\x04\x12\x10\n\x08start_us\x18\x05 \x01(\x04\x12\x0e\n\x06\x65nd_us\x18\x06 \x01(\x04\x12\'\n\x04tags\x18  \x03(\x0b\x32\x19.graphsignal.profiles.Tag\x12\x37\n\nframeworks\x18$ \x03(\x0b\x32#.graphsignal.profiles.FrameworkInfo\x12+\n\x06params\x18\x16 \x03(\x0b\x32\x1b.graphsignal.profiles.Param\x12-\n\x07metrics\x18\x1e \x03(\x0b\x32\x1c.graphsignal.profiles.Metric\x12=\n\x0finference_stats\x18% \x01(\x0b\x32$.graphsignal.profiles.InferenceStats\x12\x33\n\nmodel_info\x18& \x01(\x0b\x32\x1f.graphsignal.profiles.ModelInfo\x12<\n\ncomm_usage\x18\x1b \x01(\x0b\x32(.graphsignal.profiles.CommunicationUsage\x12\x33\n\nnode_usage\x18\x19 \x01(\x0b\x32\x1f.graphsignal.profiles.NodeUsage\x12\x39\n\rprocess_usage\x18\x1a \x01(\x0b\x32\".graphsignal.profiles.ProcessUsage\x12\x37\n\x0c\x64\x65vice_usage\x18\x12 \x03(\x0b\x32!.graphsignal.profiles.DeviceUsage\x12/\n\x08op_stats\x18\x0b \x03(\x0b\x32\x1d.graphsignal.profiles.OpStats\x12\x37\n\x0ckernel_stats\x18\x0c \x03(\x0b\x32!.graphsignal.profiles.KernelStats\x12\x12\n\ntrace_data\x18! \x01(\x0c\x12\x1a\n\x12is_trace_available\x18\" \x01(\x08\x12\x39\n\rprofiler_info\x18# \x01(\x0b\x32\".graphsignal.profiles.ProfilerInfo\x12<\n\x0fprofiler_errors\x18\x07 \x03(\x0b\x32#.graphsignal.profiles.ProfilerError\"5\n\x06SemVer\x12\r\n\x05major\x18\x01 \x01(\x05\x12\r\n\x05minor\x18\x02 \x01(\x05\x12\r\n\x05patch\x18\x03 \x01(\x05\"\xb8\x02\n\rFrameworkInfo\x12?\n\x04type\x18\x01 \x01(\x0e\x32\x31.graphsignal.profiles.FrameworkInfo.FrameworkType\x12-\n\x07version\x18\x02 \x01(\x0b\x32\x1c.graphsignal.profiles.SemVer\"\xb6\x01\n\rFrameworkType\x12\x17\n\x13\x46RAMEWORK_UNDEFINED\x10\x00\x12\x18\n\x14TENSORFLOW_FRAMEWORK\x10\x01\x12\x15\n\x11PYTORCH_FRAMEWORK\x10\x02\x12\x13\n\x0fKERAS_FRAMEWORK\x10\x03\x12\x1f\n\x1bPYTORCH_LIGHTNING_FRAMEWORK\x10\x04\x12\x11\n\rJAX_FRAMEWORK\x10\x07\x12\x12\n\x0eONNX_FRAMEWORK\x10\t\"\x14\n\x03Tag\x12\r\n\x05value\x18\x01 \x01(\t\"$\n\x05Param\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"%\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\"\xbc\x01\n\x0eInferenceStats\x12\x17\n\x0finference_count\x18\t \x01(\x04\x12\x1d\n\x15inference_time_p95_us\x18\n \x01(\x01\x12\x1d\n\x15inference_time_avg_us\x18\x0b \x01(\x01\x12\x16\n\x0einference_rate\x18\x0c \x01(\x01\x12\x13\n\x0bsample_rate\x18\r \x01(\x01\x12\x12\n\nbatch_size\x18\x04 \x01(\x05\x12\x12\n\nworld_size\x18\x06 \x01(\x05\"\xb2\x01\n\tModelInfo\x12\x41\n\x0cmodel_format\x18\x01 \x01(\x0e\x32+.graphsignal.profiles.ModelInfo.ModelFormat\x12\x18\n\x10model_size_bytes\x18\x02 \x01(\x04\"H\n\x0bModelFormat\x12\x14\n\x10\x46ORMAT_UNDEFINED\x10\x00\x12\x12\n\x0ePYTORCH_FORMAT\x10\x01\x12\x0f\n\x0bONNX_FORMAT\x10\x02\"\xd5\x01\n\x12\x43ommunicationUsage\x12W\n\x0c\x62\x61\x63kend_type\x18\x01 \x01(\x0e\x32\x41.graphsignal.profiles.CommunicationUsage.CommunicationBackendType\"f\n\x18\x43ommunicationBackendType\x12#\n\x1f\x43OMMUNICATION_BACKEND_UNDEFINED\x10\x00\x12\x08\n\x04NCCL\x10\x01\x12\x08\n\x04GLOO\x10\x02\x12\x07\n\x03MPI\x10\x03\x12\x08\n\x04RING\x10\x04\"\xc6\x01\n\tNodeUsage\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x12\n\nip_address\x18\x07 \x01(\t\x12\x11\n\tnode_rank\x18\x08 \x01(\x05\x12\x10\n\x08mem_used\x18\t \x01(\x04\x12\x11\n\tmem_total\x18\n \x01(\x04\x12\x10\n\x08platform\x18\x02 \x01(\t\x12\x0f\n\x07machine\x18\x03 \x01(\t\x12\x0f\n\x07os_name\x18\x04 \x01(\t\x12\x12\n\nos_version\x18\x05 \x01(\t\x12\x13\n\x0bnum_devices\x18\x06 \x01(\x05\"\xf9\x02\n\x0cProcessUsage\x12\x12\n\nprocess_id\x18\x05 \x01(\t\x12\x10\n\x08start_ms\x18\x0e \x01(\x04\x12\x12\n\nlocal_rank\x18\x0c \x01(\x05\x12\x13\n\x0bglobal_rank\x18\x0f \x01(\x05\x12\x10\n\x08\x63pu_name\x18\x10 \x01(\t\x12\x19\n\x11\x63pu_usage_percent\x18\x01 \x01(\x01\x12\x0f\n\x07max_rss\x18\x02 \x01(\x04\x12\x13\n\x0b\x63urrent_rss\x18\x03 \x01(\x04\x12\x0f\n\x07vm_size\x18\x04 \x01(\x04\x12;\n\x07runtime\x18\x06 \x01(\x0e\x32*.graphsignal.profiles.ProcessUsage.Runtime\x12\x35\n\x0fruntime_version\x18\x07 \x01(\x0b\x32\x1c.graphsignal.profiles.SemVer\x12\x14\n\x0cruntime_impl\x18\x08 \x01(\t\",\n\x07Runtime\x12\x15\n\x11RUNTIME_UNDEFINED\x10\x00\x12\n\n\x06PYTHON\x10\x01\"\x95\x04\n\x0b\x44\x65viceUsage\x12\x35\n\x0b\x64\x65vice_type\x18\x0b \x01(\x0e\x32 .graphsignal.profiles.DeviceType\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\x12\x14\n\x0c\x61rchitecture\x18\x11 \x01(\t\x12\x38\n\x12\x63ompute_capability\x18\x0f \x01(\x0b\x32\x1c.graphsignal.profiles.SemVer\x12\x11\n\tmem_total\x18\x03 \x01(\x04\x12\x10\n\x08mem_used\x18\x04 \x01(\x04\x12\x10\n\x08mem_free\x18\x05 \x01(\x04\x12\x1f\n\x17gpu_utilization_percent\x18\x06 \x01(\x01\x12\x1a\n\x12mem_access_percent\x18\x10 \x01(\x01\x12\x1a\n\x12pcie_throughput_tx\x18\r \x01(\x01\x12\x1a\n\x12pcie_throughput_rx\x18\x0e \x01(\x01\x12!\n\x19nvlink_throughput_tx_kibs\x18\x12 \x01(\x01\x12!\n\x19nvlink_throughput_rx_kibs\x18\x13 \x01(\x01\x12\x12\n\ngpu_temp_c\x18\x08 \x01(\x01\x12\x15\n\rpower_usage_w\x18\t \x01(\x01\x12\x19\n\x11\x66\x61n_speed_percent\x18\n \x01(\x01\x12\x1f\n\x17mxu_utilization_percent\x18\x0c \x01(\x01\"\xea\x03\n\x07OpStats\x12\x35\n\x0b\x64\x65vice_type\x18\x01 \x01(\x0e\x32 .graphsignal.profiles.DeviceType\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x0f\n\x07op_type\x18\x03 \x01(\t\x12\x0f\n\x07op_name\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\x04\x12\x1a\n\x12total_host_time_us\x18\x06 \x01(\x04\x12\x1c\n\x14total_device_time_us\x18\x07 \x01(\x04\x12\x19\n\x11self_host_time_us\x18\x08 \x01(\x04\x12\x1b\n\x13self_device_time_us\x18\t \x01(\x04\x12\x19\n\x11total_host_memory\x18\n \x01(\x04\x12\x1b\n\x13total_device_memory\x18\x0b \x01(\x04\x12\x18\n\x10self_host_memory\x18\x0c \x01(\x04\x12\x1a\n\x12self_device_memory\x18\r \x01(\x04\x12\x1d\n\x15self_host_memory_rate\x18\x0e \x01(\x04\x12\x1f\n\x17self_device_memory_rate\x18\x0f \x01(\x04\x12\r\n\x05\x66lops\x18\x10 \x01(\x04\x12\x15\n\rflops_per_sec\x18\x12 \x01(\x01\x12\x1e\n\x16tensorcore_utilization\x18\x11 \x01(\x01\"\xbe\x01\n\x0bKernelStats\x12\x35\n\x0b\x64\x65vice_type\x18\x01 \x01(\x0e\x32 .graphsignal.profiles.DeviceType\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x0f\n\x07op_name\x18\x03 \x01(\t\x12\x13\n\x0bkernel_name\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\x04\x12\x13\n\x0b\x64uration_ns\x18\x06 \x01(\x04\x12\x1b\n\x13is_using_tensorcore\x18\x07 \x01(\x08\"\xa8\x03\n\x0cProfilerInfo\x12P\n\x17operation_profiler_type\x18\x01 \x01(\x0e\x32/.graphsignal.profiles.ProfilerInfo.ProfilerType\x12P\n\x17\x66ramework_profiler_type\x18\x02 \x01(\x0e\x32/.graphsignal.profiles.ProfilerInfo.ProfilerType\x12-\n\x07version\x18\x03 \x01(\x0b\x32\x1c.graphsignal.profiles.SemVer\"\xc4\x01\n\x0cProfilerType\x12\x16\n\x12PROFILER_UNDEFINED\x10\x00\x12\x14\n\x10GENERIC_PROFILER\x10\x01\x12\x17\n\x13TENSORFLOW_PROFILER\x10\x02\x12\x14\n\x10PYTORCH_PROFILER\x10\x03\x12\x12\n\x0eKERAS_PROFILER\x10\x04\x12\x1e\n\x1aPYTORCH_LIGHTNING_PROFILER\x10\x06\x12\x10\n\x0cJAX_PROFILER\x10\x08\x12\x11\n\rONNX_PROFILER\x10\n\"5\n\rProfilerError\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x13\n\x0bstack_trace\x18\x02 \x01(\t*B\n\nDeviceType\x12\x19\n\x15\x44\x45VICE_TYPE_UNDEFINED\x10\x00\x12\x07\n\x03\x43PU\x10\x01\x12\x07\n\x03GPU\x10\x02\x12\x07\n\x03TPU\x10\x03\x62\x06proto3')

_DEVICETYPE = DESCRIPTOR.enum_types_by_name['DeviceType']
DeviceType = enum_type_wrapper.EnumTypeWrapper(_DEVICETYPE)
DEVICE_TYPE_UNDEFINED = 0
CPU = 1
GPU = 2
TPU = 3


_UPLOADREQUEST = DESCRIPTOR.message_types_by_name['UploadRequest']
_UPLOADRESPONSE = DESCRIPTOR.message_types_by_name['UploadResponse']
_PROFILERECORD = DESCRIPTOR.message_types_by_name['ProfileRecord']
_MLPROFILE = DESCRIPTOR.message_types_by_name['MLProfile']
_SEMVER = DESCRIPTOR.message_types_by_name['SemVer']
_FRAMEWORKINFO = DESCRIPTOR.message_types_by_name['FrameworkInfo']
_TAG = DESCRIPTOR.message_types_by_name['Tag']
_PARAM = DESCRIPTOR.message_types_by_name['Param']
_METRIC = DESCRIPTOR.message_types_by_name['Metric']
_INFERENCESTATS = DESCRIPTOR.message_types_by_name['InferenceStats']
_MODELINFO = DESCRIPTOR.message_types_by_name['ModelInfo']
_COMMUNICATIONUSAGE = DESCRIPTOR.message_types_by_name['CommunicationUsage']
_NODEUSAGE = DESCRIPTOR.message_types_by_name['NodeUsage']
_PROCESSUSAGE = DESCRIPTOR.message_types_by_name['ProcessUsage']
_DEVICEUSAGE = DESCRIPTOR.message_types_by_name['DeviceUsage']
_OPSTATS = DESCRIPTOR.message_types_by_name['OpStats']
_KERNELSTATS = DESCRIPTOR.message_types_by_name['KernelStats']
_PROFILERINFO = DESCRIPTOR.message_types_by_name['ProfilerInfo']
_PROFILERERROR = DESCRIPTOR.message_types_by_name['ProfilerError']
_FRAMEWORKINFO_FRAMEWORKTYPE = _FRAMEWORKINFO.enum_types_by_name['FrameworkType']
_MODELINFO_MODELFORMAT = _MODELINFO.enum_types_by_name['ModelFormat']
_COMMUNICATIONUSAGE_COMMUNICATIONBACKENDTYPE = _COMMUNICATIONUSAGE.enum_types_by_name['CommunicationBackendType']
_PROCESSUSAGE_RUNTIME = _PROCESSUSAGE.enum_types_by_name['Runtime']
_PROFILERINFO_PROFILERTYPE = _PROFILERINFO.enum_types_by_name['ProfilerType']
UploadRequest = _reflection.GeneratedProtocolMessageType('UploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADREQUEST,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.UploadRequest)
  })
_sym_db.RegisterMessage(UploadRequest)

UploadResponse = _reflection.GeneratedProtocolMessageType('UploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADRESPONSE,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.UploadResponse)
  })
_sym_db.RegisterMessage(UploadResponse)

ProfileRecord = _reflection.GeneratedProtocolMessageType('ProfileRecord', (_message.Message,), {
  'DESCRIPTOR' : _PROFILERECORD,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.ProfileRecord)
  })
_sym_db.RegisterMessage(ProfileRecord)

MLProfile = _reflection.GeneratedProtocolMessageType('MLProfile', (_message.Message,), {
  'DESCRIPTOR' : _MLPROFILE,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.MLProfile)
  })
_sym_db.RegisterMessage(MLProfile)

SemVer = _reflection.GeneratedProtocolMessageType('SemVer', (_message.Message,), {
  'DESCRIPTOR' : _SEMVER,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.SemVer)
  })
_sym_db.RegisterMessage(SemVer)

FrameworkInfo = _reflection.GeneratedProtocolMessageType('FrameworkInfo', (_message.Message,), {
  'DESCRIPTOR' : _FRAMEWORKINFO,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.FrameworkInfo)
  })
_sym_db.RegisterMessage(FrameworkInfo)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.Tag)
  })
_sym_db.RegisterMessage(Tag)

Param = _reflection.GeneratedProtocolMessageType('Param', (_message.Message,), {
  'DESCRIPTOR' : _PARAM,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.Param)
  })
_sym_db.RegisterMessage(Param)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.Metric)
  })
_sym_db.RegisterMessage(Metric)

InferenceStats = _reflection.GeneratedProtocolMessageType('InferenceStats', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCESTATS,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.InferenceStats)
  })
_sym_db.RegisterMessage(InferenceStats)

ModelInfo = _reflection.GeneratedProtocolMessageType('ModelInfo', (_message.Message,), {
  'DESCRIPTOR' : _MODELINFO,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.ModelInfo)
  })
_sym_db.RegisterMessage(ModelInfo)

CommunicationUsage = _reflection.GeneratedProtocolMessageType('CommunicationUsage', (_message.Message,), {
  'DESCRIPTOR' : _COMMUNICATIONUSAGE,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.CommunicationUsage)
  })
_sym_db.RegisterMessage(CommunicationUsage)

NodeUsage = _reflection.GeneratedProtocolMessageType('NodeUsage', (_message.Message,), {
  'DESCRIPTOR' : _NODEUSAGE,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.NodeUsage)
  })
_sym_db.RegisterMessage(NodeUsage)

ProcessUsage = _reflection.GeneratedProtocolMessageType('ProcessUsage', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSUSAGE,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.ProcessUsage)
  })
_sym_db.RegisterMessage(ProcessUsage)

DeviceUsage = _reflection.GeneratedProtocolMessageType('DeviceUsage', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEUSAGE,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.DeviceUsage)
  })
_sym_db.RegisterMessage(DeviceUsage)

OpStats = _reflection.GeneratedProtocolMessageType('OpStats', (_message.Message,), {
  'DESCRIPTOR' : _OPSTATS,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.OpStats)
  })
_sym_db.RegisterMessage(OpStats)

KernelStats = _reflection.GeneratedProtocolMessageType('KernelStats', (_message.Message,), {
  'DESCRIPTOR' : _KERNELSTATS,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.KernelStats)
  })
_sym_db.RegisterMessage(KernelStats)

ProfilerInfo = _reflection.GeneratedProtocolMessageType('ProfilerInfo', (_message.Message,), {
  'DESCRIPTOR' : _PROFILERINFO,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.ProfilerInfo)
  })
_sym_db.RegisterMessage(ProfilerInfo)

ProfilerError = _reflection.GeneratedProtocolMessageType('ProfilerError', (_message.Message,), {
  'DESCRIPTOR' : _PROFILERERROR,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.ProfilerError)
  })
_sym_db.RegisterMessage(ProfilerError)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DEVICETYPE._serialized_start=4609
  _DEVICETYPE._serialized_end=4675
  _UPLOADREQUEST._serialized_start=40
  _UPLOADREQUEST._serialized_end=128
  _UPLOADRESPONSE._serialized_start=130
  _UPLOADRESPONSE._serialized_end=146
  _PROFILERECORD._serialized_start=149
  _PROFILERECORD._serialized_end=325
  _MLPROFILE._serialized_start=328
  _MLPROFILE._serialized_end=1265
  _SEMVER._serialized_start=1267
  _SEMVER._serialized_end=1320
  _FRAMEWORKINFO._serialized_start=1323
  _FRAMEWORKINFO._serialized_end=1635
  _FRAMEWORKINFO_FRAMEWORKTYPE._serialized_start=1453
  _FRAMEWORKINFO_FRAMEWORKTYPE._serialized_end=1635
  _TAG._serialized_start=1637
  _TAG._serialized_end=1657
  _PARAM._serialized_start=1659
  _PARAM._serialized_end=1695
  _METRIC._serialized_start=1697
  _METRIC._serialized_end=1734
  _INFERENCESTATS._serialized_start=1737
  _INFERENCESTATS._serialized_end=1925
  _MODELINFO._serialized_start=1928
  _MODELINFO._serialized_end=2106
  _MODELINFO_MODELFORMAT._serialized_start=2034
  _MODELINFO_MODELFORMAT._serialized_end=2106
  _COMMUNICATIONUSAGE._serialized_start=2109
  _COMMUNICATIONUSAGE._serialized_end=2322
  _COMMUNICATIONUSAGE_COMMUNICATIONBACKENDTYPE._serialized_start=2220
  _COMMUNICATIONUSAGE_COMMUNICATIONBACKENDTYPE._serialized_end=2322
  _NODEUSAGE._serialized_start=2325
  _NODEUSAGE._serialized_end=2523
  _PROCESSUSAGE._serialized_start=2526
  _PROCESSUSAGE._serialized_end=2903
  _PROCESSUSAGE_RUNTIME._serialized_start=2859
  _PROCESSUSAGE_RUNTIME._serialized_end=2903
  _DEVICEUSAGE._serialized_start=2906
  _DEVICEUSAGE._serialized_end=3439
  _OPSTATS._serialized_start=3442
  _OPSTATS._serialized_end=3932
  _KERNELSTATS._serialized_start=3935
  _KERNELSTATS._serialized_end=4125
  _PROFILERINFO._serialized_start=4128
  _PROFILERINFO._serialized_end=4552
  _PROFILERINFO_PROFILERTYPE._serialized_start=4356
  _PROFILERINFO_PROFILERTYPE._serialized_end=4552
  _PROFILERERROR._serialized_start=4554
  _PROFILERERROR._serialized_end=4607
# @@protoc_insertion_point(module_scope)
