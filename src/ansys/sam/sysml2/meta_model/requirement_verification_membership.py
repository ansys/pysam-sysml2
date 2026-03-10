"""Generated requirement verification membership class from metamodel."""

from __future__ import annotations

from .requirement_constraint_membership import RequirementConstraintMembership


class RequirementVerificationMembership(RequirementConstraintMembership):
    """Java class 'com.ansys.medini.metamodel.sysml.RequirementVerificationMembership'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._verified_requirement = None

    @property
    def verified_requirement(self) -> None:  # noqa: F821
        """
        Get the verified requirement property.

        Returns
        -------
        None
            Value of property verified requirement.
        """
        return self._verified_requirement

    @verified_requirement.setter
    def verified_requirement(self, value: None):  # noqa: F821
        """
        Set the verified_requirement property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "verified_requirement", value)
        self._verified_requirement = value
