"""Generated state subaction membership class from metamodel."""

from __future__ import annotations

from .feature_membership import FeatureMembership


class StateSubactionMembership(FeatureMembership):
    """Java class 'com.ansys.medini.metamodel.sysml.StateSubactionMembership'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._kind = None
        self._action = None

    @property
    def kind(self) -> None:  # noqa: F821
        """
        Get the kind property.

        Returns
        -------
        None
            Value of property kind.
        """
        return self._kind

    @kind.setter
    def kind(self, value: None):  # noqa: F821
        """
        Set the kind property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "kind", value)
        self._kind = value

    @property
    def action(self) -> "ActionUsage":  # noqa: F821
        """
        Get the action property.

        Returns
        -------
        "ActionUsage"
            Value of property action.
        """
        return self._action

    @action.setter
    def action(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the action property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "action", value)
        self._action = value
