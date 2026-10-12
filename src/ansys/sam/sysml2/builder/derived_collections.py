# Copyright (C) 2024 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

"""Derive KerML/SysML collections from owned relationships when the API omits them."""

from __future__ import annotations

from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.classes.unresolved_field import UnresolvedField
from ansys.sam.sysml2.data_structures.observed_list import ObservedList
import ansys.sam.sysml2.meta_model as meta_model

# (owned view, nested view, metamodel class). One feature can match several views.
_FEATURE_VIEWS = (
    ("owned_action", "nested_action", meta_model.ActionUsage),
    ("owned_allocation", "nested_allocation", meta_model.AllocationUsage),
    ("owned_analysis_case", "nested_analysis_case", meta_model.AnalysisCaseUsage),
    ("owned_attribute", "nested_attribute", meta_model.AttributeUsage),
    ("owned_calculation", "nested_calculation", meta_model.CalculationUsage),
    ("owned_case", "nested_case", meta_model.CaseUsage),
    ("owned_concern", "nested_concern", meta_model.ConcernUsage),
    ("owned_connection", "nested_connection", meta_model.ConnectionUsage),
    ("owned_constraint", "nested_constraint", meta_model.ConstraintUsage),
    ("owned_enumeration", "nested_enumeration", meta_model.EnumerationUsage),
    ("owned_flow", "nested_flow", meta_model.FlowUsage),
    ("owned_interface", "nested_interface", meta_model.InterfaceUsage),
    ("owned_item", "nested_item", meta_model.ItemUsage),
    ("owned_metadata", "nested_metadata", meta_model.MetadataUsage),
    ("owned_occurrence", "nested_occurrence", meta_model.OccurrenceUsage),
    ("owned_part", "nested_part", meta_model.PartUsage),
    ("owned_port", "nested_port", meta_model.PortUsage),
    ("owned_reference", "nested_reference", meta_model.ReferenceUsage),
    ("owned_rendering", "nested_rendering", meta_model.RenderingUsage),
    ("owned_requirement", "nested_requirement", meta_model.RequirementUsage),
    ("owned_state", "nested_state", meta_model.StateUsage),
    ("owned_transition", "nested_transition", meta_model.TransitionUsage),
    ("owned_usage", "nested_usage", meta_model.Usage),
    ("owned_use_case", "nested_use_case", meta_model.UseCaseUsage),
    ("owned_verification_case", "nested_verification_case", meta_model.VerificationCaseUsage),
    ("owned_view", "nested_view", meta_model.ViewUsage),
    ("owned_viewpoint", "nested_viewpoint", meta_model.ViewpointUsage),
)
_LIST_DEFINITION_VIEWS = (
    ("attribute_definition", meta_model.DataType),
    ("part_definition", meta_model.PartDefinition),
    ("item_definition", meta_model.Structure),
    ("port_definition", meta_model.PortDefinition),
    ("occurrence_definition", meta_model.Class),
    ("action_definition", meta_model.Behavior),
    ("allocation_definition", meta_model.AllocationDefinition),
    ("connection_definition", meta_model.AssociationStructure),
    ("state_definition", meta_model.Behavior),
    ("flow_definition", meta_model.Interaction),
    ("interface_definition", meta_model.InterfaceDefinition),
)
_SCALAR_DEFINITION_VIEWS = (
    ("enumeration_definition", meta_model.EnumerationDefinition),
    ("requirement_definition", meta_model.RequirementDefinition),
    ("constraint_definition", meta_model.Predicate),
    ("calculation_definition", meta_model.Function),
    ("case_definition", meta_model.CaseDefinition),
    ("analysis_case_definition", meta_model.AnalysisCaseDefinition),
    ("verification_case_definition", meta_model.VerificationCaseDefinition),
    ("use_case_definition", meta_model.UseCaseDefinition),
    ("concern_definition", meta_model.ConcernDefinition),
    ("viewpoint_definition", meta_model.ViewpointDefinition),
    ("view_definition", meta_model.ViewDefinition),
    ("rendering_definition", meta_model.RenderingDefinition),
    ("metadata_definition", meta_model.Metaclass),
)


def fill_derived_collections(project: Project) -> None:
    """
    Populate main derived collections when the API omitted them.

    Parameters
    ----------
    project : Project
        Built project whose elements already have resolved relationships.
    """
    if getattr(project, "_includes_derived", True):
        return

    elements = list(project._env.values())
    relationships_by_owner, features_by_relationship = _owning_indexes(elements)
    for element in elements:
        _fill_element(element, relationships_by_owner, features_by_relationship)


