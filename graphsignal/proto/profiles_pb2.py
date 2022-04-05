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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eprofiles.proto\x12\x14graphsignal.profiles\"X\n\rUploadRequest\x12\x34\n\x0bml_profiles\x18\x01 \x03(\x0b\x32\x1f.graphsignal.profiles.MLProfile\x12\x11\n\tupload_ms\x18\x02 \x01(\x04\"\x10\n\x0eUploadResponse\"\x9a\x01\n\rProfileRecord\x12\x0f\n\x07\x64\x61ta_id\x18\x01 \x01(\t\x12\x13\n\x0bworkload_id\x18\x02 \x01(\t\x12\x12\n\nprofile_id\x18\x03 \x01(\t\x12\x33\n\nml_profile\x18\x04 \x01(\x0b\x32\x1f.graphsignal.profiles.MLProfile\x12\x1a\n\x12\x64\x61ta_retention_sec\x18\x05 \x01(\x04\"\xd4\x04\n\tMLProfile\x12\x15\n\rworkload_name\x18\x01 \x01(\t\x12\x0e\n\x06run_id\x18\x02 \x01(\t\x12\x14\n\x0crun_start_ms\x18\x03 \x01(\x04\x12\x10\n\x08start_us\x18\x05 \x01(\x04\x12\x0e\n\x06\x65nd_us\x18\x06 \x01(\x04\x12<\n\x0fprofiler_errors\x18\x07 \x03(\x0b\x32#.graphsignal.profiles.ProfilerError\x12(\n\x04span\x18\x10 \x01(\x0b\x32\x1a.graphsignal.profiles.Span\x12\x30\n\x08metadata\x18\x08 \x03(\x0b\x32\x1e.graphsignal.profiles.Metadata\x12\x35\n\x07run_env\x18\t \x01(\x0b\x32$.graphsignal.profiles.RunEnvironment\x12\x39\n\x07summary\x18\n \x01(\x0b\x32(.graphsignal.profiles.PerformanceSummary\x12/\n\x08op_stats\x18\x0b \x03(\x0b\x32\x1d.graphsignal.profiles.OpStats\x12\x37\n\x0ckernel_stats\x18\x0c \x03(\x0b\x32!.graphsignal.profiles.KernelStats\x12\x39\n\rprocess_usage\x18\x0e \x01(\x0b\x32\".graphsignal.profiles.ProcessUsage\x12\x37\n\x0c\x64\x65vice_usage\x18\x0f \x03(\x0b\x32!.graphsignal.profiles.DeviceUsage\"\xe5\x01\n\x04Span\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x04type\x18\x02 \x01(\x0e\x32#.graphsignal.profiles.Span.SpanType\x12\x13\n\x0b\x64uration_us\x18\x03 \x01(\x04\"\x86\x01\n\x08SpanType\x12\x17\n\x13SPAN_TYPE_UNDEFINED\x10\x00\x12\x11\n\rTRAINING_STEP\x10\x01\x12\x12\n\x0eTRAINING_BATCH\x10\x02\x12\x14\n\x10VALIDATION_BATCH\x10\x03\x12\x0e\n\nTEST_BATCH\x10\x04\x12\x14\n\x10PREDICTION_BATCH\x10\x05\"&\n\x08Metadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x9f\x04\n\x0eRunEnvironment\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x10\n\x08platform\x18\x02 \x01(\t\x12\x0f\n\x07machine\x18\x03 \x01(\t\x12\x0f\n\x07os_name\x18\x04 \x01(\t\x12\x12\n\nos_version\x18\x05 \x01(\t\x12=\n\x07runtime\x18\x06 \x01(\x0e\x32,.graphsignal.profiles.RunEnvironment.Runtime\x12\x35\n\x0fruntime_version\x18\x07 \x01(\x0b\x32\x1c.graphsignal.profiles.SemVer\x12\x14\n\x0cruntime_impl\x18\x08 \x01(\t\x12\x46\n\x0cml_framework\x18\t \x01(\x0e\x32\x30.graphsignal.profiles.RunEnvironment.MLFramework\x12:\n\x14ml_framework_version\x18\n \x01(\x0b\x32\x1c.graphsignal.profiles.SemVer\x12-\n\x07\x64\x65vices\x18\x0b \x03(\x0b\x32\x1c.graphsignal.profiles.Device\",\n\x07Runtime\x12\x15\n\x11RUNTIME_UNDEFINED\x10\x00\x12\n\n\x06PYTHON\x10\x01\"F\n\x0bMLFramework\x12\x1a\n\x16ML_FRAMEWORK_UNDEFINED\x10\x00\x12\x0e\n\nTENSORFLOW\x10\x01\x12\x0b\n\x07PYTORCH\x10\x02\"5\n\x06SemVer\x12\r\n\x05major\x18\x01 \x01(\x05\x12\r\n\x05minor\x18\x02 \x01(\x05\x12\r\n\x05patch\x18\x03 \x01(\x05\"\xaf\x01\n\x06\x44\x65vice\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .graphsignal.profiles.DeviceType\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\x0fis_cuda_enabled\x18\x03 \x01(\x08\x12\x38\n\x12\x63ompute_capability\x18\x04 \x01(\x0b\x32\x1c.graphsignal.profiles.SemVer\x12\x14\n\x0ctotal_memory\x18\x05 \x01(\x04\"t\n\x0cProcessUsage\x12\x12\n\nprocess_id\x18\x05 \x01(\t\x12\x19\n\x11\x63pu_usage_percent\x18\x01 \x01(\x01\x12\x0f\n\x07max_rss\x18\x02 \x01(\x04\x12\x13\n\x0b\x63urrent_rss\x18\x03 \x01(\x04\x12\x0f\n\x07vm_size\x18\x04 \x01(\x04\"\xcc\x02\n\x0b\x44\x65viceUsage\x12\x35\n\x0b\x64\x65vice_type\x18\x0b \x01(\x0e\x32 .graphsignal.profiles.DeviceType\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\x12\x11\n\tmem_total\x18\x03 \x01(\x04\x12\x10\n\x08mem_used\x18\x04 \x01(\x04\x12\x10\n\x08mem_free\x18\x05 \x01(\x04\x12\x1f\n\x17gpu_utilization_percent\x18\x06 \x01(\x01\x12\x1f\n\x17mem_utilization_percent\x18\x07 \x01(\x01\x12\x12\n\ngpu_temp_c\x18\x08 \x01(\x01\x12\x15\n\rpower_usage_w\x18\t \x01(\x01\x12\x19\n\x11\x66\x61n_speed_percent\x18\n \x01(\x01\x12\x1f\n\x17mxu_utilization_percent\x18\x0c \x01(\x01\"\x94\x02\n\x12PerformanceSummary\x12\x1b\n\x13\x64\x65vice_idle_percent\x18\x01 \x01(\x01\x12\x19\n\x11host_idle_percent\x18\x02 \x01(\x01\x12$\n\x1c\x64\x65vice_compute_16bit_percent\x18\x03 \x01(\x01\x12$\n\x1c\x64\x65vice_compute_32bit_percent\x18\x04 \x01(\x01\x12\x17\n\x0fhost_op_percent\x18\x06 \x01(\x01\x12\x19\n\x11\x64\x65vice_op_percent\x18\x07 \x01(\x01\x12\x17\n\x0fmxu_utilization\x18\x08 \x01(\x01\x12\x15\n\rinput_percent\x18\t \x01(\x01\x12\x16\n\x0eoutput_percent\x18\n \x01(\x01\"\xd3\x03\n\x07OpStats\x12\x35\n\x0b\x64\x65vice_type\x18\x01 \x01(\x0e\x32 .graphsignal.profiles.DeviceType\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x0f\n\x07op_type\x18\x03 \x01(\t\x12\x0f\n\x07op_name\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\x04\x12\x1a\n\x12total_host_time_us\x18\x06 \x01(\x04\x12\x1c\n\x14total_device_time_us\x18\x07 \x01(\x04\x12\x19\n\x11self_host_time_us\x18\x08 \x01(\x04\x12\x1b\n\x13self_device_time_us\x18\t \x01(\x04\x12\x19\n\x11total_host_memory\x18\n \x01(\x04\x12\x1b\n\x13total_device_memory\x18\x0b \x01(\x04\x12\x18\n\x10self_host_memory\x18\x0c \x01(\x04\x12\x1a\n\x12self_device_memory\x18\r \x01(\x04\x12\x1d\n\x15self_host_memory_rate\x18\x0e \x01(\x04\x12\x1f\n\x17self_device_memory_rate\x18\x0f \x01(\x04\x12\r\n\x05\x66lops\x18\x10 \x01(\x04\x12\x1e\n\x16tensorcore_utilization\x18\x11 \x01(\x01\"\xbe\x01\n\x0bKernelStats\x12\x35\n\x0b\x64\x65vice_type\x18\x01 \x01(\x0e\x32 .graphsignal.profiles.DeviceType\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x0f\n\x07op_name\x18\x03 \x01(\t\x12\x13\n\x0bkernel_name\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\x04\x12\x13\n\x0b\x64uration_ns\x18\x06 \x01(\x04\x12\x1b\n\x13is_using_tensorcore\x18\x07 \x01(\x08\"5\n\rProfilerError\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x13\n\x0bstack_trace\x18\x02 \x01(\t*B\n\nDeviceType\x12\x19\n\x15\x44\x45VICE_TYPE_UNDEFINED\x10\x00\x12\x07\n\x03\x43PU\x10\x01\x12\x07\n\x03GPU\x10\x02\x12\x07\n\x03TPU\x10\x03\x62\x06proto3')

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
_SPAN = DESCRIPTOR.message_types_by_name['Span']
_METADATA = DESCRIPTOR.message_types_by_name['Metadata']
_RUNENVIRONMENT = DESCRIPTOR.message_types_by_name['RunEnvironment']
_SEMVER = DESCRIPTOR.message_types_by_name['SemVer']
_DEVICE = DESCRIPTOR.message_types_by_name['Device']
_PROCESSUSAGE = DESCRIPTOR.message_types_by_name['ProcessUsage']
_DEVICEUSAGE = DESCRIPTOR.message_types_by_name['DeviceUsage']
_PERFORMANCESUMMARY = DESCRIPTOR.message_types_by_name['PerformanceSummary']
_OPSTATS = DESCRIPTOR.message_types_by_name['OpStats']
_KERNELSTATS = DESCRIPTOR.message_types_by_name['KernelStats']
_PROFILERERROR = DESCRIPTOR.message_types_by_name['ProfilerError']
_SPAN_SPANTYPE = _SPAN.enum_types_by_name['SpanType']
_RUNENVIRONMENT_RUNTIME = _RUNENVIRONMENT.enum_types_by_name['Runtime']
_RUNENVIRONMENT_MLFRAMEWORK = _RUNENVIRONMENT.enum_types_by_name['MLFramework']
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

