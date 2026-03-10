"""Generated for loop action usage class from metamodel."""

from __future__ import annotations

from .loop_action_usage import LoopActionUsage


class ForLoopActionUsage(LoopActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.ForLoopActionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._loop_variable = None

    @property
    def loop_variable(self) -> None:  # noqa: F821
        """
        Get the loop variable property.

        Returns
        -------
        None
            Value of property loop variable.
        """
        return self._loop_variable

    @loop_variable.setter
    def loop_variable(self, value: None):  # noqa: F821
        """
        Set the loop_variable property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "loop_variable", value)
        self._loop_variable = value
