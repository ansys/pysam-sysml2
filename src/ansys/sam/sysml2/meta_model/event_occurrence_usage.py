"""Generated event occurrence usage class from metamodel."""

from __future__ import annotations

from .occurrence_usage import OccurrenceUsage


class EventOccurrenceUsage(OccurrenceUsage):
    """Java class 'com.ansys.metamodel.sysml2.EventOccurrenceUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._event_occurrence = None

    @property
    def event_occurrence(self) -> "OccurrenceUsage":  # noqa: F821
        """
        Get the event occurrence property.

        Returns
        -------
        "OccurrenceUsage"
            Value of property event occurrence.
        """
        return self._event_occurrence

    @event_occurrence.setter
    def event_occurrence(self, value: "OccurrenceUsage"):  # noqa: F821
        """
        Set the event_occurrence property.

        Parameters
        ----------
        value: "OccurrenceUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "event_occurrence", value)
        self._event_occurrence = value
