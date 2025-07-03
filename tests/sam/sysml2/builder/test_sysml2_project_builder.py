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


from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.sysml2_project_builder import SysML2ProjectBuilder
from mocked_server.routes.const import PROJECT_1_ATTR_ID, PROJECT_ID_1
from parent_test_class import ParentTestClass


class TestSysML2ProjectBuilder(ParentTestClass):

    def test_build_project(self, valid_source: AnsysSysML2APIConnector):
        builder = SysML2ProjectBuilder(valid_source)
        project = builder.build_project(PROJECT_ID_1)
        assert len(project.get_root()) == 1
        assert project.get_root()[0]._name == "PySamTestProject-COMPLET"
        assert project.get_root_package()._name == "PySamTestProject-COMPLET"

    def test_find_element_by_id(self, valid_source: AnsysSysML2APIConnector):
        builder = SysML2ProjectBuilder(valid_source)
        project = builder.build_project(PROJECT_ID_1)
        element_id = PROJECT_1_ATTR_ID
        element_found = project.find_element_by_id(element_id)

        assert element_found._name == "Attribute"

    def test_find_elements_by_name(self, valid_source: AnsysSysML2APIConnector):
        builder = SysML2ProjectBuilder(valid_source)
        project = builder.build_project(PROJECT_ID_1)
        element_name = "Attribute"
        elements_found = project.find_elements_by_name(element_name)

        expected_id = PROJECT_1_ATTR_ID
        assert any(el._id == expected_id for el in elements_found)
