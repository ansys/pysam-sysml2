"""Generated result expression membership class from metamodel."""

from __future__ import annotations

from .feature_membership import FeatureMembership


class ResultExpressionMembership(FeatureMembership):
    """Java class 'com.ansys.medini.metamodel.sysml.ResultExpressionMembership'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

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
