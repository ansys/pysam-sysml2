"""Generated literal rational class from metamodel."""

from __future__ import annotations

from .literal_expression import LiteralExpression


class LiteralRational(LiteralExpression):
    """Java class 'com.ansys.medini.metamodel.sysml.LiteralRational'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._value = 0.0

    @property
    def value(self) -> float:
        """
        Get the value property.

        Returns
        -------
        float
            Value of property value.
        """
        return self._value

    @value.setter
    def value(self, value: float):
        """
        Set the value property.

        Parameters
        ----------
        value: float
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "value", value)
        self._value = value
