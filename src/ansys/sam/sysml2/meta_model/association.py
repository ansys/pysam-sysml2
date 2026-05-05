"""Generated association class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .classifier import Classifier
from .relationship import Relationship


class Association(Classifier, Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Association'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._association_end = ObservedList(self, "association_end")
        self._related_type = ObservedList(self, "related_type")
        self._source_type = None
        self._target_type = ObservedList(self, "target_type")

    @property
    def association_end(self) -> list["Feature"]:  # noqa: F821
        """
        Get the association end property.

        Returns
        -------
        list["Feature"]
            Value of property association end.
        """
        return self._association_end

    @property
    def related_type(self) -> list["Type"]:  # noqa: F821
        """
        Get the related type property.

        Returns
        -------
        list["Type"]
            Value of property related type.
        """
        return self._related_type

    @property
    def source_type(self) -> "Type":  # noqa: F821
        """
        Get the source type property.

        Returns
        -------
        "Type"
            Value of property source type.
        """
        return self._source_type

    @source_type.setter
    def source_type(self, value: "Type"):  # noqa: F821
        """
        Set the source_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "source_type", value)
        self._source_type = value

    @property
    def target_type(self) -> list["Type"]:  # noqa: F821
        """
        Get the target type property.

        Returns
        -------
        list["Type"]
            Value of property target type.
        """
        return self._target_type
