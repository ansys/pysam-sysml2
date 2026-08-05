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

"""Unit tests for SysML2ProjectBuilder using the mocked connector."""

from ansys.sam.sysml2.builder.sysml2_project_builder import SysML2ProjectBuilder
from tests.unit.const import PROJECT_1_ATTR_ID, PROJECT_ID_1


class TestSysML2ProjectBuilderScripting:

    def test_build_scripting_project(self, connector):
        builder = SysML2ProjectBuilder(connector)

        project = builder.build_scripting_project(PROJECT_ID_1)

        assert project.get_root_package()._name == "project-1"

    def test_find_element_by_id(self, connector):
        builder = SysML2ProjectBuilder(connector)
        project = builder.build_scripting_project(PROJECT_ID_1)

        element = project.find_element_by_id(PROJECT_1_ATTR_ID)

        assert element._name == "attribute"

    def test_find_elements_by_name(self, connector):
        builder = SysML2ProjectBuilder(connector)
        project = builder.build_scripting_project(PROJECT_ID_1)

        elements = project.find_elements_by_name("attribute")

        assert any(el._id == PROJECT_1_ATTR_ID for el in elements)

    def test_namespace_elements_have_no_owner(self, connector):
        builder = SysML2ProjectBuilder(connector)

        project = builder.build_scripting_project(PROJECT_ID_1)

        owner = project.get_root_package()._owner
        assert owner is not None
        assert getattr(owner, "_owner", None) is None


class TestSysML2ProjectBuilderSysML:

    def test_build_sysml_project(self, connector):
        builder = SysML2ProjectBuilder(connector)

        project = builder.build_sysml_project(PROJECT_ID_1)

        assert project.get_root_package().name == "project-1"

    def test_find_element_by_id_sysml(self, connector):
        builder = SysML2ProjectBuilder(connector)
        project = builder.build_sysml_project(PROJECT_ID_1)

        element = project.find_element_by_id(PROJECT_1_ATTR_ID)

        assert element.name == "attribute"

    def test_find_elements_by_name_sysml(self, connector):
        builder = SysML2ProjectBuilder(connector)
        project = builder.build_sysml_project(PROJECT_ID_1)

        elements = project.find_elements_by_name("attribute")

        assert any(el.id == PROJECT_1_ATTR_ID for el in elements)

    def test_namespace_elements_have_no_owner_sysml(self, connector):
        builder = SysML2ProjectBuilder(connector)

        project = builder.build_sysml_project(PROJECT_ID_1)

        owner = project.get_root_package().owner
        assert owner is not None
        assert owner.owner is None


class TestSysML2ProjectBuilderIncludesFlags:

    def test_build_sysml_project_passes_includes_flags(self, connector, mocker):
        get_all_elements = mocker.patch.object(connector, "get_all_elements", wraps=connector.get_all_elements)
        builder = SysML2ProjectBuilder(connector)

        builder.build_sysml_project(
            PROJECT_ID_1,
            includes_derived=False,
            includes_inherited=False,
        )

        get_all_elements.assert_called()
        assert get_all_elements.call_args.kwargs["includes_derived"] is False
        assert get_all_elements.call_args.kwargs["includes_inherited"] is False
