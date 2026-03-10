"""Generated binding connector class from metamodel."""

from .connector import Connector


class BindingConnector(Connector):
    """Java class 'com.ansys.medini.metamodel.sysml.BindingConnector'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
