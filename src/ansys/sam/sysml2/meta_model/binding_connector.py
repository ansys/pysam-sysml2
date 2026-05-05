"""Generated binding connector class from metamodel."""

from .connector import Connector


class BindingConnector(Connector):
    """Java class 'com.ansys.metamodel.sysml2.BindingConnector'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
