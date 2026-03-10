"""Generated allocation definition class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .connection_definition import ConnectionDefinition


class AllocationDefinition(ConnectionDefinition):
    """Java class 'com.ansys.medini.metamodel.sysml.AllocationDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._allocation = ObservedList(self, "allocation")

    @property
    def allocation(self) -> List["AllocationUsage"]:  # noqa: F821
        """
        Get the allocation property.

        Returns
        -------
        List["AllocationUsage"]
            Value of property allocation.
        """
        return self._allocation
