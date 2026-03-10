"""Generated feature reference expression class from metamodel."""

from __future__ import annotations

from .expression import Expression


class FeatureReferenceExpression(Expression):
    """Java class 'com.ansys.medini.metamodel.sysml.FeatureReferenceExpression'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._referent = None

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
