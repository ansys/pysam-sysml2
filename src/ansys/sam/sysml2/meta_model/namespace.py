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

"""Generated namespace class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .element import Element


class Namespace(Element):
    """Java class 'com.ansys.medini.metamodel.sysml.Namespace'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._owned_member = ObservedList(self, "owned_member")
        self._owned_import = ObservedList(self, "owned_import")
        self._member = ObservedList(self, "member")
        self._owned_membership = ObservedList(self, "owned_membership")

    @property
    def owned_member(self) -> List["Element"]:  # noqa: F821
        """
        Get the owned member property.

        Returns
        -------
        List["Element"]
            Value of property owned member.
        """
        return self._owned_member

    @property
    def owned_import(self) -> List["Import"]:  # noqa: F821
        """
        Get the owned import property.

        Returns
        -------
        List["Import"]
            Value of property owned import.
        """
        return self._owned_import

    @property
    def member(self) -> List["Element"]:  # noqa: F821
        """
        Get the member property.

        Returns
        -------
        List["Element"]
            Value of property member.
        """
        return self._member

    @property
    def owned_membership(self) -> List["Membership"]:  # noqa: F821
        """
        Get the owned membership property.

        Returns
        -------
        List["Membership"]
            Value of property owned membership.
        """
        return self._owned_membership
