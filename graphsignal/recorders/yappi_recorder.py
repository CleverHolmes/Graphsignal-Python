import logging
import os
import json
import re
import yappi

import graphsignal
from graphsignal.recorders.base_recorder import BaseRecorder
from graphsignal.proto_utils import parse_semver
from graphsignal.proto import signals_pb2
from graphsignal.proto_utils import add_framework_param

logger = logging.getLogger('graphsignal')

class YappiRecorder(BaseRecorder):
    def __init__(self):
        self._exclude_path = os.path.dirname(os.path.realpath(graphsignal.__file__))

    def setup(self):
        pass

    def on_trace_start(self, signal, context, options):
        if not options.enable_profiling:
            return

        yappi.set_clock_type("wall")
        yappi.start()

    def on_trace_stop(self, signal, context, options):
        if not options.enable_profiling:
            return

        if yappi.is_running():
            yappi.stop()
        
    def on_trace_read(self, signal, context, options):
        if not options.enable_profiling:
            return

        self._convert_to_profile(signal, yappi.get_func_stats())
        yappi.clear_stats()

    def _convert_to_profile(self, signal, ystats):
        stats = yappi.convert2pstats(ystats)

        stats.sort_stats('cumtime')
        func_keys = stats.fcn_list[:] if stats.fcn_list else list(stats.stats.keys())

        func_list = []
        total_tt = 0
        visited = {}
        for func_key in func_keys:
            func_stats = stats.stats[func_key]
            file_name, line_num, func_name = func_key
            if self._has_exclude_func(stats.stats, func_key, visited):
                continue
            cc, nc, tt, ct, _ = func_stats
            func_list.append((file_name, line_num, func_name, nc, tt, ct))
            total_tt += tt

        for file_name, line_num, func_name, nc, tt, ct in func_list[:250]:
            op_stats = signal.op_profile.add()
            op_stats.profiler_type = signals_pb2.OpStats.ProfilerType.YAPPI_PROFILER
            op_stats.op_type = signals_pb2.OpStats.OpType.PYTHON_OP
            op_stats.op_name = _format_frame(file_name, line_num, func_name)
            op_stats.count = int(nc)
            op_stats.host_time_ns = _ns(ct)
            op_stats.self_host_time_ns = _ns(tt)
            if total_tt > 0:
                op_stats.self_host_time_percent = tt / total_tt * 100

    def _has_exclude_func(self, stats, func_key, visited):
        if func_key in visited:
            return visited[func_key]

        file_name, _, _ = func_key
        _, _, _, _, callers = stats[func_key]

        if file_name.startswith(self._exclude_path):
            visited[func_key] = True
            return True
        else:
            visited[func_key] = False

        for caller_key in callers.keys():
            if self._has_exclude_func(stats, caller_key, visited):
                visited[func_key] = True
                return True

        return False


def _ns(sec):
    return int(sec * 1e9)


def _format_frame(file_name, line_num, func_name):
    if file_name == '~':
        file_name = ''

    if file_name and line_num and func_name:
        return '{func_name} ({file_name}:{line_num})'.format(
            file_name=file_name,
            func_name=func_name,
            line_num=line_num)
    elif file_name and func_name:
        return '{func_name} ({file_name})'.format(
            file_name=file_name,
            func_name=func_name)
    elif func_name:
        return func_name
    else:
        return 'unknown'