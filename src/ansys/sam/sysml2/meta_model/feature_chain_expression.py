"""Generated feature chain expression class from metamodel."""

from __future__ import annotations

from .operator_expression import OperatorExpression


class FeatureChainExpression(OperatorExpression):
    """Java class 'com.ansys.medini.metamodel.sysml.FeatureChainExpression'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._target_feature = None

    @property
    def target_feature(self) -> "Feature":  # noqa: F821
        """
        Get the target feature property.

        Returns
        -------
        "Feature"
            Value of property target feature.
        """
        return self._target_feature
