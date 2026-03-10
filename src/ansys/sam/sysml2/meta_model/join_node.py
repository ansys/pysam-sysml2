"""Generated join node class from metamodel."""

from .control_node import ControlNode


class JoinNode(ControlNode):
    """Java class 'com.ansys.medini.metamodel.sysml.JoinNode'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