def _owning_indexes(elements: list):
    """Index Factory links that point at an owner instead of sitting in an owned collection."""
    relationships_by_owner = {}
    features_by_relationship = {}
    for element in elements:
        owner = getattr(element, "owning_related_element", None)
        if owner is not None and not isinstance(owner, UnresolvedField):
            relationships_by_owner.setdefault(id(owner), []).append(element)
        relationship = getattr(element, "owning_relationship", None)
        if (
            relationship is not None
            and not isinstance(relationship, UnresolvedField)
            and isinstance(element, meta_model.Feature)
        ):
            features_by_relationship.setdefault(id(relationship), []).append(element)
    return relationships_by_owner, features_by_relationship


def _with_owning_relationships(element, relationships_by_owner: dict) -> list:
    """Return owned relationships plus those that name *element* as ``owning_related_element``."""
    owned = _as_list(element.owned_relationship)
    extra = relationships_by_owner.get(id(element), [])
    if not extra:
        return owned
    return _dedupe(owned + extra)


def _fill_element(element, relationships_by_owner: dict, features_by_relationship: dict) -> None:
    """Fill owned, inherited and typing collections for one element."""
    _fill_related_elements(element)
    relationships = _with_owning_relationships(element, relationships_by_owner)
    owned_members = _targets(
        _of_type(relationships, meta_model.OwningMembership),
        "owned_member_element",
    )
    _fill_owned_elements(element, relationships, owned_members)
    if isinstance(element, meta_model.Namespace):
        _fill_namespace(element, relationships, owned_members)
    if not isinstance(element, meta_model.Type):
        return

    owned_features, inherited_features, owned_specializations = _fill_features(
        element, relationships
    )
    input_features, output_features = _fill_parameters(element, relationships)
    _fill_directed_features(element, input_features, output_features)
    _fill_membership_views(element, relationships, features_by_relationship)
    _fill_feature_views(element, owned_features, inherited_features, owned_specializations)
    if isinstance(element, meta_model.Feature):
        _fill_feature_types(element)


def _fill_related_elements(element) -> None:
    """Fill ``related_element`` from ``source`` then ``target``."""
    if not hasattr(element, "related_element"):
        return
    sources = _resolved(_as_list(getattr(element, "source", None)))
    targets = _resolved(_as_list(getattr(element, "target", None)))
    _fill(element, "related_element", _dedupe(sources + targets))


def _fill_owned_elements(element, relationships: list, owned_members: list) -> None:
    """Fill elements, annotations and documentation owned by *element*."""
    # KerML Element::ownedElement = ownedRelationship.ownedRelatedElement.
    # Fall back to ownedMemberElement when ownedRelatedElement is empty (unit fixtures).
    owned_elements = _dedupe(_owned_related_elements(relationships) + owned_members)
    _fill(element, "owned_element", owned_elements)
    _fill(element, "owned_annotation", _of_type(relationships, meta_model.Annotation))
    documentation = _of_type(owned_elements, meta_model.Documentation)
    _fill(element, "documentation", documentation)
    _fill_requirement_text(element, documentation)


def _fill_namespace(element, relationships: list, owned_members: list) -> None:
    """Fill namespace membership, member and import collections."""
    owned_memberships = _of_type(relationships, meta_model.Membership)
    _fill(element, "owned_membership", owned_memberships)
    # ownedMember is OwningMembership targets only (may be narrower than ownedElement).
    _fill(element, "owned_member", owned_members)
    _fill(element, "owned_import", _of_type(relationships, meta_model.Import))
    inherited_memberships = _of_type(
        _as_list(getattr(element, "inherited_membership", None)),
        meta_model.Membership,
    )
    memberships = _dedupe(owned_memberships + inherited_memberships)
    _fill(element, "membership", memberships)
    _fill(element, "member", _targets(memberships, "member_element"))


