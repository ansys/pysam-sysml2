"""Generated allocation usage class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .connection_usage import ConnectionUsage


class AllocationUsage(ConnectionUsage):
    """Java class 'com.ansys.metamodel.sysml2.AllocationUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._allocation_definition = ObservedList(self, "allocation_definition")

    @property
    def allocation_definition(self) -> list["AllocationDefinition"]:  # noqa: F821
        """
        Get the allocation definition property.

        Returns
        -------
        list["AllocationDefinition"]
            Value of property allocation definition.
        """
        return self._allocation_definition
