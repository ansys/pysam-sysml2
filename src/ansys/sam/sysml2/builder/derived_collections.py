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

"""Derive KerML/SysML collections from owned relationships when the API omits them."""

from __future__ import annotations

from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.classes.scripting_project import ScriptingProject
from ansys.sam.sysml2.classes.unresolved_field import UnresolvedField
from ansys.sam.sysml2.data_structures.observed_list import ObservedList
from ansys.sam.sysml2.meta_model.allocation_definition import AllocationDefinition
from ansys.sam.sysml2.meta_model.analysis_case_definition import AnalysisCaseDefinition
from ansys.sam.sysml2.meta_model.annotation import Annotation
from ansys.sam.sysml2.meta_model.association_structure import AssociationStructure
from ansys.sam.sysml2.meta_model.behavior import Behavior
from ansys.sam.sysml2.meta_model.case_definition import CaseDefinition
from ansys.sam.sysml2.meta_model.class_ import Class
from ansys.sam.sysml2.meta_model.classifier import Classifier
from ansys.sam.sysml2.meta_model.concern_definition import ConcernDefinition
from ansys.sam.sysml2.meta_model.data_type import DataType
from ansys.sam.sysml2.meta_model.documentation import Documentation
from ansys.sam.sysml2.meta_model.enumeration_definition import EnumerationDefinition
from ansys.sam.sysml2.meta_model.feature import Feature
from ansys.sam.sysml2.meta_model.feature_chaining import FeatureChaining
from ansys.sam.sysml2.meta_model.feature_membership import FeatureMembership
from ansys.sam.sysml2.meta_model.feature_typing import FeatureTyping
from ansys.sam.sysml2.meta_model.function import Function
from ansys.sam.sysml2.meta_model.import_ import Import
from ansys.sam.sysml2.meta_model.interaction import Interaction
from ansys.sam.sysml2.meta_model.interface_definition import InterfaceDefinition
from ansys.sam.sysml2.meta_model.membership import Membership
from ansys.sam.sysml2.meta_model.metaclass import Metaclass
from ansys.sam.sysml2.meta_model.namespace import Namespace
from ansys.sam.sysml2.meta_model.owning_membership import OwningMembership
from ansys.sam.sysml2.meta_model.part_definition import PartDefinition
from ansys.sam.sysml2.meta_model.port_definition import PortDefinition
from ansys.sam.sysml2.meta_model.predicate import Predicate
from ansys.sam.sysml2.meta_model.redefinition import Redefinition
from ansys.sam.sysml2.meta_model.rendering_definition import RenderingDefinition
from ansys.sam.sysml2.meta_model.requirement_definition import RequirementDefinition
from ansys.sam.sysml2.meta_model.specialization import Specialization
from ansys.sam.sysml2.meta_model.structure import Structure
from ansys.sam.sysml2.meta_model.subsetting import Subsetting
from ansys.sam.sysml2.meta_model.type_ import Type
from ansys.sam.sysml2.meta_model.usage import Usage
from ansys.sam.sysml2.meta_model.use_case_definition import UseCaseDefinition
from ansys.sam.sysml2.meta_model.verification_case_definition import VerificationCaseDefinition
from ansys.sam.sysml2.meta_model.view_definition import ViewDefinition
from ansys.sam.sysml2.meta_model.viewpoint_definition import ViewpointDefinition
from ansys.sam.sysml2.tools.name_utils import NameUtils

