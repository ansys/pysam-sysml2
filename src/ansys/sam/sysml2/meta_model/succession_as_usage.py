"""Generated succession as usage class from metamodel."""

from .connector_as_usage import ConnectorAsUsage
from .succession import Succession


class SuccessionAsUsage(ConnectorAsUsage, Succession):
    """Java class 'com.ansys.medini.metamodel.sysml.SuccessionAsUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
