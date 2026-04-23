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

"""Unit tests for EObject (SysML project element) get/set using the mocked connector."""

import pytest

from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.exception.runtime_exception import UnsupportedValueExpression
from tests.unit.const import PROJECT_ID_1, PROJECT_ID_3, PROJECT_ID_4


class TestEObjet:

    @pytest.fixture
    def old_format_project(self, connector) -> Project:
        model_manager = SysML2ProjectManager(connector=connector)
        return model_manager.get_sysml_project(PROJECT_ID_4)

    @pytest.fixture
    def new_format_project(self, connector) -> Project:
        model_manager = SysML2ProjectManager(connector=connector)
        return model_manager.get_sysml_project(PROJECT_ID_3)

    def test_update_element(self, connector, mocker):
        project_manager = SysML2ProjectManager(connector)
        project = project_manager.get_sysml_project(PROJECT_ID_1)
        root = project.get_root_package()
        mocker.patch.object(root._observer, "reload_project")
        elem = root.get("PartDefinition").get("Attribute")
        elem.name = "NewAttr"
        assert elem.name == "NewAttr"

    def test_expression_with_old_format_project_get_values(
        self, old_format_project: Project
    ):
        package = old_format_project.get_root_package()
        assert package.get("Structure").get("Frame").get("weight").get_value() == (
            "2",
            "kg",
        )

    def test_expression_with_new_format_project_get_values(
        self, new_format_project: Project
    ):
        package = new_format_project.get_root_package()
        assert package.get("Feature").get("myExpressionFeature").get_value() == (
            10,
            "kg",
        )

    def test_expression_set_value(self, new_format_project: Project, mocker):
        package = new_format_project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        package.get("Feature").get("myExpressionFeature").parse_and_set_value("20 [kg]")
        value = package.get("Feature").get("myExpressionFeature").get_value()
        assert value is not None

    def test_expression_complex_value_throws_error(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        with pytest.raises(UnsupportedValueExpression):
            package.get("Feature").get("myComplexExpressionFeature").get_value()

    def test_int_get_values(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        assert package.get("Feature").get("myIntFeature").get_value() == 10

    def test_int_set_value(self, connector, new_format_project: Project, mocker):
        package = new_format_project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")
        package.get("Feature").get("myIntFeature").set_value(20)
        assert commit_spy.call_count >= 1

    def test_string_get_values(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        assert package.get("Feature").get("myStringFeature").get_value() == "Hello"

    def test_string_set_value(self, connector, new_format_project: Project, mocker):
        package = new_format_project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")
        package.get("Feature").get("myStringFeature").set_value("World")
        assert commit_spy.call_count >= 1

    def test_bool_get_values(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        assert package.get("Feature").get("myBoolFeature").get_value() is False

    def test_bool_set_value(self, connector, new_format_project: Project, mocker):
        package = new_format_project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")
        package.get("Feature").get("myBoolFeature").set_value(True)
        assert commit_spy.call_count >= 1

    def test_float_get_values(self, new_format_project: Project):
        package = new_format_project.get_root_package()
        assert package.get("Feature").get(
            "myFloatFeature"
        ).get_value() == pytest.approx(10.56)

    def test_float_set_value(self, connector, new_format_project: Project, mocker):
        package = new_format_project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")
        package.get("Feature").get("myFloatFeature").set_value(20.5)
        assert commit_spy.call_count >= 1
