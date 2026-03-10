"""Generated expression class from metamodel."""

from __future__ import annotations

from .step import Step


class Expression(Step):
    """Java class 'com.ansys.medini.metamodel.sysml.Expression'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._function = None
        self._result = None

    @property
    def function(self) -> "Function":  # noqa: F821
        """
        Get the function property.

        Returns
        -------
        "Function"
            Value of property function.
        """
        return self._function

    @function.setter
    def function(self, value: "Function"):  # noqa: F821
        """
        Set the function property.

        Parameters
        ----------
        value: "Function"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "function", value)
        self._function = value

    @property
    def result(self) -> None:  # noqa: F821
        """
        Get the result property.

        Returns
        -------
        None
            Value of property result.
        """
        return self._result

    @result.setter
    def result(self, value: None):  # noqa: F821
        """
        Set the result property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "result", value)
        self._result = value
