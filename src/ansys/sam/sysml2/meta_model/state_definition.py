"""Generated state definition class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .action_definition import ActionDefinition


class StateDefinition(ActionDefinition):
    """Java class 'com.ansys.metamodel.sysml2.StateDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._do_action = None
        self._entry_action = None
        self._exit_action = None
        self._state = ObservedList(self, "state")
        self._is_parallel = False

    @property
    def do_action(self) -> "ActionUsage":  # noqa: F821
        """
        Get the do action property.

        Returns
        -------
        "ActionUsage"
            Value of property do action.
        """
        return self._do_action

    @do_action.setter
    def do_action(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the do_action property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "do_action", value)
        self._do_action = value

    @property
    def entry_action(self) -> "ActionUsage":  # noqa: F821
        """
        Get the entry action property.

        Returns
        -------
        "ActionUsage"
            Value of property entry action.
        """
        return self._entry_action

    @entry_action.setter
    def entry_action(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the entry_action property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "entry_action", value)
        self._entry_action = value

    @property
    def exit_action(self) -> "ActionUsage":  # noqa: F821
        """
        Get the exit action property.

        Returns
        -------
        "ActionUsage"
            Value of property exit action.
        """
        return self._exit_action

    @exit_action.setter
    def exit_action(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the exit_action property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "exit_action", value)
        self._exit_action = value

    @property
    def state(self) -> list["StateUsage"]:  # noqa: F821
        """
        Get the state property.

        Returns
        -------
        list["StateUsage"]
            Value of property state.
        """
        return self._state

    @property
    def is_parallel(self) -> bool:  # noqa: F821
        """
        Get the is parallel property.

        Returns
        -------
        bool
            Value of property is parallel.
        """
        return self._is_parallel

    @is_parallel.setter
    def is_parallel(self, value: bool):  # noqa: F821
        """
        Set the is_parallel property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_parallel", value)
        self._is_parallel = value
