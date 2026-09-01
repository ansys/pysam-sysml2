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

"""Generated case usage class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .calculation_usage import CalculationUsage


class CaseUsage(CalculationUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.CaseUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._actor_parameter = ObservedList(self, "actor_parameter")
        self._case_definition = None
        self._subject_parameter = None
        self._objective_requirement = None

    @property
    def actor_parameter(self) -> list["PartUsage"]:  # noqa: F821
        """
        Get the actor parameter property.

        Returns
        -------
        list["PartUsage"]
            Value of property actor parameter.
        """
        return self._actor_parameter

    @property
    def case_definition(self) -> "CaseDefinition":  # noqa: F821
        """
        Get the case definition property.

        Returns
        -------
        "CaseDefinition"
            Value of property case definition.
        """
        return self._case_definition

    @case_definition.setter
    def case_definition(self, value: "CaseDefinition"):  # noqa: F821
        """
        Set the case_definition property.

        Parameters
        ----------
        value: "CaseDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "case_definition", value)
        self._case_definition = value

    @property
    def subject_parameter(self) -> "Usage":  # noqa: F821
        """
        Get the subject parameter property.

        Returns
        -------
        "Usage"
            Value of property subject parameter.
        """
        return self._subject_parameter

    @subject_parameter.setter
    def subject_parameter(self, value: "Usage"):  # noqa: F821
        """
        Set the subject_parameter property.

        Parameters
        ----------
        value: "Usage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "subject_parameter", value)
        self._subject_parameter = value

    @property
    def objective_requirement(self) -> "RequirementUsage":  # noqa: F821
        """
        Get the objective requirement property.

        Returns
        -------
        "RequirementUsage"
            Value of property objective requirement.
        """
        return self._objective_requirement

    @objective_requirement.setter
    def objective_requirement(self, value: "RequirementUsage"):  # noqa: F821
        """
        Set the objective_requirement property.

        Parameters
        ----------
        value: "RequirementUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "objective_requirement", value)
        self._objective_requirement = value
