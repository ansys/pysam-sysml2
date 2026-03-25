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

from typing import Any, Dict, List, Tuple

from ansys.sam.sysml2.api.sysml2_api_connector import SysML2APIConnector
from ansys.sam.sysml2.dto.commit.commit_class import Commit
from ansys.sam.sysml2.dto.commit.data_version import DataVersion


class ModificationObserver:
    """Modification observer for SysML elements."""

    _project_id: str = ""
    _project = None
    _connector: SysML2APIConnector
    _stack: Dict[str, List[Tuple[str, Any]]]

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

    def set_transactional_mode(self, state: bool):
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

    def notify(self, element_id: str, name: str, value: object):
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

    def list_notify(self, element_id: str, name: str, list_content: List):
        """
        Catch modification on a list.

        Parameters
        ----------
        element_id : str
            Modified element ID.
        name : str
            Key of the modified field.
        list_content : Any
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

    def _register_list_change(self, element_id: str, name: str, list_content: List):
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
            if any(x[0] == name for x in self._stack[element_id]):
                current_list = [x for x in self._stack[element_id] if x[0] == name][0]
                self._stack[element_id].remove(current_list)
            self._stack[element_id].append((name, list_content))
        else:
            self._stack[element_id] = [(name, list_content)]

    def delete_element(self, element_id: str):
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

    def reload_project(self):
        """Reload of the project."""
        from ansys.sam.sysml2.builder.sysml2_project_builder import SysML2ProjectBuilder

        builder = SysML2ProjectBuilder(self._connector)
        builder.reload_project(self, self._project)

    def stop(self):
        """Disconnect the observer."""
        self._working_observer = False

    def start(self):
        """Connect the observer."""
        self._working_observer = True

    def _commit_stack(self):
        """Commit all stacked changes."""
        commit = Commit(self._project_id)
        for key, changes in self._stack.items():
            change = DataVersion()
            if not key.startswith("value:"):
                change.identify(key)
            for field in changes:
                change.add_change(field[0], field[1])
            commit.add_change(change)
        self._connector.create_commit(self._project_id, commit.to_json())
        self.reload_project()
