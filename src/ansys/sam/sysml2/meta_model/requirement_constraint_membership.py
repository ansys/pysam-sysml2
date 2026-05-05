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

"""Generated requirement constraint membership class from metamodel."""

from __future__ import annotations

from .feature_membership import FeatureMembership


class RequirementConstraintMembership(FeatureMembership):
    """Java class 'com.ansys.metamodel.sysml2.RequirementConstraintMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._kind = None
        self._owned_constraint = None
        self._referenced_constraint = None

    @property
    def kind(self) -> "RequirementConstraintKind":  # noqa: F821
        """
        Get the kind property.

        Returns
        -------
        "RequirementConstraintKind"
            Value of property kind.
        """
        return self._kind

    @kind.setter
    def kind(self, value: "RequirementConstraintKind"):  # noqa: F821
        """
        Set the kind property.

        Parameters
        ----------
        value: "RequirementConstraintKind"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "kind", value)
        self._kind = value

    @property
    def owned_constraint(self) -> "ConstraintUsage":  # noqa: F821
        """
        Get the owned constraint property.

        Returns
        -------
        "ConstraintUsage"
            Value of property owned constraint.
        """
        return self._owned_constraint

    @owned_constraint.setter
    def owned_constraint(self, value: "ConstraintUsage"):  # noqa: F821
        """
        Set the owned_constraint property.

        Parameters
        ----------
        value: "ConstraintUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_constraint", value)
        self._owned_constraint = value

    @property
    def referenced_constraint(self) -> "ConstraintUsage":  # noqa: F821
        """
        Get the referenced constraint property.

        Returns
        -------
        "ConstraintUsage"
            Value of property referenced constraint.
        """
        return self._referenced_constraint

    @referenced_constraint.setter
    def referenced_constraint(self, value: "ConstraintUsage"):  # noqa: F821
        """
        Set the referenced_constraint property.

        Parameters
        ----------
        value: "ConstraintUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "referenced_constraint", value)
        self._referenced_constraint = value
