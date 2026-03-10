"""Generated verification case usage class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .case_usage import CaseUsage


class VerificationCaseUsage(CaseUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.VerificationCaseUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._verification_case_definition = None
        self._verified_requirement = ObservedList(self, "verified_requirement")

    @property
    def verification_case_definition(self) -> "VerificationCaseDefinition":  # noqa: F821
        """
        Get the verification case definition property.

        Returns
        -------
        "VerificationCaseDefinition"
            Value of property verification case definition.
        """
        return self._verification_case_definition

    @verification_case_definition.setter
    def verification_case_definition(self, value: "VerificationCaseDefinition"):  # noqa: F821
        """
        Set the verification_case_definition property.

        Parameters
        ----------
        value: "VerificationCaseDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "verification_case_definition", value)
        self._verification_case_definition = value

    @property
    def verified_requirement(self) -> List["RequirementUsage"]:  # noqa: F821
        """
        Get the verified requirement property.

        Returns
        -------
        List["RequirementUsage"]
            Value of property verified requirement.
        """
        return self._verified_requirement
