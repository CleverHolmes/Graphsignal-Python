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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eprofiles.proto\x12\x14graphsignal.profiles\"X\n\rUploadRequest\x12\x34\n\x0bml_profiles\x18\x01 \x03(\x0b\x32\x1f.graphsignal.profiles.MLProfile\x12\x11\n\tupload_ms\x18\x02 \x01(\x04\"\x10\n\x0eUploadResponse\"\xc2\x01\n\rProfileRecord\x12\x0f\n\x07\x64\x61ta_id\x18\x01 \x01(\t\x12\x13\n\x0bworkload_id\x18\x02 \x01(\t\x12\x10\n\x08phase_id\x18\x07 \x01(\t\x12\x12\n\nprofile_id\x18\x03 \x01(\t\x12\x33\n\nml_profile\x18\x04 \x01(\x0b\x32\x1f.graphsignal.profiles.MLProfile\x12\x1a\n\x12\x64\x61ta_retention_sec\x18\x05 \x01(\x04\x12\x14\n\x0ctime_skew_ms\x18\x06 \x01(\x12\"\xf4\x05\n\tMLProfile\x12\x15\n\rworkload_name\x18\x01 \x01(\t\x12\x12\n\nphase_name\x18\x1d \x01(\t\x12\x11\n\tworker_id\x18\x1c \x01(\t\x12\x0e\n\x06run_id\x18\x02 \x01(\t\x12\x10\n\x08start_us\x18\x05 \x01(\x04\x12\x0e\n\x06\x65nd_us\x18\x06 \x01(\x04\x12\'\n\x04tags\x18  \x03(\x0b\x32\x19.graphsignal.profiles.Tag\x12+\n\x06params\x18\x16 \x03(\x0b\x32\x1b.graphsignal.profiles.Param\x12-\n\x07metrics\x18\x1e \x03(\x0b\x32\x1c.graphsignal.profiles.Metric\x12\x33\n\nstep_stats\x18\x15 \x01(\x0b\x32\x1f.graphsignal.profiles.StepStats\x12<\n\ncomm_usage\x18\x1b \x01(\x0b\x32(.graphsignal.profiles.CommunicationUsage\x12\x33\n\nnode_usage\x18\x19 \x01(\x0b\x32\x1f.graphsignal.profiles.NodeUsage\x12\x39\n\rprocess_usage\x18\x1a \x01(\x0b\x32\".graphsignal.profiles.ProcessUsage\x12\x37\n\x0c\x64\x65vice_usage\x18\x12 \x03(\x0b\x32!.graphsignal.profiles.DeviceUsage\x12/\n\x08op_stats\x18\x0b \x03(\x0b\x32\x1d.graphsignal.profiles.OpStats\x12\x37\n\x0ckernel_stats\x18\x0c \x03(\x0b\x32!.graphsignal.profiles.KernelStats\x12\x12\n\ntrace_data\x18! \x01(\x0c\x12\x1a\n\x12is_trace_available\x18\" \x01(\x08\x12<\n\x0fprofiler_errors\x18\x07 \x03(\x0b\x32#.graphsignal.profiles.ProfilerError\"5\n\x06SemVer\x12\r\n\x05major\x18\x01 \x01(\x05\x12\r\n\x05minor\x18\x02 \x01(\x05\x12\r\n\x05patch\x18\x03 \x01(\x05\"\x14\n\x03Tag\x12\r\n\x05value\x18\x01 \x01(\t\"$\n\x05Param\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"%\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\"\xa3\x01\n\tStepStats\x12\x12\n\nstep_count\x18\x01 \x01(\x04\x12\x14\n\x0csample_count\x18\x07 \x01(\x04\x12\x12\n\nflop_count\x18\x08 \x01(\x04\x12\x15\n\rtotal_time_us\x18\x02 \x01(\x04\x12\x12\n\nbatch_size\x18\x04 \x01(\x05\x12\x19\n\x11\x64\x65vice_batch_size\x18\x05 \x01(\x05\x12\x12\n\nworld_size\x18\x06 \x01(\x05\"\xd5\x01\n\x12\x43ommunicationUsage\x12W\n\x0c\x62\x61\x63kend_type\x18\x01 \x01(\x0e\x32\x41.graphsignal.profiles.CommunicationUsage.CommunicationBackendType\"f\n\x18\x43ommunicationBackendType\x12#\n\x1f\x43OMMUNICATION_BACKEND_UNDEFINED\x10\x00\x12\x08\n\x04NCCL\x10\x01\x12\x08\n\x04GLOO\x10\x02\x12\x07\n\x03MPI\x10\x03\x12\x08\n\x04RING\x10\x04\"\xc6\x01\n\tNodeUsage\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x12\n\nip_address\x18\x07 \x01(\t\x12\x11\n\tnode_rank\x18\x08 \x01(\x05\x12\x10\n\x08mem_used\x18\t \x01(\x04\x12\x11\n\tmem_total\x18\n \x01(\x04\x12\x10\n\x08platform\x18\x02 \x01(\t\x12\x0f\n\x07machine\x18\x03 \x01(\t\x12\x0f\n\x07os_name\x18\x04 \x01(\t\x12\x12\n\nos_version\x18\x05 \x01(\t\x12\x13\n\x0bnum_devices\x18\x06 \x01(\x05\"\xe9\x04\n\x0cProcessUsage\x12\x12\n\nprocess_id\x18\x05 \x01(\t\x12\x10\n\x08start_ms\x18\x0e \x01(\x04\x12\x12\n\nlocal_rank\x18\x0c \x01(\x05\x12\x13\n\x0bglobal_rank\x18\x0f \x01(\x05\x12\x19\n\x11\x63pu_usage_percent\x18\x01 \x01(\x01\x12\x0f\n\x07max_rss\x18\x02 \x01(\x04\x12\x13\n\x0b\x63urrent_rss\x18\x03 \x01(\x04\x12\x0f\n\x07vm_size\x18\x04 \x01(\x04\x12;\n\x07runtime\x18\x06 \x01(\x0e\x32*.graphsignal.profiles.ProcessUsage.Runtime\x12\x35\n\x0fruntime_version\x18\x07 \x01(\x0b\x32\x1c.graphsignal.profiles.SemVer\x12\x14\n\x0cruntime_impl\x18\x08 \x01(\t\x12\x44\n\x0cml_framework\x18\t \x01(\x0e\x32..graphsignal.profiles.ProcessUsage.MLFramework\x12:\n\x14ml_framework_version\x18\n \x01(\x0b\x32\x1c.graphsignal.profiles.SemVer\x12\x36\n\x10profiler_version\x18\x0b \x01(\x0b\x32\x1c.graphsignal.profiles.SemVer\",\n\x07Runtime\x12\x15\n\x11RUNTIME_UNDEFINED\x10\x00\x12\n\n\x06PYTHON\x10\x01\"F\n\x0bMLFramework\x12\x1a\n\x16ML_FRAMEWORK_UNDEFINED\x10\x00\x12\x0e\n\nTENSORFLOW\x10\x01\x12\x0b\n\x07PYTORCH\x10\x02\"\xd4\x03\n\x0b\x44\x65viceUsage\x12\x35\n\x0b\x64\x65vice_type\x18\x0b \x01(\x0e\x32 .graphsignal.profiles.DeviceType\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\x12\x14\n\x0c\x61rchitecture\x18\x11 \x01(\t\x12\x38\n\x12\x63ompute_capability\x18\x0f \x01(\x0b\x32\x1c.graphsignal.profiles.SemVer\x12\x11\n\tmem_total\x18\x03 \x01(\x04\x12\x10\n\x08mem_used\x18\x04 \x01(\x04\x12\x10\n\x08mem_free\x18\x05 \x01(\x04\x12\x1f\n\x17gpu_utilization_percent\x18\x06 \x01(\x01\x12\x1f\n\x17mem_utilization_percent\x18\x07 \x01(\x01\x12\x1a\n\x12pcie_throughput_tx\x18\r \x01(\x01\x12\x1a\n\x12pcie_throughput_rx\x18\x0e \x01(\x01\x12\x12\n\ngpu_temp_c\x18\x08 \x01(\x01\x12\x15\n\rpower_usage_w\x18\t \x01(\x01\x12\x19\n\x11\x66\x61n_speed_percent\x18\n \x01(\x01\x12\x1f\n\x17mxu_utilization_percent\x18\x0c \x01(\x01\"\xea\x03\n\x07OpStats\x12\x35\n\x0b\x64\x65vice_type\x18\x01 \x01(\x0e\x32 .graphsignal.profiles.DeviceType\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x0f\n\x07op_type\x18\x03 \x01(\t\x12\x0f\n\x07op_name\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\x04\x12\x1a\n\x12total_host_time_us\x18\x06 \x01(\x04\x12\x1c\n\x14total_device_time_us\x18\x07 \x01(\x04\x12\x19\n\x11self_host_time_us\x18\x08 \x01(\x04\x12\x1b\n\x13self_device_time_us\x18\t \x01(\x04\x12\x19\n\x11total_host_memory\x18\n \x01(\x04\x12\x1b\n\x13total_device_memory\x18\x0b \x01(\x04\x12\x18\n\x10self_host_memory\x18\x0c \x01(\x04\x12\x1a\n\x12self_device_memory\x18\r \x01(\x04\x12\x1d\n\x15self_host_memory_rate\x18\x0e \x01(\x04\x12\x1f\n\x17self_device_memory_rate\x18\x0f \x01(\x04\x12\r\n\x05\x66lops\x18\x10 \x01(\x04\x12\x15\n\rflops_per_sec\x18\x12 \x01(\x01\x12\x1e\n\x16tensorcore_utilization\x18\x11 \x01(\x01\"\xbe\x01\n\x0bKernelStats\x12\x35\n\x0b\x64\x65vice_type\x18\x01 \x01(\x0e\x32 .graphsignal.profiles.DeviceType\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x0f\n\x07op_name\x18\x03 \x01(\t\x12\x13\n\x0bkernel_name\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\x04\x12\x13\n\x0b\x64uration_ns\x18\x06 \x01(\x04\x12\x1b\n\x13is_using_tensorcore\x18\x07 \x01(\x08\"5\n\rProfilerError\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x13\n\x0bstack_trace\x18\x02 \x01(\t*B\n\nDeviceType\x12\x19\n\x15\x44\x45VICE_TYPE_UNDEFINED\x10\x00\x12\x07\n\x03\x43PU\x10\x01\x12\x07\n\x03GPU\x10\x02\x12\x07\n\x03TPU\x10\x03\x62\x06proto3')

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
_TAG = DESCRIPTOR.message_types_by_name['Tag']
_PARAM = DESCRIPTOR.message_types_by_name['Param']
_METRIC = DESCRIPTOR.message_types_by_name['Metric']
_STEPSTATS = DESCRIPTOR.message_types_by_name['StepStats']
_COMMUNICATIONUSAGE = DESCRIPTOR.message_types_by_name['CommunicationUsage']
_NODEUSAGE = DESCRIPTOR.message_types_by_name['NodeUsage']
_PROCESSUSAGE = DESCRIPTOR.message_types_by_name['ProcessUsage']
_DEVICEUSAGE = DESCRIPTOR.message_types_by_name['DeviceUsage']
_OPSTATS = DESCRIPTOR.message_types_by_name['OpStats']
_KERNELSTATS = DESCRIPTOR.message_types_by_name['KernelStats']
_PROFILERERROR = DESCRIPTOR.message_types_by_name['ProfilerError']
_COMMUNICATIONUSAGE_COMMUNICATIONBACKENDTYPE = _COMMUNICATIONUSAGE.enum_types_by_name['CommunicationBackendType']
_PROCESSUSAGE_RUNTIME = _PROCESSUSAGE.enum_types_by_name['Runtime']
_PROCESSUSAGE_MLFRAMEWORK = _PROCESSUSAGE.enum_types_by_name['MLFramework']
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

