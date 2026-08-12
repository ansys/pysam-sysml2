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

"""Find the element that a connection end really points to.

A connection end (``source`` or ``target``) can point straight at an element, or
reach it through a chain of intermediate features. The answer can differ from one
parent part to another, because features get redefined and inherited along the way.
"""

from ansys.sam.sysml2.meta_model.feature import Feature
from ansys.sam.sysml2.meta_model.namespace import Namespace
from ansys.sam.sysml2.meta_model.type_ import Type
from ansys.sam.sysml2.tools.model_reader import ModelReader


class FeatureChainingResolver:
    """Resolve connection ends and feature chains in a SysML model."""

    @staticmethod
    def resolve_connector_end(connection, end):
        """Find the element that one end of ``connection`` points to."""
        model = ModelReader(connection)
        ends = model.get(connection, end, [])
        context = model.get(connection, "owner")
        return FeatureChainingResolver._resolve_end(model, ends, context)

    @staticmethod
    def resolve_end(ends, context):
        """Find the element that the first end of ``ends`` points to, seen from ``context``."""
        if not ends or context is None:
            return None
        return FeatureChainingResolver._resolve_end(ModelReader(ends[0]), ends, context)

    @staticmethod
    def resolve_representative(element, context):
        """Find the element that ``element`` points to, seen from ``context``."""
        return FeatureChainingResolver._resolve(ModelReader(element), element, context)

    @staticmethod
    def _resolve_end(model, ends, context):
        """Resolve the first end; when it points straight at something, return it unchanged."""
        if not ends or context is None:
            return None
        end = ends[0]
        resolved = FeatureChainingResolver._resolve(model, end, context)
        # A direct end (no chain) already points at the right element.
        if resolved is None and not model.is_chaining(end):
            return end
        return resolved

    @staticmethod
    def _resolve(model, element, context):
        """Follow a chain of features, or look up a single element."""
        if model.is_chaining(element):
            return FeatureChainingResolver._walk_chaining(model, element, context)
        return FeatureChainingResolver._resolve_in_context(model, element, context, climb=True)

    @staticmethod
    def _walk_chaining(model, feature, context):
        """Follow the chain one feature at a time, each step searched inside the previous result."""
        current = context
        for index, chaining in enumerate(model.get(feature, "owned_feature_chaining", [])):
            if current is None:
                return None
            step = model.get(chaining, "chaining_feature")
            # Only the first step may search up through parent parts; later steps stay local.
            current = FeatureChainingResolver._resolve_in_context(
                model, step, current, climb=(index == 0)
            )
        return current

    @staticmethod
    def _resolve_in_context(model, element, context, climb):
        """Look for ``element`` inside ``context``; go up to the parent when allowed."""
        if context is None or element is None:
            return None
        if context is element:
            return context
        inherited_element_class = model.get_inherited_element_class()
        if isinstance(context, inherited_element_class) and model.unwrap(context) is element:
            return context

        match = FeatureChainingResolver._find(
            model, model.get(context, "owned_element", []), element
        )
        if match is None and model.is_a(context, Namespace):
            members = [
                model.get(m, "member_element")
                for m in model.get(context, "imported_membership", [])
            ]
            match = FeatureChainingResolver._find(model, members, element)
        if match is None and model.is_a(context, Type) and model.is_a(element, Feature):
            inherited = model.get(model.unwrap(context), "inherited_feature", [])
            match = FeatureChainingResolver._find(model, inherited, element)

        if match is not None:
            return FeatureChainingResolver._scope(model, match, context)
        if climb:
            return FeatureChainingResolver._resolve_in_context(
                model, element, model.get(context, "owner"), climb
            )
        return None

    @staticmethod
    def _scope(model, found, context):
        """Return the found element as-is when ``context`` owns it, otherwise wrap it."""
        inherited_element_class = model.get_inherited_element_class()
        if isinstance(context, inherited_element_class):
            return inherited_element_class(context, found)
        owning_membership = model.get(found, "owning_membership")
        owned_relationship = model.get(context, "owned_relationship", [])
        if owning_membership is not None and owning_membership in owned_relationship:
            return found
        return inherited_element_class(context, found)

    @staticmethod
    def _find(model, candidates, reference):
        """Return the first candidate matching ``reference``, or a feature that redefines it."""
        for candidate in candidates:
            if candidate is not None and FeatureChainingResolver._matches(
                model, candidate, reference
            ):
                return candidate
        return None

    @staticmethod
    def _matches(model, candidate, reference):
        """Return True when ``candidate`` is the reference, or a feature that redefines it."""
        if candidate is reference:
            return True
        if model.is_a(candidate, Feature):
            return reference in model.redefined_features(candidate)
        return False