# JSON / KerML property names (camelCase), same vocabulary as the API and mappers.
_OWNED_RELATIONSHIP = "ownedRelationship"
_OWNED_RELATED_ELEMENT = "ownedRelatedElement"
_OWNED_MEMBER_ELEMENT = "ownedMemberElement"
_OWNED_MEMBER_FEATURE = "ownedMemberFeature"
_MEMBER_ELEMENT = "memberElement"
_OWNED_ELEMENT = "ownedElement"
_OWNED_MEMBERSHIP = "ownedMembership"
_OWNED_MEMBER = "ownedMember"
_OWNED_IMPORT = "ownedImport"
_OWNED_ANNOTATION = "ownedAnnotation"
_DOCUMENTATION = "documentation"
_TEXT = "text"
_OWNED_FEATURE_MEMBERSHIP = "ownedFeatureMembership"
_OWNED_FEATURE = "ownedFeature"
_FEATURE_MEMBERSHIP = "featureMembership"
_FEATURE = "feature"
_INHERITED_MEMBERSHIP = "inheritedMembership"
_INHERITED_FEATURE = "inheritedFeature"
_OWNED_SPECIALIZATION = "ownedSpecialization"
_OWNED_TYPING = "ownedTyping"
_OWNED_SUBSETTING = "ownedSubsetting"
_OWNED_REDEFINITION = "ownedRedefinition"
_CHAINING_FEATURE = "chainingFeature"
_TYPE = "type"
_DEFINITION = "definition"
_ENUMERATION_DEFINITION = "enumerationDefinition"
_GENERAL = "general"
_SUBSETTED_FEATURE = "subsettedFeature"
_REDEFINED_FEATURE = "redefinedFeature"

# (json_key, metamodel base type)
_LIST_DEFINITION_FILTERS = (
    ("attributeDefinition", DataType),
    ("partDefinition", PartDefinition),
    ("itemDefinition", Structure),
    ("portDefinition", PortDefinition),
    ("occurrenceDefinition", Class),
    ("actionDefinition", Behavior),
    ("allocationDefinition", AllocationDefinition),
    ("connectionDefinition", AssociationStructure),
    ("stateDefinition", Behavior),
    ("flowDefinition", Interaction),
    ("interfaceDefinition", InterfaceDefinition),
)
_SCALAR_DEFINITION_FILTERS = (
    ("enumerationDefinition", EnumerationDefinition),
    ("requirementDefinition", RequirementDefinition),
    ("constraintDefinition", Predicate),
    ("calculationDefinition", Function),
    ("caseDefinition", CaseDefinition),
    ("analysisCaseDefinition", AnalysisCaseDefinition),
    ("verificationCaseDefinition", VerificationCaseDefinition),
    ("useCaseDefinition", UseCaseDefinition),
    ("concernDefinition", ConcernDefinition),
    ("viewpointDefinition", ViewpointDefinition),
    ("viewDefinition", ViewDefinition),
    ("renderingDefinition", RenderingDefinition),
    ("metadataDefinition", Metaclass),
)


def _metamodel_type_names(base: type) -> frozenset[str]:
    """Collect metamodel class names that are ``base`` or a subclass of it."""
    import ansys.sam.sysml2.meta_model as meta_model

    names = []
    for attribute_name in dir(meta_model):
        candidate = getattr(meta_model, attribute_name)
        if isinstance(candidate, type) and issubclass(candidate, base):
            names.append(candidate.__name__)
    return frozenset(names)


_MEMBERSHIP_TYPE_NAMES = _metamodel_type_names(Membership)
_OWNING_MEMBERSHIP_TYPE_NAMES = _metamodel_type_names(OwningMembership)
_FEATURE_MEMBERSHIP_TYPE_NAMES = _metamodel_type_names(FeatureMembership)
_FEATURE_TYPE_NAMES = _metamodel_type_names(Feature)
_NAMESPACE_TYPE_NAMES = _metamodel_type_names(Namespace)
_TYPE_TYPE_NAMES = _metamodel_type_names(Type)
_IMPORT_TYPE_NAMES = _metamodel_type_names(Import)
_ANNOTATION_TYPE_NAMES = _metamodel_type_names(Annotation)
_DOCUMENTATION_TYPE_NAMES = _metamodel_type_names(Documentation)
_SPECIALIZATION_TYPE_NAMES = _metamodel_type_names(Specialization)
_FEATURE_TYPING_TYPE_NAMES = _metamodel_type_names(FeatureTyping)
_SUBSETTING_TYPE_NAMES = _metamodel_type_names(Subsetting)
_REDEFINITION_TYPE_NAMES = _metamodel_type_names(Redefinition)
_FEATURE_CHAINING_TYPE_NAMES = _metamodel_type_names(FeatureChaining)
_USAGE_TYPE_NAMES = _metamodel_type_names(Usage)
_CLASSIFIER_TYPE_NAMES = _metamodel_type_names(Classifier)