def _fill_features(element, relationships: list):
    """Fill feature, end and specialization collections. Return the lists views reuse."""
    owned_specializations = _of_type(relationships, meta_model.Specialization)
    _fill(element, "owned_specialization", owned_specializations)

    feature_memberships = _of_type(relationships, meta_model.FeatureMembership)
    owned_features = _features_of(feature_memberships)
    inherited_feature_memberships = _of_type(
        _as_list(getattr(element, "inherited_membership", None)),
        meta_model.FeatureMembership,
    )
    inherited_features = _features_of(inherited_feature_memberships)
    _fill(element, "owned_feature_membership", feature_memberships)
    _fill(element, "owned_feature", owned_features)
    _fill(element, "inherited_feature", inherited_features)
    _fill(element, "feature_membership", feature_memberships + inherited_feature_memberships)
    _fill(element, "feature", owned_features + inherited_features)

    end_feature_memberships = _of_type(relationships, meta_model.EndFeatureMembership)
    owned_end_features = _features_of(end_feature_memberships)
    _fill(element, "owned_end_feature", owned_end_features)
    _fill(element, "end_feature", owned_end_features)
    return owned_features, inherited_features, owned_specializations


def _fill_parameters(element, relationships: list):
    """Fill input, output and parameter collections. Return input and output features."""
    parameter_memberships = _of_type(relationships, meta_model.ParameterMembership)
    return_parameter_memberships = _of_type(relationships, meta_model.ReturnParameterMembership)
    input_memberships = [
        membership
        for membership in parameter_memberships
        if not isinstance(membership, meta_model.ReturnParameterMembership)
    ]
    input_features = _features_of(input_memberships)
    output_features = _features_of(return_parameter_memberships)
    _fill(element, "input", input_features)
    _fill(element, "output", output_features)
    if isinstance(element, meta_model.Step) or isinstance(element, meta_model.Behavior):
        _fill(element, "parameter", _features_of(parameter_memberships))
    return input_features, output_features


def _fill_directed_features(element, input_features: list, output_features: list) -> None:
    """Fill directed features from input then output."""
    directed_features = _dedupe(input_features + output_features)
    _fill_if_present(element, "directed_feature", directed_features)
    _fill_if_present(element, "directed_usage", _of_type(directed_features, meta_model.Usage))


def _fill_membership_views(element, relationships: list, features_by_relationship: dict) -> None:
    """Fill case and requirement collections from specialized memberships."""
    _fill_if_present(
        element,
        "actor_parameter",
        _features_via(
            relationships,
            meta_model.ActorMembership,
            "owned_actor_parameter",
            features_by_relationship,
        ),
    )
    _fill_if_present(
        element,
        "stakeholder_parameter",
        _features_via(
            relationships,
            meta_model.StakeholderMembership,
            "owned_stakeholder_parameter",
            features_by_relationship,
        ),
    )
    _assign_if_absent(
        element,
        "subject_parameter",
        _first_feature(
            relationships,
            meta_model.SubjectMembership,
            "owned_subject_parameter",
            features_by_relationship,
        ),
    )
    _assign_if_absent(
        element,
        "objective_requirement",
        _first_feature(
            relationships,
            meta_model.ObjectiveMembership,
            "owned_objective_requirement",
            features_by_relationship,
        ),
    )
    assumptions = []
    requirements = []
    for membership in _of_type(relationships, meta_model.RequirementConstraintMembership):
        if isinstance(membership, meta_model.FramedConcernMembership):
            continue
        feature = _feature_of_membership(
            membership, "owned_member_feature", features_by_relationship
        )
        if feature is None:
            continue
        if _kind_name(membership) == "assumption":
            assumptions.append(feature)
        elif _kind_name(membership) == "requirement":
            requirements.append(feature)
    _fill_if_present(element, "assumed_constraint", assumptions)
    _fill_if_present(element, "required_constraint", requirements)
    _fill_if_present(
        element,
        "framed_concern",
        _features_via(
            relationships,
            meta_model.FramedConcernMembership,
            "owned_concern",
            features_by_relationship,
        ),
    )


def _fill_feature_views(
    element,
    owned_features: list,
    inherited_features: list,
    owned_specializations: list,
) -> None:
    """Fill type-filtered owned and nested feature collections."""
    for owned_name, nested_name, element_type in _FEATURE_VIEWS:
        matches = _of_type(owned_features, element_type)
        _fill_if_present(element, owned_name, matches)
        _fill_if_present(element, nested_name, matches)
    _fill_if_present(
        element,
        "usage",
        _dedupe(
            _of_type(owned_features, meta_model.Usage)
            + _of_type(inherited_features, meta_model.Usage)
        ),
    )
    _fill_if_present(
        element,
        "owned_subclassification",
        _of_type(owned_specializations, meta_model.Subclassification),
    )
    _fill_if_present(element, "step", _of_type(owned_features, meta_model.Step))
    _fill_if_present(element, "expression", _of_type(owned_features, meta_model.Expression))


