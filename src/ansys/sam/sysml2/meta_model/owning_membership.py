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

"""Generated owning membership class from metamodel."""

from __future__ import annotations

from .membership import Membership


class OwningMembership(Membership):
    """Java class 'com.ansys.metamodel.sysml2.OwningMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_member_element = None
        self._owned_member_element_id = ""
        self._owned_member_name = ""
        self._owned_member_short_name = ""

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
    def owned_member_element_id(self) -> str:  # noqa: F821
        """
        Get the owned member element id property.

        Returns
        -------
        str
            Value of property owned member element id.
        """
        return self._owned_member_element_id

    @owned_member_element_id.setter
    def owned_member_element_id(self, value: str):  # noqa: F821
        """
        Set the owned_member_element_id property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_member_element_id", value)
        self._owned_member_element_id = value

    @property
    def owned_member_name(self) -> str:  # noqa: F821
        """
        Get the owned member name property.

        Returns
        -------
        str
            Value of property owned member name.
        """
        return self._owned_member_name

    @owned_member_name.setter
    def owned_member_name(self, value: str):  # noqa: F821
        """
        Set the owned_member_name property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_member_name", value)
        self._owned_member_name = value

    @property
    def owned_member_short_name(self) -> str:  # noqa: F821
        """
        Get the owned member short name property.

        Returns
        -------
        str
            Value of property owned member short name.
        """
        return self._owned_member_short_name

    @owned_member_short_name.setter
    def owned_member_short_name(self, value: str):  # noqa: F821
        """
        Set the owned_member_short_name property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_member_short_name", value)
        self._owned_member_short_name = value