_LIST_DEFINITION_TYPE_NAMES = tuple(
    (json_key, _metamodel_type_names(base)) for json_key, base in _LIST_DEFINITION_FILTERS
)
_SCALAR_DEFINITION_TYPE_NAMES = tuple(
    (json_key, _metamodel_type_names(base)) for json_key, base in _SCALAR_DEFINITION_FILTERS
)


def fill_derived_collections(project: Project | ScriptingProject) -> None:
    """
    Populate main derived collections when the API omitted them.

    Parameters
    ----------
    project : Project | ScriptingProject
        Built project whose elements already have resolved relationships.
    """
    if getattr(project, "_includes_derived", True):
        return

    is_scripting = isinstance(project, ScriptingProject)
    for element in project._env.values():
        _derive_collections_for_element(element, is_scripting)


def _attribute_name(json_key: str, is_scripting: bool) -> str:
    """
    Resolve an API JSON key to the Python attribute used by mappers.

    Scripting stores ``_ownedElement``; SysML stores ``_owned_element``.
    """
    if is_scripting:
        return "_" + json_key
    return NameUtils.to_key(json_key)


def _derive_collections_for_element(element, is_scripting: bool) -> None:
    """Fill owned/inherited/typing collections for one element from its relationships."""
    owned_relationships = _as_list(
        getattr(element, _attribute_name(_OWNED_RELATIONSHIP, is_scripting), None)
    )

    owned_memberships = _filter_by_type(owned_relationships, _MEMBERSHIP_TYPE_NAMES)
    owning_memberships = _filter_by_type(owned_relationships, _OWNING_MEMBERSHIP_TYPE_NAMES)
    feature_memberships = _filter_by_type(owned_relationships, _FEATURE_MEMBERSHIP_TYPE_NAMES)
    owned_annotations = _filter_by_type(owned_relationships, _ANNOTATION_TYPE_NAMES)
    owned_imports = _filter_by_type(owned_relationships, _IMPORT_TYPE_NAMES)

    # KerML Element::ownedElement = ownedRelationship.ownedRelatedElement.
    owned_elements = _collect_owned_related_elements(owned_relationships, is_scripting)
    owned_members = _collect_targets(
        owning_memberships,
        _attribute_name(_OWNED_MEMBER_ELEMENT, is_scripting),
    )
    # Fall back to ownedMemberElement when ownedRelatedElement is empty (unit fixtures).
    owned_elements = _dedupe_preserve_order(owned_elements + owned_members)

    _set_collection(element, _attribute_name(_OWNED_ELEMENT, is_scripting), owned_elements)
    _set_collection(element, _attribute_name(_OWNED_ANNOTATION, is_scripting), owned_annotations)
    documentation = _filter_by_type(owned_elements, _DOCUMENTATION_TYPE_NAMES)
    _set_collection(
        element,
        _attribute_name(_DOCUMENTATION, is_scripting),
        documentation,
    )
    _derive_requirement_text(element, documentation, is_scripting)

    if _has_type(element, _NAMESPACE_TYPE_NAMES):
        _set_collection(
            element,
            _attribute_name(_OWNED_MEMBERSHIP, is_scripting),
            owned_memberships,
        )
        # ownedMember is OwningMembership targets only (may be narrower than ownedElement).
        _set_collection(element, _attribute_name(_OWNED_MEMBER, is_scripting), owned_members)
        _set_collection(element, _attribute_name(_OWNED_IMPORT, is_scripting), owned_imports)

    if not _has_type(element, _TYPE_TYPE_NAMES):
        return

    owned_specializations = _filter_by_type(owned_relationships, _SPECIALIZATION_TYPE_NAMES)
    _set_collection(
        element,
        _attribute_name(_OWNED_SPECIALIZATION, is_scripting),
        owned_specializations,
    )

    owned_features = _collect_features_from_memberships(feature_memberships, is_scripting)
    inherited_feature_memberships = _filter_by_type(
        _as_list(getattr(element, _attribute_name(_INHERITED_MEMBERSHIP, is_scripting), None)),
        _FEATURE_MEMBERSHIP_TYPE_NAMES,
    )
    inherited_features = _collect_features_from_memberships(
        inherited_feature_memberships, is_scripting
    )

    _set_collection(
        element,
        _attribute_name(_OWNED_FEATURE_MEMBERSHIP, is_scripting),
        feature_memberships,
    )
    _set_collection(element, _attribute_name(_OWNED_FEATURE, is_scripting), owned_features)
    _set_collection(
        element,
        _attribute_name(_INHERITED_FEATURE, is_scripting),
        inherited_features,
    )
    _set_collection(
        element,
        _attribute_name(_FEATURE_MEMBERSHIP, is_scripting),
        feature_memberships + inherited_feature_memberships,
    )
    _set_collection(
        element,
        _attribute_name(_FEATURE, is_scripting),
        owned_features + inherited_features,
    )

    if _has_type(element, _FEATURE_TYPE_NAMES):
        _derive_feature_typing_collections(element, owned_relationships, is_scripting)


