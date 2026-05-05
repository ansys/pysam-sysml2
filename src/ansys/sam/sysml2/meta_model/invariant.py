"""Generated invariant class from metamodel."""

from __future__ import annotations

from .boolean_expression import BooleanExpression


class Invariant(BooleanExpression):
    """Java class 'com.ansys.metamodel.sysml2.Invariant'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._is_negated = False

    @property
    def is_negated(self) -> bool:  # noqa: F821
        """
        Get the is negated property.

        Returns
        -------
        bool
            Value of property is negated.
        """
        return self._is_negated

    @is_negated.setter
    def is_negated(self, value: bool):  # noqa: F821
        """
        Set the is_negated property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_negated", value)
        self._is_negated = value
