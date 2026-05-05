"""Generated boolean expression class from metamodel."""

from __future__ import annotations

from .expression import Expression


class BooleanExpression(Expression):
    """Java class 'com.ansys.metamodel.sysml2.BooleanExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._predicate = None

    @property
    def predicate(self) -> "Predicate":  # noqa: F821
        """
        Get the predicate property.

        Returns
        -------
        "Predicate"
            Value of property predicate.
        """
        return self._predicate

    @predicate.setter
    def predicate(self, value: "Predicate"):  # noqa: F821
        """
        Set the predicate property.

        Parameters
        ----------
        value: "Predicate"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "predicate", value)
        self._predicate = value
