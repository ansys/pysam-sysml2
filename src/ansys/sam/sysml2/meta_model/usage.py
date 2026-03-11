# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Generated usage class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .feature import Feature


class Usage(Feature):
    """Java class 'com.ansys.medini.metamodel.sysml.Usage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._definition = ObservedList(self, "definition")
        self._variant = ObservedList(self, "variant")
        self._nested_interface = ObservedList(self, "nested_interface")
        self._nested_part = ObservedList(self, "nested_part")
        self._nested_usage = ObservedList(self, "nested_usage")
        self._nested_port = ObservedList(self, "nested_port")
        self._nested_item = ObservedList(self, "nested_item")
        self._nested_state = ObservedList(self, "nested_state")
        self._nested_reference = ObservedList(self, "nested_reference")
        self._is_subject = False
        self._nested_attribute = ObservedList(self, "nested_attribute")
        self._nested_case = ObservedList(self, "nested_case")
        self._is_variation = None
        self._nested_action = ObservedList(self, "nested_action")
        self._nested_view = ObservedList(self, "nested_view")
        self._nested_use_case = ObservedList(self, "nested_use_case")
        self._nested_metadata = ObservedList(self, "nested_metadata")
        self._nested_flow = ObservedList(self, "nested_flow")
        self._nested_enumeration = ObservedList(self, "nested_enumeration")
        self._variant_membership = ObservedList(self, "variant_membership")
        self._nested_transition = ObservedList(self, "nested_transition")
        self._nested_occurrence = ObservedList(self, "nested_occurrence")
        self._nested_calculation = ObservedList(self, "nested_calculation")
        self._nested_verification_case = ObservedList(self, "nested_verification_case")
        self._nested_analysis_case = ObservedList(self, "nested_analysis_case")
        self._nested_requirement = ObservedList(self, "nested_requirement")
        self._nested_connection = ObservedList(self, "nested_connection")
        self._nested_allocation = ObservedList(self, "nested_allocation")
        self._nested_constraint = ObservedList(self, "nested_constraint")

    @property
    def definition(self) -> List["Classifier"]:  # noqa: F821
        """
        Get the definition property.

        Returns
        -------
        List["Classifier"]
            Value of property definition.
        """
        return self._definition

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
    def nested_interface(self) -> List["InterfaceUsage"]:  # noqa: F821
        """
        Get the nested interface property.

        Returns
        -------
        List["InterfaceUsage"]
            Value of property nested interface.
        """
        return self._nested_interface

    @property
    def nested_part(self) -> List["PartUsage"]:  # noqa: F821
        """
        Get the nested part property.

        Returns
        -------
        List["PartUsage"]
            Value of property nested part.
        """
        return self._nested_part

    @property
    def nested_usage(self) -> List["Usage"]:  # noqa: F821
        """
        Get the nested usage property.

        Returns
        -------
        List["Usage"]
            Value of property nested usage.
        """
        return self._nested_usage

    @property
    def nested_port(self) -> List["PortUsage"]:  # noqa: F821
        """
        Get the nested port property.

        Returns
        -------
        List["PortUsage"]
            Value of property nested port.
        """
        return self._nested_port

    @property
    def nested_item(self) -> List["ItemUsage"]:  # noqa: F821
        """
        Get the nested item property.

        Returns
        -------
        List["ItemUsage"]
            Value of property nested item.
        """
        return self._nested_item

    @property
    def nested_state(self) -> List["StateUsage"]:  # noqa: F821
        """
        Get the nested state property.

        Returns
        -------
        List["StateUsage"]
            Value of property nested state.
        """
        return self._nested_state

    @property
    def nested_reference(self) -> List["ReferenceUsage"]:  # noqa: F821
        """
        Get the nested reference property.

        Returns
        -------
        List["ReferenceUsage"]
            Value of property nested reference.
        """
        return self._nested_reference

    @property
    def is_subject(self) -> bool:  # noqa: F821
        """
        Get the is subject property.

        Returns
        -------
        bool
            Value of property is subject.
        """
        return self._is_subject

    @is_subject.setter
    def is_subject(self, value: bool):  # noqa: F821
        """
        Set the is_subject property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_subject", value)
        self._is_subject = value

    @property
    def nested_attribute(self) -> List["AttributeUsage"]:  # noqa: F821
        """
        Get the nested attribute property.

        Returns
        -------
        List["AttributeUsage"]
            Value of property nested attribute.
        """
        return self._nested_attribute

    @property
    def nested_case(self) -> List["CaseUsage"]:  # noqa: F821
        """
        Get the nested case property.

        Returns
        -------
        List["CaseUsage"]
            Value of property nested case.
        """
        return self._nested_case

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
    def nested_action(self) -> List["ActionUsage"]:  # noqa: F821
        """
        Get the nested action property.

        Returns
        -------
        List["ActionUsage"]
            Value of property nested action.
        """
        return self._nested_action

    @property
    def nested_view(self) -> List["ViewUsage"]:  # noqa: F821
        """
        Get the nested view property.

        Returns
        -------
        List["ViewUsage"]
            Value of property nested view.
        """
        return self._nested_view

    @property
    def nested_use_case(self) -> List["UseCaseUsage"]:  # noqa: F821
        """
        Get the nested use case property.

        Returns
        -------
        List["UseCaseUsage"]
            Value of property nested use case.
        """
        return self._nested_use_case

    @property
    def nested_metadata(self) -> List["MetadataUsage"]:  # noqa: F821
        """
        Get the nested metadata property.

        Returns
        -------
        List["MetadataUsage"]
            Value of property nested metadata.
        """
        return self._nested_metadata

    @property
    def nested_flow(self) -> List["FlowConnectionUsage"]:  # noqa: F821
        """
        Get the nested flow property.

        Returns
        -------
        List["FlowConnectionUsage"]
            Value of property nested flow.
        """
        return self._nested_flow

    @property
    def nested_enumeration(self) -> List["EnumerationUsage"]:  # noqa: F821
        """
        Get the nested enumeration property.

        Returns
        -------
        List["EnumerationUsage"]
            Value of property nested enumeration.
        """
        return self._nested_enumeration

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
    def nested_transition(self) -> List["TransitionUsage"]:  # noqa: F821
        """
        Get the nested transition property.

        Returns
        -------
        List["TransitionUsage"]
            Value of property nested transition.
        """
        return self._nested_transition

    @property
    def nested_occurrence(self) -> List["OccurrenceUsage"]:  # noqa: F821
        """
        Get the nested occurrence property.

        Returns
        -------
        List["OccurrenceUsage"]
            Value of property nested occurrence.
        """
        return self._nested_occurrence

    @property
    def nested_calculation(self) -> List["CalculationUsage"]:  # noqa: F821
        """
        Get the nested calculation property.

        Returns
        -------
        List["CalculationUsage"]
            Value of property nested calculation.
        """
        return self._nested_calculation

    @property
    def nested_verification_case(self) -> List["VerificationCaseUsage"]:  # noqa: F821
        """
        Get the nested verification case property.

        Returns
        -------
        List["VerificationCaseUsage"]
            Value of property nested verification case.
        """
        return self._nested_verification_case

    @property
    def nested_analysis_case(self) -> List["AnalysisCaseUsage"]:  # noqa: F821
        """
        Get the nested analysis case property.

        Returns
        -------
        List["AnalysisCaseUsage"]
            Value of property nested analysis case.
        """
        return self._nested_analysis_case

    @property
    def nested_requirement(self) -> List["RequirementUsage"]:  # noqa: F821
        """
        Get the nested requirement property.

        Returns
        -------
        List["RequirementUsage"]
            Value of property nested requirement.
        """
        return self._nested_requirement

    @property
    def nested_connection(self) -> List["ConnectorAsUsage"]:  # noqa: F821
        """
        Get the nested connection property.

        Returns
        -------
        List["ConnectorAsUsage"]
            Value of property nested connection.
        """
        return self._nested_connection

    @property
    def nested_allocation(self) -> List["AllocationUsage"]:  # noqa: F821
        """
        Get the nested allocation property.

        Returns
        -------
        List["AllocationUsage"]
            Value of property nested allocation.
        """
        return self._nested_allocation

    @property
    def nested_constraint(self) -> List["ConstraintUsage"]:  # noqa: F821
        """
        Get the nested constraint property.

        Returns
        -------
        List["ConstraintUsage"]
            Value of property nested constraint.
        """
        return self._nested_constraint
