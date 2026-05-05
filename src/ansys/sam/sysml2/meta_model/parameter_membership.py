"""Generated parameter membership class from metamodel."""

from __future__ import annotations

from .feature_membership import FeatureMembership


class ParameterMembership(FeatureMembership):
    """Java class 'com.ansys.metamodel.sysml2.ParameterMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_member_parameter = None

    @property
    def owned_member_parameter(self) -> "Feature":  # noqa: F821
        """
        Get the owned member parameter property.

        Returns
        -------
        "Feature"
            Value of property owned member parameter.
        """
        return self._owned_member_parameter

    @owned_member_parameter.setter
    def owned_member_parameter(self, value: "Feature"):  # noqa: F821
        """
        Set the owned_member_parameter property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_member_parameter", value)
        self._owned_member_parameter = value
