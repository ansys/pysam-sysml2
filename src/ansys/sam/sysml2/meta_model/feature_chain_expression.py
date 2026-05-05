"""Generated feature chain expression class from metamodel."""

from __future__ import annotations

from .operator_expression import OperatorExpression


class FeatureChainExpression(OperatorExpression):
    """Java class 'com.ansys.metamodel.sysml2.FeatureChainExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

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

    @target_feature.setter
    def target_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the target_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "target_feature", value)
        self._target_feature = value
