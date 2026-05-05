"""Generated calculation definition class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .action_definition import ActionDefinition
from .function import Function


class CalculationDefinition(ActionDefinition, Function):
    """Java class 'com.ansys.metamodel.sysml2.CalculationDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._calculation = ObservedList(self, "calculation")

    @property
    def calculation(self) -> list["CalculationUsage"]:  # noqa: F821
        """
        Get the calculation property.

        Returns
        -------
        list["CalculationUsage"]
            Value of property calculation.
        """
        return self._calculation
