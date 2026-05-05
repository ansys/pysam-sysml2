"""Generated binding connector as usage class from metamodel."""

from .binding_connector import BindingConnector
from .connector_as_usage import ConnectorAsUsage


class BindingConnectorAsUsage(ConnectorAsUsage, BindingConnector):
    """Java class 'com.ansys.metamodel.sysml2.BindingConnectorAsUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
