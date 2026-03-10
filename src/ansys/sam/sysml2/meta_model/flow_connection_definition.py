"""Generated flow connection definition class from metamodel."""

from .action_definition import ActionDefinition
from .connection_definition import ConnectionDefinition
from .interaction import Interaction


class FlowConnectionDefinition(ConnectionDefinition, ActionDefinition, Interaction):
    """Java class 'com.ansys.medini.metamodel.sysml.FlowConnectionDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
