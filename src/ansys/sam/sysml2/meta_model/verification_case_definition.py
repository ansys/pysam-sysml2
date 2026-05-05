"""Generated verification case definition class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .case_definition import CaseDefinition


class VerificationCaseDefinition(CaseDefinition):
    """Java class 'com.ansys.metamodel.sysml2.VerificationCaseDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._verified_requirement = ObservedList(self, "verified_requirement")

    @property
    def verified_requirement(self) -> list["RequirementUsage"]:  # noqa: F821
        """
        Get the verified requirement property.

        Returns
        -------
        list["RequirementUsage"]
            Value of property verified requirement.
        """
        return self._verified_requirement
