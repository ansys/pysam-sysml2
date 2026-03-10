"""Generated connector class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .feature import Feature
from .relationship import Relationship


class Connector(Relationship, Feature):
    """Java class 'com.ansys.medini.metamodel.sysml.Connector'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._source_feature = None
        self._connector_end = ObservedList(self, "connector_end")
        self._association = ObservedList(self, "association")
        self._is_directed = False
        self._target_feature = ObservedList(self, "target_feature")
        self._related_feature = ObservedList(self, "related_feature")

    @property
    def source_feature(self) -> None:  # noqa: F821
        """
        Get the source feature property.

        Returns
        -------
        None
            Value of property source feature.
        """
        return self._source_feature

    @source_feature.setter
    def source_feature(self, value: None):  # noqa: F821
        """
        Set the source_feature property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "source_feature", value)
        self._source_feature = value

    @property
    def connector_end(self) -> List["Feature"]:  # noqa: F821
        """
        Get the connector end property.

        Returns
        -------
        List["Feature"]
            Value of property connector end.
        """
        return self._connector_end

    @property
    def association(self) -> List["Association"]:  # noqa: F821
        """
        Get the association property.

        Returns
        -------
        List["Association"]
            Value of property association.
        """
        return self._association

    @property
    def is_directed(self) -> bool:  # noqa: F821
        """
        Get the is directed property.

        Returns
        -------
        bool
            Value of property is directed.
        """
        return self._is_directed

    @is_directed.setter
    def is_directed(self, value: bool):  # noqa: F821
        """
        Set the is_directed property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_directed", value)
        self._is_directed = value

    @property
    def target_feature(self) -> List["Feature"]:  # noqa: F821
        """
        Get the target feature property.

        Returns
        -------
        List["Feature"]
            Value of property target feature.
        """
        return self._target_feature

    @property
    def related_feature(self) -> List["Feature"]:  # noqa: F821
        """
        Get the related feature property.

        Returns
        -------
        List["Feature"]
            Value of property related feature.
        """
        return self._related_feature
