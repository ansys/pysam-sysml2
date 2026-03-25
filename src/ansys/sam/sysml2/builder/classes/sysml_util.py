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
    """Provides the SysML utility class."""

    @staticmethod
    def check_inherited_name(element: SysMLElement) -> str:
        """Check and return the name of the element."""
        if isinstance(element, str):
            return "::" + element
        if hasattr(element, "_name"):
            return getattr(element, "_name")
        elif hasattr(element, "_redefinedFeature"):
            redefined_feature = getattr(element, "_redefinedFeature", [])
            if isinstance(redefined_feature, list) and len(redefined_feature) > 0:
                redefined_feature = getattr(element, "_redefinedFeature")[0]
            return SysMLUtil.check_inherited_name(redefined_feature)
        else:
            return element.__class__.__name__.split(".")[-1] + "::" + element._id

    @staticmethod
    def check_sysml_inherited_name(element: Element) -> str:
        """Check and return the name of the element."""
        if isinstance(element, str):
            return "::" + element
        if hasattr(element, "name"):
            return getattr(element, "name")
        elif hasattr(element, "redefined_feature"):
            redefined_feature = getattr(element, "redefined_feature", [])
            if isinstance(redefined_feature, list) and len(redefined_feature) > 0:
                redefined_feature = getattr(element, "redefined_feature")[0]
            return SysMLUtil.check_sysml_inherited_name(redefined_feature)
        else:
            return element.__class__.__name__.split(".")[-1] + "::" + element.id

    @staticmethod
    def get_sysml_constructor(element_type: str) -> EObject:
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
                f"Unable to found '{module_name}'  in ansys.sam.sysml2.meta_model. package."
            )
        except AttributeError:
            raise ImportError(f"'{element_type}' class not found in module '{module_name}'.")
