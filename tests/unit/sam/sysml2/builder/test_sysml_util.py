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

_ID = "53f1d978-9696-4c68-bb93-4d38571fa4a5"


class TestCheckInheritedName:
    """No-name fallback differs: sysml uses ``::``, scripting uses a dot-safe identifier."""

    def _make_part_definition(self):
        return SysMLUtil.get_sysml_constructor("PartDefinition")(_ID)

    def test_returns_declared_name_when_present(self):
        element = self._make_part_definition()
        element.declared_name = "MyPart"

        assert SysMLUtil.check_sysml_inherited_name(element) == "MyPart"

    def test_sysml_fallback_uses_double_colon(self):
        element = self._make_part_definition()

        assert SysMLUtil.check_sysml_inherited_name(element) == f"PartDefinition::{_ID}"

    def test_scripting_fallback_is_dot_safe_identifier(self):
        element = self._make_part_definition()

        resolved = SysMLUtil.check_sysml_inherited_name(element, dot_safe=True)

        assert resolved == "PartDefinition_53f1d978_9696_4c68_bb93_4d38571fa4a5"
        assert "::" not in resolved
        assert "-" not in resolved
        assert resolved.isidentifier()
