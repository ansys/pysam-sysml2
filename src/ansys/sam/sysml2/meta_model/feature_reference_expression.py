"""Generated feature reference expression class from metamodel."""

from __future__ import annotations

from .expression import Expression


class FeatureReferenceExpression(Expression):
    """Java class 'com.ansys.metamodel.sysml2.FeatureReferenceExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

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
