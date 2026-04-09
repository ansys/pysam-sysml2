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

"""Generated element class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .e_object import EObject


class Element(EObject):
    """Java class 'com.ansys.medini.metamodel.sysml.Element'."""

    def __init__(self, id: str):
        """Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._name = ""
        self._owner = None
        self._comment = ObservedList(self, "comment")
        self._short_name = None
        self._documentation = ObservedList(self, "documentation")
        self._owning_namespace = None
        self._owned_element = ObservedList(self, "owned_element")
        self._owned_annotation = ObservedList(self, "owned_annotation")
        self._qualified_name = ""
        self._alias_ids = ObservedList(self, "alias_ids")
        self._visibility = None
        self._owned_relationship = ObservedList(self, "owned_relationship")
        self._textual_representation = ObservedList(self, "textual_representation")
        self._owned_inherited_relationship = ObservedList(self, "owned_inherited_relationship")

    @property
    def name(self) -> str:  # noqa: F821
        """
        Get the name property.

        Returns
        -------
        str
            Value of property name.
        """
        return self._name

    @name.setter
    def name(self, value: str):  # noqa: F821
        """
        Set the name property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "name", value)
        self._name = value

    @property
    def owner(self) -> "Element":  # noqa: F821
        """
        Get the owner property.

        Returns
        -------
        "Element"
            Value of property owner.
        """
        return self._owner

    @owner.setter
    def owner(self, value: "Element"):  # noqa: F821
        """
        Set the owner property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owner", value)
        self._owner = value

    @property
    def comment(self) -> List["Comment"]:  # noqa: F821
        """
        Get the comment property.

        Returns
        -------
        List["Comment"]
            Value of property comment.
        """
        return self._comment

    @property
    def short_name(self) -> None:  # noqa: F821
        """
        Get the short name property.

        Returns
        -------
        None
            Value of property short name.
        """
        return self._short_name

    @short_name.setter
    def short_name(self, value: None):  # noqa: F821
        """
        Set the short_name property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "short_name", value)
        self._short_name = value

    @property
    def documentation(self) -> List["Documentation"]:  # noqa: F821
        """
        Get the documentation property.

        Returns
        -------
        List["Documentation"]
            Value of property documentation.
        """
        return self._documentation

    @property
    def owning_namespace(self) -> "Namespace":  # noqa: F821
        """
        Get the owning namespace property.

        Returns
        -------
        "Namespace"
            Value of property owning namespace.
        """
        return self._owning_namespace

    @owning_namespace.setter
    def owning_namespace(self, value: "Namespace"):  # noqa: F821
        """
        Set the owning_namespace property.

        Parameters
        ----------
        value: "Namespace"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_namespace", value)
        self._owning_namespace = value

    @property
    def owned_element(self) -> List["Element"]:  # noqa: F821
        """
        Get the owned element property.

        Returns
        -------
        List["Element"]
            Value of property owned element.
        """
        return self._owned_element

    @property
    def owned_annotation(self) -> List["Annotation"]:  # noqa: F821
        """
        Get the owned annotation property.

        Returns
        -------
        List["Annotation"]
            Value of property owned annotation.
        """
        return self._owned_annotation

    @property
    def qualified_name(self) -> str:  # noqa: F821
        """
        Get the qualified name property.

        Returns
        -------
        str
            Value of property qualified name.
        """
        return self._qualified_name

    @property
    def alias_ids(self) -> List[str]:  # noqa: F821
        """
        Get the alias ids property.

        Returns
        -------
        List[str]
            Value of property alias ids.
        """
        return self._alias_ids

    @property
    def visibility(self) -> None:  # noqa: F821
        """
        Get the visibility property.

        Returns
        -------
        None
            Value of property visibility.
        """
        return self._visibility

    @visibility.setter
    def visibility(self, value: None):  # noqa: F821
        """
        Set the visibility property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "visibility", value)
        self._visibility = value

    @property
    def owned_relationship(self) -> List["Relationship"]:  # noqa: F821
        """
        Get the owned relationship property.

        Returns
        -------
        List["Relationship"]
            Value of property owned relationship.
        """
        return self._owned_relationship

    @property
    def textual_representation(self) -> List["TextualRepresentation"]:  # noqa: F821
        """
        Get the textual representation property.

        Returns
        -------
        List["TextualRepresentation"]
            Value of property textual representation.
        """
        return self._textual_representation

    @property
    def owned_inherited_relationship(self) -> List["Relationship"]:  # noqa: F821
        """
        Get the owned inherited relationship property.

        Returns
        -------
        List["Relationship"]
            Value of property owned inherited relationship.
        """
        return self._owned_inherited_relationship
