"""Generated action usage class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .occurrence_usage import OccurrenceUsage
from .step import Step


class ActionUsage(OccurrenceUsage, Step):
    """Java class 'com.ansys.metamodel.sysml2.ActionUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._action_definition = ObservedList(self, "action_definition")
        self._subaction_usage = False

    @property
    def action_definition(self) -> list["Behavior"]:  # noqa: F821
        """
        Get the action definition property.

        Returns
        -------
        list["Behavior"]
            Value of property action definition.
        """
        return self._action_definition

    @property
    def subaction_usage(self) -> bool:  # noqa: F821
        """
        Get the subaction usage property.

        Returns
        -------
        bool
            Value of property subaction usage.
        """
        return self._subaction_usage
