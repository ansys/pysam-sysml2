"""Generated connection definition class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .association_structure import AssociationStructure
from .part_definition import PartDefinition


class ConnectionDefinition(PartDefinition, AssociationStructure):
    """Java class 'com.ansys.medini.metamodel.sysml.ConnectionDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._connection_end = ObservedList(self, "connection_end")

    @property
    def connection_end(self) -> List["Usage"]:  # noqa: F821
        """
        Get the connection end property.

        Returns
        -------
        List["Usage"]
            Value of property connection end.
        """
        return self._connection_end
