"""Generated fork node class from metamodel."""

from .control_node import ControlNode


class ForkNode(ControlNode):
    """Java class 'com.ansys.medini.metamodel.sysml.ForkNode'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
