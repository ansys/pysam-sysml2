# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
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

from ansys.sam.sysml2.api.sysml2_api_connector import SysML2APIConnector
from ansys.sam.sysml2.dto.commit.commit_class import Commit
from ansys.sam.sysml2.dto.commit.data_version import DataVersion


class ModificationObserver:
    """Modification observer for SysML elements."""

    _project_id: str = ""
    _project = None
    _connector: SysML2APIConnector

    def __init__(self, project, connector: SysML2APIConnector):
        """Construct a new instance."""
        self._project_id = project._id
        self._project = project
        self._connector = connector
        self._working_observer = True

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
            commit = Commit(self._project_id)
            change = DataVersion()

            change.identify(element_id)
            change.add_change(name[1:], value)

            commit.add_change(change)

            self._connector.create_commit(self._project_id, commit.to_json())
            self.reload_project()

    def list_notify(self, element_id, name, list_content):
        """
        Catch modification on a list.

        Parameters
        ----------
        element_id : _type_
            _description_
        name : _type_
            _description_
        list_content : _type_
            _description_
        """
        if self._working_observer:
            commit = Commit(self._project_id)
            change = DataVersion()

            change.identify(element_id)
            change.add_change(name[1:], list_content)

            commit.add_change(change)

            self._connector.create_commit(self._project_id, commit.to_json())
            self.reload_project()

    def reload_project(self):
        """Reload of the project."""
        from ansys.sam.sysml2.builder.sysml2_project_builder import SysML2ProjectBuilder

        builder = SysML2ProjectBuilder(self._connector)
        builder.reload_project(self, self._project)

    def stop_observer(self):
        """Disconnect the observer."""
        self._working_observer = False

    def start_observer(self):
        """Connect the observer."""
        self._working_observer = True
