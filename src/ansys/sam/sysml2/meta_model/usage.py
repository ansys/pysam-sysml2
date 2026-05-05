"""Generated usage class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .feature import Feature


class Usage(Feature):
    """Java class 'com.ansys.metamodel.sysml2.Usage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._definition = ObservedList(self, "definition")
        self._directed_usage = ObservedList(self, "directed_usage")
        self._nested_action = ObservedList(self, "nested_action")
        self._nested_allocation = ObservedList(self, "nested_allocation")
        self._nested_analysis_case = ObservedList(self, "nested_analysis_case")
        self._nested_attribute = ObservedList(self, "nested_attribute")
        self._nested_calculation = ObservedList(self, "nested_calculation")
        self._nested_case = ObservedList(self, "nested_case")
        self._nested_concern = ObservedList(self, "nested_concern")
        self._nested_connection = ObservedList(self, "nested_connection")
        self._nested_constraint = ObservedList(self, "nested_constraint")
        self._nested_enumeration = ObservedList(self, "nested_enumeration")
        self._nested_flow = ObservedList(self, "nested_flow")
        self._nested_interface = ObservedList(self, "nested_interface")
        self._nested_item = ObservedList(self, "nested_item")
        self._nested_metadata = ObservedList(self, "nested_metadata")
        self._nested_occurrence = ObservedList(self, "nested_occurrence")
        self._nested_part = ObservedList(self, "nested_part")
        self._nested_port = ObservedList(self, "nested_port")
        self._nested_reference = ObservedList(self, "nested_reference")
        self._nested_rendering = ObservedList(self, "nested_rendering")
        self._nested_requirement = ObservedList(self, "nested_requirement")
        self._nested_state = ObservedList(self, "nested_state")
        self._nested_transition = ObservedList(self, "nested_transition")
        self._nested_usage = ObservedList(self, "nested_usage")
        self._nested_use_case = ObservedList(self, "nested_use_case")
        self._nested_verification_case = ObservedList(self, "nested_verification_case")
        self._nested_view = ObservedList(self, "nested_view")
        self._nested_viewpoint = ObservedList(self, "nested_viewpoint")
        self._owning_definition = None
        self._owning_usage = None
        self._usage = ObservedList(self, "usage")
        self._variant = ObservedList(self, "variant")
        self._variant_membership = ObservedList(self, "variant_membership")
        self._is_reference = False
        self._is_variation = False
        self._may_time_vary = False

    @property
    def definition(self) -> list["Classifier"]:  # noqa: F821
        """
        Get the definition property.

        Returns
        -------
        list["Classifier"]
            Value of property definition.
        """
        return self._definition

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
    def nested_action(self) -> list["ActionUsage"]:  # noqa: F821
        """
        Get the nested action property.

        Returns
        -------
        list["ActionUsage"]
            Value of property nested action.
        """
        return self._nested_action

    @property
    def nested_allocation(self) -> list["AllocationUsage"]:  # noqa: F821
        """
        Get the nested allocation property.

        Returns
        -------
        list["AllocationUsage"]
            Value of property nested allocation.
        """
        return self._nested_allocation

    @property
    def nested_analysis_case(self) -> list["AnalysisCaseUsage"]:  # noqa: F821
        """
        Get the nested analysis case property.

        Returns
        -------
        list["AnalysisCaseUsage"]
            Value of property nested analysis case.
        """
        return self._nested_analysis_case

    @property
    def nested_attribute(self) -> list["AttributeUsage"]:  # noqa: F821
        """
        Get the nested attribute property.

        Returns
        -------
        list["AttributeUsage"]
            Value of property nested attribute.
        """
        return self._nested_attribute

    @property
    def nested_calculation(self) -> list["CalculationUsage"]:  # noqa: F821
        """
        Get the nested calculation property.

        Returns
        -------
        list["CalculationUsage"]
            Value of property nested calculation.
        """
        return self._nested_calculation

    @property
    def nested_case(self) -> list["CaseUsage"]:  # noqa: F821
        """
        Get the nested case property.

        Returns
        -------
        list["CaseUsage"]
            Value of property nested case.
        """
        return self._nested_case

    @property
    def nested_concern(self) -> list["ConcernUsage"]:  # noqa: F821
        """
        Get the nested concern property.

        Returns
        -------
        list["ConcernUsage"]
            Value of property nested concern.
        """
        return self._nested_concern

    @property
    def nested_connection(self) -> list["ConnectorAsUsage"]:  # noqa: F821
        """
        Get the nested connection property.

        Returns
        -------
        list["ConnectorAsUsage"]
            Value of property nested connection.
        """
        return self._nested_connection

    @property
    def nested_constraint(self) -> list["ConstraintUsage"]:  # noqa: F821
        """
        Get the nested constraint property.

        Returns
        -------
        list["ConstraintUsage"]
            Value of property nested constraint.
        """
        return self._nested_constraint

    @property
    def nested_enumeration(self) -> list["EnumerationUsage"]:  # noqa: F821
        """
        Get the nested enumeration property.

        Returns
        -------
        list["EnumerationUsage"]
            Value of property nested enumeration.
        """
        return self._nested_enumeration

    @property
    def nested_flow(self) -> list["FlowUsage"]:  # noqa: F821
        """
        Get the nested flow property.

        Returns
        -------
        list["FlowUsage"]
            Value of property nested flow.
        """
        return self._nested_flow

    @property
    def nested_interface(self) -> list["InterfaceUsage"]:  # noqa: F821
        """
        Get the nested interface property.

        Returns
        -------
        list["InterfaceUsage"]
            Value of property nested interface.
        """
        return self._nested_interface

    @property
    def nested_item(self) -> list["ItemUsage"]:  # noqa: F821
        """
        Get the nested item property.

        Returns
        -------
        list["ItemUsage"]
            Value of property nested item.
        """
        return self._nested_item

    @property
    def nested_metadata(self) -> list["MetadataUsage"]:  # noqa: F821
        """
        Get the nested metadata property.

        Returns
        -------
        list["MetadataUsage"]
            Value of property nested metadata.
        """
        return self._nested_metadata

    @property
    def nested_occurrence(self) -> list["OccurrenceUsage"]:  # noqa: F821
        """
        Get the nested occurrence property.

        Returns
        -------
        list["OccurrenceUsage"]
            Value of property nested occurrence.
        """
        return self._nested_occurrence

    @property
    def nested_part(self) -> list["PartUsage"]:  # noqa: F821
        """
        Get the nested part property.

        Returns
        -------
        list["PartUsage"]
            Value of property nested part.
        """
        return self._nested_part

    @property
    def nested_port(self) -> list["PortUsage"]:  # noqa: F821
        """
        Get the nested port property.

        Returns
        -------
        list["PortUsage"]
            Value of property nested port.
        """
        return self._nested_port

    @property
    def nested_reference(self) -> list["ReferenceUsage"]:  # noqa: F821
        """
        Get the nested reference property.

        Returns
        -------
        list["ReferenceUsage"]
            Value of property nested reference.
        """
        return self._nested_reference

    @property
    def nested_rendering(self) -> list["RenderingUsage"]:  # noqa: F821
        """
        Get the nested rendering property.

        Returns
        -------
        list["RenderingUsage"]
            Value of property nested rendering.
        """
        return self._nested_rendering

    @property
    def nested_requirement(self) -> list["RequirementUsage"]:  # noqa: F821
        """
        Get the nested requirement property.

        Returns
        -------
        list["RequirementUsage"]
            Value of property nested requirement.
        """
        return self._nested_requirement

    @property
    def nested_state(self) -> list["StateUsage"]:  # noqa: F821
        """
        Get the nested state property.

        Returns
        -------
        list["StateUsage"]
            Value of property nested state.
        """
        return self._nested_state

    @property
    def nested_transition(self) -> list["TransitionUsage"]:  # noqa: F821
        """
        Get the nested transition property.

        Returns
        -------
        list["TransitionUsage"]
            Value of property nested transition.
        """
        return self._nested_transition

    @property
    def nested_usage(self) -> list["Usage"]:  # noqa: F821
        """
        Get the nested usage property.

        Returns
        -------
        list["Usage"]
            Value of property nested usage.
        """
        return self._nested_usage

    @property
    def nested_use_case(self) -> list["UseCaseUsage"]:  # noqa: F821
        """
        Get the nested use case property.

        Returns
        -------
        list["UseCaseUsage"]
            Value of property nested use case.
        """
        return self._nested_use_case

    @property
    def nested_verification_case(self) -> list["VerificationCaseUsage"]:  # noqa: F821
        """
        Get the nested verification case property.

        Returns
        -------
        list["VerificationCaseUsage"]
            Value of property nested verification case.
        """
        return self._nested_verification_case

    @property
    def nested_view(self) -> list["ViewUsage"]:  # noqa: F821
        """
        Get the nested view property.

        Returns
        -------
        list["ViewUsage"]
            Value of property nested view.
        """
        return self._nested_view

    @property
    def nested_viewpoint(self) -> list["ViewpointUsage"]:  # noqa: F821
        """
        Get the nested viewpoint property.

        Returns
        -------
        list["ViewpointUsage"]
            Value of property nested viewpoint.
        """
        return self._nested_viewpoint

    @property
    def owning_definition(self) -> "Definition":  # noqa: F821
        """
        Get the owning definition property.

        Returns
        -------
        "Definition"
            Value of property owning definition.
        """
        return self._owning_definition

    @owning_definition.setter
    def owning_definition(self, value: "Definition"):  # noqa: F821
        """
        Set the owning_definition property.

        Parameters
        ----------
        value: "Definition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_definition", value)
        self._owning_definition = value

    @property
    def owning_usage(self) -> "Usage":  # noqa: F821
        """
        Get the owning usage property.

        Returns
        -------
        "Usage"
            Value of property owning usage.
        """
        return self._owning_usage

    @owning_usage.setter
    def owning_usage(self, value: "Usage"):  # noqa: F821
        """
        Set the owning_usage property.

        Parameters
        ----------
        value: "Usage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_usage", value)
        self._owning_usage = value

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
    def is_reference(self) -> bool:  # noqa: F821
        """
        Get the is reference property.

        Returns
        -------
        bool
            Value of property is reference.
        """
        return self._is_reference

    @is_reference.setter
    def is_reference(self, value: bool):  # noqa: F821
        """
        Set the is_reference property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_reference", value)
        self._is_reference = value

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

    @property
    def may_time_vary(self) -> bool:  # noqa: F821
        """
        Get the may time vary property.

        Returns
        -------
        bool
            Value of property may time vary.
        """
        return self._may_time_vary

    @may_time_vary.setter
    def may_time_vary(self, value: bool):  # noqa: F821
        """
        Set the may_time_vary property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "may_time_vary", value)
        self._may_time_vary = value
