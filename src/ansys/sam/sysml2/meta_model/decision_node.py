"""Generated decision node class from metamodel."""

from .control_node import ControlNode


class DecisionNode(ControlNode):
    """Java class 'com.ansys.medini.metamodel.sysml.DecisionNode'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
