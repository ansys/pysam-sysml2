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
