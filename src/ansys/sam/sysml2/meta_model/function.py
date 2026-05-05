"""Generated function class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .behavior import Behavior


class Function(Behavior):
    """Java class 'com.ansys.metamodel.sysml2.Function'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._expression = ObservedList(self, "expression")
        self._result = None
        self._is_model_level_evaluable = False

    @property
    def expression(self) -> list["Expression"]:  # noqa: F821
        """
        Get the expression property.

        Returns
        -------
        list["Expression"]
            Value of property expression.
        """
        return self._expression

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
