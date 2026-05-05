"""Generated feature inverting class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class FeatureInverting(Relationship):
    """Java class 'com.ansys.metamodel.sysml2.FeatureInverting'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._feature_inverted = None
        self._inverting_feature = None
        self._owning_feature = None

    @property
    def feature_inverted(self) -> "Feature":  # noqa: F821
        """
        Get the feature inverted property.

        Returns
        -------
        "Feature"
            Value of property feature inverted.
        """
        return self._feature_inverted

    @feature_inverted.setter
    def feature_inverted(self, value: "Feature"):  # noqa: F821
        """
        Set the feature_inverted property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "feature_inverted", value)
        self._feature_inverted = value

    @property
    def inverting_feature(self) -> "Feature":  # noqa: F821
        """
        Get the inverting feature property.

        Returns
        -------
        "Feature"
            Value of property inverting feature.
        """
        return self._inverting_feature

    @inverting_feature.setter
    def inverting_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the inverting_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "inverting_feature", value)
        self._inverting_feature = value

    @property
    def owning_feature(self) -> "Feature":  # noqa: F821
        """
        Get the owning feature property.

        Returns
        -------
        "Feature"
            Value of property owning feature.
        """
        return self._owning_feature

    @owning_feature.setter
    def owning_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the owning_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_feature", value)
        self._owning_feature = value
