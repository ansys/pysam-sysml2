"""Generated literal string class from metamodel."""

from __future__ import annotations

from .literal_expression import LiteralExpression


class LiteralString(LiteralExpression):
    """Java class 'com.ansys.medini.metamodel.sysml.LiteralString'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._value = ""

    @property
    def value(self) -> str:  # noqa: F821
        """
        Get the value property.

        Returns
        -------
        str
            Value of property value.
        """
        return self._value

    @value.setter
    def value(self, value: str):  # noqa: F821
        """
        Set the value property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "value", value)
        self._value = value
