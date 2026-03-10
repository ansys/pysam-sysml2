"""Generated objective membership class from metamodel."""

from __future__ import annotations

from .feature_membership import FeatureMembership


class ObjectiveMembership(FeatureMembership):
    """Java class 'com.ansys.medini.metamodel.sysml.ObjectiveMembership'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._owned_objective_requirement = None

    @property
    def owned_objective_requirement(self) -> "RequirementUsage":  # noqa: F821
        """
        Get the owned objective requirement property.

        Returns
        -------
        "RequirementUsage"
            Value of property owned objective requirement.
        """
        return self._owned_objective_requirement

    @owned_objective_requirement.setter
    def owned_objective_requirement(self, value: "RequirementUsage"):  # noqa: F821
        """
        Set the owned_objective_requirement property.

        Parameters
        ----------
        value: "RequirementUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_objective_requirement", value)
        self._owned_objective_requirement = value
