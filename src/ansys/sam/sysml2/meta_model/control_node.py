"""Generated control node class from metamodel."""

from .action_usage import ActionUsage


class ControlNode(ActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.ControlNode'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
