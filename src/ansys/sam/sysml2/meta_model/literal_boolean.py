"""Generated literal boolean class from metamodel."""

from __future__ import annotations

from .literal_expression import LiteralExpression


class LiteralBoolean(LiteralExpression):
    """Java class 'com.ansys.medini.metamodel.sysml.LiteralBoolean'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._value = None

    @property
    def value(self) -> None:  # noqa: F821
        """
        Get the value property.

        Returns
        -------
        None
            Value of property value.
        """
        return self._value

    @value.setter
    def value(self, value: None):  # noqa: F821
        """
        Set the value property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "value", value)
        self._value = value
