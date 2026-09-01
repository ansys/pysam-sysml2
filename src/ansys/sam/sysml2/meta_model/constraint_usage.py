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
    """Java class 'com.ansys.medini.metamodel.sysml.ConstraintUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._kind = None
        self._set_kind = False
        self._constraint_definition = None
        self._constraint_expression = None
        self._set_constraint_expression = False

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
    def set_kind(self) -> bool:  # noqa: F821
        """
        Get the set kind property.

        Returns
        -------
        bool
            Value of property set kind.
        """
        return self._set_kind

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

    @property
    def constraint_expression(self) -> "Expression":  # noqa: F821
        """
        Get the constraint expression property.

        Returns
        -------
        "Expression"
            Value of property constraint expression.
        """
        return self._constraint_expression

    @constraint_expression.setter
    def constraint_expression(self, value: "Expression"):  # noqa: F821
        """
        Set the constraint_expression property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "constraint_expression", value)
        self._constraint_expression = value

    @property
    def set_constraint_expression(self) -> bool:  # noqa: F821
        """
        Get the set constraint expression property.

        Returns
        -------
        bool
            Value of property set constraint expression.
        """
        return self._set_constraint_expression
