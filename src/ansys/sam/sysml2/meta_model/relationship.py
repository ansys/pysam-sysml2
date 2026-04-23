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

"""Generated relationship class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .element import Element


class Relationship(Element):
    """Java class 'com.ansys.medini.metamodel.sysml.Relationship'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._target = ObservedList(self, "target")
        self._source = ObservedList(self, "source")
        self._related_element = ObservedList(self, "related_element")
        self._inheriting_element = None
        self._owned_related_element = ObservedList(self, "owned_related_element")
        self._owning_related_element = None

    @property
    def target(self) -> list["Element"]:  # noqa: F821
        """
        Get the target property.

        Returns
        -------
        list["Element"]
            Value of property target.
        """
        return self._target

    @property
    def source(self) -> list["Element"]:  # noqa: F821
        """
        Get the source property.

        Returns
        -------
        list["Element"]
            Value of property source.
        """
        return self._source

    @property
    def related_element(self) -> list["Element"]:  # noqa: F821
        """
        Get the related element property.

        Returns
        -------
        list["Element"]
            Value of property related element.
        """
        return self._related_element

    @property
    def inheriting_element(self) -> "Element":  # noqa: F821
        """
        Get the inheriting element property.

        Returns
        -------
        "Element"
            Value of property inheriting element.
        """
        return self._inheriting_element

    @inheriting_element.setter
    def inheriting_element(self, value: "Element"):  # noqa: F821
        """
        Set the inheriting_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "inheriting_element", value)
        self._inheriting_element = value

    @property
    def owned_related_element(self) -> list["Element"]:  # noqa: F821
        """
        Get the owned related element property.

        Returns
        -------
        list["Element"]
            Value of property owned related element.
        """
        return self._owned_related_element

    @property
    def owning_related_element(self) -> "Element":  # noqa: F821
        """
        Get the owning related element property.

        Returns
        -------
        "Element"
            Value of property owning related element.
        """
        return self._owning_related_element

    @owning_related_element.setter
    def owning_related_element(self, value: "Element"):  # noqa: F821
        """
        Set the owning_related_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_related_element", value)
        self._owning_related_element = value
