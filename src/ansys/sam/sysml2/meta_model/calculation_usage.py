"""Generated calculation usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage
from .expression import Expression


class CalculationUsage(ActionUsage, Expression):
    """Java class 'com.ansys.medini.metamodel.sysml.CalculationUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._calculation_definition = None

    @property
    def calculation_definition(self) -> "Function":  # noqa: F821
        """
        Get the calculation definition property.

        Returns
        -------
        "Function"
            Value of property calculation definition.
        """
        return self._calculation_definition

    @calculation_definition.setter
    def calculation_definition(self, value: "Function"):  # noqa: F821
        """
        Set the calculation_definition property.

        Parameters
        ----------
        value: "Function"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "calculation_definition", value)
        self._calculation_definition = value
