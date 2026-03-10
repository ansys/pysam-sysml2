"""Generated use case definition class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .case_definition import CaseDefinition


class UseCaseDefinition(CaseDefinition):
    """Java class 'com.ansys.medini.metamodel.sysml.UseCaseDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._included_use_case = ObservedList(self, "included_use_case")

    @property
    def included_use_case(self) -> List["UseCaseUsage"]:  # noqa: F821
        """
        Get the included use case property.

        Returns
        -------
        List["UseCaseUsage"]
            Value of property included use case.
        """
        return self._included_use_case
