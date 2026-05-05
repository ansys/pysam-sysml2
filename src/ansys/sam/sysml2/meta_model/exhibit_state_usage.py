"""Generated exhibit state usage class from metamodel."""

from __future__ import annotations

from .perform_action_usage import PerformActionUsage
from .state_usage import StateUsage


class ExhibitStateUsage(PerformActionUsage, StateUsage):
    """Java class 'com.ansys.metamodel.sysml2.ExhibitStateUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._exhibited_state = None

    @property
    def exhibited_state(self) -> "StateUsage":  # noqa: F821
        """
        Get the exhibited state property.

        Returns
        -------
        "StateUsage"
            Value of property exhibited state.
        """
        return self._exhibited_state

    @exhibited_state.setter
    def exhibited_state(self, value: "StateUsage"):  # noqa: F821
        """
        Set the exhibited_state property.

        Parameters
        ----------
        value: "StateUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "exhibited_state", value)
        self._exhibited_state = value
