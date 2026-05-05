"""Generated feature membership class from metamodel."""

from __future__ import annotations

from .owning_membership import OwningMembership


class FeatureMembership(OwningMembership):
    """Java class 'com.ansys.metamodel.sysml2.FeatureMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_member_feature = None
        self._owning_type = None

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
