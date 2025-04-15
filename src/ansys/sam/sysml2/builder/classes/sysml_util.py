# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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
"""SysML Util class."""
from ansys.sam.sysml2.classes.sysml_element import SysMLElement


class SysMLUtil:
    """SysML Util class."""

    @staticmethod
    def check_inherited_name(element: SysMLElement) -> str:
        """
        Check and return the name.

        Parameters
        ----------
        element : SysMLElement
            Element

        Returns
        -------
        str
            The Name
        """
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
