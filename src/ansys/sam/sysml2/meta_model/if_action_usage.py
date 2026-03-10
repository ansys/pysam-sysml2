"""Generated if action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage


class IfActionUsage(ActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.IfActionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._if_argument = None
        self._then_action = None
        self._else_action = None

    @property
    def if_argument(self) -> None:  # noqa: F821
        """
        Get the if argument property.

        Returns
        -------
        None
            Value of property if argument.
        """
        return self._if_argument

    @if_argument.setter
    def if_argument(self, value: None):  # noqa: F821
        """
        Set the if_argument property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "if_argument", value)
        self._if_argument = value

    @property
    def then_action(self) -> "ActionUsage":  # noqa: F821
        """
        Get the then action property.

        Returns
        -------
        "ActionUsage"
            Value of property then action.
        """
        return self._then_action

    @then_action.setter
    def then_action(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the then_action property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "then_action", value)
        self._then_action = value

    @property
    def else_action(self) -> "ActionUsage":  # noqa: F821
        """
        Get the else action property.

        Returns
        -------
        "ActionUsage"
            Value of property else action.
        """
        return self._else_action

    @else_action.setter
    def else_action(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the else_action property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "else_action", value)
        self._else_action = value
