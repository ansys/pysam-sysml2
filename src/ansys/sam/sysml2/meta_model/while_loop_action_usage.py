"""Generated while loop action usage class from metamodel."""

from __future__ import annotations

from .loop_action_usage import LoopActionUsage


class WhileLoopActionUsage(LoopActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.WhileLoopActionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._while_argument = None
        self._until_argument = None

    @property
    def while_argument(self) -> None:  # noqa: F821
        """
        Get the while argument property.

        Returns
        -------
        None
            Value of property while argument.
        """
        return self._while_argument

    @while_argument.setter
    def while_argument(self, value: None):  # noqa: F821
        """
        Set the while_argument property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "while_argument", value)
        self._while_argument = value

    @property
    def until_argument(self) -> "Expression":  # noqa: F821
        """
        Get the until argument property.

        Returns
        -------
        "Expression"
            Value of property until argument.
        """
        return self._until_argument

    @until_argument.setter
    def until_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the until_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "until_argument", value)
        self._until_argument = value
