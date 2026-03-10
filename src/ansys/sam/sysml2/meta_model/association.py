"""Generated association class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .classifier import Classifier
from .relationship import Relationship


class Association(Classifier, Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.Association'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._association_end = ObservedList(self, "association_end")
        self._target_type = ObservedList(self, "target_type")
        self._source_type = None
        self._related_type = ObservedList(self, "related_type")

    @property
    def association_end(self) -> List["Feature"]:  # noqa: F821
        """
        Get the association end property.

        Returns
        -------
        List["Feature"]
            Value of property association end.
        """
        return self._association_end

    @property
    def target_type(self) -> List["Type"]:  # noqa: F821
        """
        Get the target type property.

        Returns
        -------
        List["Type"]
            Value of property target type.
        """
        return self._target_type

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
    def related_type(self) -> List["Type"]:  # noqa: F821
        """
        Get the related type property.

        Returns
        -------
        List["Type"]
            Value of property related type.
        """
        return self._related_type
