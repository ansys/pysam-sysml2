"""Generated flow usage class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .action_usage import ActionUsage
from .connector_as_usage import ConnectorAsUsage
from .flow import Flow


class FlowUsage(ActionUsage, Flow, ConnectorAsUsage):
    """Java class 'com.ansys.metamodel.sysml2.FlowUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._flow_definition = ObservedList(self, "flow_definition")

    @property
    def flow_definition(self) -> list["Interaction"]:  # noqa: F821
        """
        Get the flow definition property.

        Returns
        -------
        list["Interaction"]
            Value of property flow definition.
        """
        return self._flow_definition
