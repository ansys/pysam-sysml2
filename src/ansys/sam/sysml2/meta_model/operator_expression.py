"""Generated operator expression class from metamodel."""

from __future__ import annotations

from .invocation_expression import InvocationExpression


class OperatorExpression(InvocationExpression):
    """Java class 'com.ansys.metamodel.sysml2.OperatorExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._operator = ""

    @property
    def operator(self) -> str:  # noqa: F821
        """
        Get the operator property.

        Returns
        -------
        str
            Value of property operator.
        """
        return self._operator

    @operator.setter
    def operator(self, value: str):  # noqa: F821
        """
        Set the operator property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "operator", value)
        self._operator = value
