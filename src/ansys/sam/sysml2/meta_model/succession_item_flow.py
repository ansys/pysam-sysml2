"""Generated succession item flow class from metamodel."""

from .item_flow import ItemFlow
from .succession import Succession


class SuccessionItemFlow(ItemFlow, Succession):
    """Java class 'com.ansys.medini.metamodel.sysml.SuccessionItemFlow'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
