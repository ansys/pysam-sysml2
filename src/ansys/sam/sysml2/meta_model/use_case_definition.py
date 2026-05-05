"""Generated use case definition class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .case_definition import CaseDefinition


class UseCaseDefinition(CaseDefinition):
    """Java class 'com.ansys.metamodel.sysml2.UseCaseDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._included_use_case = ObservedList(self, "included_use_case")

    @property
    def included_use_case(self) -> list["UseCaseUsage"]:  # noqa: F821
        """
        Get the included use case property.

        Returns
        -------
        list["UseCaseUsage"]
            Value of property included use case.
        """
        return self._included_use_case