def _derive_feature_typing_collections(
    feature, owned_relationships: list, is_scripting: bool
) -> None:
    """Fill typing-related derived collections for a Feature (KerML deriveFeatureType)."""
    owned_typings = _filter_by_type(owned_relationships, _FEATURE_TYPING_TYPE_NAMES)
    owned_subsettings = _filter_by_type(owned_relationships, _SUBSETTING_TYPE_NAMES)
    owned_redefinitions = _filter_by_type(owned_relationships, _REDEFINITION_TYPE_NAMES)
    chaining_features = _collect_targets(
        _filter_by_type(owned_relationships, _FEATURE_CHAINING_TYPE_NAMES),
        _attribute_name(_CHAINING_FEATURE, is_scripting),
    )

    _set_collection(feature, _attribute_name(_OWNED_TYPING, is_scripting), owned_typings)
    _set_collection(
        feature,
        _attribute_name(_OWNED_SUBSETTING, is_scripting),
        owned_subsettings,
    )
    _set_collection(
        feature,
        _attribute_name(_OWNED_REDEFINITION, is_scripting),
        owned_redefinitions,
    )
    _set_collection(
        feature,
        _attribute_name(_CHAINING_FEATURE, is_scripting),
        chaining_features,
    )

    feature_types = _collect_feature_types(feature, is_scripting, visited=set())
    if not feature_types:
        enumeration_definition = _resolve_enumeration_definition(feature, is_scripting)
        if enumeration_definition is not None:
            feature_types = [enumeration_definition]
    _set_collection(feature, _attribute_name(_TYPE, is_scripting), feature_types)

    if not _has_type(feature, _USAGE_TYPE_NAMES):
        return

    definitions = _filter_by_type(feature_types, _CLASSIFIER_TYPE_NAMES)
    if not definitions:
        definitions = feature_types
    _set_collection(feature, _attribute_name(_DEFINITION, is_scripting), definitions)
    _fill_definition_views(feature, definitions, is_scripting)


