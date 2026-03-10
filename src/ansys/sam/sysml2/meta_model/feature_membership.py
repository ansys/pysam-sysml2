"""Generated feature membership class from metamodel."""

from __future__ import annotations

from .membership import Membership
from .type_featuring import TypeFeaturing


class FeatureMembership(Membership, TypeFeaturing):
    """Java class 'com.ansys.medini.metamodel.sysml.FeatureMembership'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._member_feature = None
        self._owning_type = None
        self._is_composite = False
        self._direction = None
        self._owned_member_feature = None

    @property
    def member_feature(self) -> "Feature":  # noqa: F821
        """
        Get the member feature property.

        Returns
        -------
        "Feature"
            Value of property member feature.
        """
        return self._member_feature

    @member_feature.setter
    def member_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the member_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "member_feature", value)
        self._member_feature = value

    @property
    def owning_type(self) -> "Type":  # noqa: F821
        """
        Get the owning type property.

        Returns
        -------
        "Type"
            Value of property owning type.
        """
        return self._owning_type

    @owning_type.setter
    def owning_type(self, value: "Type"):  # noqa: F821
        """
        Set the owning_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_type", value)
        self._owning_type = value

    @property
    def is_composite(self) -> bool:  # noqa: F821
        """
        Get the is composite property.

        Returns
        -------
        bool
            Value of property is composite.
        """
        return self._is_composite

    @is_composite.setter
    def is_composite(self, value: bool):  # noqa: F821
        """
        Set the is_composite property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_composite", value)
        self._is_composite = value

    @property
    def direction(self) -> "FeatureDirectionKind":  # noqa: F821
        """
        Get the direction property.

        Returns
        -------
        "FeatureDirectionKind"
            Value of property direction.
        """
        return self._direction

    @direction.setter
    def direction(self, value: "FeatureDirectionKind"):  # noqa: F821
        """
        Set the direction property.

        Parameters
        ----------
        value: "FeatureDirectionKind"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "direction", value)
        self._direction = value

    @property
    def owned_member_feature(self) -> "Feature":  # noqa: F821
        """
        Get the owned member feature property.

        Returns
        -------
        "Feature"
            Value of property owned member feature.
        """
        return self._owned_member_feature

    @owned_member_feature.setter
    def owned_member_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the owned_member_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_member_feature", value)
        self._owned_member_feature = value
