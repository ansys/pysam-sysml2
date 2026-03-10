"""Generated requirement definition class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .constraint_definition import ConstraintDefinition


class RequirementDefinition(ConstraintDefinition):
    """Java class 'com.ansys.medini.metamodel.sysml.RequirementDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._text = ObservedList(self, "text")
        self._actor_parameter = ObservedList(self, "actor_parameter")
        self._framed_concern = ObservedList(self, "framed_concern")
        self._all_text = ObservedList(self, "all_text")
        self._req_id = ""
        self._assumed_constraint = ObservedList(self, "assumed_constraint")
        self._required_constraint = ObservedList(self, "required_constraint")
        self._subject_parameter = None
        self._stakeholder_parameter = ObservedList(self, "stakeholder_parameter")

    @property
    def text(self) -> List[str]:  # noqa: F821
        """
        Get the text property.

        Returns
        -------
        List[str]
            Value of property text.
        """
        return self._text

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
    def framed_concern(self) -> List["ConcernUsage"]:  # noqa: F821
        """
        Get the framed concern property.

        Returns
        -------
        List["ConcernUsage"]
            Value of property framed concern.
        """
        return self._framed_concern

    @property
    def all_text(self) -> List[str]:  # noqa: F821
        """
        Get the all text property.

        Returns
        -------
        List[str]
            Value of property all text.
        """
        return self._all_text

    @property
    def req_id(self) -> str:  # noqa: F821
        """
        Get the req id property.

        Returns
        -------
        str
            Value of property req id.
        """
        return self._req_id

    @req_id.setter
    def req_id(self, value: str):  # noqa: F821
        """
        Set the req_id property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "req_id", value)
        self._req_id = value

    @property
    def assumed_constraint(self) -> List["ConstraintUsage"]:  # noqa: F821
        """
        Get the assumed constraint property.

        Returns
        -------
        List["ConstraintUsage"]
            Value of property assumed constraint.
        """
        return self._assumed_constraint

    @property
    def required_constraint(self) -> List["ConstraintUsage"]:  # noqa: F821
        """
        Get the required constraint property.

        Returns
        -------
        List["ConstraintUsage"]
            Value of property required constraint.
        """
        return self._required_constraint

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

    @property
    def stakeholder_parameter(self) -> List["PartUsage"]:  # noqa: F821
        """
        Get the stakeholder parameter property.

        Returns
        -------
        List["PartUsage"]
            Value of property stakeholder parameter.
        """
        return self._stakeholder_parameter
