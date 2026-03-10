"""Generated succession flow connection usage class from metamodel."""

from .flow_connection_usage import FlowConnectionUsage
from .succession_item_flow import SuccessionItemFlow


class SuccessionFlowConnectionUsage(FlowConnectionUsage, SuccessionItemFlow):
    """Java class 'com.ansys.medini.metamodel.sysml.SuccessionFlowConnectionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
