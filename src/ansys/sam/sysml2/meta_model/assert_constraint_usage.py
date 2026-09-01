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

"""Generated assert constraint usage class from metamodel."""

from __future__ import annotations

from .constraint_usage import ConstraintUsage
from .invariant import Invariant


class AssertConstraintUsage(ConstraintUsage, Invariant):
    """Java class 'com.ansys.medini.metamodel.sysml.AssertConstraintUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._asserted_constraint = None

    @property
    def asserted_constraint(self) -> "ConstraintUsage":  # noqa: F821
        """
        Get the asserted constraint property.

        Returns
        -------
        "ConstraintUsage"
            Value of property asserted constraint.
        """
        return self._asserted_constraint

    @asserted_constraint.setter
    def asserted_constraint(self, value: "ConstraintUsage"):  # noqa: F821
        """
        Set the asserted_constraint property.

        Parameters
        ----------
        value: "ConstraintUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "asserted_constraint", value)
        self._asserted_constraint = value
