"""Generated terminate action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage


class TerminateActionUsage(ActionUsage):
    """Java class 'com.ansys.metamodel.sysml2.TerminateActionUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._terminated_occurrence_argument = None

    @property
    def terminated_occurrence_argument(self) -> "Expression":  # noqa: F821
        """
        Get the terminated occurrence argument property.

        Returns
        -------
        "Expression"
            Value of property terminated occurrence argument.
        """
        return self._terminated_occurrence_argument

    @terminated_occurrence_argument.setter
    def terminated_occurrence_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the terminated_occurrence_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "terminated_occurrence_argument", value)
        self._terminated_occurrence_argument = value