StepStats = _reflection.GeneratedProtocolMessageType('StepStats', (_message.Message,), {
  'DESCRIPTOR' : _STEPSTATS,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.StepStats)
  })
_sym_db.RegisterMessage(StepStats)

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

ProfilerError = _reflection.GeneratedProtocolMessageType('ProfilerError', (_message.Message,), {
  'DESCRIPTOR' : _PROFILERERROR,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.ProfilerError)
  })
_sym_db.RegisterMessage(ProfilerError)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DEVICETYPE._serialized_start=3673
  _DEVICETYPE._serialized_end=3739
  _UPLOADREQUEST._serialized_start=40
  _UPLOADREQUEST._serialized_end=128
  _UPLOADRESPONSE._serialized_start=130
  _UPLOADRESPONSE._serialized_end=146
  _PROFILERECORD._serialized_start=149
  _PROFILERECORD._serialized_end=343
  _MLPROFILE._serialized_start=346
  _MLPROFILE._serialized_end=1102
  _SEMVER._serialized_start=1104
  _SEMVER._serialized_end=1157
  _TAG._serialized_start=1159
  _TAG._serialized_end=1179
  _PARAM._serialized_start=1181
  _PARAM._serialized_end=1217
  _METRIC._serialized_start=1219
  _METRIC._serialized_end=1256
  _STEPSTATS._serialized_start=1259
  _STEPSTATS._serialized_end=1422
  _COMMUNICATIONUSAGE._serialized_start=1425
  _COMMUNICATIONUSAGE._serialized_end=1638
  _COMMUNICATIONUSAGE_COMMUNICATIONBACKENDTYPE._serialized_start=1536
  _COMMUNICATIONUSAGE_COMMUNICATIONBACKENDTYPE._serialized_end=1638
  _NODEUSAGE._serialized_start=1641
  _NODEUSAGE._serialized_end=1839
  _PROCESSUSAGE._serialized_start=1842
  _PROCESSUSAGE._serialized_end=2459
  _PROCESSUSAGE_RUNTIME._serialized_start=2343
  _PROCESSUSAGE_RUNTIME._serialized_end=2387
  _PROCESSUSAGE_MLFRAMEWORK._serialized_start=2389
  _PROCESSUSAGE_MLFRAMEWORK._serialized_end=2459
  _DEVICEUSAGE._serialized_start=2462
  _DEVICEUSAGE._serialized_end=2930
  _OPSTATS._serialized_start=2933
  _OPSTATS._serialized_end=3423
  _KERNELSTATS._serialized_start=3426
  _KERNELSTATS._serialized_end=3616
  _PROFILERERROR._serialized_start=3618
  _PROFILERERROR._serialized_end=3671
# @@protoc_insertion_point(module_scope)
