"""Generated connection definition class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .association_structure import AssociationStructure
from .part_definition import PartDefinition


class ConnectionDefinition(PartDefinition, AssociationStructure):
    """Java class 'com.ansys.metamodel.sysml2.ConnectionDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._connection_end = ObservedList(self, "connection_end")

    @property
    def connection_end(self) -> list["Usage"]:  # noqa: F821
        """
        Get the connection end property.

        Returns
        -------
        list["Usage"]
            Value of property connection end.
        """
        return self._connection_end
