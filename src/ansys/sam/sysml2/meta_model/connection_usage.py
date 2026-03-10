"""Generated connection usage class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .connector_as_usage import ConnectorAsUsage
from .part_usage import PartUsage


class ConnectionUsage(PartUsage, ConnectorAsUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.ConnectionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._connection_definition = ObservedList(self, "connection_definition")

    @property
    def connection_definition(self) -> List["AssociationStructure"]:  # noqa: F821
        """
        Get the connection definition property.

        Returns
        -------
        List["AssociationStructure"]
            Value of property connection definition.
        """
        return self._connection_definition
