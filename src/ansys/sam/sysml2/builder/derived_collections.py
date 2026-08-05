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
from ansys.sam.sysml2.data_structures.observed_list import ObservedList
from ansys.sam.sysml2.meta_model.feature import Feature
from ansys.sam.sysml2.meta_model.feature_membership import FeatureMembership
from ansys.sam.sysml2.meta_model.membership import Membership
from ansys.sam.sysml2.meta_model.namespace import Namespace
from ansys.sam.sysml2.meta_model.owning_membership import OwningMembership
from ansys.sam.sysml2.meta_model.type_ import Type
from ansys.sam.sysml2.tools.name_utils import NameUtils

# JSON / KerML property names (camelCase), same vocabulary as the API and mappers.
_OWNED_RELATIONSHIP = "ownedRelationship"
_OWNED_MEMBER_ELEMENT = "ownedMemberElement"
_OWNED_MEMBER_FEATURE = "ownedMemberFeature"
_MEMBER_ELEMENT = "memberElement"
_OWNED_ELEMENT = "ownedElement"
_OWNED_MEMBERSHIP = "ownedMembership"
_OWNED_FEATURE_MEMBERSHIP = "ownedFeatureMembership"
_OWNED_FEATURE = "ownedFeature"
_INHERITED_MEMBERSHIP = "inheritedMembership"
_INHERITED_FEATURE = "inheritedFeature"


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
    """Fill owned/inherited collections for one element from its relationships."""
    owned_relationships = _as_list(
        getattr(element, _attribute_name(_OWNED_RELATIONSHIP, is_scripting), None)
    )

    owned_memberships = _filter_by_type(owned_relationships, _MEMBERSHIP_TYPE_NAMES)
    owning_memberships = _filter_by_type(
        owned_relationships, _OWNING_MEMBERSHIP_TYPE_NAMES
    )
    feature_memberships = _filter_by_type(
        owned_relationships, _FEATURE_MEMBERSHIP_TYPE_NAMES
    )

    _set_collection(
        element,
        _attribute_name(_OWNED_ELEMENT, is_scripting),
        _collect_targets(
            owning_memberships,
            _attribute_name(_OWNED_MEMBER_ELEMENT, is_scripting),
        ),
    )

    if _has_type(element, _NAMESPACE_TYPE_NAMES):
        _set_collection(
            element,
            _attribute_name(_OWNED_MEMBERSHIP, is_scripting),
            owned_memberships,
        )

    if not _has_type(element, _TYPE_TYPE_NAMES):
        return

    _set_collection(
        element,
        _attribute_name(_OWNED_FEATURE_MEMBERSHIP, is_scripting),
        feature_memberships,
    )
    _set_collection(
        element,
        _attribute_name(_OWNED_FEATURE, is_scripting),
        _collect_owned_features(feature_memberships, is_scripting),
    )
    _set_collection(
        element,
        _attribute_name(_INHERITED_FEATURE, is_scripting),
        _collect_inherited_features(element, is_scripting),
    )


def _collect_owned_features(feature_memberships: list, is_scripting: bool) -> list:
    """Return features pointed by feature memberships."""
    owned_member_feature = _attribute_name(_OWNED_MEMBER_FEATURE, is_scripting)
    owned_member_element = _attribute_name(_OWNED_MEMBER_ELEMENT, is_scripting)
    features = []
    for membership in feature_memberships:
        feature = getattr(membership, owned_member_feature, None)
        if feature is None:
            feature = getattr(membership, owned_member_element, None)
        if feature is not None and _has_type(feature, _FEATURE_TYPE_NAMES):
            features.append(feature)
    return features


def _collect_inherited_features(element, is_scripting: bool) -> list:
    """Return features pointed by inherited memberships, when present."""
    inherited_memberships = _as_list(
        getattr(element, _attribute_name(_INHERITED_MEMBERSHIP, is_scripting), None)
    )
    return _collect_targets(
        inherited_memberships,
        _attribute_name(_MEMBER_ELEMENT, is_scripting),
        allowed_types=_FEATURE_TYPE_NAMES,
    )


def _collect_targets(
    relationships: list,
    target_attribute: str,
    allowed_types: frozenset[str] | None = None,
) -> list:
    """Collect non-null targets from relationships, optionally filtered by type."""
    targets = []
    for relationship in relationships:
        target = getattr(relationship, target_attribute, None)
        if target is None:
            continue
        if allowed_types is not None and not _has_type(target, allowed_types):
            continue
        targets.append(target)
    return targets


def _filter_by_type(elements: list, type_names: frozenset[str]) -> list:
    """Keep elements whose concrete class name is in ``type_names``."""
    return [element for element in elements if _has_type(element, type_names)]


def _has_type(element, type_names: frozenset[str]) -> bool:
    """Return whether ``element``'s class name is in ``type_names``."""
    class_name = element.__class__.__name__.split(".")[-1]
    return class_name in type_names


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
