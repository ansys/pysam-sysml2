"""Generated binding connector as usage class from metamodel."""

from .binding_connector import BindingConnector
from .connector_as_usage import ConnectorAsUsage


class BindingConnectorAsUsage(ConnectorAsUsage, BindingConnector):
    """Java class 'com.ansys.medini.metamodel.sysml.BindingConnectorAsUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
