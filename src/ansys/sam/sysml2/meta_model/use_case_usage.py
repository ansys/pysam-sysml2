"""Generated use case usage class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .case_usage import CaseUsage


class UseCaseUsage(CaseUsage):
    """Java class 'com.ansys.metamodel.sysml2.UseCaseUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._included_use_case = ObservedList(self, "included_use_case")
        self._use_case_definition = None

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

    @property
    def use_case_definition(self) -> "UseCaseDefinition":  # noqa: F821
        """
        Get the use case definition property.

        Returns
        -------
        "UseCaseDefinition"
            Value of property use case definition.
        """
        return self._use_case_definition

    @use_case_definition.setter
    def use_case_definition(self, value: "UseCaseDefinition"):  # noqa: F821
        """
        Set the use_case_definition property.

        Parameters
        ----------
        value: "UseCaseDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "use_case_definition", value)
        self._use_case_definition = value