Span = _reflection.GeneratedProtocolMessageType('Span', (_message.Message,), {
  'DESCRIPTOR' : _SPAN,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.Span)
  })
_sym_db.RegisterMessage(Span)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.Metadata)
  })
_sym_db.RegisterMessage(Metadata)

RunEnvironment = _reflection.GeneratedProtocolMessageType('RunEnvironment', (_message.Message,), {
  'DESCRIPTOR' : _RUNENVIRONMENT,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.RunEnvironment)
  })
_sym_db.RegisterMessage(RunEnvironment)

SemVer = _reflection.GeneratedProtocolMessageType('SemVer', (_message.Message,), {
  'DESCRIPTOR' : _SEMVER,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.SemVer)
  })
_sym_db.RegisterMessage(SemVer)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.Device)
  })
_sym_db.RegisterMessage(Device)

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

PerformanceSummary = _reflection.GeneratedProtocolMessageType('PerformanceSummary', (_message.Message,), {
  'DESCRIPTOR' : _PERFORMANCESUMMARY,
  '__module__' : 'profiles_pb2'
  # @@protoc_insertion_point(class_scope:graphsignal.profiles.PerformanceSummary)
  })
_sym_db.RegisterMessage(PerformanceSummary)

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
  _DEVICETYPE._serialized_start=3405
  _DEVICETYPE._serialized_end=3471
  _UPLOADREQUEST._serialized_start=40
  _UPLOADREQUEST._serialized_end=128
  _UPLOADRESPONSE._serialized_start=130
  _UPLOADRESPONSE._serialized_end=146
  _PROFILERECORD._serialized_start=149
  _PROFILERECORD._serialized_end=303
  _MLPROFILE._serialized_start=306
  _MLPROFILE._serialized_end=902
  _SPAN._serialized_start=905
  _SPAN._serialized_end=1134
  _SPAN_SPANTYPE._serialized_start=1000
  _SPAN_SPANTYPE._serialized_end=1134
  _METADATA._serialized_start=1136
  _METADATA._serialized_end=1174
  _RUNENVIRONMENT._serialized_start=1177
  _RUNENVIRONMENT._serialized_end=1720
  _RUNENVIRONMENT_RUNTIME._serialized_start=1604
  _RUNENVIRONMENT_RUNTIME._serialized_end=1648
  _RUNENVIRONMENT_MLFRAMEWORK._serialized_start=1650
  _RUNENVIRONMENT_MLFRAMEWORK._serialized_end=1720
  _SEMVER._serialized_start=1722
  _SEMVER._serialized_end=1775
  _DEVICE._serialized_start=1778
  _DEVICE._serialized_end=1953
  _PROCESSUSAGE._serialized_start=1955
  _PROCESSUSAGE._serialized_end=2071
  _DEVICEUSAGE._serialized_start=2074
  _DEVICEUSAGE._serialized_end=2406
  _PERFORMANCESUMMARY._serialized_start=2409
  _PERFORMANCESUMMARY._serialized_end=2685
  _OPSTATS._serialized_start=2688
  _OPSTATS._serialized_end=3155
  _KERNELSTATS._serialized_start=3158
  _KERNELSTATS._serialized_end=3348
  _PROFILERERROR._serialized_start=3350
  _PROFILERERROR._serialized_end=3403
# @@protoc_insertion_point(module_scope)
