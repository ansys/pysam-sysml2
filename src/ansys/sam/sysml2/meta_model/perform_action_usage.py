"""Generated perform action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage
from .event_occurrence_usage import EventOccurrenceUsage


class PerformActionUsage(ActionUsage, EventOccurrenceUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.PerformActionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._performed_action = None

    @property
    def performed_action(self) -> None:  # noqa: F821
        """
        Get the performed action property.

        Returns
        -------
        None
            Value of property performed action.
        """
        return self._performed_action

    @performed_action.setter
    def performed_action(self, value: None):  # noqa: F821
        """
        Set the performed_action property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "performed_action", value)
        self._performed_action = value
