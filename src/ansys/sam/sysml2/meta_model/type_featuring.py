"""Generated type featuring class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class TypeFeaturing(Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.TypeFeaturing'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._feature_of_type = None
        self._featuring_type = None
        self._owning_feature_of_type = None

    @property
    def feature_of_type(self) -> None:  # noqa: F821
        """
        Get the feature of type property.

        Returns
        -------
        None
            Value of property feature of type.
        """
        return self._feature_of_type

    @feature_of_type.setter
    def feature_of_type(self, value: None):  # noqa: F821
        """
        Set the feature_of_type property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "feature_of_type", value)
        self._feature_of_type = value

    @property
    def featuring_type(self) -> "Type":  # noqa: F821
        """
        Get the featuring type property.

        Returns
        -------
        "Type"
            Value of property featuring type.
        """
        return self._featuring_type

    @featuring_type.setter
    def featuring_type(self, value: "Type"):  # noqa: F821
        """
        Set the featuring_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "featuring_type", value)
        self._featuring_type = value

    @property
    def owning_feature_of_type(self) -> "Feature":  # noqa: F821
        """
        Get the owning feature of type property.

        Returns
        -------
        "Feature"
            Value of property owning feature of type.
        """
        return self._owning_feature_of_type

    @owning_feature_of_type.setter
    def owning_feature_of_type(self, value: "Feature"):  # noqa: F821
        """
        Set the owning_feature_of_type property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_feature_of_type", value)
        self._owning_feature_of_type = value
