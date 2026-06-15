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

"""Generated annotating element class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .element import Element


class AnnotatingElement(Element):
    """Java class 'com.ansys.metamodel.sysml2.AnnotatingElement'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._annotated_element = ObservedList(self, "annotated_element")
        self._annotation = ObservedList(self, "annotation")
        self._owned_annotating_relationship = ObservedList(self, "owned_annotating_relationship")
        self._owning_annotating_relationship = None

    @property
    def annotated_element(self) -> list["Element"]:  # noqa: F821
        """
        Get the annotated element property.

        Returns
        -------
        list["Element"]
            Value of property annotated element.
        """
        return self._annotated_element

    @property
    def annotation(self) -> list["Annotation"]:  # noqa: F821
        """
        Get the annotation property.

        Returns
        -------
        list["Annotation"]
            Value of property annotation.
        """
        return self._annotation

    @property
    def owned_annotating_relationship(self) -> list["Annotation"]:  # noqa: F821
        """
        Get the owned annotating relationship property.

        Returns
        -------
        list["Annotation"]
            Value of property owned annotating relationship.
        """
        return self._owned_annotating_relationship

    @property
    def owning_annotating_relationship(self) -> "Annotation":  # noqa: F821
        """
        Get the owning annotating relationship property.

        Returns
        -------
        "Annotation"
            Value of property owning annotating relationship.
        """
        return self._owning_annotating_relationship

    @owning_annotating_relationship.setter
    def owning_annotating_relationship(self, value: "Annotation"):  # noqa: F821
        """
        Set the owning_annotating_relationship property.

        Parameters
        ----------
        value: "Annotation"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_annotating_relationship", value)
        self._owning_annotating_relationship = value
