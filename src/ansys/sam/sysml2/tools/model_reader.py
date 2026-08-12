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

"""Read a SysML model the same way for scripting and metamodel elements."""

from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.meta_model.feature import Feature
from ansys.sam.sysml2.tools.name_utils import NameUtils


class ModelReader:
    """Read a SysML model the same way, whether it comes from the scripting API or the metamodel."""

    def __init__(self, element):
        """Detect the model kind and keep the class used to wrap inherited elements."""
        from ansys.sam.sysml2.classes.sysml_element import SysMLElement

        self._scripting = isinstance(element, SysMLElement)
        if self._scripting:
            from ansys.sam.sysml2.classes.inherited_element import InheritedElement

            self._inherited_element_class = InheritedElement
        else:
            from ansys.sam.sysml2.classes.sysml_inherited_element import SysMLInheritedElement

            self._inherited_element_class = SysMLInheritedElement

    def get_inherited_element_class(self):
        """Return the class used to wrap an inherited element under a parent part."""
        return self._inherited_element_class

    def get(self, element, key, default=None):
        """Read a field of ``element`` by its plain name."""
        name = f"_{NameUtils.snake_to_camel(key)}" if self._scripting else key
        value = getattr(element, name, default)
        if value is None and default is not None:
            return default
        return value

    def unwrap(self, element):
        """Return the real element, without the wrapper that ties it to a parent part."""
        if isinstance(element, self._inherited_element_class):
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