def _collect_feature_types(feature, is_scripting: bool, visited: set[int]) -> list:
    """
    Collect Feature types per KerML deriveFeatureType (local graph in ``_env``).

    Unions types from owned FeatureTypings, recursively from subsetted/redefined
    features, and from the last chainingFeature. Deduplicates by identity.
    """
    feature_key = id(feature)
    if feature_key in visited:
        return []
    visited.add(feature_key)

    owned_relationships = _as_list(
        getattr(feature, _attribute_name(_OWNED_RELATIONSHIP, is_scripting), None)
    )
    types = []

    for typing in _filter_by_type(owned_relationships, _FEATURE_TYPING_TYPE_NAMES):
        typing_type = _resolve_typing_type(typing, is_scripting)
        if typing_type is not None:
            types.append(typing_type)

    for subsetting in _filter_by_type(owned_relationships, _SUBSETTING_TYPE_NAMES):
        subsetted = _resolve_subsetted_feature(subsetting, is_scripting)
        if subsetted is not None:
            types.extend(_collect_feature_types(subsetted, is_scripting, visited))

    chaining_features = _collect_targets(
        _filter_by_type(owned_relationships, _FEATURE_CHAINING_TYPE_NAMES),
        _attribute_name(_CHAINING_FEATURE, is_scripting),
    )
    if chaining_features:
        types.extend(_collect_feature_types(chaining_features[-1], is_scripting, visited))

    return _dedupe_preserve_order(types)


def _resolve_typing_type(typing, is_scripting: bool):
    """Return the Type applied by a FeatureTyping, if resolved."""
    type_attribute = _attribute_name(_TYPE, is_scripting)
    general_attribute = _attribute_name(_GENERAL, is_scripting)
    typing_type = getattr(typing, type_attribute, None)
    if typing_type is None and not is_scripting:
        typing_type = getattr(typing, "type_", None)
    if typing_type is None:
        typing_type = getattr(typing, general_attribute, None)
        if typing_type is None and not is_scripting:
            typing_type = getattr(typing, "general", None)
    if typing_type is None or isinstance(typing_type, UnresolvedField):
        return None
    return typing_type


def _resolve_subsetted_feature(subsetting, is_scripting: bool):
    """Return the subsetted/redefined feature of a Subsetting, if resolved."""
    subsetted_attribute = _attribute_name(_SUBSETTED_FEATURE, is_scripting)
    redefined_attribute = _attribute_name(_REDEFINED_FEATURE, is_scripting)
    general_attribute = _attribute_name(_GENERAL, is_scripting)
    subsetted = getattr(subsetting, subsetted_attribute, None)
    if subsetted is None:
        subsetted = getattr(subsetting, redefined_attribute, None)
    if subsetted is None:
        subsetted = getattr(subsetting, general_attribute, None)
        if subsetted is None and not is_scripting:
            subsetted = getattr(subsetting, "general", None)
    if subsetted is None or isinstance(subsetted, UnresolvedField):
        return None
    if not _has_type(subsetted, _FEATURE_TYPE_NAMES):
        return None
    return subsetted


def _fill_definition_views(usage, definitions: list, is_scripting: bool) -> None:
    """Fill Usage *Definition views filtered from ``definitions``."""
    for json_key, type_names in _LIST_DEFINITION_TYPE_NAMES:
        if not _usage_has_definition_attribute(usage, json_key, is_scripting):
            continue
        matches = _filter_by_type(definitions, type_names)
        _set_collection(usage, _attribute_name(json_key, is_scripting), matches)

    for json_key, type_names in _SCALAR_DEFINITION_TYPE_NAMES:
        if not _usage_has_definition_attribute(usage, json_key, is_scripting):
            continue
        matches = _filter_by_type(definitions, type_names)
        attribute_name = _attribute_name(json_key, is_scripting)
        setattr(usage, attribute_name, matches[0] if matches else None)


def _usage_has_definition_attribute(usage, json_key: str, is_scripting: bool) -> bool:
    """Return whether ``usage`` exposes the given definition attribute."""
    attribute_name = _attribute_name(json_key, is_scripting)
    if hasattr(usage, attribute_name):
        return True
    if is_scripting:
        return False
    snake = NameUtils.to_snake_case(json_key)
    return hasattr(usage, snake)


