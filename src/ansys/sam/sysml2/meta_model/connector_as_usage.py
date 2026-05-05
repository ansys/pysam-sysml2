"""Generated connector as usage class from metamodel."""

from .connector import Connector
from .usage import Usage


class ConnectorAsUsage(Usage, Connector):
    """Java class 'com.ansys.metamodel.sysml2.ConnectorAsUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
