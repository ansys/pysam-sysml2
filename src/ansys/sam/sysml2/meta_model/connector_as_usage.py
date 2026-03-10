"""Generated connector as usage class from metamodel."""

from .connector import Connector
from .usage import Usage


class ConnectorAsUsage(Usage, Connector):
    """Java class 'com.ansys.medini.metamodel.sysml.ConnectorAsUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