def _collect_owned_related_elements(owned_relationships: list, is_scripting: bool) -> list:
    """Collect resolved ``ownedRelatedElement`` targets from all owned relationships."""
    owned_related_element = _attribute_name(_OWNED_RELATED_ELEMENT, is_scripting)
    elements = []
    for relationship in owned_relationships:
        for target in _as_list(getattr(relationship, owned_related_element, None)):
            if target is None or isinstance(target, UnresolvedField):
                continue
            elements.append(target)
    return elements


def _resolve_enumeration_definition(feature, is_scripting: bool):
    """Return a resolved ``enumerationDefinition`` already present on the feature, if any."""
    attribute_name = _attribute_name(_ENUMERATION_DEFINITION, is_scripting)
    enumeration_definition = getattr(feature, attribute_name, None)
    if enumeration_definition is None and not is_scripting:
        enumeration_definition = getattr(feature, "enumeration_definition", None)
    if enumeration_definition is None or isinstance(enumeration_definition, UnresolvedField):
        return None
    return enumeration_definition


def _collect_features_from_memberships(feature_memberships: list, is_scripting: bool) -> list:
    """Return resolved features pointed by feature memberships."""
    owned_member_feature = _attribute_name(_OWNED_MEMBER_FEATURE, is_scripting)
    owned_member_element = _attribute_name(_OWNED_MEMBER_ELEMENT, is_scripting)
    member_element = _attribute_name(_MEMBER_ELEMENT, is_scripting)
    features = []
    for membership in feature_memberships:
        feature = getattr(membership, owned_member_feature, None)
        if feature is None:
            feature = getattr(membership, owned_member_element, None)
        if feature is None:
            feature = getattr(membership, member_element, None)
        if feature is not None and _is_resolved_feature(feature):
            features.append(feature)
    return features


def _is_resolved_feature(element) -> bool:
    """Return whether ``element`` is a resolved Feature (not an unresolved ref)."""
    if isinstance(element, UnresolvedField):
        return False
    return _has_type(element, _FEATURE_TYPE_NAMES)


def _collect_targets(
    relationships: list,
    target_attribute: str,
    allowed_types: frozenset[str] | None = None,
) -> list:
    """Collect non-null resolved targets from relationships, optionally filtered by type."""
    targets = []
    for relationship in relationships:
        target = getattr(relationship, target_attribute, None)
        if target is None or isinstance(target, UnresolvedField):
            continue
        if allowed_types is not None and not _has_type(target, allowed_types):
            continue
        targets.append(target)
    return targets


def _dedupe_preserve_order(values: list) -> list:
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


def _filter_by_type(elements: list, type_names: frozenset[str]) -> list:
    """Keep elements whose concrete class name is in ``type_names``."""
    return [element for element in elements if _has_type(element, type_names)]


def _has_type(element, type_names: frozenset[str]) -> bool:
    """Return whether ``element``'s class name is in ``type_names``."""
    class_name = element.__class__.__name__.split(".")[-1]
    return class_name in type_names


def _derive_requirement_text(element, documentation: list, is_scripting: bool) -> None:
    """Fill ``text`` from documentation bodies when the element exposes ``_text``."""
    text_attribute = _attribute_name(_TEXT, is_scripting)
    if not hasattr(element, text_attribute):
        return
    bodies = []
    for document in documentation:
        body = getattr(document, "_body", None)
        if body:
            bodies.append(body)
    _set_collection(element, text_attribute, bodies)


def _as_list(value) -> list:
    """Normalize a missing or empty collection attribute to a list."""
    if not value:
        return []
    return list(value)


def _set_collection(owner, attribute_name: str, values: list) -> None:
    """Replace an ObservedList in place, or assign a new one."""
    current = getattr(owner, attribute_name, None)
    if isinstance(current, ObservedList):
        current.clear()
        current.extend(values)
        return
    setattr(owner, attribute_name, ObservedList(owner, attribute_name, *values))
