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

"""Unit tests for SysMLElement value get/set using the mocked connector."""

import pytest

from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.scripting_project import ScriptingProject
from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.exception.connector_exception import BadRequestConnectionException
from ansys.sam.sysml2.exception.runtime_exception import UnsupportedValueExpression
from tests.unit.const import PROJECT_ID_1, PROJECT_ID_3


class TestSysMLElement:

    @pytest.fixture
    def project(self, connector) -> ScriptingProject:
        manager = SysML2ProjectManager(connector)
        return manager.get_scripting_project(PROJECT_ID_3)

    def test_update_element_name(self, connector, mocker):
        manager = SysML2ProjectManager(connector)
        project = manager.get_scripting_project(PROJECT_ID_1)
        root = project.get_root_package()
        mocker.patch.object(root._observer, "reload_project")
        attr = root.PartDefinition.attribute

        attr._name = "NewAttr"

        assert attr._name == "NewAttr"

    def test_expression_get_value(self, project):
        package = project.get_root_package()

        assert package.Feature.myExpressionFeature.get_value() == (10, "kg")

    def test_expression_set_value(self, connector, project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        package.Feature.myExpressionFeature.parse_and_set_value("20 [kg]")

        assert commit_spy.call_count == 1

    def test_expression_complex_value_throws_error(self, project):
        package = project.get_root_package()

        with pytest.raises(UnsupportedValueExpression):
            package.Feature.myComplexExpressionFeature.get_value()

    def test_int_get_set_value(self, connector, project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        assert package.Feature.myIntFeature.get_value() == 10

        package.Feature.myIntFeature.set_value(20)

        assert commit_spy.call_count == 1

    def test_string_get_set_value(self, connector, project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        assert package.Feature.myStringFeature.get_value() == "Hello"

        package.Feature.myStringFeature.set_value("World")

        assert commit_spy.call_count == 1

    def test_bool_get_set_value(self, connector, project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        assert package.Feature.myBoolFeature.get_value() is False

        package.Feature.myBoolFeature.set_value(True)

        assert commit_spy.call_count == 1

    def test_float_get_set_value(self, connector, project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        assert package.Feature.myFloatFeature.get_value() == pytest.approx(10.56)

        package.Feature.myFloatFeature.set_value(20.5)

        assert commit_spy.call_count == 1

    def test_setattr_commit_rejected(self, connector, mocker):
        manager = SysML2ProjectManager(connector)
        project = manager.get_scripting_project(PROJECT_ID_1)
        root = project.get_root_package()
        mocker.patch.object(
            connector,
            "create_commit",
            side_effect=BadRequestConnectionException("Invalid key"),
        )

        with pytest.raises(BadRequestConnectionException):
            root._name = ["ShouldFail"]


class TestSysMLElementDir:
    """Value methods are listed in dir() only for value-capable (Feature) elements."""

    def test_value_methods_hidden_on_non_feature(self):
        # The scripting mapper sets __class__ to a subclass named after the @type.
        comment_cls = type("Comment", (SysMLElement,), {})
        element = comment_cls("element_id")

        listing = dir(element)
        assert "get_value" not in listing
        assert "set_value" not in listing
        assert "parse_and_set_value" not in listing

    def test_value_methods_listed_on_feature_descendant(self):
        part_usage_cls = type("PartUsage", (SysMLElement,), {})
        element = part_usage_cls("element_id")

        listing = dir(element)
        assert "get_value" in listing
        assert "set_value" in listing
        assert "parse_and_set_value" in listing
