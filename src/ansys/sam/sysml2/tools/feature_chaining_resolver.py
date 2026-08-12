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

    def __init__(self, element):
        """Keep the seed element and a metamodel reader."""
        self._element = element
        self._model = ModelReader()

    def resolve_connector_end(self, end):
        """Find the element that one end of the seed connection points to."""
        ends = self._model.get(self._element, end, [])
        context = self._model.get(self._element, "owner")
        return self._resolve_end(ends, context)

    def resolve_end(self, ends, context):
        """Find the element that the first end of ``ends`` points to, seen from ``context``."""
        if not ends or context is None:
            return None
        return self._resolve_end(ends, context)

    def resolve_representative(self, element, context):
        """Find the element that ``element`` points to, seen from ``context``."""
        return self._resolve(element, context)

    def _resolve_end(self, ends, context):
        """Resolve the first end; when it points straight at something, return it unchanged."""
        if not ends or context is None:
            return None
        end = ends[0]
        resolved = self._resolve(end, context)
        # A direct end (no chain) already points at the right element.
        if resolved is None and not self._model.is_chaining(end):
            return end
        return resolved

    def _resolve(self, element, context):
        """Follow a chain of features, or look up a single element."""
        if self._model.is_chaining(element):
            return self._walk_chaining(element, context)
        return self._resolve_in_context(element, context, climb=True)

    def _walk_chaining(self, feature, context):
        """Follow the chain one feature at a time, each step searched inside the previous result."""
        current = context
        for index, chaining in enumerate(self._model.get(feature, "owned_feature_chaining", [])):
            if current is None:
                return None
            step = self._model.get(chaining, "chaining_feature")
            # Only the first step may search up through parent parts; later steps stay local.
            current = self._resolve_in_context(step, current, climb=(index == 0))
        return current

    def _resolve_in_context(self, element, context, climb):
        """Look for ``element`` inside ``context``; go up to the parent when allowed."""
        if context is None or element is None:
            return None
        if context is element:
            return context
        inherited_element_class = self._model.get_inherited_element_class()
        if isinstance(context, inherited_element_class) and self._model.unwrap(context) is element:
            return context

        match = self._find(self._model.get(context, "owned_element", []), element)
        if match is None and self._model.is_a(context, Namespace):
            members = [
                self._model.get(m, "member_element")
                for m in self._model.get(context, "imported_membership", [])
            ]
            match = self._find(members, element)
        if match is None and self._model.is_a(context, Type) and self._model.is_a(element, Feature):
            inherited = self._model.get(self._model.unwrap(context), "inherited_feature", [])
            match = self._find(inherited, element)

        if match is not None:
            return self._scope(match, context)
        if climb:
            return self._resolve_in_context(element, self._model.get(context, "owner"), climb)
        return None

    def _scope(self, found, context):
        """Return the found element as-is when ``context`` owns it, otherwise wrap it."""
        inherited_element_class = self._model.get_inherited_element_class()
        if isinstance(context, inherited_element_class):
            return inherited_element_class(context, found)
        owning_membership = self._model.get(found, "owning_membership")
        owned_relationship = self._model.get(context, "owned_relationship", [])
        if owning_membership is not None and owning_membership in owned_relationship:
            return found
        return inherited_element_class(context, found)

    def _find(self, candidates, reference):
        """Return the first candidate matching ``reference``, or a feature that redefines it."""
        for candidate in candidates:
            if candidate is not None and self._matches(candidate, reference):
                return candidate
        return None

    def _matches(self, candidate, reference):
        """Return True when ``candidate`` is the reference, or a feature that redefines it."""
        if candidate is reference:
            return True
        if self._model.is_a(candidate, Feature):
            return reference in self._model.redefined_features(candidate)
        return False
