"""Generated merge node class from metamodel."""

from .control_node import ControlNode


class MergeNode(ControlNode):
    """Java class 'com.ansys.medini.metamodel.sysml.MergeNode'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
