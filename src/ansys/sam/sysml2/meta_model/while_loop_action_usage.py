"""Generated while loop action usage class from metamodel."""

from __future__ import annotations

from .loop_action_usage import LoopActionUsage


class WhileLoopActionUsage(LoopActionUsage):
    """Java class 'com.ansys.metamodel.sysml2.WhileLoopActionUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._until_argument = None
        self._while_argument = None

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

    @property
    def while_argument(self) -> "Expression":  # noqa: F821
        """
        Get the while argument property.

        Returns
        -------
        "Expression"
            Value of property while argument.
        """
        return self._while_argument

    @while_argument.setter
    def while_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the while_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "while_argument", value)
        self._while_argument = value
