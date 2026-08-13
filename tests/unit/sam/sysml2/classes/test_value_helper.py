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
from ansys.sam.sysml2.classes.value_helper import ValueHelper
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

        SysMLTools.parse_and_set_value(attribute, "attribute4 * attribute2")

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

    def test_adapt_value_escapes_kerml_string_literal(self):
        helper = ValueHelper("_")

        assert helper._adapt_value("Hello\\World") == '"Hello\\\\World"'
        assert helper._adapt_value("try\\to") == '"try\\\\to"'
        assert helper._adapt_value('say "hi"') == '"say \\"hi\\""'
        assert helper._adapt_value("a\tb\nc\rd") == '"a\\tb\\nc\\rd"'

    def test_unescape_kerml_string(self):
        assert ValueHelper.unescape_kerml_string("try\\\\to") == "try\\to"
        assert ValueHelper.unescape_kerml_string("Hello\\\\World") == "Hello\\World"
        assert ValueHelper.unescape_kerml_string('say \\"hi\\"') == 'say "hi"'
        assert ValueHelper.unescape_kerml_string("a\\tb\\nc\\rd") == "a\tb\nc\rd"

    def test_unescape_kerml_string_leaves_decoded_controls(self):
        decoded = "try\\\\\nto"
        assert decoded.count("\\") == 2
        assert "\n" in decoded
        assert ValueHelper.unescape_kerml_string(decoded) == decoded

    def test_escape_unescape_kerml_string_roundtrip(self):
        samples = [
            "Hello\\World",
            'say "hi"',
            "a\tb\nc",
            "plain",
            "try\\\\\nto",
        ]
        for sample in samples:
            escaped = ValueHelper.escape_kerml_string(sample)
            assert ValueHelper.unescape_kerml_string(escaped) == sample

    def test_set_value_commits_escaped_backslash_string(self, connector, mocker):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)
        package = project.get_root_package()
        attribute = package.get("attribute")
        mocker.patch.object(attribute._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        attribute.set_value("Hello\\World")

        committed = json.loads(commit_spy.call_args.args[1])
        payload = committed["change"][-1]["payload"]
        assert payload["@type"] == "FeatureValue"
        assert payload["value"] == '"Hello\\\\World"'

    def test_set_value_commits_escaped_quote_string(self, connector, mocker):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)
        package = project.get_root_package()
        attribute = package.get("attribute")
        mocker.patch.object(attribute._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        attribute.set_value('say "hi"')

        committed = json.loads(commit_spy.call_args.args[1])
        payload = committed["change"][-1]["payload"]
        assert payload["@type"] == "FeatureValue"
        assert payload["value"] == '"say \\"hi\\""'

    def test_commit_literal_update_escapes_kerml_string(self, mocker):
        """In-place LiteralString updates escape content without wrapping quotes."""
        helper = ValueHelper("_")
        connector = mocker.Mock()
        observer = mocker.Mock()
        observer._project_id = "project-id"
        observer._connector = connector
        feature = mocker.Mock()
        feature._observer = observer
        literal = mocker.Mock()
        literal._id = "literal-id"

        helper._commit_literal_update(feature, literal, "LiteralString", "try\\to")

        committed_change = json.loads(connector.create_commit.call_args.args[1])["change"][-1]
        assert committed_change["identity"]["@id"] == "literal-id"
        assert committed_change["payload"] == {
            "@type": "LiteralString",
            "value": "try\\\\to",
        }