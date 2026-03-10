"""Generated exhibit state usage class from metamodel."""

from __future__ import annotations

from .perform_action_usage import PerformActionUsage
from .state_usage import StateUsage


class ExhibitStateUsage(StateUsage, PerformActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.ExhibitStateUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._exhibited_state = None

    @property
    def exhibited_state(self) -> None:  # noqa: F821
        """
        Get the exhibited state property.

        Returns
        -------
        None
            Value of property exhibited state.
        """
        return self._exhibited_state

    @exhibited_state.setter
    def exhibited_state(self, value: None):  # noqa: F821
        """
        Set the exhibited_state property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "exhibited_state", value)
        self._exhibited_state = value
