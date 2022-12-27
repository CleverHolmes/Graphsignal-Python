import logging
import os
import json
import re
import cProfile, pstats

import graphsignal
from graphsignal.recorders.base_recorder import BaseRecorder
from graphsignal.proto_utils import parse_semver
from graphsignal.proto import signals_pb2
from graphsignal.proto_utils import add_framework_param

logger = logging.getLogger('graphsignal')

class CProfileRecorder(BaseRecorder):
    def __init__(self):
        self._profiler = None
        self._exclude_path = os.path.dirname(os.path.realpath(graphsignal.__file__))

    def setup(self):
        pass

    def on_trace_start(self, signal, context, options):
        if not options.enable_profiling:
            return

        self._profiler = cProfile.Profile()
        self._profiler.enable()

    def on_trace_stop(self, signal, context, options):
        if not options.enable_profiling:
            return

        if not self._profiler:
            return

        self._profiler.disable()
        
    def on_trace_read(self, signal, context, options):
        if not options.enable_profiling:
            return

        if not self._profiler:
            return

        self._convert_to_profile(signal)
        self._profiler = None

    def _convert_to_profile(self, signal):
        signal.call_profile.profile_type = signals_pb2.Profile.ProfileType.PROFILE_TYPE_PYTHON
        stats = pstats.Stats(self._profiler)

        stats.sort_stats('time')
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

        for file_name, line_num, func_name, nc, tt, ct in func_list[:25]:
            call_stats = signal.call_profile.stats.add()
            call_stats.file_name = file_name
            call_stats.line_num = line_num
            call_stats.func_name = func_name
            call_stats.count = int(nc)
            call_stats.total_self_wall_time_ns = _to_ns(tt)
            call_stats.total_cum_wall_time_ns = _to_ns(ct)
            if total_tt > 0:
                call_stats.total_self_wall_time_percent = tt / total_tt * 100

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

def _to_ns(sec):
    return int(sec * 1e9)
