"""Generated boolean expression class from metamodel."""

from __future__ import annotations

from .expression import Expression


class BooleanExpression(Expression):
    """Java class 'com.ansys.medini.metamodel.sysml.BooleanExpression'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._predicate = None

    @property
    def predicate(self) -> None:  # noqa: F821
        """
        Get the predicate property.

        Returns
        -------
        None
            Value of property predicate.
        """
        return self._predicate

    @predicate.setter
    def predicate(self, value: None):  # noqa: F821
        """
        Set the predicate property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "predicate", value)
        self._predicate = value
