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

"""Unit tests for ValueHelper reading and writing complex expressions as text."""

import json

import pytest

from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.tools.sysmltools import SysMLTools
from tests.unit.const import PROJECT_ID_5


class TestValueHelperComplexExpressions:
    """Read and write complex expressions as text, for both project layers."""

    @pytest.fixture
    def scripting_package(self, connector):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)
        return project.get_root_package()

    @pytest.fixture
    def sysml_package(self, connector):
        project = SysML2ProjectManager(connector).get_sysml_project(PROJECT_ID_5)
        return project.get_root_package()

    def test_scripting_arithmetic_expression(self, scripting_package):
        value = scripting_package.get("attribute").get_value()
        assert SysMLTools.isinstance(value, "OperatorExpression")
        assert SysMLTools.serialize_expression(value) == "5 + 5"

    def test_scripting_nested_arithmetic_expression(self, scripting_package):
        value = scripting_package.get("attribute3").get_value()
        assert SysMLTools.serialize_expression(value) == "1 + 2 + 3"

    def test_scripting_reference_expression(self, scripting_package):
        value = scripting_package.get("attribute2").get_value()
        assert SysMLTools.serialize_expression(value) == "attribute + attribute1"

    def test_scripting_unary_not_expression(self, scripting_package):
        value = scripting_package.get("attribute4").get_value()
        assert SysMLTools.serialize_expression(value) == "not true"

    def test_scripting_unit_expression_resolves_library_referent(self, connector):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)
        package = project.get_root_package()

        value = package.get("attribute1").get_value()

        assert SysMLTools.serialize_expression(value) == "5 [kg]"

    def test_sysml_arithmetic_expression(self, sysml_package):
        value = sysml_package.get("attribute").get_value()
        assert SysMLTools.isinstance(value, "OperatorExpression")
        assert SysMLTools.serialize_expression(value) == "5 + 5"

    def test_sysml_nested_arithmetic_expression(self, sysml_package):
        value = sysml_package.get("attribute3").get_value()
        assert SysMLTools.serialize_expression(value) == "1 + 2 + 3"

    def test_sysml_reference_expression(self, sysml_package):
        value = sysml_package.get("attribute2").get_value()
        assert SysMLTools.serialize_expression(value) == "attribute + attribute1"

    def test_sysml_unary_not_expression(self, sysml_package):
        value = sysml_package.get("attribute4").get_value()
        assert SysMLTools.serialize_expression(value) == "not true"

    def test_sysml_unit_expression_resolves_library_referent(self, connector):
        project = SysML2ProjectManager(connector).get_sysml_project(PROJECT_ID_5)
        package = project.get_root_package()

        value = package.get("attribute1").get_value()

        assert SysMLTools.serialize_expression(value) == "5 [kg]"

    def test_set_complex_expression_commits_text(self, connector, mocker):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)
        package = project.get_root_package()
        attribute = package.get("attribute")
        mocker.patch.object(attribute._observer, "reload_project")
        original_expr_id = attribute._valuation._value._id
        commit_spy = mocker.spy(connector, "create_commit")

        attribute.parse_and_set_value("attribute4 * attribute2")

        assert commit_spy.call_count == 2
        drop = json.loads(commit_spy.call_args_list[0].args[1])
        drop_change = drop["change"][0]
        assert "payload" not in drop_change
        assert drop_change["identity"]["@id"] == original_expr_id
        committed = json.loads(commit_spy.call_args_list[1].args[1])
        payload = committed["change"][0]["payload"]
        assert payload["@type"] == "FeatureValue"
        assert payload["value"] == "attribute4 * attribute2"
        assert payload["isDefault"] is True
        assert payload["isInitial"] is False
        assert payload["owner"] == {"@id": attribute._id}

    def test_set_value_commits_quoted_string(self, connector, mocker):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)
        package = project.get_root_package()
        attribute = package.get("attribute")
        mocker.patch.object(attribute._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        attribute.set_value("attribute4 * attribute2")

        committed = json.loads(commit_spy.call_args.args[1])
        payload = committed["change"][-1]["payload"]
        assert payload["@type"] == "FeatureValue"
        assert payload["value"] == '"attribute4 * attribute2"'
