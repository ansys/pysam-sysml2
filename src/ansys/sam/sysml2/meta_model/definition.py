"""Generated definition class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .classifier import Classifier


class Definition(Classifier):
    """Java class 'com.ansys.medini.metamodel.sysml.Definition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._variant = ObservedList(self, "variant")
        self._is_variation = None
        self._owned_metadata = ObservedList(self, "owned_metadata")
        self._owned_flow = ObservedList(self, "owned_flow")
        self._owned_occurrence = ObservedList(self, "owned_occurrence")
        self._owned_attribute = ObservedList(self, "owned_attribute")
        self._owned_use_case = ObservedList(self, "owned_use_case")
        self._owned_usage = ObservedList(self, "owned_usage")
        self._owned_state = ObservedList(self, "owned_state")
        self._owned_connection = ObservedList(self, "owned_connection")
        self._owned_interface = ObservedList(self, "owned_interface")
        self._owned_port = ObservedList(self, "owned_port")
        self._owned_allocation = ObservedList(self, "owned_allocation")
        self._owned_case = ObservedList(self, "owned_case")
        self._owned_transition = ObservedList(self, "owned_transition")
        self._owned_view = ObservedList(self, "owned_view")
        self._owned_item = ObservedList(self, "owned_item")
        self._owned_constraint = ObservedList(self, "owned_constraint")
        self._owned_reference = ObservedList(self, "owned_reference")
        self._owned_part = ObservedList(self, "owned_part")
        self._owned_action = ObservedList(self, "owned_action")
        self._variant_membership = ObservedList(self, "variant_membership")
        self._owned_verification_case = ObservedList(self, "owned_verification_case")
        self._owned_calculation = ObservedList(self, "owned_calculation")
        self._owned_analysis_case = ObservedList(self, "owned_analysis_case")
        self._owned_enumeration = ObservedList(self, "owned_enumeration")
        self._owned_requirement = ObservedList(self, "owned_requirement")

    @property
    def variant(self) -> List["Usage"]:  # noqa: F821
        """
        Get the variant property.

        Returns
        -------
        List["Usage"]
            Value of property variant.
        """
        return self._variant

    @property
    def is_variation(self) -> None:  # noqa: F821
        """
        Get the is variation property.

        Returns
        -------
        None
            Value of property is variation.
        """
        return self._is_variation

    @is_variation.setter
    def is_variation(self, value: None):  # noqa: F821
        """
        Set the is_variation property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_variation", value)
        self._is_variation = value

    @property
    def owned_metadata(self) -> List["MetadataUsage"]:  # noqa: F821
        """
        Get the owned metadata property.

        Returns
        -------
        List["MetadataUsage"]
            Value of property owned metadata.
        """
        return self._owned_metadata

    @property
    def owned_flow(self) -> List["FlowConnectionUsage"]:  # noqa: F821
        """
        Get the owned flow property.

        Returns
        -------
        List["FlowConnectionUsage"]
            Value of property owned flow.
        """
        return self._owned_flow

    @property
    def owned_occurrence(self) -> List["OccurrenceUsage"]:  # noqa: F821
        """
        Get the owned occurrence property.

        Returns
        -------
        List["OccurrenceUsage"]
            Value of property owned occurrence.
        """
        return self._owned_occurrence

    @property
    def owned_attribute(self) -> List["AttributeUsage"]:  # noqa: F821
        """
        Get the owned attribute property.

        Returns
        -------
        List["AttributeUsage"]
            Value of property owned attribute.
        """
        return self._owned_attribute

    @property
    def owned_use_case(self) -> List["UseCaseUsage"]:  # noqa: F821
        """
        Get the owned use case property.

        Returns
        -------
        List["UseCaseUsage"]
            Value of property owned use case.
        """
        return self._owned_use_case

    @property
    def owned_usage(self) -> List["Usage"]:  # noqa: F821
        """
        Get the owned usage property.

        Returns
        -------
        List["Usage"]
            Value of property owned usage.
        """
        return self._owned_usage

    @property
    def owned_state(self) -> List["StateUsage"]:  # noqa: F821
        """
        Get the owned state property.

        Returns
        -------
        List["StateUsage"]
            Value of property owned state.
        """
        return self._owned_state

    @property
    def owned_connection(self) -> List["ConnectorAsUsage"]:  # noqa: F821
        """
        Get the owned connection property.

        Returns
        -------
        List["ConnectorAsUsage"]
            Value of property owned connection.
        """
        return self._owned_connection

    @property
    def owned_interface(self) -> List["InterfaceUsage"]:  # noqa: F821
        """
        Get the owned interface property.

        Returns
        -------
        List["InterfaceUsage"]
            Value of property owned interface.
        """
        return self._owned_interface

    @property
    def owned_port(self) -> List["PortUsage"]:  # noqa: F821
        """
        Get the owned port property.

        Returns
        -------
        List["PortUsage"]
            Value of property owned port.
        """
        return self._owned_port

    @property
    def owned_allocation(self) -> List["AllocationUsage"]:  # noqa: F821
        """
        Get the owned allocation property.

        Returns
        -------
        List["AllocationUsage"]
            Value of property owned allocation.
        """
        return self._owned_allocation

    @property
    def owned_case(self) -> List["CaseUsage"]:  # noqa: F821
        """
        Get the owned case property.

        Returns
        -------
        List["CaseUsage"]
            Value of property owned case.
        """
        return self._owned_case

    @property
    def owned_transition(self) -> List["TransitionUsage"]:  # noqa: F821
        """
        Get the owned transition property.

        Returns
        -------
        List["TransitionUsage"]
            Value of property owned transition.
        """
        return self._owned_transition

    @property
    def owned_view(self) -> List["ViewUsage"]:  # noqa: F821
        """
        Get the owned view property.

        Returns
        -------
        List["ViewUsage"]
            Value of property owned view.
        """
        return self._owned_view

    @property
    def owned_item(self) -> List["ItemUsage"]:  # noqa: F821
        """
        Get the owned item property.

        Returns
        -------
        List["ItemUsage"]
            Value of property owned item.
        """
        return self._owned_item

    @property
    def owned_constraint(self) -> List["ConstraintUsage"]:  # noqa: F821
        """
        Get the owned constraint property.

        Returns
        -------
        List["ConstraintUsage"]
            Value of property owned constraint.
        """
        return self._owned_constraint

    @property
    def owned_reference(self) -> List["ReferenceUsage"]:  # noqa: F821
        """
        Get the owned reference property.

        Returns
        -------
        List["ReferenceUsage"]
            Value of property owned reference.
        """
        return self._owned_reference

    @property
    def owned_part(self) -> List["PartUsage"]:  # noqa: F821
        """
        Get the owned part property.

        Returns
        -------
        List["PartUsage"]
            Value of property owned part.
        """
        return self._owned_part

    @property
    def owned_action(self) -> List["ActionUsage"]:  # noqa: F821
        """
        Get the owned action property.

        Returns
        -------
        List["ActionUsage"]
            Value of property owned action.
        """
        return self._owned_action

    @property
    def variant_membership(self) -> List["VariantMembership"]:  # noqa: F821
        """
        Get the variant membership property.

        Returns
        -------
        List["VariantMembership"]
            Value of property variant membership.
        """
        return self._variant_membership

    @property
    def owned_verification_case(self) -> List["VerificationCaseUsage"]:  # noqa: F821
        """
        Get the owned verification case property.

        Returns
        -------
        List["VerificationCaseUsage"]
            Value of property owned verification case.
        """
        return self._owned_verification_case

    @property
    def owned_calculation(self) -> List["CalculationUsage"]:  # noqa: F821
        """
        Get the owned calculation property.

        Returns
        -------
        List["CalculationUsage"]
            Value of property owned calculation.
        """
        return self._owned_calculation

    @property
    def owned_analysis_case(self) -> List["AnalysisCaseUsage"]:  # noqa: F821
        """
        Get the owned analysis case property.

        Returns
        -------
        List["AnalysisCaseUsage"]
            Value of property owned analysis case.
        """
        return self._owned_analysis_case

    @property
    def owned_enumeration(self) -> List["EnumerationUsage"]:  # noqa: F821
        """
        Get the owned enumeration property.

        Returns
        -------
        List["EnumerationUsage"]
            Value of property owned enumeration.
        """
        return self._owned_enumeration

    @property
    def owned_requirement(self) -> List["RequirementUsage"]:  # noqa: F821
        """
        Get the owned requirement property.

        Returns
        -------
        List["RequirementUsage"]
            Value of property owned requirement.
        """
        return self._owned_requirement
