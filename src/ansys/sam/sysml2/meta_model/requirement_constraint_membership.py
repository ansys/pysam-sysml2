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
    """Java class 'com.ansys.medini.metamodel.sysml.RequirementConstraintMembership'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._kind = None
        self._constraint = None

    @property
    def kind(self) -> None:  # noqa: F821
        """
        Get the kind property.

        Returns
        -------
        None
            Value of property kind.
        """
        return self._kind

    @kind.setter
    def kind(self, value: None):  # noqa: F821
        """
        Set the kind property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "kind", value)
        self._kind = value

    @property
    def constraint(self) -> None:  # noqa: F821
        """
        Get the constraint property.

        Returns
        -------
        None
            Value of property constraint.
        """
        return self._constraint

    @constraint.setter
    def constraint(self, value: None):  # noqa: F821
        """
        Set the constraint property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "constraint", value)
        self._constraint = value
