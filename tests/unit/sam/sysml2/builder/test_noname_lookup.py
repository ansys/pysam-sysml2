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

"""No-name elements must be reachable via the resolved declared name (ElementType::ID)."""

import pytest

from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.classes.scripting_project import ScriptingProject
from tests.unit.const import PROJECT_6_NONAME_ID, PROJECT_ID_1, PROJECT_ID_6


class TestStaticNoNameLookup:
    """SysML (static) no-name children resolve through declared_name = ElementType::ID."""

    @pytest.fixture
    def project(self, connector) -> Project:
        return SysML2ProjectManager(connector).get_sysml_project(PROJECT_ID_6)

    def test_get_resolves_noname_child_by_element_type_id(self, project):
        root = project.get_root_package()

        child = root.get("ConnectionUsage::4C27A76D-EB0D-4391-806F-C6103E0F41AB")

        assert child is not None
        assert child.id == PROJECT_6_NONAME_ID

    def test_noname_child_keeps_empty_name_and_declared_name_fallback(self, project):
        child = project.find_element_by_id(PROJECT_6_NONAME_ID)

        assert child.name == ""
        assert child.declared_name == "ConnectionUsage::4C27A76D-EB0D-4391-806F-C6103E0F41AB"

    def test_find_elements_by_name_matches_element_type_id(self, project):
        matches = project.find_elements_by_name(
            "ConnectionUsage::4C27A76D-EB0D-4391-806F-C6103E0F41AB"
        )

        assert len(matches) == 1
        assert matches[0].id == PROJECT_6_NONAME_ID

    def test_named_child_still_resolves(self, connector):
        """A named element is still reachable by its real name (declared_name == name)."""
        project = SysML2ProjectManager(connector).get_sysml_project(PROJECT_ID_1)
        root = project.get_root_package()

        assert root.get("PartDefinition").get("attribute") is not None


class TestScriptingNoNameLookup:
    """Scripting no-name children resolve through the dot-safe declared name fallback."""

    @pytest.fixture
    def project(self, connector) -> ScriptingProject:
        return SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_6)

    def test_dot_access_resolves_noname_child(self, project):
        root = project.get_root_package()

        assert (
            root.ConnectionUsage_4C27A76D_EB0D_4391_806F_C6103E0F41AB._id == PROJECT_6_NONAME_ID
        )

    def test_get_resolves_noname_child_by_dot_safe_fallback(self, project):
        root = project.get_root_package()

        child = root.get("ConnectionUsage_4C27A76D_EB0D_4391_806F_C6103E0F41AB")

        assert child is not None
        assert child._id == PROJECT_6_NONAME_ID

    def test_name_is_not_overwritten_with_fallback(self, project):
        child = project.find_element_by_id(PROJECT_6_NONAME_ID)

        assert child._name == ""
        assert child._declaredName == "ConnectionUsage_4C27A76D_EB0D_4391_806F_C6103E0F41AB"

    def test_find_elements_by_name_matches_fallback(self, project):
        matches = project.find_elements_by_name(
            "ConnectionUsage_4C27A76D_EB0D_4391_806F_C6103E0F41AB"
        )

        assert len(matches) == 1
        assert matches[0]._id == PROJECT_6_NONAME_ID
