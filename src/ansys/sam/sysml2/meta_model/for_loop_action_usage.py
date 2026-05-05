"""Generated for loop action usage class from metamodel."""

from __future__ import annotations

from .loop_action_usage import LoopActionUsage


class ForLoopActionUsage(LoopActionUsage):
    """Java class 'com.ansys.metamodel.sysml2.ForLoopActionUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._loop_variable = None
        self._seq_argument = None

    @property
    def loop_variable(self) -> "ReferenceUsage":  # noqa: F821
        """
        Get the loop variable property.

        Returns
        -------
        "ReferenceUsage"
            Value of property loop variable.
        """
        return self._loop_variable

    @loop_variable.setter
    def loop_variable(self, value: "ReferenceUsage"):  # noqa: F821
        """
        Set the loop_variable property.

        Parameters
        ----------
        value: "ReferenceUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "loop_variable", value)
        self._loop_variable = value

    @property
    def seq_argument(self) -> "Expression":  # noqa: F821
        """
        Get the seq argument property.

        Returns
        -------
        "Expression"
            Value of property seq argument.
        """
        return self._seq_argument

    @seq_argument.setter
    def seq_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the seq_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "seq_argument", value)
        self._seq_argument = value
