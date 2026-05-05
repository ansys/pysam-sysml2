"""Generated flow definition class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .action_definition import ActionDefinition
from .interaction import Interaction


class FlowDefinition(ActionDefinition, Interaction):
    """Java class 'com.ansys.metamodel.sysml2.FlowDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._flow_end = ObservedList(self, "flow_end")

    @property
    def flow_end(self) -> list["Usage"]:  # noqa: F821
        """
        Get the flow end property.

        Returns
        -------
        list["Usage"]
            Value of property flow end.
        """
        return self._flow_end
