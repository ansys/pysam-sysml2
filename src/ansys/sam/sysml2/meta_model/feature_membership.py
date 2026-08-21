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

"""Generated feature membership class from metamodel."""

from __future__ import annotations

from .owning_membership import OwningMembership


class FeatureMembership(OwningMembership):
    """Java class 'com.ansys.metamodel.sysml2.FeatureMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_member_feature = None
        self._owning_type = None

    @property
    def owned_member_feature(self) -> "Feature":  # noqa: F821
        """
        Get the owned member feature property.

        Returns
        -------
        "Feature"
            Value of property owned member feature.
        """
        return self._owned_member_feature

    @owned_member_feature.setter
    def owned_member_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the owned_member_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_member_feature", value)
        self._owned_member_feature = value

    @property
    def owning_type(self) -> "Type":  # noqa: F821
        """
        Get the owning type property.

        Returns
        -------
        "Type"
            Value of property owning type.
        """
        return self._owning_type

    @owning_type.setter
    def owning_type(self, value: "Type"):  # noqa: F821
        """
        Set the owning_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_type", value)
        self._owning_type = value
