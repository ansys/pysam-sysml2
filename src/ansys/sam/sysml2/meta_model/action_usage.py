"""Generated action usage class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .occurrence_usage import OccurrenceUsage
from .step import Step


class ActionUsage(OccurrenceUsage, Step):
    """Java class 'com.ansys.medini.metamodel.sysml.ActionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._action_definition = ObservedList(self, "action_definition")

    @property
    def action_definition(self) -> List["Behavior"]:  # noqa: F821
        """
        Get the action definition property.

        Returns
        -------
        List["Behavior"]
            Value of property action definition.
        """
        return self._action_definition
