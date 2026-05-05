"""Generated interaction class from metamodel."""

from .association import Association
from .behavior import Behavior


class Interaction(Association, Behavior):
    """Java class 'com.ansys.metamodel.sysml2.Interaction'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
