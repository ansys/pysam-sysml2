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

"""Unit tests for ModificationObserver, transactional and immediate commit flows."""

import json

import pytest

from ansys.sam.sysml2.builder.classes.project_impl import ProjectImpl
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.exception.connector_exception import BadRequestConnectionException
from ansys.sam.sysml2.meta_model.documentation import Documentation
from ansys.sam.sysml2.observer.observer import ModificationObserver
from tests.unit.const import PROJECT_ID_1

class TestObserverTransactional:
    """Transactional mode defers every change into a single commit at stop time.

    These tests assert the public observable contract via ``create_commit``:
    no commit fires until ``set_transactional_mode(False)``, then exactly one
    commit is sent whose JSON payload reflects the registered changes.
    """

    @pytest.fixture
    def observer(self, connector, mocker) -> ModificationObserver:
        """Build an observer wired to the mocked connector, with ``reload_project`` stubbed out."""
        observer = ModificationObserver(ProjectImpl("", ""), connector)
        mocker.patch.object(observer, "reload_project")
        return observer

    def test_transactional_notify_defers_commit_until_stop(self, observer, connector, mocker):
        commit_mock = mocker.patch.object(connector, "create_commit")

        observer.set_transactional_mode(True)
        observer.notify("id", "name", "New Name")

        assert commit_mock.call_count == 0

        observer.set_transactional_mode(False)

        assert commit_mock.call_count == 1

        payload = json.loads(commit_mock.call_args.args[1])

        assert payload["change"][0]["identity"]["@id"] == "id"
        assert payload["change"][0]["payload"] == {"name": "New Name"}

    def test_transactional_list_notify_defers_commit_until_stop(self, observer, connector, mocker):
        commit_mock = mocker.patch.object(connector, "create_commit")

        observer.set_transactional_mode(True)
        observer.list_notify("id", "definition", ["t", "t"])

        assert commit_mock.call_count == 0

        observer.set_transactional_mode(False)

        assert commit_mock.call_count == 1

        payload = json.loads(commit_mock.call_args.args[1])

        assert payload["change"][0]["identity"]["@id"] == "id"
        assert payload["change"][0]["payload"] == {"definition": ["t", "t"]}

    def test_transactional_delete_defers_commit_until_stop(self, observer, connector, mocker):
        commit_mock = mocker.patch.object(connector, "create_commit")

        observer.set_transactional_mode(True)
        observer.delete_element("id")

        assert commit_mock.call_count == 0

        observer.set_transactional_mode(False)

        assert commit_mock.call_count == 1

        payload = json.loads(commit_mock.call_args.args[1])

        assert payload["change"][0]["identity"]["@id"] == "id"
        assert "payload" not in payload["change"][0]

    def test_transactional_create_defers_list_links_after_creates(self, observer, connector, mocker):
        """List links on a create are a separate update after all creates."""
        commit_mock = mocker.patch.object(connector, "create_commit")
        requirement_id = "req-id"
        documentation_id = "doc-id"
        documentation = Documentation(documentation_id)

        observer.set_transactional_mode(True)
        observer.notify(requirement_id, "@type", "RequirementUsage")
        observer.notify(requirement_id, "declaredName", "MassLimit")
        observer.notify(requirement_id, "owner", "bike-id")
        observer.notify(documentation_id, "@type", "Documentation")
        observer.notify(documentation_id, "body", "Shall not exceed 15 kg")
        observer.list_notify(requirement_id, "documentation", [documentation])
        observer.notify(requirement_id, "reqId", "REQ-001")
        observer.set_transactional_mode(False)

        changes = json.loads(commit_mock.call_args.args[1])["change"]
        requirement_create, documentation_create, documentation_link = changes

        assert requirement_create["identity"]["@id"] == requirement_id
        assert requirement_create["payload"] == {
            "@type": "RequirementUsage",
            "declaredName": "MassLimit",
            "owner": "bike-id",
            "reqId": "REQ-001",
        }
        assert "documentation" not in requirement_create["payload"]

        assert documentation_create["identity"]["@id"] == documentation_id
        assert documentation_create["payload"] == {
            "@type": "Documentation",
            "body": "Shall not exceed 15 kg",
        }

        assert documentation_link["identity"]["@id"] == requirement_id
        assert documentation_link["payload"] == {
            "documentation": [{"@id": documentation_id}],
        }


class TestObserverImmediate:
    """Tests for immediate commit flows using the mocked connector."""

    def test_notify_immediate_calls_create_commit(self, connector, mocker):
        manager = SysML2ProjectManager(connector)
        project = manager.get_scripting_project(PROJECT_ID_1)
        root = project.get_root_package()
        mocker.patch.object(root._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        root._declaredName = "RenamedRoot"

        assert root._declaredName == "RenamedRoot"
        assert commit_spy.call_count == 1

    def test_list_notify_immediate_calls_create_commit(self, connector, mocker):
        manager = SysML2ProjectManager(connector)
        project = manager.get_scripting_project(PROJECT_ID_1)
        root = project.get_root_package()
        mocker.patch.object(root._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")
        from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil

        valid_el = SysMLUtil.get_scripting_constructor("PartUsage")("valid_id")

        root._ownedElement.append(valid_el)

        assert commit_spy.call_count == 1

    def test_delete_element_immediate_calls_create_commit(self, connector, mocker):
        manager = SysML2ProjectManager(connector)
        project = manager.get_scripting_project(PROJECT_ID_1)
        root = project.get_root_package()
        mocker.patch.object(root._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        root.delete()

        assert commit_spy.call_count == 1

    def test_notify_commit_error_propagates(self, connector, mocker):
        """Verify BadRequestConnectionException from create_commit propagates to the caller."""
        manager = SysML2ProjectManager(connector)
        project = manager.get_scripting_project(PROJECT_ID_1)
        root = project.get_root_package()
        mocker.patch.object(
            connector,
            "create_commit",
            side_effect=BadRequestConnectionException("Bad commit"),
        )

        with pytest.raises(BadRequestConnectionException):
            root._declaredName = ["ShouldFail"]

    def test_delete_commit_error_propagates(self, connector, mocker):
        """Verify BadRequestConnectionException from create_commit propagates on delete."""
        manager = SysML2ProjectManager(connector)
        project = manager.get_scripting_project(PROJECT_ID_1)
        root = project.get_root_package()
        mocker.patch.object(
            connector,
            "create_commit",
            side_effect=BadRequestConnectionException("Bad commit"),
        )

        with pytest.raises(BadRequestConnectionException):
            root.delete()
