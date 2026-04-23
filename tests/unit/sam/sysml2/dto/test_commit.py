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

"""Pure unit tests for Commit and DataVersion serialization."""

import json

from ansys.sam.sysml2.dto.commit.commit_class import Commit
from ansys.sam.sysml2.dto.commit.data_version import DataVersion


class TestCommit:

    def test_commit_json_has_required_keys(self):
        commit = Commit("proj-1")
        change = DataVersion()
        change.identify("elem-1")
        change.add_change("name", "TestName")
        commit.add_change(change)

        result = json.loads(commit.to_json())
        assert result["@type"] == "Commit"
        assert "change" in result
        assert "owningProject" in result
        assert result["owningProject"]["@id"] == "proj-1"
        assert "previousCommit" in result
        assert result["previousCommit"]["@id"] == "head"

    def test_data_version_json_has_type(self):
        dv = DataVersion()
        dv.identify("elem-1")
        dv.add_change("name", "Test")
        result = dv.to_json()
        assert result["@type"] == "DataVersion"

    def test_data_identity_includes_type(self):
        dv = DataVersion()
        dv.identify("elem-1")
        result = dv.to_json()
        assert result["identity"]["@id"] == "elem-1"
        assert result["identity"]["@type"] == "DataIdentity"

    def test_data_version_add_change(self):
        dv = DataVersion()
        dv.add_change("name", "Value")
        result = dv.to_json()
        assert result["payload"]["name"] == "Value"

    def test_empty_commit(self):
        commit = Commit("proj-1")
        result = json.loads(commit.to_json())
        assert result["change"] == []
        assert result["@type"] == "Commit"

    def test_delete_element_commit_structure(self):
        commit = Commit("proj-1")
        change = DataVersion()
        change.identify("elem-to-delete")
        commit.add_change(change)
        result = json.loads(commit.to_json())
        dv = result["change"][0]
        assert dv["identity"]["@id"] == "elem-to-delete"
        assert "payload" not in dv

    def test_update_element_commit_structure(self):
        commit = Commit("proj-1")
        change = DataVersion()
        change.identify("elem-1")
        change.add_change("name", "NewName")
        commit.add_change(change)
        result = json.loads(commit.to_json())
        dv = result["change"][0]
        assert dv["identity"]["@id"] == "elem-1"
        assert dv["payload"]["name"] == "NewName"

    def test_commit_matches_fixture(self):
        commit = Commit("1")
        result = json.loads(commit.to_json())
        assert result["owningProject"]["@id"] == "1"
        assert result["previousCommit"]["@id"] == "head"
