"""Generated constraint definition class from metamodel."""

from __future__ import annotations

from .occurrence_definition import OccurrenceDefinition
from .predicate import Predicate


class ConstraintDefinition(Predicate, OccurrenceDefinition):
    """Java class 'com.ansys.medini.metamodel.sysml.ConstraintDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._constraint_expression = None
        self._set_constraint_expression = False

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
