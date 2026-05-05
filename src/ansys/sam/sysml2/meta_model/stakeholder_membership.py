"""Generated stakeholder membership class from metamodel."""

from __future__ import annotations

from .parameter_membership import ParameterMembership


class StakeholderMembership(ParameterMembership):
    """Java class 'com.ansys.metamodel.sysml2.StakeholderMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_stakeholder_parameter = None

    @property
    def owned_stakeholder_parameter(self) -> "PartUsage":  # noqa: F821
        """
        Get the owned stakeholder parameter property.

        Returns
        -------
        "PartUsage"
            Value of property owned stakeholder parameter.
        """
        return self._owned_stakeholder_parameter

    @owned_stakeholder_parameter.setter
    def owned_stakeholder_parameter(self, value: "PartUsage"):  # noqa: F821
        """
        Set the owned_stakeholder_parameter property.

        Parameters
        ----------
        value: "PartUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_stakeholder_parameter", value)
        self._owned_stakeholder_parameter = value
