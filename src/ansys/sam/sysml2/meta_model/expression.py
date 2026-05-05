"""Generated expression class from metamodel."""

from __future__ import annotations

from .step import Step


class Expression(Step):
    """Java class 'com.ansys.metamodel.sysml2.Expression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._function = None
        self._result = None
        self._is_model_level_evaluable = False

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
    def result(self) -> "Feature":  # noqa: F821
        """
        Get the result property.

        Returns
        -------
        "Feature"
            Value of property result.
        """
        return self._result

    @result.setter
    def result(self, value: "Feature"):  # noqa: F821
        """
        Set the result property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "result", value)
        self._result = value

    @property
    def is_model_level_evaluable(self) -> bool:  # noqa: F821
        """
        Get the is model level evaluable property.

        Returns
        -------
        bool
            Value of property is model level evaluable.
        """
        return self._is_model_level_evaluable

    @is_model_level_evaluable.setter
    def is_model_level_evaluable(self, value: bool):  # noqa: F821
        """
        Set the is_model_level_evaluable property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_model_level_evaluable", value)
        self._is_model_level_evaluable = value
