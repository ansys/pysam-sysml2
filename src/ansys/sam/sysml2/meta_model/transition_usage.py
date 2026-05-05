"""Generated transition usage class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .action_usage import ActionUsage


class TransitionUsage(ActionUsage):
    """Java class 'com.ansys.metamodel.sysml2.TransitionUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._effect_action = ObservedList(self, "effect_action")
        self._guard_expression = ObservedList(self, "guard_expression")
        self._source = None
        self._succession = None
        self._target = None
        self._trigger_action = ObservedList(self, "trigger_action")

    @property
    def effect_action(self) -> list["ActionUsage"]:  # noqa: F821
        """
        Get the effect action property.

        Returns
        -------
        list["ActionUsage"]
            Value of property effect action.
        """
        return self._effect_action

    @property
    def guard_expression(self) -> list["Expression"]:  # noqa: F821
        """
        Get the guard expression property.

        Returns
        -------
        list["Expression"]
            Value of property guard expression.
        """
        return self._guard_expression

    @property
    def source(self) -> "ActionUsage":  # noqa: F821
        """
        Get the source property.

        Returns
        -------
        "ActionUsage"
            Value of property source.
        """
        return self._source

    @source.setter
    def source(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the source property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "source", value)
        self._source = value

    @property
    def succession(self) -> "Succession":  # noqa: F821
        """
        Get the succession property.

        Returns
        -------
        "Succession"
            Value of property succession.
        """
        return self._succession

    @succession.setter
    def succession(self, value: "Succession"):  # noqa: F821
        """
        Set the succession property.

        Parameters
        ----------
        value: "Succession"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "succession", value)
        self._succession = value

    @property
    def target(self) -> "ActionUsage":  # noqa: F821
        """
        Get the target property.

        Returns
        -------
        "ActionUsage"
            Value of property target.
        """
        return self._target

    @target.setter
    def target(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the target property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "target", value)
        self._target = value

    @property
    def trigger_action(self) -> list["AcceptActionUsage"]:  # noqa: F821
        """
        Get the trigger action property.

        Returns
        -------
        list["AcceptActionUsage"]
            Value of property trigger action.
        """
        return self._trigger_action
