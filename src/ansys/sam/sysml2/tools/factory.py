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
"""Factory class to create new elements."""

from uuid import uuid4

from ansys.sam.sysml2.meta_model.accept_action_usage import AcceptActionUsage as AcceptActionUsage
from ansys.sam.sysml2.meta_model.action_definition import ActionDefinition as ActionDefinition
from ansys.sam.sysml2.meta_model.action_usage import ActionUsage as ActionUsage
from ansys.sam.sysml2.meta_model.actor_membership import ActorMembership as ActorMembership
from ansys.sam.sysml2.meta_model.allocation_definition import (
    AllocationDefinition as AllocationDefinition,
)
from ansys.sam.sysml2.meta_model.allocation_usage import AllocationUsage as AllocationUsage
from ansys.sam.sysml2.meta_model.analysis_case_definition import (
    AnalysisCaseDefinition as AnalysisCaseDefinition,
)
from ansys.sam.sysml2.meta_model.analysis_case_usage import AnalysisCaseUsage as AnalysisCaseUsage
from ansys.sam.sysml2.meta_model.annotating_element import AnnotatingElement as AnnotatingElement
from ansys.sam.sysml2.meta_model.annotation import Annotation as Annotation
from ansys.sam.sysml2.meta_model.assert_constraint_usage import (
    AssertConstraintUsage as AssertConstraintUsage,
)
from ansys.sam.sysml2.meta_model.assignment_action_usage import (
    AssignmentActionUsage as AssignmentActionUsage,
)
from ansys.sam.sysml2.meta_model.association import Association as Association
from ansys.sam.sysml2.meta_model.association_structure import (
    AssociationStructure as AssociationStructure,
)
from ansys.sam.sysml2.meta_model.attribute_definition import (
    AttributeDefinition as AttributeDefinition,
)
from ansys.sam.sysml2.meta_model.attribute_usage import AttributeUsage as AttributeUsage
from ansys.sam.sysml2.meta_model.behavior import Behavior as Behavior
from ansys.sam.sysml2.meta_model.binding_connector import BindingConnector as BindingConnector
from ansys.sam.sysml2.meta_model.binding_connector_as_usage import (
    BindingConnectorAsUsage as BindingConnectorAsUsage,
)
from ansys.sam.sysml2.meta_model.boolean_expression import BooleanExpression as BooleanExpression
from ansys.sam.sysml2.meta_model.calculation_definition import (
    CalculationDefinition as CalculationDefinition,
)
from ansys.sam.sysml2.meta_model.calculation_usage import CalculationUsage as CalculationUsage
from ansys.sam.sysml2.meta_model.case_definition import CaseDefinition as CaseDefinition
from ansys.sam.sysml2.meta_model.case_usage import CaseUsage as CaseUsage
from ansys.sam.sysml2.meta_model.class_ import Class as Class
from ansys.sam.sysml2.meta_model.classifier import Classifier as Classifier
from ansys.sam.sysml2.meta_model.collect_expression import CollectExpression as CollectExpression
from ansys.sam.sysml2.meta_model.comment import Comment as Comment
from ansys.sam.sysml2.meta_model.concern_definition import ConcernDefinition as ConcernDefinition
from ansys.sam.sysml2.meta_model.concern_usage import ConcernUsage as ConcernUsage
from ansys.sam.sysml2.meta_model.conjugated_port_definition import (
    ConjugatedPortDefinition as ConjugatedPortDefinition,
)
from ansys.sam.sysml2.meta_model.conjugated_port_typing import (
    ConjugatedPortTyping as ConjugatedPortTyping,
)
from ansys.sam.sysml2.meta_model.conjugation import Conjugation as Conjugation
from ansys.sam.sysml2.meta_model.connection_definition import (
    ConnectionDefinition as ConnectionDefinition,
)
from ansys.sam.sysml2.meta_model.connection_usage import ConnectionUsage as ConnectionUsage
from ansys.sam.sysml2.meta_model.connector import Connector as Connector
from ansys.sam.sysml2.meta_model.connector_as_usage import ConnectorAsUsage as ConnectorAsUsage
from ansys.sam.sysml2.meta_model.constraint_definition import (
    ConstraintDefinition as ConstraintDefinition,
)
from ansys.sam.sysml2.meta_model.constraint_usage import ConstraintUsage as ConstraintUsage
from ansys.sam.sysml2.meta_model.constructor_expression import (
    ConstructorExpression as ConstructorExpression,
)
from ansys.sam.sysml2.meta_model.control_node import ControlNode as ControlNode
from ansys.sam.sysml2.meta_model.cross_subsetting import CrossSubsetting as CrossSubsetting
from ansys.sam.sysml2.meta_model.data_type import DataType as DataType
from ansys.sam.sysml2.meta_model.decision_node import DecisionNode as DecisionNode
from ansys.sam.sysml2.meta_model.definition import Definition as Definition
from ansys.sam.sysml2.meta_model.dependency import Dependency as Dependency
from ansys.sam.sysml2.meta_model.differencing import Differencing as Differencing
from ansys.sam.sysml2.meta_model.disjoining import Disjoining as Disjoining
from ansys.sam.sysml2.meta_model.documentation import Documentation as Documentation
from ansys.sam.sysml2.meta_model.element import Element as Element
from ansys.sam.sysml2.meta_model.element_filter_membership import (
    ElementFilterMembership as ElementFilterMembership,
)
from ansys.sam.sysml2.meta_model.end_feature_membership import (
    EndFeatureMembership as EndFeatureMembership,
)
from ansys.sam.sysml2.meta_model.enumeration_definition import (
    EnumerationDefinition as EnumerationDefinition,
)
from ansys.sam.sysml2.meta_model.enumeration_usage import EnumerationUsage as EnumerationUsage
from ansys.sam.sysml2.meta_model.event_occurrence_usage import (
    EventOccurrenceUsage as EventOccurrenceUsage,
)
from ansys.sam.sysml2.meta_model.exhibit_state_usage import ExhibitStateUsage as ExhibitStateUsage
from ansys.sam.sysml2.meta_model.expose import Expose as Expose
from ansys.sam.sysml2.meta_model.expression import Expression as Expression
from ansys.sam.sysml2.meta_model.feature import Feature as Feature
from ansys.sam.sysml2.meta_model.feature_chain_expression import (
    FeatureChainExpression as FeatureChainExpression,
)
from ansys.sam.sysml2.meta_model.feature_chaining import FeatureChaining as FeatureChaining
from ansys.sam.sysml2.meta_model.feature_direction_kind import (
    FeatureDirectionKind as FeatureDirectionKind,
)
from ansys.sam.sysml2.meta_model.feature_inverting import FeatureInverting as FeatureInverting
from ansys.sam.sysml2.meta_model.feature_membership import FeatureMembership as FeatureMembership
from ansys.sam.sysml2.meta_model.feature_reference_expression import (
    FeatureReferenceExpression as FeatureReferenceExpression,
)
from ansys.sam.sysml2.meta_model.feature_typing import FeatureTyping as FeatureTyping
from ansys.sam.sysml2.meta_model.feature_value import FeatureValue as FeatureValue
from ansys.sam.sysml2.meta_model.flow import Flow as Flow
from ansys.sam.sysml2.meta_model.flow_definition import FlowDefinition as FlowDefinition
from ansys.sam.sysml2.meta_model.flow_end import FlowEnd as FlowEnd
from ansys.sam.sysml2.meta_model.flow_usage import FlowUsage as FlowUsage
from ansys.sam.sysml2.meta_model.for_loop_action_usage import (
    ForLoopActionUsage as ForLoopActionUsage,
)
from ansys.sam.sysml2.meta_model.fork_node import ForkNode as ForkNode
from ansys.sam.sysml2.meta_model.framed_concern_membership import (
    FramedConcernMembership as FramedConcernMembership,
)
from ansys.sam.sysml2.meta_model.function import Function as Function
from ansys.sam.sysml2.meta_model.if_action_usage import IfActionUsage as IfActionUsage
from ansys.sam.sysml2.meta_model.import_ import Import as Import
from ansys.sam.sysml2.meta_model.include_use_case_usage import (
    IncludeUseCaseUsage as IncludeUseCaseUsage,
)
from ansys.sam.sysml2.meta_model.index_expression import IndexExpression as IndexExpression
from ansys.sam.sysml2.meta_model.instantiation_expression import (
    InstantiationExpression as InstantiationExpression,
)
from ansys.sam.sysml2.meta_model.interaction import Interaction as Interaction
from ansys.sam.sysml2.meta_model.interface_definition import (
    InterfaceDefinition as InterfaceDefinition,
)
from ansys.sam.sysml2.meta_model.interface_usage import InterfaceUsage as InterfaceUsage
from ansys.sam.sysml2.meta_model.intersecting import Intersecting as Intersecting
from ansys.sam.sysml2.meta_model.invariant import Invariant as Invariant
from ansys.sam.sysml2.meta_model.invocation_expression import (
    InvocationExpression as InvocationExpression,
)
from ansys.sam.sysml2.meta_model.item_definition import ItemDefinition as ItemDefinition
from ansys.sam.sysml2.meta_model.item_usage import ItemUsage as ItemUsage
from ansys.sam.sysml2.meta_model.join_node import JoinNode as JoinNode
from ansys.sam.sysml2.meta_model.library_package import LibraryPackage as LibraryPackage
from ansys.sam.sysml2.meta_model.literal_boolean import LiteralBoolean as LiteralBoolean
from ansys.sam.sysml2.meta_model.literal_expression import LiteralExpression as LiteralExpression
from ansys.sam.sysml2.meta_model.literal_infinity import LiteralInfinity as LiteralInfinity
from ansys.sam.sysml2.meta_model.literal_integer import LiteralInteger as LiteralInteger
from ansys.sam.sysml2.meta_model.literal_rational import LiteralRational as LiteralRational
from ansys.sam.sysml2.meta_model.literal_string import LiteralString as LiteralString
from ansys.sam.sysml2.meta_model.loop_action_usage import LoopActionUsage as LoopActionUsage
from ansys.sam.sysml2.meta_model.membership import Membership as Membership
from ansys.sam.sysml2.meta_model.membership_expose import MembershipExpose as MembershipExpose
from ansys.sam.sysml2.meta_model.membership_import import MembershipImport as MembershipImport
from ansys.sam.sysml2.meta_model.merge_node import MergeNode as MergeNode
from ansys.sam.sysml2.meta_model.metaclass import Metaclass as Metaclass
from ansys.sam.sysml2.meta_model.metadata_access_expression import (
    MetadataAccessExpression as MetadataAccessExpression,
)
from ansys.sam.sysml2.meta_model.metadata_definition import MetadataDefinition as MetadataDefinition
from ansys.sam.sysml2.meta_model.metadata_feature import MetadataFeature as MetadataFeature
from ansys.sam.sysml2.meta_model.metadata_usage import MetadataUsage as MetadataUsage
from ansys.sam.sysml2.meta_model.multiplicity import Multiplicity as Multiplicity
from ansys.sam.sysml2.meta_model.multiplicity_range import MultiplicityRange as MultiplicityRange
from ansys.sam.sysml2.meta_model.namespace import Namespace as Namespace
from ansys.sam.sysml2.meta_model.namespace_expose import NamespaceExpose as NamespaceExpose
from ansys.sam.sysml2.meta_model.namespace_import import NamespaceImport as NamespaceImport
from ansys.sam.sysml2.meta_model.null_expression import NullExpression as NullExpression
from ansys.sam.sysml2.meta_model.objective_membership import (
    ObjectiveMembership as ObjectiveMembership,
)
from ansys.sam.sysml2.meta_model.occurrence_definition import (
    OccurrenceDefinition as OccurrenceDefinition,
)
from ansys.sam.sysml2.meta_model.occurrence_usage import OccurrenceUsage as OccurrenceUsage
from ansys.sam.sysml2.meta_model.operator_expression import OperatorExpression as OperatorExpression
from ansys.sam.sysml2.meta_model.owning_membership import OwningMembership as OwningMembership
from ansys.sam.sysml2.meta_model.package import Package as Package
from ansys.sam.sysml2.meta_model.parameter_membership import (
    ParameterMembership as ParameterMembership,
)
from ansys.sam.sysml2.meta_model.part_definition import PartDefinition as PartDefinition
from ansys.sam.sysml2.meta_model.part_usage import PartUsage as PartUsage
from ansys.sam.sysml2.meta_model.payload_feature import PayloadFeature as PayloadFeature
from ansys.sam.sysml2.meta_model.perform_action_usage import (
    PerformActionUsage as PerformActionUsage,
)
from ansys.sam.sysml2.meta_model.port_conjugation import PortConjugation as PortConjugation
from ansys.sam.sysml2.meta_model.port_definition import PortDefinition as PortDefinition
from ansys.sam.sysml2.meta_model.port_usage import PortUsage as PortUsage
from ansys.sam.sysml2.meta_model.portion_kind import PortionKind as PortionKind
from ansys.sam.sysml2.meta_model.predicate import Predicate as Predicate
from ansys.sam.sysml2.meta_model.redefinition import Redefinition as Redefinition
from ansys.sam.sysml2.meta_model.reference_subsetting import (
    ReferenceSubsetting as ReferenceSubsetting,
)
from ansys.sam.sysml2.meta_model.reference_usage import ReferenceUsage as ReferenceUsage
from ansys.sam.sysml2.meta_model.relationship import Relationship as Relationship
from ansys.sam.sysml2.meta_model.rendering_definition import (
    RenderingDefinition as RenderingDefinition,
)
from ansys.sam.sysml2.meta_model.rendering_usage import RenderingUsage as RenderingUsage
from ansys.sam.sysml2.meta_model.requirement_constraint_kind import (
    RequirementConstraintKind as RequirementConstraintKind,
)
from ansys.sam.sysml2.meta_model.requirement_constraint_membership import (
    RequirementConstraintMembership as RequirementConstraintMembership,
)
from ansys.sam.sysml2.meta_model.requirement_definition import (
    RequirementDefinition as RequirementDefinition,
)
from ansys.sam.sysml2.meta_model.requirement_usage import RequirementUsage as RequirementUsage
from ansys.sam.sysml2.meta_model.requirement_verification_membership import (
    RequirementVerificationMembership as RequirementVerificationMembership,
)
from ansys.sam.sysml2.meta_model.result_expression_membership import (
    ResultExpressionMembership as ResultExpressionMembership,
)
from ansys.sam.sysml2.meta_model.return_parameter_membership import (
    ReturnParameterMembership as ReturnParameterMembership,
)
from ansys.sam.sysml2.meta_model.satisfy_requirement_usage import (
    SatisfyRequirementUsage as SatisfyRequirementUsage,
)
from ansys.sam.sysml2.meta_model.select_expression import SelectExpression as SelectExpression
from ansys.sam.sysml2.meta_model.send_action_usage import SendActionUsage as SendActionUsage
from ansys.sam.sysml2.meta_model.specialization import Specialization as Specialization
from ansys.sam.sysml2.meta_model.stakeholder_membership import (
    StakeholderMembership as StakeholderMembership,
)
from ansys.sam.sysml2.meta_model.state_definition import StateDefinition as StateDefinition
from ansys.sam.sysml2.meta_model.state_subaction_kind import (
    StateSubactionKind as StateSubactionKind,
)
from ansys.sam.sysml2.meta_model.state_subaction_membership import (
    StateSubactionMembership as StateSubactionMembership,
)
from ansys.sam.sysml2.meta_model.state_usage import StateUsage as StateUsage
from ansys.sam.sysml2.meta_model.step import Step as Step
from ansys.sam.sysml2.meta_model.structure import Structure as Structure
from ansys.sam.sysml2.meta_model.subclassification import Subclassification as Subclassification
from ansys.sam.sysml2.meta_model.subject_membership import SubjectMembership as SubjectMembership
from ansys.sam.sysml2.meta_model.subsetting import Subsetting as Subsetting
from ansys.sam.sysml2.meta_model.succession import Succession as Succession
from ansys.sam.sysml2.meta_model.succession_as_usage import SuccessionAsUsage as SuccessionAsUsage
from ansys.sam.sysml2.meta_model.succession_flow import SuccessionFlow as SuccessionFlow
from ansys.sam.sysml2.meta_model.succession_flow_usage import (
    SuccessionFlowUsage as SuccessionFlowUsage,
)
from ansys.sam.sysml2.meta_model.terminate_action_usage import (
    TerminateActionUsage as TerminateActionUsage,
)
from ansys.sam.sysml2.meta_model.textual_representation import (
    TextualRepresentation as TextualRepresentation,
)
from ansys.sam.sysml2.meta_model.transition_feature_kind import (
    TransitionFeatureKind as TransitionFeatureKind,
)
from ansys.sam.sysml2.meta_model.transition_feature_membership import (
    TransitionFeatureMembership as TransitionFeatureMembership,
)
from ansys.sam.sysml2.meta_model.transition_usage import TransitionUsage as TransitionUsage
from ansys.sam.sysml2.meta_model.trigger_invocation_expression import (
    TriggerInvocationExpression as TriggerInvocationExpression,
)
from ansys.sam.sysml2.meta_model.trigger_kind import TriggerKind as TriggerKind
from ansys.sam.sysml2.meta_model.type_ import Type as Type
from ansys.sam.sysml2.meta_model.type_featuring import TypeFeaturing as TypeFeaturing
from ansys.sam.sysml2.meta_model.unioning import Unioning as Unioning
from ansys.sam.sysml2.meta_model.usage import Usage as Usage
from ansys.sam.sysml2.meta_model.use_case_definition import UseCaseDefinition as UseCaseDefinition
from ansys.sam.sysml2.meta_model.use_case_usage import UseCaseUsage as UseCaseUsage
from ansys.sam.sysml2.meta_model.variant_membership import VariantMembership as VariantMembership
from ansys.sam.sysml2.meta_model.verification_case_definition import (
    VerificationCaseDefinition as VerificationCaseDefinition,
)
from ansys.sam.sysml2.meta_model.verification_case_usage import (
    VerificationCaseUsage as VerificationCaseUsage,
)
from ansys.sam.sysml2.meta_model.view_definition import ViewDefinition as ViewDefinition
from ansys.sam.sysml2.meta_model.view_rendering_membership import (
    ViewRenderingMembership as ViewRenderingMembership,
)
from ansys.sam.sysml2.meta_model.view_usage import ViewUsage as ViewUsage
from ansys.sam.sysml2.meta_model.viewpoint_definition import (
    ViewpointDefinition as ViewpointDefinition,
)
from ansys.sam.sysml2.meta_model.viewpoint_usage import ViewpointUsage as ViewpointUsage
from ansys.sam.sysml2.meta_model.visibility_kind import VisibilityKind as VisibilityKind
from ansys.sam.sysml2.meta_model.while_loop_action_usage import (
    WhileLoopActionUsage as WhileLoopActionUsage,
)


