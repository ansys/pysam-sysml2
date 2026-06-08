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

"""Generated view definition class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .part_definition import PartDefinition


class ViewDefinition(PartDefinition):
    """Java class 'com.ansys.metamodel.sysml2.ViewDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._satisfied_viewpoint = ObservedList(self, "satisfied_viewpoint")
        self._view = ObservedList(self, "view")
        self._view_condition = ObservedList(self, "view_condition")
        self._view_rendering = None

    @property
    def satisfied_viewpoint(self) -> list["ViewpointUsage"]:  # noqa: F821
        """
        Get the satisfied viewpoint property.

        Returns
        -------
        list["ViewpointUsage"]
            Value of property satisfied viewpoint.
        """
        return self._satisfied_viewpoint

    @property
    def view(self) -> list["ViewUsage"]:  # noqa: F821
        """
        Get the view property.

        Returns
        -------
        list["ViewUsage"]
            Value of property view.
        """
        return self._view

    @property
    def view_condition(self) -> list["Expression"]:  # noqa: F821
        """
        Get the view condition property.

        Returns
        -------
        list["Expression"]
            Value of property view condition.
        """
        return self._view_condition

    @property
    def view_rendering(self) -> "RenderingUsage":  # noqa: F821
        """
        Get the view rendering property.

        Returns
        -------
        "RenderingUsage"
            Value of property view rendering.
        """
        return self._view_rendering

    @view_rendering.setter
    def view_rendering(self, value: "RenderingUsage"):  # noqa: F821
        """
        Set the view_rendering property.

        Parameters
        ----------
        value: "RenderingUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "view_rendering", value)
        self._view_rendering = value
