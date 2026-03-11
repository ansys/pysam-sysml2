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
"""Metamodel package."""

from .accept_action_usage import AcceptActionUsage as AcceptActionUsage
from .action_definition import ActionDefinition as ActionDefinition
from .action_usage import ActionUsage as ActionUsage
from .actor_membership import ActorMembership as ActorMembership
from .allocation_definition import AllocationDefinition as AllocationDefinition
from .allocation_usage import AllocationUsage as AllocationUsage
from .annotating_element import AnnotatingElement as AnnotatingElement
from .annotation import Annotation as Annotation
from .assert_constraint_usage import AssertConstraintUsage as AssertConstraintUsage
from .assignment_action_usage import AssignmentActionUsage as AssignmentActionUsage
from .association import Association as Association
from .association_structure import AssociationStructure as AssociationStructure
from .attribute_definition import AttributeDefinition as AttributeDefinition
from .attribute_usage import AttributeUsage as AttributeUsage
from .behavior import Behavior as Behavior
from .binding_connector import BindingConnector as BindingConnector
from .binding_connector_as_usage import (
    BindingConnectorAsUsage as BindingConnectorAsUsage,
)
from .boolean_expression import BooleanExpression as BooleanExpression
from .calculation_definition import CalculationDefinition as CalculationDefinition
from .calculation_usage import CalculationUsage as CalculationUsage
from .case_definition import CaseDefinition as CaseDefinition
from .case_usage import CaseUsage as CaseUsage
from .class_ import Class as Class
from .classifier import Classifier as Classifier
from .comment import Comment as Comment
from .concern_usage import ConcernUsage as ConcernUsage
from .connection_definition import ConnectionDefinition as ConnectionDefinition
from .connection_usage import ConnectionUsage as ConnectionUsage
from .connector import Connector as Connector
from .constraint_definition import ConstraintDefinition as ConstraintDefinition
from .constraint_usage import ConstraintUsage as ConstraintUsage
from .data_type import DataType as DataType
from .decision_node import DecisionNode as DecisionNode
from .definition import Definition as Definition
from .dependency import Dependency as Dependency
from .documentation import Documentation as Documentation
from .element import Element as Element
from .end_feature_membership import EndFeatureMembership as EndFeatureMembership
from .enumeration_definition import EnumerationDefinition as EnumerationDefinition
from .enumeration_usage import EnumerationUsage as EnumerationUsage
from .event_occurrence_usage import EventOccurrenceUsage as EventOccurrenceUsage
from .exhibit_state_usage import ExhibitStateUsage as ExhibitStateUsage
from .expression import Expression as Expression
from .feature import Feature as Feature
from .feature_chain_expression import FeatureChainExpression as FeatureChainExpression
from .feature_chaining import FeatureChaining as FeatureChaining
from .feature_membership import FeatureMembership as FeatureMembership
from .feature_reference_expression import (
    FeatureReferenceExpression as FeatureReferenceExpression,
)
from .feature_typing import FeatureTyping as FeatureTyping
from .feature_value import FeatureValue as FeatureValue
from .flow_connection_definition import (
    FlowConnectionDefinition as FlowConnectionDefinition,
)
from .flow_connection_usage import FlowConnectionUsage as FlowConnectionUsage
from .for_loop_action_usage import ForLoopActionUsage as ForLoopActionUsage
from .fork_node import ForkNode as ForkNode
from .function import Function as Function
from .if_action_usage import IfActionUsage as IfActionUsage
from .import_ import Import as Import
from .include_use_case_usage import IncludeUseCaseUsage as IncludeUseCaseUsage
from .interaction import Interaction as Interaction
from .interface_definition import InterfaceDefinition as InterfaceDefinition
from .interface_usage import InterfaceUsage as InterfaceUsage
from .invariant import Invariant as Invariant
from .invocation_expression import InvocationExpression as InvocationExpression
from .item_definition import ItemDefinition as ItemDefinition
from .item_feature import ItemFeature as ItemFeature
from .item_flow import ItemFlow as ItemFlow
from .item_flow_end import ItemFlowEnd as ItemFlowEnd
from .item_usage import ItemUsage as ItemUsage
from .join_node import JoinNode as JoinNode
from .library_package import LibraryPackage as LibraryPackage
from .life_class import LifeClass as LifeClass
from .literal_boolean import LiteralBoolean as LiteralBoolean
from .literal_expression import LiteralExpression as LiteralExpression
from .literal_integer import LiteralInteger as LiteralInteger
from .literal_rational import LiteralRational as LiteralRational
from .literal_real import LiteralReal as LiteralReal
from .literal_string import LiteralString as LiteralString
from .literal_unbounded import LiteralUnbounded as LiteralUnbounded
from .loop_action_usage import LoopActionUsage as LoopActionUsage
from .membership import Membership as Membership
from .merge_node import MergeNode as MergeNode
from .metaclass import Metaclass as Metaclass
from .metadata_definition import MetadataDefinition as MetadataDefinition
from .metadata_feature import MetadataFeature as MetadataFeature
from .metadata_usage import MetadataUsage as MetadataUsage
from .multiplicity import Multiplicity as Multiplicity
from .multiplicity_range import MultiplicityRange as MultiplicityRange
from .namespace import Namespace as Namespace
from .null_expression import NullExpression as NullExpression
from .objective_membership import ObjectiveMembership as ObjectiveMembership
from .occurrence_definition import OccurrenceDefinition as OccurrenceDefinition
from .occurrence_usage import OccurrenceUsage as OccurrenceUsage
from .operator_expression import OperatorExpression as OperatorExpression
from .package import Package as Package
from .parameter_membership import ParameterMembership as ParameterMembership
from .part_definition import PartDefinition as PartDefinition
from .part_usage import PartUsage as PartUsage
from .perform_action_usage import PerformActionUsage as PerformActionUsage
from .port_definition import PortDefinition as PortDefinition
from .port_usage import PortUsage as PortUsage
from .portioning_feature import PortioningFeature as PortioningFeature
from .predicate import Predicate as Predicate
from .redefinition import Redefinition as Redefinition
from .reference_subsetting import ReferenceSubsetting as ReferenceSubsetting
from .reference_usage import ReferenceUsage as ReferenceUsage
from .relationship import Relationship as Relationship
from .requirement_constraint_membership import (
    RequirementConstraintMembership as RequirementConstraintMembership,
)
from .requirement_definition import RequirementDefinition as RequirementDefinition
from .requirement_usage import RequirementUsage as RequirementUsage
from .result_expression_membership import (
    ResultExpressionMembership as ResultExpressionMembership,
)
from .return_parameter_membership import (
    ReturnParameterMembership as ReturnParameterMembership,
)
from .satisfy_requirement_usage import (
    SatisfyRequirementUsage as SatisfyRequirementUsage,
)
from .send_action_usage import SendActionUsage as SendActionUsage
from .specialization import Specialization as Specialization
from .stakeholder_membership import StakeholderMembership as StakeholderMembership
from .state_definition import StateDefinition as StateDefinition
from .state_subaction_membership import (
    StateSubactionMembership as StateSubactionMembership,
)
from .state_usage import StateUsage as StateUsage
from .step import Step as Step
from .structure import Structure as Structure
from .subclassification import Subclassification as Subclassification
from .subject_membership import SubjectMembership as SubjectMembership
from .subsetting import Subsetting as Subsetting
from .succession import Succession as Succession
from .succession_as_usage import SuccessionAsUsage as SuccessionAsUsage
from .succession_flow_connection_usage import (
    SuccessionFlowConnectionUsage as SuccessionFlowConnectionUsage,
)
from .succession_item_flow import SuccessionItemFlow as SuccessionItemFlow
from .textual_representation import TextualRepresentation as TextualRepresentation
from .transition_feature_membership import (
    TransitionFeatureMembership as TransitionFeatureMembership,
)
from .transition_usage import TransitionUsage as TransitionUsage
from .trigger_invocation_expression import (
    TriggerInvocationExpression as TriggerInvocationExpression,
)
from .type_ import Type as Type
from .type_featuring import TypeFeaturing as TypeFeaturing
from .usage import Usage as Usage
from .use_case_definition import UseCaseDefinition as UseCaseDefinition
from .use_case_usage import UseCaseUsage as UseCaseUsage
from .variant_membership import VariantMembership as VariantMembership
from .view_definition import ViewDefinition as ViewDefinition
from .view_usage import ViewUsage as ViewUsage
from .while_loop_action_usage import WhileLoopActionUsage as WhileLoopActionUsage
