"""Generated case usage class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .calculation_usage import CalculationUsage


class CaseUsage(CalculationUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.CaseUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._case_definition = None
        self._actor_parameter = ObservedList(self, "actor_parameter")
        self._objective_requirement = None
        self._subject_parameter = None

    @property
    def case_definition(self) -> "CaseDefinition":  # noqa: F821
        """
        Get the case definition property.

        Returns
        -------
        "CaseDefinition"
            Value of property case definition.
        """
        return self._case_definition

    @case_definition.setter
    def case_definition(self, value: "CaseDefinition"):  # noqa: F821
        """
        Set the case_definition property.

        Parameters
        ----------
        value: "CaseDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "case_definition", value)
        self._case_definition = value

    @property
    def actor_parameter(self) -> List["PartUsage"]:  # noqa: F821
        """
        Get the actor parameter property.

        Returns
        -------
        List["PartUsage"]
            Value of property actor parameter.
        """
        return self._actor_parameter

    @property
    def objective_requirement(self) -> None:  # noqa: F821
        """
        Get the objective requirement property.

        Returns
        -------
        None
            Value of property objective requirement.
        """
        return self._objective_requirement

    @objective_requirement.setter
    def objective_requirement(self, value: None):  # noqa: F821
        """
        Set the objective_requirement property.

        Parameters
        ----------
        value: None
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
