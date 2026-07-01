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

"""Unit tests for the opt-in method timing instrumentation."""

import pytest

from ansys.sam.sysml2.tools import timing


@pytest.fixture
def profiler():
    """Return the shared profiler reset to a known disabled state around each test."""
    instance = timing.get_profiler()
    instance.disable()
    instance.reset()
    yield instance
    instance.disable()
    instance.reset()


class TestProfilerDisabled:
    """The decorators must be transparent no-ops while profiling is disabled."""

    def test_timed_is_noop_when_disabled(self, profiler):
        calls = []

        @timing.timed
        def add(left, right):
            calls.append((left, right))
            return left + right

        assert add(2, 3) == 5
        assert calls == [(2, 3)]
        assert profiler.report() == "PySAM timing report: no measurements recorded."

    def test_profile_entrypoint_is_noop_when_disabled(self, profiler, capsys):
        @timing.profile_entrypoint
        def entry():
            return "done"

        assert entry() == "done"
        assert capsys.readouterr().err == ""


class TestProfilerEnabled:
    """When enabled the profiler records counts and totals and reports them."""

    def test_record_accumulates_count_and_total(self, profiler):
        profiler.enable()
        profiler.record("foo", 0.5)
        profiler.record("foo", 1.5)

        report = profiler.report()

        assert "foo" in report
        assert "2" in report

    def test_timed_records_when_enabled(self, profiler):
        profiler.enable()

        @timing.timed
        def work():
            return 42

        assert work() == 42
        assert work() == 42
        assert "work" in profiler.report()

    def test_reset_clears_records(self, profiler):
        profiler.enable()
        profiler.record("foo", 1.0)
        profiler.reset()

        assert profiler.report() == "PySAM timing report: no measurements recorded."

    def test_profile_entrypoint_prints_report_to_stderr(self, profiler, capsys):
        profiler.enable()

        @timing.timed
        def step():
            return 1

        @timing.profile_entrypoint
        def entry():
            step()
            return "ok"

        assert entry() == "ok"
        err = capsys.readouterr().err
        assert "PySAM timing report" in err
        assert "step" in err

    def test_entrypoint_resets_between_runs(self, profiler, capsys):
        profiler.enable()

        @timing.timed
        def step():
            return 1

        @timing.profile_entrypoint
        def entry():
            step()
            return "ok"

        entry()
        entry()
        capsys.readouterr()

        assert profiler.report().count("step") == 1
