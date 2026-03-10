"""Generated flow connection usage class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .action_usage import ActionUsage
from .connection_usage import ConnectionUsage
from .item_flow import ItemFlow


class FlowConnectionUsage(ConnectionUsage, ItemFlow, ActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.FlowConnectionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._flow_connection_definition = ObservedList(self, "flow_connection_definition")

    @property
    def flow_connection_definition(self) -> List["Interaction"]:  # noqa: F821
        """
        Get the flow connection definition property.

        Returns
        -------
        List["Interaction"]
            Value of property flow connection definition.
        """
        return self._flow_connection_definition
