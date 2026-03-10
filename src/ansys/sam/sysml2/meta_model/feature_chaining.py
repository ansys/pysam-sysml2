"""Generated feature chaining class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class FeatureChaining(Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.FeatureChaining'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._chaining_feature = None
        self._feature_chained = None

    @property
    def chaining_feature(self) -> "Feature":  # noqa: F821
        """
        Get the chaining feature property.

        Returns
        -------
        "Feature"
            Value of property chaining feature.
        """
        return self._chaining_feature

    @chaining_feature.setter
    def chaining_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the chaining_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "chaining_feature", value)
        self._chaining_feature = value

    @property
    def feature_chained(self) -> None:  # noqa: F821
        """
        Get the feature chained property.

        Returns
        -------
        None
            Value of property feature chained.
        """
        return self._feature_chained

    @feature_chained.setter
    def feature_chained(self, value: None):  # noqa: F821
        """
        Set the feature_chained property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "feature_chained", value)
        self._feature_chained = value
