# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Opt-in timing instrumentation for method-level profiling.

Profiling is disabled by default and turned on by setting the ``PYSAM_PROFILE`` environment
variable (to any non-empty value). When disabled the decorators add no measurable overhead.
"""

import functools
import os
import sys
import time


class Profiler:
    """Accumulate per-method call counts and elapsed time for opt-in profiling."""

    def __init__(self):
        """Construct a new instance, enabled from the ``PYSAM_PROFILE`` environment variable."""
        self.enabled = bool(os.environ.get("PYSAM_PROFILE"))
        self._records = {}

    def enable(self) -> None:
        """Turn profiling on."""
        self.enabled = True

    def disable(self) -> None:
        """Turn profiling off."""
        self.enabled = False

    def reset(self) -> None:
        """Clear all recorded measurements."""
        self._records = {}

    def record(self, name: str, elapsed: float) -> None:
        """Add a single measurement for ``name``."""
        count, total = self._records.get(name, (0, 0.0))
        self._records[name] = (count + 1, total + elapsed)

    def report(self) -> str:
        """Build a summary of recorded measurements sorted by total time descending."""
        if not self._records:
            return "PySAM timing report: no measurements recorded."
        rows = sorted(self._records.items(), key=lambda item: item[1][1], reverse=True)
        lines = [
            f"{'method':<60} {'calls':>7} {'total ms':>12} {'avg ms':>10}",
            f"{'-' * 60} {'-' * 7} {'-' * 12} {'-' * 10}",
        ]
        for name, (count, total) in rows:
            total_ms = total * 1000
            avg_ms = total_ms / count if count else 0.0
            lines.append(f"{name:<60} {count:>7} {total_ms:>12.2f} {avg_ms:>10.3f}")
        return "\n".join(lines)

    def print_report(self, label: str, total: float) -> None:
        """Write the timing summary for ``label`` to standard error."""
        header = f"=== PySAM timing report: {label} ({total * 1000:.2f} ms total) ==="
        print(header, file=sys.stderr)
        print(self.report(), file=sys.stderr)


_profiler = Profiler()


def get_profiler() -> Profiler:
    """Return the shared profiler instance."""
    return _profiler


def timed(func):
    """Record the wrapped callable's elapsed time when profiling is enabled.

    Parameters
    ----------
    func : callable
        Function to measure.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Measure elapsed time and record it under the function name."""
        if not _profiler.enabled:
            return func(*args, **kwargs)
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            _profiler.record(func.__qualname__, time.perf_counter() - start)

    return wrapper


def profile_entrypoint(func):
    """Reset the profiler before the call and print the report after it when enabled.

    Parameters
    ----------
    func : callable
        Entry-point function whose nested ``timed`` calls are aggregated and reported.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Run the entry point and emit a timing report when profiling is enabled."""
        if not _profiler.enabled:
            return func(*args, **kwargs)
        _profiler.reset()
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            _profiler.print_report(func.__qualname__, time.perf_counter() - start)

    return wrapper