def _fill_feature_types(feature) -> None:
    """Fill typing collections for a Feature (KerML deriveFeatureType)."""
    relationships = _as_list(feature.owned_relationship)
    feature_chainings = _of_type(relationships, meta_model.FeatureChaining)
    _fill(feature, "owned_typing", _of_type(relationships, meta_model.FeatureTyping))
    _fill(feature, "owned_subsetting", _of_type(relationships, meta_model.Subsetting))
    _fill(feature, "owned_redefinition", _of_type(relationships, meta_model.Redefinition))
    _fill(feature, "owned_feature_chaining", feature_chainings)
    _fill(feature, "chaining_feature", _targets(feature_chainings, "chaining_feature"))

    feature_types = _collect_feature_types(feature, visited=set())
    if not feature_types:
        enumeration_definition = _enumeration_definition(feature)
        if enumeration_definition is not None:
            feature_types = [enumeration_definition]
    _fill(feature, "type_", feature_types)
    if not isinstance(feature, meta_model.Usage):
        return

    definitions = _of_type(feature_types, meta_model.Classifier)
    if not definitions:
        definitions = feature_types
    _fill(feature, "definition", definitions)
    _fill_definition_views(feature, definitions)


def _collect_feature_types(feature, visited: set[int]) -> list:
    """
    Collect Feature types per KerML deriveFeatureType (local graph in ``_env``).

    Unions types from owned FeatureTypings, recursively from subsetted/redefined
    features, and from the last chainingFeature. Deduplicates by identity.
    """
    feature_key = id(feature)
    if feature_key in visited:
        return []
    visited.add(feature_key)

    relationships = _as_list(getattr(feature, "owned_relationship", None))
    types = []
    for typing in _of_type(relationships, meta_model.FeatureTyping):
        typing_type = _typing_type(typing)
        if typing_type is not None:
            types.append(typing_type)
    for subsetting in _of_type(relationships, meta_model.Subsetting):
        subsetted = _subsetted_feature(subsetting)
        if subsetted is not None:
            types.extend(_collect_feature_types(subsetted, visited))
    chaining_features = _targets(
        _of_type(relationships, meta_model.FeatureChaining),
        "chaining_feature",
    )
    if chaining_features:
        types.extend(_collect_feature_types(chaining_features[-1], visited))
    return _dedupe(types)


def _typing_type(typing):
    """Return the Type applied by a FeatureTyping, if resolved."""
    found = getattr(typing, "type_", None)
    if found is None:
        found = getattr(typing, "general", None)
    if found is None or isinstance(found, UnresolvedField):
        return None
    return found


def _subsetted_feature(subsetting):
    """Return the subsetted or redefined feature of a Subsetting, if resolved."""
    subsetted = getattr(subsetting, "subsetted_feature", None)
    if subsetted is None:
        subsetted = getattr(subsetting, "redefined_feature", None)
    if subsetted is None:
        subsetted = getattr(subsetting, "general", None)
    if subsetted is None or isinstance(subsetted, UnresolvedField):
        return None
    if not isinstance(subsetted, meta_model.Feature):
        return None
    return subsetted


def _fill_definition_views(usage, definitions: list) -> None:
    """Fill Usage *Definition views filtered from ``definitions``."""
    for name, element_type in _LIST_DEFINITION_VIEWS:
        if not _has_definition(usage, name):
            continue
        _fill(usage, name, _of_type(definitions, element_type))
    for name, element_type in _SCALAR_DEFINITION_VIEWS:
        if not _has_definition(usage, name):
            continue
        matches = _of_type(definitions, element_type)
        setattr(usage, f"_{name}", matches[0] if matches else None)


def _has_definition(usage, name: str) -> bool:
    """Return whether ``usage`` exposes the given definition attribute."""
    return hasattr(usage, f"_{name}") or hasattr(usage, name)


def _enumeration_definition(feature):
    """Return a resolved ``enumeration_definition`` already present on the feature, if any."""
    enumeration_definition = getattr(feature, "enumeration_definition", None)
    if enumeration_definition is None or isinstance(enumeration_definition, UnresolvedField):
        return None
    return enumeration_definition


