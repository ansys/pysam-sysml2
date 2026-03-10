"""Generated constraint usage class from metamodel."""

from __future__ import annotations

from .boolean_expression import BooleanExpression
from .occurrence_usage import OccurrenceUsage


class ConstraintUsage(BooleanExpression, OccurrenceUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.ConstraintUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._set_kind = False
        self._kind = None
        self._constraint_definition = None
        self._constraint_expression = None
        self._set_constraint_expression = False

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
    def constraint_expression(self) -> None:  # noqa: F821
        """
        Get the constraint expression property.

        Returns
        -------
        None
            Value of property constraint expression.
        """
        return self._constraint_expression

    @constraint_expression.setter
    def constraint_expression(self, value: None):  # noqa: F821
        """
        Set the constraint_expression property.

        Parameters
        ----------
        value: None
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
