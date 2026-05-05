"""Generated literal boolean class from metamodel."""

from __future__ import annotations

from .literal_expression import LiteralExpression


class LiteralBoolean(LiteralExpression):
    """Java class 'com.ansys.metamodel.sysml2.LiteralBoolean'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._value = False

    @property
    def value(self) -> bool:  # noqa: F821
        """
        Get the value property.

        Returns
        -------
        bool
            Value of property value.
        """
        return self._value

    @value.setter
    def value(self, value: bool):  # noqa: F821
        """
        Set the value property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "value", value)
        self._value = value
