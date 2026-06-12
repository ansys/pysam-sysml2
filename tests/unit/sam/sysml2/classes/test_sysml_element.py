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
from ansys.sam.sysml2.classes.inherited_element import InheritedElement
from ansys.sam.sysml2.classes.scripting_project import ScriptingProject
from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.exception.connector_exception import BadRequestConnectionException
from ansys.sam.sysml2.exception.runtime_exception import UnsupportedValueExpression
from tests.unit.const import PROJECT_ID_1, PROJECT_ID_3, PROJECT_ID_4


class TestSysMLElement:

    @pytest.fixture
    def old_format_project(self, connector) -> ScriptingProject:
        manager = SysML2ProjectManager(connector)
        return manager.get_scripting_project(PROJECT_ID_4)

    @pytest.fixture
    def new_format_project(self, connector) -> ScriptingProject:
        manager = SysML2ProjectManager(connector)
        return manager.get_scripting_project(PROJECT_ID_3)

    def test_update_element_name(self, connector, mocker):
        manager = SysML2ProjectManager(connector)
        project = manager.get_scripting_project(PROJECT_ID_1)
        root = project.get_root_package()
        mocker.patch.object(root._observer, "reload_project")
        attr = root.PartDefinition.attribute

        attr._declaredName = "NewAttr"

        assert attr._declaredName == "NewAttr"

    def test_expression_get_value_old_format(self, old_format_project):
        package = old_format_project.get_root_package()

        assert package.Structure.Frame.weight.get_value() == ("2", "kg")

    def test_expression_get_value_new_format(self, new_format_project):
        package = new_format_project.get_root_package()

        assert package.Feature.myExpressionFeature.get_value() == (10, "kg")

    def test_expression_set_value_new_format(
        self, connector, new_format_project, mocker
    ):
        package = new_format_project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        package.Feature.myExpressionFeature.parse_and_set_value("20 [kg]")

        assert commit_spy.call_count == 1

    def test_expression_complex_value_throws_error(self, new_format_project):
        package = new_format_project.get_root_package()

        with pytest.raises(UnsupportedValueExpression):
            package.Feature.myComplexExpressionFeature.get_value()

    def test_int_get_set_value(self, connector, new_format_project, mocker):
        package = new_format_project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        assert package.Feature.myIntFeature.get_value() == 10

        package.Feature.myIntFeature.set_value(20)

        assert commit_spy.call_count == 1

    def test_string_get_set_value(self, connector, new_format_project, mocker):
        package = new_format_project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        assert package.Feature.myStringFeature.get_value() == "Hello"

        package.Feature.myStringFeature.set_value("World")

        assert commit_spy.call_count == 1

    def test_bool_get_set_value(self, connector, new_format_project, mocker):
        package = new_format_project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        assert package.Feature.myBoolFeature.get_value() is False

        package.Feature.myBoolFeature.set_value(True)

        assert commit_spy.call_count == 1

    def test_float_get_set_value(self, connector, new_format_project, mocker):
        package = new_format_project.get_root_package()
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
            root._declaredName = ["ShouldFail"]


class TestSysMLElementDir:
    """Connection getters are listed in dir() only when the element has ends."""

    def test_source_target_hidden_without_ends(self):
        element = SysMLElement("element_id")

        listing = dir(element)
        assert "get_source" not in listing
        assert "get_target" not in listing

    def test_get_source_listed_when_source_populated(self):
        element = SysMLElement("element_id")
        element._source = [SysMLElement("end_id")]

        assert "get_source" in dir(element)
        assert "get_target" not in dir(element)

    def test_get_target_listed_when_target_populated(self):
        element = SysMLElement("element_id")
        element._target = [SysMLElement("end_id")]

        assert "get_target" in dir(element)
        assert "get_source" not in dir(element)


class TestSysMLElementGet:
    """The get(name) accessor reaches children whose names dot access cannot express."""

    def _build_parent_with_spaced_child(self):
        child = SysMLElement("child-id")
        child._identifier = "child-id"
        child._declaredName = "Part Definition"
        parent = SysMLElement("parent-id")
        parent._element_hash_map = {"Part Definition": child}
        parent._ownedElement = [child]
        return parent, child

    def test_get_returns_owned_child_with_spaced_name(self):
        parent, child = self._build_parent_with_spaced_child()

        assert parent.get("Part Definition") is child

    def test_get_returns_none_for_missing_name(self):
        parent, _ = self._build_parent_with_spaced_child()

        assert parent.get("missing") is None

    def test_get_through_inherited_element_proxy(self):
        parent, _ = self._build_parent_with_spaced_child()
        owner = SysMLElement("owner-id")
        owner._owner = None
        proxy = InheritedElement(owner, parent)

        resolved = proxy.get("Part Definition")

        assert resolved is not None
        assert resolved._name == "Part Definition"
        assert proxy.get("missing") is None