def _fill_requirement_text(element, documentation: list) -> None:
    """Fill ``text`` from documentation bodies when the element exposes it."""
    if not hasattr(element, "text"):
        return
    bodies = []
    for document in documentation:
        body = getattr(document, "body", None)
        if body:
            bodies.append(body)
    _fill(element, "text", bodies)


def _features_via(
    relationships: list, element_type: type, name: str, features_by_relationship: dict
) -> list:
    """Return features owned by memberships of *element_type*, via *name* when set."""
    features = []
    for membership in _of_type(relationships, element_type):
        feature = _feature_of_membership(membership, name, features_by_relationship)
        if feature is not None:
            features.append(feature)
    return features


def _first_feature(
    relationships: list, element_type: type, name: str, features_by_relationship: dict
):
    """Return the first feature owned by memberships of *element_type*."""
    features = _features_via(relationships, element_type, name, features_by_relationship)
    if not features:
        return None
    return features[0]


def _feature_of_membership(membership, name: str, features_by_relationship: dict):
    """Return the feature named by *name*, or the membership's owned feature."""
    feature = getattr(membership, name, None)
    if feature is None or isinstance(feature, UnresolvedField):
        owned = _features_of([membership])
        if owned:
            return owned[0]
        owned_by_relationship = features_by_relationship.get(id(membership), [])
        return owned_by_relationship[0] if owned_by_relationship else None
    if isinstance(feature, list):
        resolved = _resolved(feature)
        return resolved[0] if resolved else None
    if not isinstance(feature, meta_model.Feature):
        return None
    return feature


def _kind_name(membership) -> str:
    """Return the requirement constraint kind as its API string."""
    kind = getattr(membership, "kind", None)
    value = getattr(kind, "value", kind)
    if value is None:
        return ""
    return str(value)


def _features_of(memberships: list) -> list:
    """Return resolved features pointed by feature memberships."""
    features = []
    for membership in memberships:
        feature = getattr(membership, "owned_member_feature", None)
        if feature is None:
            feature = getattr(membership, "owned_member_element", None)
        if feature is None:
            feature = getattr(membership, "member_element", None)
        if (
            feature is not None
            and not isinstance(feature, UnresolvedField)
            and isinstance(feature, meta_model.Feature)
        ):
            features.append(feature)
    return features


def _owned_related_elements(relationships: list) -> list:
    """Collect resolved ``owned_related_element`` targets from owned relationships."""
    elements = []
    for relationship in relationships:
        for target in _as_list(getattr(relationship, "owned_related_element", None)):
            if target is None or isinstance(target, UnresolvedField):
                continue
            elements.append(target)
    return elements


def _targets(relationships: list, name: str) -> list:
    """Collect non-null resolved targets from relationships."""
    targets = []
    for relationship in relationships:
        target = getattr(relationship, name, None)
        if target is None or isinstance(target, UnresolvedField):
            continue
        targets.append(target)
    return targets


def _of_type(elements: list, element_type: type) -> list:
    """Keep elements that are instances of *element_type*."""
    return [element for element in elements if isinstance(element, element_type)]


def _resolved(values: list) -> list:
    """Drop missing and unresolved references."""
    return [
        value for value in values if value is not None and not isinstance(value, UnresolvedField)
    ]


def _dedupe(values: list) -> list:
    """Deduplicate values by identity while preserving order."""
    unique = []
    seen = set()
    for value in values:
        key = id(value)
        if key in seen:
            continue
        seen.add(key)
        unique.append(value)
    return unique


def _as_list(value) -> list:
    """Normalize a missing or empty collection attribute to a list."""
    if not value:
        return []
    return list(value)


def _fill(element, name: str, values: list) -> None:
    """Replace an ObservedList in place, or assign a new one on the backing field."""
    current = getattr(element, name, None)
    if isinstance(current, ObservedList):
        current.clear()
        current.extend(values)
        return
    backing = f"_{name}"
    setattr(element, backing, ObservedList(element, backing, *values))


def _fill_if_present(element, name: str, values: list) -> None:
    """Fill *name* when the element declares that collection."""
    if hasattr(element, name):
        _fill(element, name, values)


def _assign_if_absent(element, name: str, value) -> None:
    """Set a scalar derived reference when the API left it empty."""
    if value is None or isinstance(value, UnresolvedField):
        return
    backing = f"_{name}"
    if not hasattr(element, backing) and not hasattr(element, name):
        return
    current = getattr(element, name, None)
    if current is not None and not isinstance(current, UnresolvedField):
        return
    setattr(element, backing, value)
