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

"""Generated constraint usage class from metamodel."""

from __future__ import annotations

from .boolean_expression import BooleanExpression
from .occurrence_usage import OccurrenceUsage


class ConstraintUsage(BooleanExpression, OccurrenceUsage):
    """Java class 'com.ansys.metamodel.sysml2.ConstraintUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._constraint_definition = None

    @property
    def constraint_definition(self) -> "Predicate":  # noqa: F821
        """
        Get the constraint definition property.

        Returns
        -------
        "Predicate"
            Value of property constraint definition.
        """
        return self._constraint_definition

    @constraint_definition.setter
    def constraint_definition(self, value: "Predicate"):  # noqa: F821
        """
        Set the constraint_definition property.

        Parameters
        ----------
        value: "Predicate"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "constraint_definition", value)
        self._constraint_definition = value
