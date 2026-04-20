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
"""EObject test class."""

from conftest import restore_projects_backup_between_tests
from mocked_server.routes.const import PROJECT_ID_1, PROJECT_ID_3, PROJECT_ID_4
from parent_test_class import ParentTestClass
import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.exception.runtime_exception import UnsupportedValueExpression


class TestEObjet(ParentTestClass):
    """EObject test class instance."""

    @pytest.fixture(scope="function", autouse=True)
    def restore_jsons(self):
        """Restores project backups between tests."""
        restore_projects_backup_between_tests()

    @pytest.fixture
    def old_format_project(self, valid_source: AnsysSysML2APIConnector) -> Project:
        """Provide an old-format project instance."""
        model_manager = SysML2ProjectManager(connector=valid_source)
        project = model_manager.get_sysml_project(PROJECT_ID_4)
        return project

    @pytest.fixture
    def new_format_project(self, valid_source: AnsysSysML2APIConnector) -> Project:
        """Provide a new-format project instance."""
        model_manager = SysML2ProjectManager(connector=valid_source)
        project = model_manager.get_sysml_project(PROJECT_ID_3)
        return project

    def test_update_element(self, valid_source: AnsysSysML2APIConnector):
        """Verifies element attribute update."""
        project_manager = SysML2ProjectManager(valid_source)
        project = project_manager.get_sysml_project(PROJECT_ID_1)

        project_root = project.get_root_package()
        project_root.get("PartDefinition").get("Attribute").name = "NewAttr"

        assert project_root.get("PartDefinition").get("NewAttr").name == "NewAttr"
        assert project_root.get("PartDefinition").get("Attribute") is None

    def test_expression_with_old_format_project_get_values(self, old_format_project: Project):
        """Verifies expression value in old project."""
        package = old_format_project.get_root_package()
        assert package.get("Structure").get("Frame").get("weight").get_value() == (
            "2",
            "kilogram",
        )

    def test_expression_with_new_format_project_get_values(self, new_format_project: Project):
        """Verifies expression value in new project."""
        package = new_format_project.get_root_package()
        assert package.get("Feature").get("myExpressionFeature").get_value() == (
            10,
            "kilogram",
        )

    def test_expression_with_new_format_set_value_without_errors(self, new_format_project: Project):
        """Verifies expression value set without error."""
        package = new_format_project.get_root_package()
        package.get("Feature").get("myExpressionFeature").parse_and_set_value("10 [kg]")

    def test_expression_with_new_format_get_value_with_complex_value_throw_error(self, new_format_project: Project):
        """Verifies error for complex expression value."""
        package = new_format_project.get_root_package()
        with pytest.raises(UnsupportedValueExpression):
            package.get("Feature").get("myComplexExpressionFeature").get_value()

    def test_int_with_new_format_get_values(self, new_format_project: Project):
        """Verifies integer value."""
        package = new_format_project.get_root_package()
        assert package.get("Feature").get("myIntFeature").get_value() == 10

    def test_int_with_new_format_set_value_without_errors(self, new_format_project: Project):
        """Verifies integer value set without error."""
        package = new_format_project.get_root_package()
        package.get("Feature").get("myIntFeature").set_value(10)

    def test_string_with_new_format_get_values(self, new_format_project: Project):
        """Verifies string value."""
        package = new_format_project.get_root_package()
        assert package.get("Feature").get("myStringFeature").get_value() == "Hello"

    def test_string_with_new_format_set_value_without_errors(self, new_format_project: Project):
        """Verifies string value set without error."""
        package = new_format_project.get_root_package()
        package.get("Feature").get("myStringFeature").set_value("Hello")

    def test_bool_with_new_format_get_values(self, new_format_project: Project):
        """Verifies boolean value."""
        package = new_format_project.get_root_package()
        assert package.get("Feature").get("myBoolFeature").get_value() is False

    def test_bool_with_new_format_set_value_without_errors(self, new_format_project: Project):
        """Verifies boolean value set without error."""
        package = new_format_project.get_root_package()
        package.get("Feature").get("myBoolFeature").set_value(True)

    def test_float_with_new_format_get_values(self, new_format_project: Project):
        """Verifies float value."""
        package = new_format_project.get_root_package()
        assert package.get("Feature").get("myFloatFeature").get_value() == pytest.approx(10.56)

    def test_float_with_new_format_set_value_without_errors(self, new_format_project: Project):
        """Verifies float value set without error."""
        package = new_format_project.get_root_package()
        package.get("Feature").get("myFloatFeature").set_value(10.5)
