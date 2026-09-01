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

"""Generated verification case usage class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .case_usage import CaseUsage


class VerificationCaseUsage(CaseUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.VerificationCaseUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._verification_case_definition = None
        self._verified_requirement = ObservedList(self, "verified_requirement")

    @property
    def verification_case_definition(self) -> "VerificationCaseDefinition":  # noqa: F821
        """
        Get the verification case definition property.

        Returns
        -------
        "VerificationCaseDefinition"
            Value of property verification case definition.
        """
        return self._verification_case_definition

    @verification_case_definition.setter
    def verification_case_definition(self, value: "VerificationCaseDefinition"):  # noqa: F821
        """
        Set the verification_case_definition property.

        Parameters
        ----------
        value: "VerificationCaseDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "verification_case_definition", value)
        self._verification_case_definition = value

    @property
    def verified_requirement(self) -> list["RequirementUsage"]:  # noqa: F821
        """
        Get the verified requirement property.

        Returns
        -------
        list["RequirementUsage"]
            Value of property verified requirement.
        """
        return self._verified_requirement
