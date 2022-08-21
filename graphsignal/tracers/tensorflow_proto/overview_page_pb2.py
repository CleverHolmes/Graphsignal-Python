# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: graphsignal/tracers/tensorflow_proto/overview_page.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from graphsignal.tracers.tensorflow_proto import diagnostics_pb2 as graphsignal_dot_tracers_dot_tensorflow__proto_dot_diagnostics__pb2
from graphsignal.tracers.tensorflow_proto import input_pipeline_pb2 as graphsignal_dot_tracers_dot_tensorflow__proto_dot_input__pipeline__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8graphsignal/tracers/tensorflow_proto/overview_page.proto\x12\x13tensorflow.profiler\x1a\x19google/protobuf/any.proto\x1a\x36graphsignal/tracers/tensorflow_proto/diagnostics.proto\x1a\x39graphsignal/tracers/tensorflow_proto/input_pipeline.proto\"\xc2\x01\n\x0cOverviewTfOp\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x1a\n\x12self_time_fraction\x18\x03 \x01(\x01\x12 \n\x18\x63umulative_time_fraction\x18\x04 \x01(\x01\x12\x11\n\tflop_rate\x18\x05 \x01(\x01\x12!\n\x19is_op_tensorcore_eligible\x18\x06 \x01(\x08\x12\x1e\n\x16is_op_using_tensorcore\x18\x07 \x01(\x08\"\xf5\x04\n\x14OverviewPageAnalysis\x12\x1f\n\x17mxu_utilization_percent\x18\x01 \x01(\x01\x12 \n\x18\x64\x65vice_idle_time_percent\x18\x02 \x01(\x01\x12\x1e\n\x16host_idle_time_percent\x18\x03 \x01(\x01\x12\x39\n\x0etop_device_ops\x18\x04 \x03(\x0b\x32!.tensorflow.profiler.OverviewTfOp\x12\x13\n\x0bremark_text\x18\x05 \x01(\t\x12\x14\n\x0cremark_color\x18\x06 \x01(\t\x12:\n2flop_rate_utilization_relative_to_roofline_percent\x18\x07 \x01(\x01\x12:\n2memory_bw_utilization_relative_to_hw_limit_percent\x18\x08 \x01(\x01\x12$\n\x1c\x64\x65vice_compute_16bit_percent\x18\t \x01(\x01\x12$\n\x1c\x64\x65vice_compute_32bit_percent\x18\n \x01(\x01\x12\x1a\n\x12host_tf_op_percent\x18\x0b \x01(\x01\x12\x1c\n\x14\x64\x65vice_tf_op_percent\x18\x0c \x01(\x01\x12\x18\n\x10host_trace_level\x18\r \x01(\r\x12\"\n\x1ahost_op_time_eager_percent\x18\x0e \x01(\x01\x12$\n\x1c\x64\x65vice_op_time_eager_percent\x18\x0f \x01(\x01\x12\x32\n*device_op_time_outside_compilation_percent\x18\x10 \x01(\x01\"\x1f\n\x0fOverviewPageTip\x12\x0c\n\x04link\x18\x01 \x01(\t\"\xff\x01\n\x15GenericRecommendation\x12 \n\x18kernel_launch_bottleneck\x18\x01 \x01(\t\x12\x1f\n\x17kernel_launch_statement\x18\x02 \x01(\t\x12\x1c\n\x14\x61ll_other_bottleneck\x18\x03 \x01(\t\x12\x1b\n\x13\x61ll_other_statement\x18\x04 \x01(\t\x12\x1b\n\x13precision_statement\x18\x05 \x01(\t\x12%\n\x1d\x64\x65vice_collectives_bottleneck\x18\x06 \x01(\t\x12$\n\x1c\x64\x65vice_collectives_statement\x18\x07 \x01(\t\"\xdf\x04\n\x1aOverviewPageRecommendation\x12\x12\n\nbottleneck\x18\x01 \x01(\t\x12\x11\n\tstatement\x18\x02 \x01(\t\x12\x38\n\ninput_tips\x18\x0b \x03(\x0b\x32$.tensorflow.profiler.OverviewPageTip\x12\x18\n\x10output_statement\x18\t \x01(\t\x12\x1c\n\x14\x65\x61ger_statement_html\x18\x0c \x01(\t\x12*\n\"outside_compilation_statement_html\x18\r \x01(\t\x12\"\n\x1atf_function_statement_html\x18\n \x01(\t\x12\x37\n\thost_tips\x18\x03 \x03(\x0b\x32$.tensorflow.profiler.OverviewPageTip\x12\x39\n\x0b\x64\x65vice_tips\x18\x04 \x03(\x0b\x32$.tensorflow.profiler.OverviewPageTip\x12@\n\x12\x64ocumentation_tips\x18\x05 \x03(\x0b\x32$.tensorflow.profiler.OverviewPageTip\x12,\n\x0erecommendation\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x36\n\x08\x66\x61q_tips\x18\x07 \x03(\x0b\x32$.tensorflow.profiler.OverviewPageTip\x12<\n\x0einference_tips\x18\x08 \x03(\x0b\x32$.tensorflow.profiler.OverviewPageTip\"\x80\x01\n\"OverviewPageHostIndependentJobInfo\x12\x13\n\x0b\x63hange_list\x18\x01 \x01(\x03\x12\x12\n\nbuild_time\x18\x02 \x01(\x03\x12\x14\n\x0c\x62uild_target\x18\x03 \x01(\t\x12\x1b\n\x13profile_duration_ms\x18\x04 \x01(\r\"\x8b\x01\n OverviewPageHostDependentJobInfo\x12\x0f\n\x07host_id\x18\x01 \x01(\t\x12\x14\n\x0c\x63ommand_line\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\x03\x12\x13\n\x0b\x62ns_address\x18\x04 \x01(\t\x12\x17\n\x0fprofile_time_ns\x18\x05 \x01(\x04\"\x80\x04\n\x1aOverviewPageRunEnvironment\x12\x12\n\nhost_count\x18\x01 \x01(\x05\x12\x12\n\ntask_count\x18\x02 \x01(\x05\x12Q\n\thostnames\x18\x03 \x03(\x0b\x32>.tensorflow.profiler.OverviewPageRunEnvironment.HostnamesEntry\x12\x13\n\x0b\x64\x65vice_type\x18\x04 \x01(\t\x12\x19\n\x11\x64\x65vice_core_count\x18\x05 \x01(\x05\x12\x1b\n\x13per_core_batch_size\x18\x06 \x01(\x05\x12Z\n\x19host_independent_job_info\x18\x07 \x01(\x0b\x32\x37.tensorflow.profiler.OverviewPageHostIndependentJobInfo\x12V\n\x17host_dependent_job_info\x18\x08 \x03(\x0b\x32\x35.tensorflow.profiler.OverviewPageHostDependentJobInfo\x12\x15\n\rreplica_count\x18\t \x01(\x05\x12\x1d\n\x15num_cores_per_replica\x18\n \x01(\x05\x1a\x30\n\x0eHostnamesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"\xf1\x02\n\x0cOverviewPage\x12H\n\x0frun_environment\x18\x06 \x01(\x0b\x32/.tensorflow.profiler.OverviewPageRunEnvironment\x12H\n\x0einput_analysis\x18\x02 \x01(\x0b\x32\x30.tensorflow.profiler.InputPipelineAnalysisResult\x12;\n\x08\x61nalysis\x18\x03 \x01(\x0b\x32).tensorflow.profiler.OverviewPageAnalysis\x12G\n\x0erecommendation\x18\x04 \x01(\x0b\x32/.tensorflow.profiler.OverviewPageRecommendation\x12\x35\n\x0b\x64iagnostics\x18\x08 \x01(\x0b\x32 .tensorflow.profiler.DiagnosticsJ\x04\x08\x01\x10\x02J\x04\x08\x05\x10\x06J\x04\x08\x07\x10\x08\x62\x06proto3')



_OVERVIEWTFOP = DESCRIPTOR.message_types_by_name['OverviewTfOp']
_OVERVIEWPAGEANALYSIS = DESCRIPTOR.message_types_by_name['OverviewPageAnalysis']
_OVERVIEWPAGETIP = DESCRIPTOR.message_types_by_name['OverviewPageTip']
_GENERICRECOMMENDATION = DESCRIPTOR.message_types_by_name['GenericRecommendation']
_OVERVIEWPAGERECOMMENDATION = DESCRIPTOR.message_types_by_name['OverviewPageRecommendation']
_OVERVIEWPAGEHOSTINDEPENDENTJOBINFO = DESCRIPTOR.message_types_by_name['OverviewPageHostIndependentJobInfo']
_OVERVIEWPAGEHOSTDEPENDENTJOBINFO = DESCRIPTOR.message_types_by_name['OverviewPageHostDependentJobInfo']
_OVERVIEWPAGERUNENVIRONMENT = DESCRIPTOR.message_types_by_name['OverviewPageRunEnvironment']
_OVERVIEWPAGERUNENVIRONMENT_HOSTNAMESENTRY = _OVERVIEWPAGERUNENVIRONMENT.nested_types_by_name['HostnamesEntry']
_OVERVIEWPAGE = DESCRIPTOR.message_types_by_name['OverviewPage']
OverviewTfOp = _reflection.GeneratedProtocolMessageType('OverviewTfOp', (_message.Message,), {
  'DESCRIPTOR' : _OVERVIEWTFOP,
  '__module__' : 'graphsignal.tracers.tensorflow_proto.overview_page_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.OverviewTfOp)
  })
_sym_db.RegisterMessage(OverviewTfOp)

OverviewPageAnalysis = _reflection.GeneratedProtocolMessageType('OverviewPageAnalysis', (_message.Message,), {
  'DESCRIPTOR' : _OVERVIEWPAGEANALYSIS,
  '__module__' : 'graphsignal.tracers.tensorflow_proto.overview_page_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.OverviewPageAnalysis)
  })
_sym_db.RegisterMessage(OverviewPageAnalysis)

OverviewPageTip = _reflection.GeneratedProtocolMessageType('OverviewPageTip', (_message.Message,), {
  'DESCRIPTOR' : _OVERVIEWPAGETIP,
  '__module__' : 'graphsignal.tracers.tensorflow_proto.overview_page_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.OverviewPageTip)
  })
_sym_db.RegisterMessage(OverviewPageTip)

GenericRecommendation = _reflection.GeneratedProtocolMessageType('GenericRecommendation', (_message.Message,), {
  'DESCRIPTOR' : _GENERICRECOMMENDATION,
  '__module__' : 'graphsignal.tracers.tensorflow_proto.overview_page_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.GenericRecommendation)
  })
_sym_db.RegisterMessage(GenericRecommendation)

OverviewPageRecommendation = _reflection.GeneratedProtocolMessageType('OverviewPageRecommendation', (_message.Message,), {
  'DESCRIPTOR' : _OVERVIEWPAGERECOMMENDATION,
  '__module__' : 'graphsignal.tracers.tensorflow_proto.overview_page_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.OverviewPageRecommendation)
  })
_sym_db.RegisterMessage(OverviewPageRecommendation)

OverviewPageHostIndependentJobInfo = _reflection.GeneratedProtocolMessageType('OverviewPageHostIndependentJobInfo', (_message.Message,), {
  'DESCRIPTOR' : _OVERVIEWPAGEHOSTINDEPENDENTJOBINFO,
  '__module__' : 'graphsignal.tracers.tensorflow_proto.overview_page_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.OverviewPageHostIndependentJobInfo)
  })
_sym_db.RegisterMessage(OverviewPageHostIndependentJobInfo)

OverviewPageHostDependentJobInfo = _reflection.GeneratedProtocolMessageType('OverviewPageHostDependentJobInfo', (_message.Message,), {
  'DESCRIPTOR' : _OVERVIEWPAGEHOSTDEPENDENTJOBINFO,
  '__module__' : 'graphsignal.tracers.tensorflow_proto.overview_page_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.OverviewPageHostDependentJobInfo)
  })
_sym_db.RegisterMessage(OverviewPageHostDependentJobInfo)

OverviewPageRunEnvironment = _reflection.GeneratedProtocolMessageType('OverviewPageRunEnvironment', (_message.Message,), {

  'HostnamesEntry' : _reflection.GeneratedProtocolMessageType('HostnamesEntry', (_message.Message,), {
    'DESCRIPTOR' : _OVERVIEWPAGERUNENVIRONMENT_HOSTNAMESENTRY,
    '__module__' : 'graphsignal.tracers.tensorflow_proto.overview_page_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.profiler.OverviewPageRunEnvironment.HostnamesEntry)
    })
  ,
  'DESCRIPTOR' : _OVERVIEWPAGERUNENVIRONMENT,
  '__module__' : 'graphsignal.tracers.tensorflow_proto.overview_page_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.OverviewPageRunEnvironment)
  })
_sym_db.RegisterMessage(OverviewPageRunEnvironment)
_sym_db.RegisterMessage(OverviewPageRunEnvironment.HostnamesEntry)

OverviewPage = _reflection.GeneratedProtocolMessageType('OverviewPage', (_message.Message,), {
  'DESCRIPTOR' : _OVERVIEWPAGE,
  '__module__' : 'graphsignal.tracers.tensorflow_proto.overview_page_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.OverviewPage)
  })
_sym_db.RegisterMessage(OverviewPage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OVERVIEWPAGERUNENVIRONMENT_HOSTNAMESENTRY._options = None
  _OVERVIEWPAGERUNENVIRONMENT_HOSTNAMESENTRY._serialized_options = b'8\001'
  _OVERVIEWTFOP._serialized_start=224
  _OVERVIEWTFOP._serialized_end=418
  _OVERVIEWPAGEANALYSIS._serialized_start=421
  _OVERVIEWPAGEANALYSIS._serialized_end=1050
  _OVERVIEWPAGETIP._serialized_start=1052
  _OVERVIEWPAGETIP._serialized_end=1083
  _GENERICRECOMMENDATION._serialized_start=1086
  _GENERICRECOMMENDATION._serialized_end=1341
  _OVERVIEWPAGERECOMMENDATION._serialized_start=1344
  _OVERVIEWPAGERECOMMENDATION._serialized_end=1951
  _OVERVIEWPAGEHOSTINDEPENDENTJOBINFO._serialized_start=1954
  _OVERVIEWPAGEHOSTINDEPENDENTJOBINFO._serialized_end=2082
  _OVERVIEWPAGEHOSTDEPENDENTJOBINFO._serialized_start=2085
  _OVERVIEWPAGEHOSTDEPENDENTJOBINFO._serialized_end=2224
  _OVERVIEWPAGERUNENVIRONMENT._serialized_start=2227
  _OVERVIEWPAGERUNENVIRONMENT._serialized_end=2739
  _OVERVIEWPAGERUNENVIRONMENT_HOSTNAMESENTRY._serialized_start=2691
  _OVERVIEWPAGERUNENVIRONMENT_HOSTNAMESENTRY._serialized_end=2739
  _OVERVIEWPAGE._serialized_start=2742
  _OVERVIEWPAGE._serialized_end=3111
# @@protoc_insertion_point(module_scope)
