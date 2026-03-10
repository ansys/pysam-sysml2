"""Generated calculation definition class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .action_definition import ActionDefinition
from .function import Function


class CalculationDefinition(ActionDefinition, Function):
    """Java class 'com.ansys.medini.metamodel.sysml.CalculationDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._calculation = ObservedList(self, "calculation")

    @property
    def calculation(self) -> List["CalculationUsage"]:  # noqa: F821
        """
        Get the calculation property.

        Returns
        -------
        List["CalculationUsage"]
            Value of property calculation.
        """
        return self._calculation
