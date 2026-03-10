"""Generated redefinition class from metamodel."""

from __future__ import annotations

from .subsetting import Subsetting


class Redefinition(Subsetting):
    """Java class 'com.ansys.medini.metamodel.sysml.Redefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._redefined_feature = None
        self._redefining_feature = None

    @property
    def redefined_feature(self) -> "Feature":  # noqa: F821
        """
        Get the redefined feature property.

        Returns
        -------
        "Feature"
            Value of property redefined feature.
        """
        return self._redefined_feature

    @redefined_feature.setter
    def redefined_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the redefined_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "redefined_feature", value)
        self._redefined_feature = value

    @property
    def redefining_feature(self) -> "Feature":  # noqa: F821
        """
        Get the redefining feature property.

        Returns
        -------
        "Feature"
            Value of property redefining feature.
        """
        return self._redefining_feature

    @redefining_feature.setter
    def redefining_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the redefining_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "redefining_feature", value)
        self._redefining_feature = value
