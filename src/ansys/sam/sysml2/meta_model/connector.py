"""Generated connector class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .feature import Feature
from .relationship import Relationship


class Connector(Feature, Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Connector'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._association = ObservedList(self, "association")
        self._connector_end = ObservedList(self, "connector_end")
        self._default_featuring_type = None
        self._related_feature = ObservedList(self, "related_feature")
        self._source_feature = None
        self._target_feature = ObservedList(self, "target_feature")

    @property
    def association(self) -> list["Association"]:  # noqa: F821
        """
        Get the association property.

        Returns
        -------
        list["Association"]
            Value of property association.
        """
        return self._association

    @property
    def connector_end(self) -> list["Feature"]:  # noqa: F821
        """
        Get the connector end property.

        Returns
        -------
        list["Feature"]
            Value of property connector end.
        """
        return self._connector_end

    @property
    def default_featuring_type(self) -> "Type":  # noqa: F821
        """
        Get the default featuring type property.

        Returns
        -------
        "Type"
            Value of property default featuring type.
        """
        return self._default_featuring_type

    @default_featuring_type.setter
    def default_featuring_type(self, value: "Type"):  # noqa: F821
        """
        Set the default_featuring_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "default_featuring_type", value)
        self._default_featuring_type = value

    @property
    def related_feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the related feature property.

        Returns
        -------
        list["Feature"]
            Value of property related feature.
        """
        return self._related_feature

    @property
    def source_feature(self) -> "Feature":  # noqa: F821
        """
        Get the source feature property.

        Returns
        -------
        "Feature"
            Value of property source feature.
        """
        return self._source_feature

    @source_feature.setter
    def source_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the source_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "source_feature", value)
        self._source_feature = value

    @property
    def target_feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the target feature property.

        Returns
        -------
        list["Feature"]
            Value of property target feature.
        """
        return self._target_feature
