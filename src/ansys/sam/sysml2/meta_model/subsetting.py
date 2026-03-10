"""Generated subsetting class from metamodel."""

from __future__ import annotations

from .specialization import Specialization


class Subsetting(Specialization):
    """Java class 'com.ansys.medini.metamodel.sysml.Subsetting'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._subsetted_feature = None
        self._subsetting_feature = None

    @property
    def subsetted_feature(self) -> "Feature":  # noqa: F821
        """
        Get the subsetted feature property.

        Returns
        -------
        "Feature"
            Value of property subsetted feature.
        """
        return self._subsetted_feature

    @subsetted_feature.setter
    def subsetted_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the subsetted_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "subsetted_feature", value)
        self._subsetted_feature = value

    @property
    def subsetting_feature(self) -> None:  # noqa: F821
        """
        Get the subsetting feature property.

        Returns
        -------
        None
            Value of property subsetting feature.
        """
        return self._subsetting_feature

    @subsetting_feature.setter
    def subsetting_feature(self, value: None):  # noqa: F821
        """
        Set the subsetting_feature property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "subsetting_feature", value)
        self._subsetting_feature = value