class Factory:
    """Provides the Python factory class for creating new SysML elements."""

    _project_id: str
    _project: Project | ScriptingProject
    _conn: AnsysSysML2APIConnector

    def __init__(self, project: Project | ScriptingProject, conn: AnsysSysML2APIConnector) -> None:
        """Initialize a new instance.

        Parameters
        ----------
        project: Project | ScriptingProject
            Project to be modified by the factory.
        conn: AnsysSysML2APIConnector
            Connector to make API calls.
        """
        self._project_id = project._id
        self._project = project
        self._conn = conn

    def create_function(self, **kwargs) -> Function:
        """
        Create a new Function.

        Returns
        -------
        Function
            The new model element
        """
        return self._create_element("Function", **kwargs)

    def create_class(self, **kwargs) -> Class:
        """
        Create a new Class.

        Returns
        -------
        Class
            The new model element
        """
        return self._create_element("Class", **kwargs)

    def create_behavior(self, **kwargs) -> Behavior:
        """
        Create a new Behavior.

        Returns
        -------
        Behavior
            The new model element
        """
        return self._create_element("Behavior", **kwargs)

    def create_comment(self, **kwargs) -> Comment:
        """
        Create a new Comment.

        Returns
        -------
        Comment
            The new model element
        """
        return self._create_element("Comment", **kwargs)

    def create_connector(self, **kwargs) -> Connector:
        """
        Create a new Connector.

        Returns
        -------
        Connector
            The new model element
        """
        return self._create_element("Connector", **kwargs)

    def create_element(self, **kwargs) -> Element:
        """
        Create a new Element.

        Returns
        -------
        Element
            The new model element
        """
        return self._create_element("Element", **kwargs)

    def create_association(self, **kwargs) -> Association:
        """
        Create a new Association.

        Returns
        -------
        Association
            The new model element
        """
        return self._create_element("Association", **kwargs)

    def create_classifier(self, **kwargs) -> Classifier:
        """
        Create a new Classifier.

        Returns
        -------
        Classifier
            The new model element
        """
        return self._create_element("Classifier", **kwargs)

    def create_data_type(self, **kwargs) -> DataType:
        """
        Create a new DataType.

        Returns
        -------
        DataType
            The new model element
        """
        return self._create_element("DataType", **kwargs)

    def create_expression(self, **kwargs) -> Expression:
        """
        Create a new Expression.

        Returns
        -------
        Expression
            The new model element
        """
        return self._create_element("Expression", **kwargs)

    def create_feature(self, **kwargs) -> Feature:
        """
        Create a new Feature.

        Returns
        -------
        Feature
            The new model element
        """
        return self._create_element("Feature", **kwargs)

    def create_annotation(self, **kwargs) -> Annotation:
        """
        Create a new Annotation.

        Returns
        -------
        Annotation
            The new model element
        """
        return self._create_element("Annotation", **kwargs)

    def create_import(self, **kwargs) -> Import:
        """
        Create a new Import.

        Returns
        -------
        Import
            The new model element
        """
        return self._create_element("Import", **kwargs)

    def create_structure(self, **kwargs) -> Structure:
        """
        Create a new Structure.

        Returns
        -------
        Structure
            The new model element
        """
        return self._create_element("Structure", **kwargs)

    def create_item_feature(self, **kwargs) -> ItemFeature:
        """
        Create a new ItemFeature.

        Returns
        -------
        ItemFeature
            The new model element
        """
        return self._create_element("ItemFeature", **kwargs)

    def create_dependency(self, **kwargs) -> Dependency:
        """
        Create a new Dependency.

        Returns
        -------
        Dependency
            The new model element
        """
        return self._create_element("Dependency", **kwargs)

    def create_interaction(self, **kwargs) -> Interaction:
        """
        Create a new Interaction.

        Returns
        -------
        Interaction
            The new model element
        """
        return self._create_element("Interaction", **kwargs)

    def create_redefinition(self, **kwargs) -> Redefinition:
        """
        Create a new Redefinition.

        Returns
        -------
        Redefinition
            The new model element
        """
        return self._create_element("Redefinition", **kwargs)

    def create_state_usage(self, **kwargs) -> StateUsage:
        """
        Create a new StateUsage.

        Returns
        -------
        StateUsage
            The new model element
        """
        return self._create_element("StateUsage", **kwargs)

    def create_life_class(self, **kwargs) -> LifeClass:
        """
        Create a new LifeClass.

        Returns
        -------
        LifeClass
            The new model element
        """
        return self._create_element("LifeClass", **kwargs)

    def create_metaclass(self, **kwargs) -> Metaclass:
        """
        Create a new Metaclass.

        Returns
        -------
        Metaclass
            The new model element
        """
        return self._create_element("Metaclass", **kwargs)

    def create_port_usage(self, **kwargs) -> PortUsage:
        """
        Create a new PortUsage.

        Returns
        -------
        PortUsage
            The new model element
        """
        return self._create_element("PortUsage", **kwargs)

    def create_namespace(self, **kwargs) -> Namespace:
        """
        Create a new Namespace.

        Returns
        -------
        Namespace
            The new model element
        """
        return self._create_element("Namespace", **kwargs)

    def create_step(self, **kwargs) -> Step:
        """
        Create a new Step.

        Returns
        -------
        Step
            The new model element
        """
        return self._create_element("Step", **kwargs)

    def create_succession(self, **kwargs) -> Succession:
        """
        Create a new Succession.

        Returns
        -------
        Succession
            The new model element
        """
        return self._create_element("Succession", **kwargs)

    def create_definition(self, **kwargs) -> Definition:
        """
        Create a new Definition.

        Returns
        -------
        Definition
            The new model element
        """
        return self._create_element("Definition", **kwargs)

    def create_concern_usage(self, **kwargs) -> ConcernUsage:
        """
        Create a new ConcernUsage.

        Returns
        -------
        ConcernUsage
            The new model element
        """
        return self._create_element("ConcernUsage", **kwargs)

    def create_item_flow(self, **kwargs) -> ItemFlow:
        """
        Create a new ItemFlow.

        Returns
        -------
        ItemFlow
            The new model element
        """
        return self._create_element("ItemFlow", **kwargs)

    def create_predicate(self, **kwargs) -> Predicate:
        """
        Create a new Predicate.

        Returns
        -------
        Predicate
            The new model element
        """
        return self._create_element("Predicate", **kwargs)

    def create_part_usage(self, **kwargs) -> PartUsage:
        """
        Create a new PartUsage.

        Returns
        -------
        PartUsage
            The new model element
        """
        return self._create_element("PartUsage", **kwargs)

    def create_package(self, **kwargs) -> Package:
        """
        Create a new Package.

        Returns
        -------
        Package
            The new model element
        """
        return self._create_element("Package", **kwargs)

    def create_merge_node(self, **kwargs) -> MergeNode:
        """
        Create a new MergeNode.

        Returns
        -------
        MergeNode
            The new model element
        """
        return self._create_element("MergeNode", **kwargs)

    def create_literal_real(self, **kwargs) -> LiteralReal:
        """
        Create a new LiteralReal.

        Returns
        -------
        LiteralReal
            The new model element
        """
        return self._create_element("LiteralReal", **kwargs)

    def create_fork_node(self, **kwargs) -> ForkNode:
        """
        Create a new ForkNode.

        Returns
        -------
        ForkNode
            The new model element
        """
        return self._create_element("ForkNode", **kwargs)

    def create_view_usage(self, **kwargs) -> ViewUsage:
        """
        Create a new ViewUsage.

        Returns
        -------
        ViewUsage
            The new model element
        """
        return self._create_element("ViewUsage", **kwargs)

    def create_case_usage(self, **kwargs) -> CaseUsage:
        """
        Create a new CaseUsage.

        Returns
        -------
        CaseUsage
            The new model element
        """
        return self._create_element("CaseUsage", **kwargs)

    def create_multiplicity(self, **kwargs) -> Multiplicity:
        """
        Create a new Multiplicity.

        Returns
        -------
        Multiplicity
            The new model element
        """
        return self._create_element("Multiplicity", **kwargs)

    def create_decision_node(self, **kwargs) -> DecisionNode:
        """
        Create a new DecisionNode.

        Returns
        -------
        DecisionNode
            The new model element
        """
        return self._create_element("DecisionNode", **kwargs)

    def create_item_usage(self, **kwargs) -> ItemUsage:
        """
        Create a new ItemUsage.

        Returns
        -------
        ItemUsage
            The new model element
        """
        return self._create_element("ItemUsage", **kwargs)

    def create_subsetting(self, **kwargs) -> Subsetting:
        """
        Create a new Subsetting.

        Returns
        -------
        Subsetting
            The new model element
        """
        return self._create_element("Subsetting", **kwargs)

    def create_usage(self, **kwargs) -> Usage:
        """
        Create a new Usage.

        Returns
        -------
        Usage
            The new model element
        """
        return self._create_element("Usage", **kwargs)

    def create_use_case_usage(self, **kwargs) -> UseCaseUsage:
        """
        Create a new UseCaseUsage.

        Returns
        -------
        UseCaseUsage
            The new model element
        """
        return self._create_element("UseCaseUsage", **kwargs)

    def create_feature_value(self, **kwargs) -> FeatureValue:
        """
        Create a new FeatureValue.

        Returns
        -------
        FeatureValue
            The new model element
        """
        return self._create_element("FeatureValue", **kwargs)

    def create_action_usage(self, **kwargs) -> ActionUsage:
        """
        Create a new ActionUsage.

        Returns
        -------
        ActionUsage
            The new model element
        """
        return self._create_element("ActionUsage", **kwargs)

    def create_membership(self, **kwargs) -> Membership:
        """
        Create a new Membership.

        Returns
        -------
        Membership
            The new model element
        """
        return self._create_element("Membership", **kwargs)

    def create_type(self, **kwargs) -> Type:
        """
        Create a new Type.

        Returns
        -------
        Type
            The new model element
        """
        return self._create_element("Type", **kwargs)

    def create_invariant(self, **kwargs) -> Invariant:
        """
        Create a new Invariant.

        Returns
        -------
        Invariant
            The new model element
        """
        return self._create_element("Invariant", **kwargs)

    def create_relationship(self, **kwargs) -> Relationship:
        """
        Create a new Relationship.

        Returns
        -------
        Relationship
            The new model element
        """
        return self._create_element("Relationship", **kwargs)

    def create_item_flow_end(self, **kwargs) -> ItemFlowEnd:
        """
        Create a new ItemFlowEnd.

        Returns
        -------
        ItemFlowEnd
            The new model element
        """
        return self._create_element("ItemFlowEnd", **kwargs)

    def create_join_node(self, **kwargs) -> JoinNode:
        """
        Create a new JoinNode.

        Returns
        -------
        JoinNode
            The new model element
        """
        return self._create_element("JoinNode", **kwargs)

    def create_attribute_definition(self, **kwargs) -> AttributeDefinition:
        """
        Create a new AttributeDefinition.

        Returns
        -------
        AttributeDefinition
            The new model element
        """
        return self._create_element("AttributeDefinition", **kwargs)

    def create_accept_action_usage(self, **kwargs) -> AcceptActionUsage:
        """
        Create a new AcceptActionUsage.

        Returns
        -------
        AcceptActionUsage
            The new model element
        """
        return self._create_element("AcceptActionUsage", **kwargs)

    def create_documentation(self, **kwargs) -> Documentation:
        """
        Create a new Documentation.

        Returns
        -------
        Documentation
            The new model element
        """
        return self._create_element("Documentation", **kwargs)

    def create_assignment_action_usage(self, **kwargs) -> AssignmentActionUsage:
        """
        Create a new AssignmentActionUsage.

        Returns
        -------
        AssignmentActionUsage
            The new model element
        """
        return self._create_element("AssignmentActionUsage", **kwargs)

    def create_item_definition(self, **kwargs) -> ItemDefinition:
        """
        Create a new ItemDefinition.

        Returns
        -------
        ItemDefinition
            The new model element
        """
        return self._create_element("ItemDefinition", **kwargs)

    def create_literal_boolean(self, **kwargs) -> LiteralBoolean:
        """
        Create a new LiteralBoolean.

        Returns
        -------
        LiteralBoolean
            The new model element
        """
        return self._create_element("LiteralBoolean", **kwargs)

    def create_binding_connector_as_usage(self, **kwargs) -> BindingConnectorAsUsage:
        """
        Create a new BindingConnectorAsUsage.

        Returns
        -------
        BindingConnectorAsUsage
            The new model element
        """
        return self._create_element("BindingConnectorAsUsage", **kwargs)

    def create_constraint_usage(self, **kwargs) -> ConstraintUsage:
        """
        Create a new ConstraintUsage.

        Returns
        -------
        ConstraintUsage
            The new model element
        """
        return self._create_element("ConstraintUsage", **kwargs)

    def create_literal_expression(self, **kwargs) -> LiteralExpression:
        """
        Create a new LiteralExpression.

        Returns
        -------
        LiteralExpression
            The new model element
        """
        return self._create_element("LiteralExpression", **kwargs)

    def create_parameter_membership(self, **kwargs) -> ParameterMembership:
        """
        Create a new ParameterMembership.

        Returns
        -------
        ParameterMembership
            The new model element
        """
        return self._create_element("ParameterMembership", **kwargs)

    def create_association_structure(self, **kwargs) -> AssociationStructure:
        """
        Create a new AssociationStructure.

        Returns
        -------
        AssociationStructure
            The new model element
        """
        return self._create_element("AssociationStructure", **kwargs)

    def create_reference_subsetting(self, **kwargs) -> ReferenceSubsetting:
        """
        Create a new ReferenceSubsetting.

        Returns
        -------
        ReferenceSubsetting
            The new model element
        """
        return self._create_element("ReferenceSubsetting", **kwargs)

    def create_interface_usage(self, **kwargs) -> InterfaceUsage:
        """
        Create a new InterfaceUsage.

        Returns
        -------
        InterfaceUsage
            The new model element
        """
        return self._create_element("InterfaceUsage", **kwargs)

    def create_binding_connector(self, **kwargs) -> BindingConnector:
        """
        Create a new BindingConnector.

        Returns
        -------
        BindingConnector
            The new model element
        """
        return self._create_element("BindingConnector", **kwargs)

    def create_feature_chaining(self, **kwargs) -> FeatureChaining:
        """
        Create a new FeatureChaining.

        Returns
        -------
        FeatureChaining
            The new model element
        """
        return self._create_element("FeatureChaining", **kwargs)

    def create_literal_integer(self, **kwargs) -> LiteralInteger:
        """
        Create a new LiteralInteger.

        Returns
        -------
        LiteralInteger
            The new model element
        """
        return self._create_element("LiteralInteger", **kwargs)

    def create_invocation_expression(self, **kwargs) -> InvocationExpression:
        """
        Create a new InvocationExpression.

        Returns
        -------
        InvocationExpression
            The new model element
        """
        return self._create_element("InvocationExpression", **kwargs)

    def create_perform_action_usage(self, **kwargs) -> PerformActionUsage:
        """
        Create a new PerformActionUsage.

        Returns
        -------
        PerformActionUsage
            The new model element
        """
        return self._create_element("PerformActionUsage", **kwargs)

    def create_portioning_feature(self, **kwargs) -> PortioningFeature:
        """
        Create a new PortioningFeature.

        Returns
        -------
        PortioningFeature
            The new model element
        """
        return self._create_element("PortioningFeature", **kwargs)

    def create_feature_chain_expression(self, **kwargs) -> FeatureChainExpression:
        """
        Create a new FeatureChainExpression.

        Returns
        -------
        FeatureChainExpression
            The new model element
        """
        return self._create_element("FeatureChainExpression", **kwargs)

    def create_constraint_definition(self, **kwargs) -> ConstraintDefinition:
        """
        Create a new ConstraintDefinition.

        Returns
        -------
        ConstraintDefinition
            The new model element
        """
        return self._create_element("ConstraintDefinition", **kwargs)

    def create_literal_unbounded(self, **kwargs) -> LiteralUnbounded:
        """
        Create a new LiteralUnbounded.

        Returns
        -------
        LiteralUnbounded
            The new model element
        """
        return self._create_element("LiteralUnbounded", **kwargs)

    def create_calculation_definition(self, **kwargs) -> CalculationDefinition:
        """
        Create a new CalculationDefinition.

        Returns
        -------
        CalculationDefinition
            The new model element
        """
        return self._create_element("CalculationDefinition", **kwargs)

    def create_end_feature_membership(self, **kwargs) -> EndFeatureMembership:
        """
        Create a new EndFeatureMembership.

        Returns
        -------
        EndFeatureMembership
            The new model element
        """
        return self._create_element("EndFeatureMembership", **kwargs)

    def create_feature_membership(self, **kwargs) -> FeatureMembership:
        """
        Create a new FeatureMembership.

        Returns
        -------
        FeatureMembership
            The new model element
        """
        return self._create_element("FeatureMembership", **kwargs)

    def create_requirement_definition(self, **kwargs) -> RequirementDefinition:
        """
        Create a new RequirementDefinition.

        Returns
        -------
        RequirementDefinition
            The new model element
        """
        return self._create_element("RequirementDefinition", **kwargs)

    def create_requirement_usage(self, **kwargs) -> RequirementUsage:
        """
        Create a new RequirementUsage.

        Returns
        -------
        RequirementUsage
            The new model element
        """
        return self._create_element("RequirementUsage", **kwargs)

    def create_return_parameter_membership(self, **kwargs) -> ReturnParameterMembership:
        """
        Create a new ReturnParameterMembership.

        Returns
        -------
        ReturnParameterMembership
            The new model element
        """
        return self._create_element("ReturnParameterMembership", **kwargs)

    def create_reference_usage(self, **kwargs) -> ReferenceUsage:
        """
        Create a new ReferenceUsage.

        Returns
        -------
        ReferenceUsage
            The new model element
        """
        return self._create_element("ReferenceUsage", **kwargs)

    def create_port_definition(self, **kwargs) -> PortDefinition:
        """
        Create a new PortDefinition.

        Returns
        -------
        PortDefinition
            The new model element
        """
        return self._create_element("PortDefinition", **kwargs)

    def create_result_expression_membership(self, **kwargs) -> ResultExpressionMembership:
        """
        Create a new ResultExpressionMembership.

        Returns
        -------
        ResultExpressionMembership
            The new model element
        """
        return self._create_element("ResultExpressionMembership", **kwargs)

    def create_satisfy_requirement_usage(self, **kwargs) -> SatisfyRequirementUsage:
        """
        Create a new SatisfyRequirementUsage.

        Returns
        -------
        SatisfyRequirementUsage
            The new model element
        """
        return self._create_element("SatisfyRequirementUsage", **kwargs)

    def create_specialization(self, **kwargs) -> Specialization:
        """
        Create a new Specialization.

        Returns
        -------
        Specialization
            The new model element
        """
        return self._create_element("Specialization", **kwargs)

    def create_literal_rational(self, **kwargs) -> LiteralRational:
        """
        Create a new LiteralRational.

        Returns
        -------
        LiteralRational
            The new model element
        """
        return self._create_element("LiteralRational", **kwargs)

    def create_stakeholder_membership(self, **kwargs) -> StakeholderMembership:
        """
        Create a new StakeholderMembership.

        Returns
        -------
        StakeholderMembership
            The new model element
        """
        return self._create_element("StakeholderMembership", **kwargs)

    def create_state_definition(self, **kwargs) -> StateDefinition:
        """
        Create a new StateDefinition.

        Returns
        -------
        StateDefinition
            The new model element
        """
        return self._create_element("StateDefinition", **kwargs)

    def create_literal_string(self, **kwargs) -> LiteralString:
        """
        Create a new LiteralString.

        Returns
        -------
        LiteralString
            The new model element
        """
        return self._create_element("LiteralString", **kwargs)

    def create_annotating_element(self, **kwargs) -> AnnotatingElement:
        """
        Create a new AnnotatingElement.

        Returns
        -------
        AnnotatingElement
            The new model element
        """
        return self._create_element("AnnotatingElement", **kwargs)

    def create_attribute_usage(self, **kwargs) -> AttributeUsage:
        """
        Create a new AttributeUsage.

        Returns
        -------
        AttributeUsage
            The new model element
        """
        return self._create_element("AttributeUsage", **kwargs)

    def create_boolean_expression(self, **kwargs) -> BooleanExpression:
        """
        Create a new BooleanExpression.

        Returns
        -------
        BooleanExpression
            The new model element
        """
        return self._create_element("BooleanExpression", **kwargs)

    def create_interface_definition(self, **kwargs) -> InterfaceDefinition:
        """
        Create a new InterfaceDefinition.

        Returns
        -------
        InterfaceDefinition
            The new model element
        """
        return self._create_element("InterfaceDefinition", **kwargs)

    def create_send_action_usage(self, **kwargs) -> SendActionUsage:
        """
        Create a new SendActionUsage.

        Returns
        -------
        SendActionUsage
            The new model element
        """
        return self._create_element("SendActionUsage", **kwargs)

    def create_null_expression(self, **kwargs) -> NullExpression:
        """
        Create a new NullExpression.

        Returns
        -------
        NullExpression
            The new model element
        """
        return self._create_element("NullExpression", **kwargs)

    def create_part_definition(self, **kwargs) -> PartDefinition:
        """
        Create a new PartDefinition.

        Returns
        -------
        PartDefinition
            The new model element
        """
        return self._create_element("PartDefinition", **kwargs)

    def create_connection_definition(self, **kwargs) -> ConnectionDefinition:
        """
        Create a new ConnectionDefinition.

        Returns
        -------
        ConnectionDefinition
            The new model element
        """
        return self._create_element("ConnectionDefinition", **kwargs)

    def create_assert_constraint_usage(self, **kwargs) -> AssertConstraintUsage:
        """
        Create a new AssertConstraintUsage.

        Returns
        -------
        AssertConstraintUsage
            The new model element
        """
        return self._create_element("AssertConstraintUsage", **kwargs)

    def create_connection_usage(self, **kwargs) -> ConnectionUsage:
        """
        Create a new ConnectionUsage.

        Returns
        -------
        ConnectionUsage
            The new model element
        """
        return self._create_element("ConnectionUsage", **kwargs)

    def create_feature_reference_expression(self, **kwargs) -> FeatureReferenceExpression:
        """
        Create a new FeatureReferenceExpression.

        Returns
        -------
        FeatureReferenceExpression
            The new model element
        """
        return self._create_element("FeatureReferenceExpression", **kwargs)

    def create_view_definition(self, **kwargs) -> ViewDefinition:
        """
        Create a new ViewDefinition.

        Returns
        -------
        ViewDefinition
            The new model element
        """
        return self._create_element("ViewDefinition", **kwargs)

    def create_library_package(self, **kwargs) -> LibraryPackage:
        """
        Create a new LibraryPackage.

        Returns
        -------
        LibraryPackage
            The new model element
        """
        return self._create_element("LibraryPackage", **kwargs)

    def create_textual_representation(self, **kwargs) -> TextualRepresentation:
        """
        Create a new TextualRepresentation.

        Returns
        -------
        TextualRepresentation
            The new model element
        """
        return self._create_element("TextualRepresentation", **kwargs)

    def create_transition_usage(self, **kwargs) -> TransitionUsage:
        """
        Create a new TransitionUsage.

        Returns
        -------
        TransitionUsage
            The new model element
        """
        return self._create_element("TransitionUsage", **kwargs)

    def create_case_definition(self, **kwargs) -> CaseDefinition:
        """
        Create a new CaseDefinition.

        Returns
        -------
        CaseDefinition
            The new model element
        """
        return self._create_element("CaseDefinition", **kwargs)

    def create_allocation_usage(self, **kwargs) -> AllocationUsage:
        """
        Create a new AllocationUsage.

        Returns
        -------
        AllocationUsage
            The new model element
        """
        return self._create_element("AllocationUsage", **kwargs)

    def create_trigger_invocation_expression(self, **kwargs) -> TriggerInvocationExpression:
        """
        Create a new TriggerInvocationExpression.

        Returns
        -------
        TriggerInvocationExpression
            The new model element
        """
        return self._create_element("TriggerInvocationExpression", **kwargs)

    def create_transition_feature_membership(self, **kwargs) -> TransitionFeatureMembership:
        """
        Create a new TransitionFeatureMembership.

        Returns
        -------
        TransitionFeatureMembership
            The new model element
        """
        return self._create_element("TransitionFeatureMembership", **kwargs)

    def create_type_featuring(self, **kwargs) -> TypeFeaturing:
        """
        Create a new TypeFeaturing.

        Returns
        -------
        TypeFeaturing
            The new model element
        """
        return self._create_element("TypeFeaturing", **kwargs)

    def create_flow_connection_definition(self, **kwargs) -> FlowConnectionDefinition:
        """
        Create a new FlowConnectionDefinition.

        Returns
        -------
        FlowConnectionDefinition
            The new model element
        """
        return self._create_element("FlowConnectionDefinition", **kwargs)

    def create_variant_membership(self, **kwargs) -> VariantMembership:
        """
        Create a new VariantMembership.

        Returns
        -------
        VariantMembership
            The new model element
        """
        return self._create_element("VariantMembership", **kwargs)

    def create_exhibit_state_usage(self, **kwargs) -> ExhibitStateUsage:
        """
        Create a new ExhibitStateUsage.

        Returns
        -------
        ExhibitStateUsage
            The new model element
        """
        return self._create_element("ExhibitStateUsage", **kwargs)

    def create_for_loop_action_usage(self, **kwargs) -> ForLoopActionUsage:
        """
        Create a new ForLoopActionUsage.

        Returns
        -------
        ForLoopActionUsage
            The new model element
        """
        return self._create_element("ForLoopActionUsage", **kwargs)

    def create_metadata_feature(self, **kwargs) -> MetadataFeature:
        """
        Create a new MetadataFeature.

        Returns
        -------
        MetadataFeature
            The new model element
        """
        return self._create_element("MetadataFeature", **kwargs)

    def create_actor_membership(self, **kwargs) -> ActorMembership:
        """
        Create a new ActorMembership.

        Returns
        -------
        ActorMembership
            The new model element
        """
        return self._create_element("ActorMembership", **kwargs)

    def create_action_definition(self, **kwargs) -> ActionDefinition:
        """
        Create a new ActionDefinition.

        Returns
        -------
        ActionDefinition
            The new model element
        """
        return self._create_element("ActionDefinition", **kwargs)

    def create_event_occurrence_usage(self, **kwargs) -> EventOccurrenceUsage:
        """
        Create a new EventOccurrenceUsage.

        Returns
        -------
        EventOccurrenceUsage
            The new model element
        """
        return self._create_element("EventOccurrenceUsage", **kwargs)

    def create_operator_expression(self, **kwargs) -> OperatorExpression:
        """
        Create a new OperatorExpression.

        Returns
        -------
        OperatorExpression
            The new model element
        """
        return self._create_element("OperatorExpression", **kwargs)

    def create_enumeration_usage(self, **kwargs) -> EnumerationUsage:
        """
        Create a new EnumerationUsage.

        Returns
        -------
        EnumerationUsage
            The new model element
        """
        return self._create_element("EnumerationUsage", **kwargs)

    def create_occurrence_usage(self, **kwargs) -> OccurrenceUsage:
        """
        Create a new OccurrenceUsage.

        Returns
        -------
        OccurrenceUsage
            The new model element
        """
        return self._create_element("OccurrenceUsage", **kwargs)

    def create_flow_connection_usage(self, **kwargs) -> FlowConnectionUsage:
        """
        Create a new FlowConnectionUsage.

        Returns
        -------
        FlowConnectionUsage
            The new model element
        """
        return self._create_element("FlowConnectionUsage", **kwargs)

    def create_state_subaction_membership(self, **kwargs) -> StateSubactionMembership:
        """
        Create a new StateSubactionMembership.

        Returns
        -------
        StateSubactionMembership
            The new model element
        """
        return self._create_element("StateSubactionMembership", **kwargs)

    def create_succession_as_usage(self, **kwargs) -> SuccessionAsUsage:
        """
        Create a new SuccessionAsUsage.

        Returns
        -------
        SuccessionAsUsage
            The new model element
        """
        return self._create_element("SuccessionAsUsage", **kwargs)

    def create_subclassification(self, **kwargs) -> Subclassification:
        """
        Create a new Subclassification.

        Returns
        -------
        Subclassification
            The new model element
        """
        return self._create_element("Subclassification", **kwargs)

    def create_if_action_usage(self, **kwargs) -> IfActionUsage:
        """
        Create a new IfActionUsage.

        Returns
        -------
        IfActionUsage
            The new model element
        """
        return self._create_element("IfActionUsage", **kwargs)

    def create_allocation_definition(self, **kwargs) -> AllocationDefinition:
        """
        Create a new AllocationDefinition.

        Returns
        -------
        AllocationDefinition
            The new model element
        """
        return self._create_element("AllocationDefinition", **kwargs)

    def create_metadata_usage(self, **kwargs) -> MetadataUsage:
        """
        Create a new MetadataUsage.

        Returns
        -------
        MetadataUsage
            The new model element
        """
        return self._create_element("MetadataUsage", **kwargs)

    def create_feature_typing(self, **kwargs) -> FeatureTyping:
        """
        Create a new FeatureTyping.

        Returns
        -------
        FeatureTyping
            The new model element
        """
        return self._create_element("FeatureTyping", **kwargs)

    def create_objective_membership(self, **kwargs) -> ObjectiveMembership:
        """
        Create a new ObjectiveMembership.

        Returns
        -------
        ObjectiveMembership
            The new model element
        """
        return self._create_element("ObjectiveMembership", **kwargs)

    def create_subject_membership(self, **kwargs) -> SubjectMembership:
        """
        Create a new SubjectMembership.

        Returns
        -------
        SubjectMembership
            The new model element
        """
        return self._create_element("SubjectMembership", **kwargs)

    def create_calculation_usage(self, **kwargs) -> CalculationUsage:
        """
        Create a new CalculationUsage.

        Returns
        -------
        CalculationUsage
            The new model element
        """
        return self._create_element("CalculationUsage", **kwargs)

    def create_occurrence_definition(self, **kwargs) -> OccurrenceDefinition:
        """
        Create a new OccurrenceDefinition.

        Returns
        -------
        OccurrenceDefinition
            The new model element
        """
        return self._create_element("OccurrenceDefinition", **kwargs)

    def create_metadata_definition(self, **kwargs) -> MetadataDefinition:
        """
        Create a new MetadataDefinition.

        Returns
        -------
        MetadataDefinition
            The new model element
        """
        return self._create_element("MetadataDefinition", **kwargs)

    def create_while_loop_action_usage(self, **kwargs) -> WhileLoopActionUsage:
        """
        Create a new WhileLoopActionUsage.

        Returns
        -------
        WhileLoopActionUsage
            The new model element
        """
        return self._create_element("WhileLoopActionUsage", **kwargs)

    def create_enumeration_definition(self, **kwargs) -> EnumerationDefinition:
        """
        Create a new EnumerationDefinition.

        Returns
        -------
        EnumerationDefinition
            The new model element
        """
        return self._create_element("EnumerationDefinition", **kwargs)

    def create_use_case_definition(self, **kwargs) -> UseCaseDefinition:
        """
        Create a new UseCaseDefinition.

        Returns
        -------
        UseCaseDefinition
            The new model element
        """
        return self._create_element("UseCaseDefinition", **kwargs)

    def create_include_use_case_usage(self, **kwargs) -> IncludeUseCaseUsage:
        """
        Create a new IncludeUseCaseUsage.

        Returns
        -------
        IncludeUseCaseUsage
            The new model element
        """
        return self._create_element("IncludeUseCaseUsage", **kwargs)

    def create_succession_item_flow(self, **kwargs) -> SuccessionItemFlow:
        """
        Create a new SuccessionItemFlow.

        Returns
        -------
        SuccessionItemFlow
            The new model element
        """
        return self._create_element("SuccessionItemFlow", **kwargs)

    def create_multiplicity_range(self, **kwargs) -> MultiplicityRange:
        """
        Create a new MultiplicityRange.

        Returns
        -------
        MultiplicityRange
            The new model element
        """
        return self._create_element("MultiplicityRange", **kwargs)

    def create_loop_action_usage(self, **kwargs) -> LoopActionUsage:
        """
        Create a new LoopActionUsage.

        Returns
        -------
        LoopActionUsage
            The new model element
        """
        return self._create_element("LoopActionUsage", **kwargs)

    def create_requirement_constraint_membership(self, **kwargs) -> RequirementConstraintMembership:
        """
        Create a new RequirementConstraintMembership.

        Returns
        -------
        RequirementConstraintMembership
            The new model element
        """
        return self._create_element("RequirementConstraintMembership", **kwargs)

    def create_succession_flow_connection_usage(self, **kwargs) -> SuccessionFlowConnectionUsage:
        """
        Create a new SuccessionFlowConnectionUsage.

        Returns
        -------
        SuccessionFlowConnectionUsage
            The new model element
        """
        return self._create_element("SuccessionFlowConnectionUsage", **kwargs)

    def _create_element(self, element_type: str, **kwargs) -> Element | SysMLElement:
        """Create a new element in the model and return it.

        Parameters
        ----------
        element_type : str
            Type of the element.
        kwargs : Any
            Other parameters of the new element.

        Returns
        -------
        Union[Element|SysMLElement]
            Created element.
        """
        if self._project.get_root_package()._observer._is_transactional_mode:
            return self._create_local_element_and_stack(element_type, **kwargs)
        else:
            return self._direct_create_element(element_type, **kwargs)

    def _create_local_element_and_stack(self, element_type, **kwargs):
        """
        Create a new local element in the stack.

        Parameters
        ----------
        element_type : str
            Type of the element.

        Returns
        -------
        [SysMLElement|Element]
            Created element.
        """
        from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil

        element_id = str(uuid4())
        is_scripting = not isinstance(self._project, Project)
        if not is_scripting:
            constructor = SysMLUtil.get_sysml_constructor(element_type)
            instance = constructor(element_id)
        else:
            instance = SysMLElement(element_id)
            instance.__class__ = type(element_type, (SysMLElement,), {})

        instance._observer = self._project.get_root_package()._observer
        instance._observer.notify(element_id, "@type", element_type)
        for key, value in kwargs.items():
            attr_name = key
            if is_scripting and not key.startswith("_"):
                attr_name = "_" + key
            if isinstance(value, list):
                if not hasattr(instance, attr_name):
                    from ansys.sam.sysml2.data_structures.observed_list import (
                        ObservedList,
                    )

                    setattr(instance, attr_name, ObservedList(owner=instance, name=attr_name))
                getattr(instance, attr_name).extend(value)
            else:
                setattr(instance, attr_name, value)
        self._project.add_element(instance)
        return instance

    def _direct_create_element(self, element_type, **kwargs):
        """
        Create a new element from the API.

        Parameters
        ----------
        element_type : str
            Type of the element.

        Returns
        -------
        [SysMLElement|Element]
            Created element.
        """
        existing_elements = set(self._project._env.keys())
        commit = Commit(self._project_id)
        change = DataVersion()

        change.add_change("@type", element_type)

        if "owner" in kwargs:
            change.add_change("owner", kwargs["owner"])

        for key, value in kwargs.items():
            if key != "owner":
                change.add_change(key, value)

        commit.add_change(change)

        self._conn.create_commit(self._project_id, commit.to_json())
        self._reload_project()

        element = self._extract_created_element(element_type, existing_elements)
        if "value" in kwargs:
            element.set_value(kwargs.get("value"))
        elif "expression" in kwargs:
            element.parse_and_set_value(kwargs.get("expression"))
        return element

    def _extract_created_element(self, element_type: str, existing_elements: set):
        """Extract the newly created element.

        Parameters
        ----------
        element_type : str
            Type of the element.
        existing_elements : set
            Elements contained in the project environment.

        Returns
        -------
        SysMLElement
            Created element.
        """
        from ansys.sam.sysml2.tools import SysMLTools

        diff_elements = set(self._project._env.keys()).difference(existing_elements)

        new_elements_ids = [
            x for x in diff_elements if SysMLTools.isinstance(self._project._env[x], element_type)
        ]

        if len(new_elements_ids) == 0:
            raise ValueError(f"No element of type '{element_type}' found after reload")
        if len(new_elements_ids) > 1:
            raise ValueError("Too many elements of this type found on reload")

        return self._project._env[new_elements_ids[0]]

    def _reload_project(self):
        """Reload the project."""
        from ansys.sam.sysml2.builder.sysml2_project_builder import SysML2ProjectBuilder

        builder = SysML2ProjectBuilder(self._conn)
        observer = self._project.get_root_package()._observer
        builder.reload_project(observer, self._project)
