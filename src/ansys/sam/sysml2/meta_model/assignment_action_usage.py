"""Generated assignment action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage


class AssignmentActionUsage(ActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.AssignmentActionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._value_expression = None
        self._target_argument = None
        self._referent = None

    @property
    def value_expression(self) -> "Expression":  # noqa: F821
        """
        Get the value expression property.

        Returns
        -------
        "Expression"
            Value of property value expression.
        """
        return self._value_expression

    @property
    def target_argument(self) -> "Expression":  # noqa: F821
        """
        Get the target argument property.

        Returns
        -------
        "Expression"
            Value of property target argument.
        """
        return self._target_argument

    @property
    def referent(self) -> "Feature":  # noqa: F821
        """
        Get the referent property.

        Returns
        -------
        "Feature"
            Value of property referent.
        """
        return self._referent
