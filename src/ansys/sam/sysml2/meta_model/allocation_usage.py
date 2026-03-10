"""Generated allocation usage class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .connection_usage import ConnectionUsage


class AllocationUsage(ConnectionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.AllocationUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._allocation_definition = ObservedList(self, "allocation_definition")

    @property
    def allocation_definition(self) -> List["AllocationDefinition"]:  # noqa: F821
        """
        Get the allocation definition property.

        Returns
        -------
        List["AllocationDefinition"]
            Value of property allocation definition.
        """
        return self._allocation_definition
