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

"""Generated framed concern membership class from metamodel."""

from __future__ import annotations

from .requirement_constraint_membership import RequirementConstraintMembership


class FramedConcernMembership(RequirementConstraintMembership):
    """Java class 'com.ansys.metamodel.sysml2.FramedConcernMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_concern = None
        self._referenced_concern = None

    @property
    def owned_concern(self) -> "ConcernUsage":  # noqa: F821
        """
        Get the owned concern property.

        Returns
        -------
        "ConcernUsage"
            Value of property owned concern.
        """
        return self._owned_concern

    @owned_concern.setter
    def owned_concern(self, value: "ConcernUsage"):  # noqa: F821
        """
        Set the owned_concern property.

        Parameters
        ----------
        value: "ConcernUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_concern", value)
        self._owned_concern = value

    @property
    def referenced_concern(self) -> "ConcernUsage":  # noqa: F821
        """
        Get the referenced concern property.

        Returns
        -------
        "ConcernUsage"
            Value of property referenced concern.
        """
        return self._referenced_concern

    @referenced_concern.setter
    def referenced_concern(self, value: "ConcernUsage"):  # noqa: F821
        """
        Set the referenced_concern property.

        Parameters
        ----------
        value: "ConcernUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "referenced_concern", value)
        self._referenced_concern = value
