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

"""Generated membership class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Membership(Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.Membership'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._member_name = ""
        self._member_element = None
        self._owned_member_element = None
        self._membership_owning_namespace = None

    @property
    def member_name(self) -> str:  # noqa: F821
        """
        Get the member name property.

        Returns
        -------
        str
            Value of property member name.
        """
        return self._member_name

    @member_name.setter
    def member_name(self, value: str):  # noqa: F821
        """
        Set the member_name property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "member_name", value)
        self._member_name = value

    @property
    def member_element(self) -> None:  # noqa: F821
        """
        Get the member element property.

        Returns
        -------
        None
            Value of property member element.
        """
        return self._member_element

    @member_element.setter
    def member_element(self, value: None):  # noqa: F821
        """
        Set the member_element property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "member_element", value)
        self._member_element = value

    @property
    def owned_member_element(self) -> "Element":  # noqa: F821
        """
        Get the owned member element property.

        Returns
        -------
        "Element"
            Value of property owned member element.
        """
        return self._owned_member_element

    @owned_member_element.setter
    def owned_member_element(self, value: "Element"):  # noqa: F821
        """
        Set the owned_member_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_member_element", value)
        self._owned_member_element = value

    @property
    def membership_owning_namespace(self) -> None:  # noqa: F821
        """
        Get the membership owning namespace property.

        Returns
        -------
        None
            Value of property membership owning namespace.
        """
        return self._membership_owning_namespace

    @membership_owning_namespace.setter
    def membership_owning_namespace(self, value: None):  # noqa: F821
        """
        Set the membership_owning_namespace property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "membership_owning_namespace", value)
        self._membership_owning_namespace = value
