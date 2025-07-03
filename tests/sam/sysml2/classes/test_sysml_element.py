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

import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.exception.runtime_exception import UnsupportedValueExpression
from mocked_server.routes.const import PROJECT_ID_1, PROJECT_ID_3, PROJECT_ID_4
from parent_test_class import ParentTestClass
from conftest import restore_projects_backup_between_tests


class TestSysMLElement(ParentTestClass):

    @pytest.fixture(scope="function", autouse=True)
    def restore_jsons(self):
        restore_projects_backup_between_tests()

    @pytest.fixture
    def old_format_project(self, valid_source: AnsysSysML2APIConnector) -> Project:
        model_manager = SysML2ProjectManager(connector=valid_source)
        project = model_manager.get_project(PROJECT_ID_4)
        return project

    @pytest.fixture
    def new_format_project(self, valid_source: AnsysSysML2APIConnector) -> Project:
        model_manager = SysML2ProjectManager(connector=valid_source)
        project = model_manager.get_project(PROJECT_ID_3)
        return project

    def test_update_element(self, valid_source: AnsysSysML2APIConnector):
        project_manager = SysML2ProjectManager(valid_source)
        project = project_manager.get_project(PROJECT_ID_1)

        project_root = project.get_root_package()
        project_root.PartDefinition.Attribute._name = "NewAttr"

        assert project_root.PartDefinition.NewAttr._name == "NewAttr"

        with pytest.raises(AttributeError):
            project_root.PartDefinition.Attribute

    def test_expression_with_old_format_project_get_values(self, old_format_project: Project):
        package = old_format_project.get_root_package()
        assert package.Structure.Frame.weight.get_value() == ("2", "kg")

    def test_expression_with_new_format_project_get_values(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        assert package.Feature.myExpressionFeature.get_value() == (10, "kg")

    def test_expression_with_new_format_set_value_without_errors(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        package.Feature.myExpressionFeature.parse_and_set_value("10 [kg]")

    def test_expression_with_new_format_get_value_with_complex_value_throw_error(
        self, new_format_project: Project
    ):
        package = new_format_project.get_root_package()
        with pytest.raises(UnsupportedValueExpression):
            package.Feature.myComplexExpressionFeature.get_value()

    def test_int_with_new_format_get_values(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        assert package.Feature.myIntFeature.get_value() == 10

    def test_int_with_new_format_set_value_without_errors(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        package.Feature.myIntFeature.set_value(10)

    def test_string_with_new_format_get_values(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        assert package.Feature.myStringFeature.get_value() == "Hello"

    def test_string_with_new_format_set_value_without_errors(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        package.Feature.myStringFeature.set_value("Hello")

    def test_bool_with_new_format_get_values(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        assert package.Feature.myBoolFeature.get_value() is False

    def test_bool_with_new_format_set_value_without_errors(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        package.Feature.myBoolFeature.set_value(True)

    def test_float_with_new_format_get_values(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        assert package.Feature.myFloatFeature.get_value() == pytest.approx(10.56)

    def test_float_with_new_format_set_value_without_errors(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        package.Feature.myFloatFeature.set_value(10.5)
