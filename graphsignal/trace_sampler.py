import logging
import time

logger = logging.getLogger('graphsignal')

class TraceSampler:
    MIN_INTERVAL_SEC = 60

    def __init__(self):
        self._current_trace_idx = 0
        self._trace_counters = {}
        self._last_reset_ts = time.time()

    def sample(self, group, limit_per_interval=1, limit_after=10):
        self._current_trace_idx += 1

        sampled_trace_idx = self._current_trace_idx

        now = time.time()

        # reset counters
        if now - self._last_reset_ts > self.MIN_INTERVAL_SEC:
            self._trace_counters = {}
            self._last_reset_ts = time.time()

        # check counters
        if group in self._trace_counters:
            self._trace_counters[group] += 1
        else:
            self._trace_counters[group] = 1
        if self._trace_counters[group] <= limit_per_interval:
            return True

        # check include_trace_idx
        if sampled_trace_idx <= limit_after:
            return True

        return False
