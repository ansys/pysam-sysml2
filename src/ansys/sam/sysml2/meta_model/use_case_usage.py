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

"""Generated use case usage class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .case_usage import CaseUsage


class UseCaseUsage(CaseUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.UseCaseUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._included_use_case = ObservedList(self, "included_use_case")
        self._use_case_definition = None

    @property
    def included_use_case(self) -> List["UseCaseUsage"]:  # noqa: F821
        """
        Get the included use case property.

        Returns
        -------
        List["UseCaseUsage"]
            Value of property included use case.
        """
        return self._included_use_case

    @property
    def use_case_definition(self) -> "UseCaseDefinition":  # noqa: F821
        """
        Get the use case definition property.

        Returns
        -------
        "UseCaseDefinition"
            Value of property use case definition.
        """
        return self._use_case_definition

    @use_case_definition.setter
    def use_case_definition(self, value: "UseCaseDefinition"):  # noqa: F821
        """
        Set the use_case_definition property.

        Parameters
        ----------
        value: "UseCaseDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "use_case_definition", value)
        self._use_case_definition = value
