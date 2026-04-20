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

"""Generated include use case usage class from metamodel."""

from __future__ import annotations

from .perform_action_usage import PerformActionUsage
from .use_case_usage import UseCaseUsage


class IncludeUseCaseUsage(UseCaseUsage, PerformActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.IncludeUseCaseUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._use_case_included = None

    @property
    def use_case_included(self) -> "UseCaseUsage":  # noqa: F821
        """
        Get the use case included property.

        Returns
        -------
        "UseCaseUsage"
            Value of property use case included.
        """
        return self._use_case_included

    @use_case_included.setter
    def use_case_included(self, value: "UseCaseUsage"):  # noqa: F821
        """
        Set the use_case_included property.

        Parameters
        ----------
        value: "UseCaseUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "use_case_included", value)
        self._use_case_included = value
