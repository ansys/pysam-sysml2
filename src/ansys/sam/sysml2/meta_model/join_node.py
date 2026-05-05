"""Generated join node class from metamodel."""

from .control_node import ControlNode


class JoinNode(ControlNode):
    """Java class 'com.ansys.metamodel.sysml2.JoinNode'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
