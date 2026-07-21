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

from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.meta_model.feature import Feature
from ansys.sam.sysml2.meta_model.namespace import Namespace
from ansys.sam.sysml2.meta_model.type_ import Type
from ansys.sam.sysml2.tools.name_utils import NameUtils


class ModelReader:
    """Read a SysML model the same way, whether it comes from the scripting API or the metamodel."""

    def __init__(self, element):
        """Detect the model kind and keep the class used to wrap inherited elements."""
        from ansys.sam.sysml2.classes.sysml_element import SysMLElement

        self._scripting = isinstance(element, SysMLElement)
        if self._scripting:
            from ansys.sam.sysml2.classes.inherited_element import InheritedElement

            self.Proxy = InheritedElement
        else:
            from ansys.sam.sysml2.classes.sysml_inherited_element import SysMLInheritedElement

            self.Proxy = SysMLInheritedElement

    def get(self, element, key, default=None):
        """Read a field of ``element`` by its plain name."""
        name = f"_{NameUtils.snake_to_camel(key)}" if self._scripting else key
        value = getattr(element, name, default)
        if value is None and default is not None:
            return default
        return value

    def unwrap(self, element):
        """Return the real element, without the wrapper that ties it to a parent part."""
        if isinstance(element, self.Proxy):
            return getattr(element, "_element", element)
        return element

    def is_a(self, element, base):
        """Tell whether ``element`` is a ``base`` (a Feature, a Type, a Namespace...)."""
        kind = self._metamodel_class(element)
        return kind is not None and issubclass(kind, base)

    def is_chaining(self, element):
        """Tell whether ``element`` reaches its target through a chain of features."""
        return self.is_a(element, Feature) and bool(self.get(element, "owned_feature_chaining", []))

    def redefined_features(self, feature):
        """Return every feature that ``feature`` redefines, directly or indirectly."""
        result = []
        seen = set()
        stack = list(self.get(feature, "owned_redefinition", []))
        while stack:
            redefinition = stack.pop()
            redefined = self.get(redefinition, "redefined_feature")
            if redefined is None or id(redefined) in seen:
                continue
            seen.add(id(redefined))
            result.append(redefined)
            stack.extend(self.get(redefined, "owned_redefinition", []))
        return result

    def _metamodel_class(self, element):
        """Return the metamodel class of ``element``, for both model kinds."""
        element = self.unwrap(element)
        if isinstance(element, Element):
            return type(element)
        # Scripting objects are plain data: map their class name to a metamodel class.
        from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil

        try:
            return SysMLUtil.get_sysml_constructor(type(element).__name__)
        except ImportError:
            return None


def resolve_connector_end(connection, end):
    """Find the element that one end (``"source"`` or ``"target"``) of ``connection`` points to."""
    model = ModelReader(connection)
    ends = model.get(connection, end, [])
    context = model.get(connection, "owner")
    return _resolve_end(model, ends, context)


def resolve_end(ends, context):
    """Find the element that the first end of ``ends`` points to, seen from ``context``."""
    if not ends or context is None:
        return None
    return _resolve_end(ModelReader(ends[0]), ends, context)


def resolve_representative(element, context):
    """Find the element that ``element`` points to, seen from ``context``."""
    return _resolve(ModelReader(element), element, context)


def _resolve_end(model, ends, context):
    """Resolve the first end; when it points straight at something, return it unchanged."""
    if not ends or context is None:
        return None
    end = ends[0]
    resolved = _resolve(model, end, context)
    # A direct end (no chain) already points at the right element.
    if resolved is None and not model.is_chaining(end):
        return end
    return resolved


def _resolve(model, element, context):
    """Follow a chain of features, or look up a single element."""
    if model.is_chaining(element):
        return _walk_chaining(model, element, context)
    return _resolve_in_context(model, element, context, climb=True)


def _walk_chaining(model, feature, context):
    """Follow the chain one feature at a time, each step searched inside the previous result."""
    current = context
    for index, chaining in enumerate(model.get(feature, "owned_feature_chaining", [])):
        if current is None:
            return None
        step = model.get(chaining, "chaining_feature")
        # Only the first step may search up through parent parts; later steps stay local.
        current = _resolve_in_context(model, step, current, climb=(index == 0))
    return current


def _resolve_in_context(model, element, context, climb):
    """Look for ``element`` inside ``context``; go up to the parent when allowed."""
    if context is None or element is None:
        return None
    if context is element:
        return context
    if isinstance(context, model.Proxy) and model.unwrap(context) is element:
        return context

    match = _find(model, model.get(context, "owned_element", []), element)
    if match is None and model.is_a(context, Namespace):
        members = [
            model.get(m, "member_element") for m in model.get(context, "imported_membership", [])
        ]
        match = _find(model, members, element)
    if match is None and model.is_a(context, Type) and model.is_a(element, Feature):
        inherited = model.get(model.unwrap(context), "inherited_feature", [])
        match = _find(model, inherited, element)

    if match is not None:
        return _scope(model, match, context)
    if climb:
        return _resolve_in_context(model, element, model.get(context, "owner"), climb)
    return None


def _scope(model, found, context):
    """Return the found element as-is when ``context`` owns it, otherwise wrap it."""
    if isinstance(context, model.Proxy):
        return model.Proxy(context, found)
    owning_membership = model.get(found, "owning_membership")
    owned_relationship = model.get(context, "owned_relationship", [])
    if owning_membership is not None and owning_membership in owned_relationship:
        return found
    return model.Proxy(context, found)


def _find(model, candidates, reference):
    """Return the first candidate that is ``reference`` itself, or a feature that redefines it."""
    for candidate in candidates:
        if candidate is not None and _matches(model, candidate, reference):
            return candidate
    return None


def _matches(model, candidate, reference):
    """Return True when ``candidate`` is the reference, or a feature that redefines it."""
    if candidate is reference:
        return True
    if model.is_a(candidate, Feature):
        return reference in model.redefined_features(candidate)
    return False
