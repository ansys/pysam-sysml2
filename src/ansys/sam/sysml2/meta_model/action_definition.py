"""Generated action definition class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .behavior import Behavior
from .occurrence_definition import OccurrenceDefinition


class ActionDefinition(OccurrenceDefinition, Behavior):
    """Java class 'com.ansys.metamodel.sysml2.ActionDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._action = ObservedList(self, "action")

    @property
    def action(self) -> list["ActionUsage"]:  # noqa: F821
        """
        Get the action property.

        Returns
        -------
        list["ActionUsage"]
            Value of property action.
        """
        return self._action
