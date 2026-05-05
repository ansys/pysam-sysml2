"""Generated definition class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .classifier import Classifier


class Definition(Classifier):
    """Java class 'com.ansys.metamodel.sysml2.Definition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._directed_usage = ObservedList(self, "directed_usage")
        self._owned_action = ObservedList(self, "owned_action")
        self._owned_allocation = ObservedList(self, "owned_allocation")
        self._owned_analysis_case = ObservedList(self, "owned_analysis_case")
        self._owned_attribute = ObservedList(self, "owned_attribute")
        self._owned_calculation = ObservedList(self, "owned_calculation")
        self._owned_case = ObservedList(self, "owned_case")
        self._owned_concern = ObservedList(self, "owned_concern")
        self._owned_connection = ObservedList(self, "owned_connection")
        self._owned_constraint = ObservedList(self, "owned_constraint")
        self._owned_enumeration = ObservedList(self, "owned_enumeration")
        self._owned_flow = ObservedList(self, "owned_flow")
        self._owned_interface = ObservedList(self, "owned_interface")
        self._owned_item = ObservedList(self, "owned_item")
        self._owned_metadata = ObservedList(self, "owned_metadata")
        self._owned_occurrence = ObservedList(self, "owned_occurrence")
        self._owned_part = ObservedList(self, "owned_part")
        self._owned_port = ObservedList(self, "owned_port")
        self._owned_reference = ObservedList(self, "owned_reference")
        self._owned_rendering = ObservedList(self, "owned_rendering")
        self._owned_requirement = ObservedList(self, "owned_requirement")
        self._owned_state = ObservedList(self, "owned_state")
        self._owned_transition = ObservedList(self, "owned_transition")
        self._owned_usage = ObservedList(self, "owned_usage")
        self._owned_use_case = ObservedList(self, "owned_use_case")
        self._owned_verification_case = ObservedList(self, "owned_verification_case")
        self._owned_view = ObservedList(self, "owned_view")
        self._owned_viewpoint = ObservedList(self, "owned_viewpoint")
        self._usage = ObservedList(self, "usage")
        self._variant = ObservedList(self, "variant")
        self._variant_membership = ObservedList(self, "variant_membership")
        self._is_variation = False

    @property
    def directed_usage(self) -> list["Usage"]:  # noqa: F821
        """
        Get the directed usage property.

        Returns
        -------
        list["Usage"]
            Value of property directed usage.
        """
        return self._directed_usage

    @property
    def owned_action(self) -> list["ActionUsage"]:  # noqa: F821
        """
        Get the owned action property.

        Returns
        -------
        list["ActionUsage"]
            Value of property owned action.
        """
        return self._owned_action

    @property
    def owned_allocation(self) -> list["AllocationUsage"]:  # noqa: F821
        """
        Get the owned allocation property.

        Returns
        -------
        list["AllocationUsage"]
            Value of property owned allocation.
        """
        return self._owned_allocation

    @property
    def owned_analysis_case(self) -> list["AnalysisCaseUsage"]:  # noqa: F821
        """
        Get the owned analysis case property.

        Returns
        -------
        list["AnalysisCaseUsage"]
            Value of property owned analysis case.
        """
        return self._owned_analysis_case

    @property
    def owned_attribute(self) -> list["AttributeUsage"]:  # noqa: F821
        """
        Get the owned attribute property.

        Returns
        -------
        list["AttributeUsage"]
            Value of property owned attribute.
        """
        return self._owned_attribute

    @property
    def owned_calculation(self) -> list["CalculationUsage"]:  # noqa: F821
        """
        Get the owned calculation property.

        Returns
        -------
        list["CalculationUsage"]
            Value of property owned calculation.
        """
        return self._owned_calculation

    @property
    def owned_case(self) -> list["CaseUsage"]:  # noqa: F821
        """
        Get the owned case property.

        Returns
        -------
        list["CaseUsage"]
            Value of property owned case.
        """
        return self._owned_case

    @property
    def owned_concern(self) -> list["ConcernUsage"]:  # noqa: F821
        """
        Get the owned concern property.

        Returns
        -------
        list["ConcernUsage"]
            Value of property owned concern.
        """
        return self._owned_concern

    @property
    def owned_connection(self) -> list["ConnectorAsUsage"]:  # noqa: F821
        """
        Get the owned connection property.

        Returns
        -------
        list["ConnectorAsUsage"]
            Value of property owned connection.
        """
        return self._owned_connection

    @property
    def owned_constraint(self) -> list["ConstraintUsage"]:  # noqa: F821
        """
        Get the owned constraint property.

        Returns
        -------
        list["ConstraintUsage"]
            Value of property owned constraint.
        """
        return self._owned_constraint

    @property
    def owned_enumeration(self) -> list["EnumerationUsage"]:  # noqa: F821
        """
        Get the owned enumeration property.

        Returns
        -------
        list["EnumerationUsage"]
            Value of property owned enumeration.
        """
        return self._owned_enumeration

    @property
    def owned_flow(self) -> list["FlowUsage"]:  # noqa: F821
        """
        Get the owned flow property.

        Returns
        -------
        list["FlowUsage"]
            Value of property owned flow.
        """
        return self._owned_flow

    @property
    def owned_interface(self) -> list["InterfaceUsage"]:  # noqa: F821
        """
        Get the owned interface property.

        Returns
        -------
        list["InterfaceUsage"]
            Value of property owned interface.
        """
        return self._owned_interface

    @property
    def owned_item(self) -> list["ItemUsage"]:  # noqa: F821
        """
        Get the owned item property.

        Returns
        -------
        list["ItemUsage"]
            Value of property owned item.
        """
        return self._owned_item

    @property
    def owned_metadata(self) -> list["MetadataUsage"]:  # noqa: F821
        """
        Get the owned metadata property.

        Returns
        -------
        list["MetadataUsage"]
            Value of property owned metadata.
        """
        return self._owned_metadata

    @property
    def owned_occurrence(self) -> list["OccurrenceUsage"]:  # noqa: F821
        """
        Get the owned occurrence property.

        Returns
        -------
        list["OccurrenceUsage"]
            Value of property owned occurrence.
        """
        return self._owned_occurrence

    @property
    def owned_part(self) -> list["PartUsage"]:  # noqa: F821
        """
        Get the owned part property.

        Returns
        -------
        list["PartUsage"]
            Value of property owned part.
        """
        return self._owned_part

    @property
    def owned_port(self) -> list["PortUsage"]:  # noqa: F821
        """
        Get the owned port property.

        Returns
        -------
        list["PortUsage"]
            Value of property owned port.
        """
        return self._owned_port

    @property
    def owned_reference(self) -> list["ReferenceUsage"]:  # noqa: F821
        """
        Get the owned reference property.

        Returns
        -------
        list["ReferenceUsage"]
            Value of property owned reference.
        """
        return self._owned_reference

    @property
    def owned_rendering(self) -> list["RenderingUsage"]:  # noqa: F821
        """
        Get the owned rendering property.

        Returns
        -------
        list["RenderingUsage"]
            Value of property owned rendering.
        """
        return self._owned_rendering

    @property
    def owned_requirement(self) -> list["RequirementUsage"]:  # noqa: F821
        """
        Get the owned requirement property.

        Returns
        -------
        list["RequirementUsage"]
            Value of property owned requirement.
        """
        return self._owned_requirement

    @property
    def owned_state(self) -> list["StateUsage"]:  # noqa: F821
        """
        Get the owned state property.

        Returns
        -------
        list["StateUsage"]
            Value of property owned state.
        """
        return self._owned_state

    @property
    def owned_transition(self) -> list["TransitionUsage"]:  # noqa: F821
        """
        Get the owned transition property.

        Returns
        -------
        list["TransitionUsage"]
            Value of property owned transition.
        """
        return self._owned_transition

    @property
    def owned_usage(self) -> list["Usage"]:  # noqa: F821
        """
        Get the owned usage property.

        Returns
        -------
        list["Usage"]
            Value of property owned usage.
        """
        return self._owned_usage

    @property
    def owned_use_case(self) -> list["UseCaseUsage"]:  # noqa: F821
        """
        Get the owned use case property.

        Returns
        -------
        list["UseCaseUsage"]
            Value of property owned use case.
        """
        return self._owned_use_case

    @property
    def owned_verification_case(self) -> list["VerificationCaseUsage"]:  # noqa: F821
        """
        Get the owned verification case property.

        Returns
        -------
        list["VerificationCaseUsage"]
            Value of property owned verification case.
        """
        return self._owned_verification_case

    @property
    def owned_view(self) -> list["ViewUsage"]:  # noqa: F821
        """
        Get the owned view property.

        Returns
        -------
        list["ViewUsage"]
            Value of property owned view.
        """
        return self._owned_view

    @property
    def owned_viewpoint(self) -> list["ViewpointUsage"]:  # noqa: F821
        """
        Get the owned viewpoint property.

        Returns
        -------
        list["ViewpointUsage"]
            Value of property owned viewpoint.
        """
        return self._owned_viewpoint

    @property
    def usage(self) -> list["Usage"]:  # noqa: F821
        """
        Get the usage property.

        Returns
        -------
        list["Usage"]
            Value of property usage.
        """
        return self._usage

    @property
    def variant(self) -> list["Usage"]:  # noqa: F821
        """
        Get the variant property.

        Returns
        -------
        list["Usage"]
            Value of property variant.
        """
        return self._variant

    @property
    def variant_membership(self) -> list["VariantMembership"]:  # noqa: F821
        """
        Get the variant membership property.

        Returns
        -------
        list["VariantMembership"]
            Value of property variant membership.
        """
        return self._variant_membership

    @property
    def is_variation(self) -> bool:  # noqa: F821
        """
        Get the is variation property.

        Returns
        -------
        bool
            Value of property is variation.
        """
        return self._is_variation

    @is_variation.setter
    def is_variation(self, value: bool):  # noqa: F821
        """
        Set the is_variation property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_variation", value)
        self._is_variation = value
