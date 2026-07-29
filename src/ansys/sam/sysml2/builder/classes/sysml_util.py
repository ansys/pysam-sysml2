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
"""SysML utility class."""

import importlib

from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.meta_model.e_object import EObject
from ansys.sam.sysml2.meta_model.element import Element


class SysMLUtil:
    """Provides utility methods for SysML element name resolution and class lookup."""

    _dynamic_class_cache: dict[str, type] = {}

    @staticmethod
    def check_inherited_name(element: SysMLElement) -> str:
        """Resolve the name with a dot-safe ``ClassName_<id>`` fallback when empty."""
        name = getattr(element, "_name", None)
        if name:
            return name
        class_name = element.__class__.__name__.split(".")[-1]
        return f"{class_name}_{element._id}".replace("-", "_")

    @staticmethod
    def check_sysml_inherited_name(element: Element, dot_safe: bool = False) -> str:
        """Resolve the element name, with a ``ClassName::id`` (or dot-safe) fallback."""
        name = getattr(element, "name", None)
        if name:
            return name
        declared_name = getattr(element, "declared_name", None)
        if declared_name:
            return declared_name
        class_name = element.__class__.__name__.split(".")[-1]
        if dot_safe:
            return f"{class_name}_{element.id}".replace("-", "_")
        return f"{class_name}::{element.id}"

    @staticmethod
    def get_sysml_constructor(element_type: str) -> type[EObject]:
        """Get the class constructor from type."""
        from ansys.sam.sysml2.tools.name_utils import NameUtils

        try:
            name = NameUtils.to_snake_case(element_type)
            module_name = f"ansys.sam.sysml2.meta_model.{name}"
            module = importlib.import_module(module_name)

            class_ = getattr(module, element_type)
            return class_
        except ModuleNotFoundError:
            raise ImportError(
                f"Unable to find module '{module_name}' in ansys.sam.sysml2.meta_model package."
            )
        except AttributeError:
            raise ImportError(f"'{element_type}' class not found in module '{module_name}'.")

    @staticmethod
    def get_dynamic_constructor(element_type: str) -> type[EObject]:
        """Get a class composing the dynamic mixin in front of the generated class."""
        from ansys.sam.sysml2.classes.dynamic_e_object import DynamicEObject

        cached = SysMLUtil._dynamic_class_cache.get(element_type)
        if cached is None:
            base = SysMLUtil.get_sysml_constructor(element_type)
            cached = type(element_type, (DynamicEObject, base), {})
            SysMLUtil._dynamic_class_cache[element_type] = cached
        return cached
