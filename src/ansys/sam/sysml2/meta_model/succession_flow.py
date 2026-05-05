"""Generated succession flow class from metamodel."""

from .flow import Flow
from .succession import Succession


class SuccessionFlow(Flow, Succession):
    """Java class 'com.ansys.metamodel.sysml2.SuccessionFlow'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
