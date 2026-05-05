"""Generated reference subsetting class from metamodel."""

from __future__ import annotations

from .subsetting import Subsetting


class ReferenceSubsetting(Subsetting):
    """Java class 'com.ansys.metamodel.sysml2.ReferenceSubsetting'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._referenced_feature = None
        self._referencing_feature = None

    @property
    def referenced_feature(self) -> "Feature":  # noqa: F821
        """
        Get the referenced feature property.

        Returns
        -------
        "Feature"
            Value of property referenced feature.
        """
        return self._referenced_feature

    @referenced_feature.setter
    def referenced_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the referenced_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "referenced_feature", value)
        self._referenced_feature = value

    @property
    def referencing_feature(self) -> "Feature":  # noqa: F821
        """
        Get the referencing feature property.

        Returns
        -------
        "Feature"
            Value of property referencing feature.
        """
        return self._referencing_feature

    @referencing_feature.setter
    def referencing_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the referencing_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "referencing_feature", value)
        self._referencing_feature = value
