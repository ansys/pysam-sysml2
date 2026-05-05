"""Generated cross subsetting class from metamodel."""

from __future__ import annotations

from .subsetting import Subsetting


class CrossSubsetting(Subsetting):
    """Java class 'com.ansys.metamodel.sysml2.CrossSubsetting'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._crossed_feature = None
        self._crossing_feature = None

    @property
    def crossed_feature(self) -> "Feature":  # noqa: F821
        """
        Get the crossed feature property.

        Returns
        -------
        "Feature"
            Value of property crossed feature.
        """
        return self._crossed_feature

    @crossed_feature.setter
    def crossed_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the crossed_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "crossed_feature", value)
        self._crossed_feature = value

    @property
    def crossing_feature(self) -> "Feature":  # noqa: F821
        """
        Get the crossing feature property.

        Returns
        -------
        "Feature"
            Value of property crossing feature.
        """
        return self._crossing_feature

    @crossing_feature.setter
    def crossing_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the crossing_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "crossing_feature", value)
        self._crossing_feature = value
