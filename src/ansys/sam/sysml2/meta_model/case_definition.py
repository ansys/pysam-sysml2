"""Generated case definition class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .calculation_definition import CalculationDefinition


class CaseDefinition(CalculationDefinition):
    """Java class 'com.ansys.metamodel.sysml2.CaseDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._actor_parameter = ObservedList(self, "actor_parameter")
        self._objective_requirement = None
        self._subject_parameter = None

    @property
    def actor_parameter(self) -> list["PartUsage"]:  # noqa: F821
        """
        Get the actor parameter property.

        Returns
        -------
        list["PartUsage"]
            Value of property actor parameter.
        """
        return self._actor_parameter

    @property
    def objective_requirement(self) -> "RequirementUsage":  # noqa: F821
        """
        Get the objective requirement property.

        Returns
        -------
        "RequirementUsage"
            Value of property objective requirement.
        """
        return self._objective_requirement

    @objective_requirement.setter
    def objective_requirement(self, value: "RequirementUsage"):  # noqa: F821
        """
        Set the objective_requirement property.

        Parameters
        ----------
        value: "RequirementUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "objective_requirement", value)
        self._objective_requirement = value

    @property
    def subject_parameter(self) -> "Usage":  # noqa: F821
        """
        Get the subject parameter property.

        Returns
        -------
        "Usage"
            Value of property subject parameter.
        """
        return self._subject_parameter

    @subject_parameter.setter
    def subject_parameter(self, value: "Usage"):  # noqa: F821
        """
        Set the subject_parameter property.

        Parameters
        ----------
        value: "Usage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "subject_parameter", value)
        self._subject_parameter = value
