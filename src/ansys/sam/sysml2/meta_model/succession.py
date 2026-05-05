"""Generated succession class from metamodel."""

from .connector import Connector


class Succession(Connector):
    """Java class 'com.ansys.metamodel.sysml2.Succession'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
