"""Generated requirement verification membership class from metamodel."""

from __future__ import annotations

from .requirement_constraint_membership import RequirementConstraintMembership


class RequirementVerificationMembership(RequirementConstraintMembership):
    """Java class 'com.ansys.metamodel.sysml2.RequirementVerificationMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_requirement = None
        self._verified_requirement = None

    @property
    def owned_requirement(self) -> "RequirementUsage":  # noqa: F821
        """
        Get the owned requirement property.

        Returns
        -------
        "RequirementUsage"
            Value of property owned requirement.
        """
        return self._owned_requirement

    @owned_requirement.setter
    def owned_requirement(self, value: "RequirementUsage"):  # noqa: F821
        """
        Set the owned_requirement property.

        Parameters
        ----------
        value: "RequirementUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_requirement", value)
        self._owned_requirement = value

    @property
    def verified_requirement(self) -> "RequirementUsage":  # noqa: F821
        """
        Get the verified requirement property.

        Returns
        -------
        "RequirementUsage"
            Value of property verified requirement.
        """
        return self._verified_requirement

    @verified_requirement.setter
    def verified_requirement(self, value: "RequirementUsage"):  # noqa: F821
        """
        Set the verified_requirement property.

        Parameters
        ----------
        value: "RequirementUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "verified_requirement", value)
        self._verified_requirement = value
