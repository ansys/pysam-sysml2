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

"""Tests for the IPython completion hook that makes the element __dir__ authoritative."""

from ansys.sam.sysml2 import _complete_element_attrs
from ansys.sam.sysml2.classes.sysml_element import SysMLElement


class TestCompleteElementAttrs:
    """``_complete_element_attrs`` must return the element's own ``__dir__``."""

    def test_returns_object_dir_not_class_dir_union(self):
        element = SysMLElement("element_id")

        assert _complete_element_attrs(element, ["get_source", "get_value"]) == sorted(
            element.__dir__()
        )

    def test_fallback_returns_prev_completions_on_error(self):
        class Broken:
            def __dir__(self):
                raise RuntimeError("boom")

        prev = ["a", "b"]

        assert _complete_element_attrs(Broken(), prev) is prev
