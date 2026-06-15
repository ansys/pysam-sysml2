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

"""Generated viewpoint usage class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .requirement_usage import RequirementUsage


class ViewpointUsage(RequirementUsage):
    """Java class 'com.ansys.metamodel.sysml2.ViewpointUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._viewpoint_definition = None
        self._viewpoint_stakeholder = ObservedList(self, "viewpoint_stakeholder")

    @property
    def viewpoint_definition(self) -> "ViewpointDefinition":  # noqa: F821
        """
        Get the viewpoint definition property.

        Returns
        -------
        "ViewpointDefinition"
            Value of property viewpoint definition.
        """
        return self._viewpoint_definition

    @viewpoint_definition.setter
    def viewpoint_definition(self, value: "ViewpointDefinition"):  # noqa: F821
        """
        Set the viewpoint_definition property.

        Parameters
        ----------
        value: "ViewpointDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "viewpoint_definition", value)
        self._viewpoint_definition = value

    @property
    def viewpoint_stakeholder(self) -> list["PartUsage"]:  # noqa: F821
        """
        Get the viewpoint stakeholder property.

        Returns
        -------
        list["PartUsage"]
            Value of property viewpoint stakeholder.
        """
        return self._viewpoint_stakeholder
