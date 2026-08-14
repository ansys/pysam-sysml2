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

"""Observer class."""

from typing import Any

from ansys.sam.sysml2.api.sysml2_api_connector import SysML2APIConnector
from ansys.sam.sysml2.dto.commit.commit_class import Commit
from ansys.sam.sysml2.dto.commit.data_version import DataVersion


class ModificationObserver:
    """Modification observer for SysML elements."""

    _project_id: str = ""
    _project = None
    _connector: SysML2APIConnector
    _stack: dict[str, list[tuple[str, Any]]]

    def __init__(self, project, connector: SysML2APIConnector):
        """
        Construct a new instance.

        Parameters
        ----------
        project : ProjectImpl
            Project instance to observe.
        connector: SysML2APIConnector
            SysML2 API Connector to make API calls.
        """
        self._project_id = project._id
        self._project = project
        self._connector = connector
        self._working_observer = True
        self._stack = {}
        self._is_transactional_mode = False

    def set_transactional_mode(self, state: bool) -> None:
        """
        Set the new value for transactional mode.

        Parameters
        ----------
        state : bool
            The new value.
        """
        if self._is_transactional_mode and not state:
            self._commit_stack()

        if state and not self._is_transactional_mode:
            self._stack = {}

        self._is_transactional_mode = state

    def notify(self, element_id: str, name: str, value: object) -> None:
        """
        Catch a modification notification.

        Parameters
        ----------
        element_id : str
            Modified element ID.
        name : str
            Key of the modified field.
        value : object
            Value of the modified field.
        """
        if self._working_observer:
            if self._is_transactional_mode:
                self._register_change(element_id, name, value)
            else:
                self._commit_single_change(element_id, name, value)

    def list_notify(self, element_id: str, name: str, list_content: list) -> None:
        """
        Catch modification on a list.

        Parameters
        ----------
        element_id : str
            Modified element ID.
        name : str
            Key of the modified field.
        list_content : list
            Updated content of the modified list field.
        """
        if self._working_observer:
            if self._is_transactional_mode:
                self._register_list_change(element_id, name, list_content)
            else:
                self._commit_single_change(element_id, name, list_content)

    def _commit_single_change(self, element_id: str, name: str, value: Any):
        """
        Commit a single field change on the element.

        Parameters
        ----------
        element_id : str
            ID of the changed element.
        name : str
            Name of the field updated.
        value : Any
            New value for the field.
        """
        commit = Commit(self._project_id)
        change = DataVersion()

        change.identify(element_id)
        if name.startswith("_"):
            name = name[1:]
        change.add_change(name, value)

        commit.add_change(change)
        self._connector.create_commit(self._project_id, commit.to_json())
        self.reload_project()

    def _register_change(self, element_id: str, name: str, value: Any):
        """
        Register current change on the element in the stack.

        Parameters
        ----------
        element_id : str
            ID of the changed element.
        name : str
            Name of the field updated.
        value : Any
            New value for the field.
        """
        if element_id in self._stack:
            self._stack[element_id].append((name, value))
        else:
            self._stack[element_id] = [(name, value)]

    def _register_list_change(self, element_id: str, name: str, list_content: list):
        """
        Register current change on a list in the stack.

        Parameters
        ----------
        element_id : str
            Modified element ID.
        name : str
            Name of the list.
        list_content : List
            New content of the list.
        """
        if element_id in self._stack:
            entries = self._stack[element_id]
            for i, entry in enumerate(entries):
                if entry[0] == name:
                    entries.pop(i)
                    break
            self._stack[element_id].append((name, list_content))
        else:
            self._stack[element_id] = [(name, list_content)]

    def delete_element(self, element_id: str) -> None:
        """
        Delete function for observer.

        Parameters
        ----------
        element_id : str
            The ID of the element to delete.
        """
        if self._working_observer:
            if self._is_transactional_mode:
                self._register_deletion(element_id)
            else:
                self._commit_deletion(element_id)

    def _register_deletion(self, element_id: str):
        """
        Register delete command.

        Parameters
        ----------
        element_id : str
            The element's ID to delete.
        """
        self._stack[element_id] = []

    def _commit_deletion(self, element_id: str):
        """
        Commit direct delete command.

        Parameters
        ----------
        element_id : str
            The element's ID to delete
        """
        commit = Commit(self._project_id)
        change = DataVersion()

        change.identify(element_id)
        commit.add_change(change)

        self._connector.create_commit(self._project_id, commit.to_json())
        self.reload_project()

    def reload_project(self) -> None:
        """Reload of the project."""
        from ansys.sam.sysml2.builder.sysml2_project_builder import SysML2ProjectBuilder

        builder = SysML2ProjectBuilder(self._connector)
        builder.reload_project(self, self._project)

    def stop(self) -> None:
        """Disconnect the observer."""
        self._working_observer = False

    def start(self) -> None:
        """Connect the observer."""
        self._working_observer = True

    @staticmethod
    def _normalized_fields(
        stacked_changes: list[tuple[str, Any]],
    ) -> list[tuple[str, Any]]:
        """Strip leading underscores from scripting-style field names."""
        fields = []
        for field_name, value in stacked_changes:
            if field_name.startswith("_"):
                field_name = field_name[1:]
            fields.append((field_name, value))
        return fields

    @staticmethod
    def _is_create(fields: list[tuple[str, Any]]) -> bool:
        """Return True when the stacked fields include an element ``@type``."""
        for field_name, _value in fields:
            if field_name == "@type":
                return True
        return False

    @staticmethod
    def _partition_create_fields_and_list_links(
        fields: list[tuple[str, Any]],
    ) -> tuple[list[tuple[str, Any]], list[tuple[str, Any]]]:
        """Split non-list create fields from list link fields."""
        create_fields = []
        list_links = []
        for field_name, value in fields:
            if isinstance(value, list):
                list_links.append((field_name, value))
            else:
                create_fields.append((field_name, value))
        return create_fields, list_links

    def _add_change(self, commit: Commit, element_id: str, fields: list[tuple[str, Any]]) -> None:
        """Build a DataVersion from fields and append it to the commit."""
        change = DataVersion()
        if not element_id.startswith("value:"):
            change.identify(element_id)
        for field_name, value in fields:
            change.add_change(field_name, value)
        commit.add_change(change)

    def _commit_stack(self):
        """Commit all stacked changes."""
        commit = Commit(self._project_id)
        deferred_list_updates = []

        for element_id, stacked_changes in self._stack.items():
            fields = self._normalized_fields(stacked_changes)
            if self._is_create(fields):
                create_fields, list_links = self._partition_create_fields_and_list_links(fields)
                self._add_change(commit, element_id, create_fields)
                if list_links:
                    deferred_list_updates.append((element_id, list_links))
            else:
                self._add_change(commit, element_id, fields)

        for element_id, list_links in deferred_list_updates:
            self._add_change(commit, element_id, list_links)

        if len(commit.changes) > 0:
            self._connector.create_commit(self._project_id, commit.to_json())
            self.reload_project()
