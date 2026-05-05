"""Generated fork node class from metamodel."""

from .control_node import ControlNode


class ForkNode(ControlNode):
    """Java class 'com.ansys.metamodel.sysml2.ForkNode'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
