"""Generated result expression membership class from metamodel."""

from __future__ import annotations

from .feature_membership import FeatureMembership


class ResultExpressionMembership(FeatureMembership):
    """Java class 'com.ansys.metamodel.sysml2.ResultExpressionMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_result_expression = None

    @property
    def owned_result_expression(self) -> "Expression":  # noqa: F821
        """
        Get the owned result expression property.

        Returns
        -------
        "Expression"
            Value of property owned result expression.
        """
        return self._owned_result_expression

    @owned_result_expression.setter
    def owned_result_expression(self, value: "Expression"):  # noqa: F821
        """
        Set the owned_result_expression property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_result_expression", value)
        self._owned_result_expression = value
