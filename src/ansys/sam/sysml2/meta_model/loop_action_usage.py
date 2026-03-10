"""Generated loop action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage


class LoopActionUsage(ActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.LoopActionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._body_action = None

    @property
    def body_action(self) -> "ActionUsage":  # noqa: F821
        """
        Get the body action property.

        Returns
        -------
        "ActionUsage"
            Value of property body action.
        """
        return self._body_action

    @body_action.setter
    def body_action(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the body_action property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "body_action", value)
        self._body_action = value
