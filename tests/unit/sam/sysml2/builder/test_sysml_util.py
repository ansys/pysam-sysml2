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

"""Tests for SysMLUtil name resolution."""

from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil
from ansys.sam.sysml2.classes.sysml_element import SysMLElement


class TestCheckInheritedName:
    """Scripting fallback names must be dot-safe Python identifiers."""

    def test_returns_real_name_when_present(self):
        element = SysMLElement("53f1d978-9696-4c68-bb93-4d38571fa4a5")
        object.__setattr__(element, "_name", "MyPart")

        assert SysMLUtil.check_inherited_name(element) == "MyPart"

    def test_fallback_replaces_colons_and_dashes_with_underscores(self):
        part_def_cls = type("PartDefinition", (SysMLElement,), {})
        element = part_def_cls("53f1d978-9696-4c68-bb93-4d38571fa4a5")

        resolved = SysMLUtil.check_inherited_name(element)

        assert resolved == "PartDefinition_53f1d978_9696_4c68_bb93_4d38571fa4a5"
        assert "::" not in resolved
        assert "-" not in resolved
        assert resolved.isidentifier()
