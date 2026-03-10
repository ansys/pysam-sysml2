"""Generated function class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .behavior import Behavior


class Function(Behavior):
    """Java class 'com.ansys.medini.metamodel.sysml.Function'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._result = None
        self._expression = ObservedList(self, "expression")

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

    @property
    def expression(self) -> List["Expression"]:  # noqa: F821
        """
        Get the expression property.

        Returns
        -------
        List["Expression"]
            Value of property expression.
        """
        return self._expression
