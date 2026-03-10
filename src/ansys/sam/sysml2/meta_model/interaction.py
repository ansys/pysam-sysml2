"""Generated interaction class from metamodel."""

from .association import Association
from .behavior import Behavior


class Interaction(Behavior, Association):
    """Java class 'com.ansys.medini.metamodel.sysml.Interaction'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
