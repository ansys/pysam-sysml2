"""Generated literal rational class from metamodel."""

from .literal_expression import LiteralExpression


class LiteralRational(LiteralExpression):
    """Java class 'com.ansys.metamodel.sysml2.LiteralRational'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

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
