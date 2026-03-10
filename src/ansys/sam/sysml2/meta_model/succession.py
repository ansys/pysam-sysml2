"""Generated succession class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .connector import Connector


class Succession(Connector):
    """Java class 'com.ansys.medini.metamodel.sysml.Succession'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._guard_expression = ObservedList(self, "guard_expression")
        self._transition_step = None
        self._trigger_step = ObservedList(self, "trigger_step")
        self._effect_step = ObservedList(self, "effect_step")

    @property
    def guard_expression(self) -> List["Expression"]:  # noqa: F821
        """
        Get the guard expression property.

        Returns
        -------
        List["Expression"]
            Value of property guard expression.
        """
        return self._guard_expression

    @property
    def transition_step(self) -> "Step":  # noqa: F821
        """
        Get the transition step property.

        Returns
        -------
        "Step"
            Value of property transition step.
        """
        return self._transition_step

    @transition_step.setter
    def transition_step(self, value: "Step"):  # noqa: F821
        """
        Set the transition_step property.

        Parameters
        ----------
        value: "Step"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "transition_step", value)
        self._transition_step = value

    @property
    def trigger_step(self) -> List["Step"]:  # noqa: F821
        """
        Get the trigger step property.

        Returns
        -------
        List["Step"]
            Value of property trigger step.
        """
        return self._trigger_step

    @property
    def effect_step(self) -> List["Step"]:  # noqa: F821
        """
        Get the effect step property.

        Returns
        -------
        List["Step"]
            Value of property effect step.
        """
        return self._effect_step
