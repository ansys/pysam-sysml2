"""Generated action definition class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .behavior import Behavior
from .occurrence_definition import OccurrenceDefinition


class ActionDefinition(OccurrenceDefinition, Behavior):
    """Java class 'com.ansys.medini.metamodel.sysml.ActionDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._action = ObservedList(self, "action")

    @property
    def action(self) -> List["ActionUsage"]:  # noqa: F821
        """
        Get the action property.

        Returns
        -------
        List["ActionUsage"]
            Value of property action.
        """
        return self._action
