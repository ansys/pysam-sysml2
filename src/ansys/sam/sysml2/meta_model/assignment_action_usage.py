"""Generated assignment action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage


class AssignmentActionUsage(ActionUsage):
    """Java class 'com.ansys.metamodel.sysml2.AssignmentActionUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._referent = None
        self._target_argument = None
        self._value_expression = None

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

    @referent.setter
    def referent(self, value: "Feature"):  # noqa: F821
        """
        Set the referent property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "referent", value)
        self._referent = value

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

    @target_argument.setter
    def target_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the target_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "target_argument", value)
        self._target_argument = value

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

    @value_expression.setter
    def value_expression(self, value: "Expression"):  # noqa: F821
        """
        Set the value_expression property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "value_expression", value)
        self._value_expression = value
