"""Generated succession as usage class from metamodel."""

from .connector_as_usage import ConnectorAsUsage
from .succession import Succession


class SuccessionAsUsage(ConnectorAsUsage, Succession):
    """Java class 'com.ansys.metamodel.sysml2.SuccessionAsUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
