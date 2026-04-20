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

"""Generated association class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .classifier import Classifier
from .relationship import Relationship


class Association(Classifier, Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.Association'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._source_type = None
        self._related_type = ObservedList(self, "related_type")
        self._association_end = ObservedList(self, "association_end")
        self._target_type = ObservedList(self, "target_type")

    @property
    def source_type(self) -> "Type":  # noqa: F821
        """
        Get the source type property.

        Returns
        -------
        "Type"
            Value of property source type.
        """
        return self._source_type

    @source_type.setter
    def source_type(self, value: "Type"):  # noqa: F821
        """
        Set the source_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "source_type", value)
        self._source_type = value

    @property
    def related_type(self) -> list["Type"]:  # noqa: F821
        """
        Get the related type property.

        Returns
        -------
        list["Type"]
            Value of property related type.
        """
        return self._related_type

    @property
    def association_end(self) -> list["Feature"]:  # noqa: F821
        """
        Get the association end property.

        Returns
        -------
        list["Feature"]
            Value of property association end.
        """
        return self._association_end

    @property
    def target_type(self) -> list["Type"]:  # noqa: F821
        """
        Get the target type property.

        Returns
        -------
        list["Type"]
            Value of property target type.
        """
        return self._target_type
