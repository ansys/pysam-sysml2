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

"""Opt-in live progress reporting for the project build loop.

Reporting is disabled by default; pass ``progress=True`` (and optionally ``progress_log``)
when loading a project. When disabled the reporter is a no-op with no measurable overhead.
"""

from __future__ import annotations

from pathlib import Path
import sys
import time

# File name (sibling of the recap log) that collects every fetched element id.
_IDS_LOG_NAME = "elements_fetched.log"


class BuildProgressReporter:
    """Emit live build metrics: per-round queried/received counts, totals, and elapsed time.

    Output is split across two append-only destinations when a ``log_path`` is given:
    the recap lines (identical to standard error) go to ``log_path`` (e.g. ``build.log``),
    and every fetched element id, one per line, goes to a sibling ``elements_fetched.log``.
    Both files are only appended to; the caller is responsible for deleting them between runs.
    """

    def __init__(
        self,
        enabled: bool,
        label: str,
        log_path: str | Path | None = None,
    ):
        """Construct a reporter.

        Parameters
        ----------
        enabled : bool
            When False, every method is a no-op.
        label : str
            Human-readable label for the build being reported (e.g. the project id).
        log_path : str | Path | None, default: None
            Optional recap log path (e.g. ``build.log``); when set, recap lines are appended
            there and fetched ids are appended to a sibling ``elements_fetched.log``.
        """
        self.enabled = enabled
        self._label = label
        self._start = time.perf_counter()
        self._recap_file = None
        self._ids_file = None
        if self.enabled and log_path is not None:
            recap_path = Path(log_path)
            self._recap_file = recap_path.open("a", encoding="utf-8")
            self._ids_file = (recap_path.parent / _IDS_LOG_NAME).open("a", encoding="utf-8")
        self._emit(f"load start: {label}")

    def _elapsed(self) -> float:
        """Return seconds elapsed since the reporter was constructed."""
        return time.perf_counter() - self._start

    def _emit(self, message: str) -> None:
        """Write a recap line to stderr and the recap log (build.log) when enabled."""
        if not self.enabled:
            return
        line = f"[pysam progress] {message}"
        print(line, file=sys.stderr)
        if self._recap_file is not None:
            self._recap_file.write(line + "\n")
            self._recap_file.flush()

    def _write_ids(self, ids) -> None:
        """Append each id string, one per line, to elements_fetched.log when enabled."""
        if not self.enabled or self._ids_file is None:
            return
        for element_id in ids:
            self._ids_file.write(f"{element_id}\n")
        self._ids_file.flush()

    def bulk_loaded(self, elements) -> None:
        """Report the initial bulk fetch: recap to stderr/build.log, ids to elements_fetched.log."""
        if not self.enabled:
            return
        self._emit(f"bulk: fetched {len(elements)} elements (elapsed {self._elapsed():.2f}s)")
        self._write_ids(element.get("@id") for element in elements)

    def round_start(self, round_no: int, queried_ids) -> None:
        """Report the start of a missing-fetch round, before its query is sent.

        Emits a recap line and appends the queried ids to elements_fetched.log so the
        output advances immediately instead of appearing frozen during the long query wait.
        """
        if not self.enabled:
            return
        self._emit(
            f"round {round_no} start: querying {len(queried_ids)} ids "
            f"(elapsed {self._elapsed():.2f}s)"
        )
        self._write_ids(queried_ids)

    def round(
        self,
        round_no: int,
        queried_ids,
        received_elements,
        total_mapped: int,
        remaining: int,
    ) -> None:
        """Report one missing-fetch round.

        Parameters
        ----------
        round_no : int
            1-based round counter.
        queried_ids : collection
            Ids requested in this round's query.
        received_elements : list[dict]
            Element payloads returned by the query.
        total_mapped : int
            Number of elements mapped into the project so far.
        remaining : int
            New missing ids still to resolve after this round.
        """
        if not self.enabled:
            return
        self._emit(
            f"round {round_no}: queried {len(queried_ids)} "
            f"-> received {len(received_elements)} "
            f"| mapped {total_mapped} | remaining {remaining} "
            f"| elapsed {self._elapsed():.2f}s"
        )

    def done(self, total_mapped: int, rounds: int) -> None:
        """Report completion and close both log files."""
        self._emit(
            f"done: {total_mapped} elements mapped in {rounds} round(s), "
            f"elapsed {self._elapsed():.2f}s"
        )
        if self._recap_file is not None:
            self._recap_file.close()
            self._recap_file = None
        if self._ids_file is not None:
            self._ids_file.close()
            self._ids_file = None
