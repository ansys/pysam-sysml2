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
"""Factory class to create new elements."""

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.dto.commit.commit_class import Commit
from ansys.sam.sysml2.dto.commit.data_version import DataVersion


class Factory:
    """Provides the Python factory class for creating new SysML elements."""

    _project_id: str
    _project: Project
    _conn: AnsysSysML2APIConnector

    def __init__(self, project: Project, conn: AnsysSysML2APIConnector) -> None:
        """Initialize a new instance."""
        self._project_id = project._id
        self._project = project
        self._conn = conn

    def create_element(self, element_type: str, **kwargs):
        """Create a new element in the model and return it.

        Parameters
        ----------
        element_type : str
            Type of the element.
        kwargs : Any
            Other parameters of the new element.

        Returns
        -------
        SysMLElement
            Created element.
        """
        existing_elements = set(self._project._env.keys())
        commit = Commit(self._project_id)
        change = DataVersion()

        change.add_change("@type", element_type)

        if "owner" in kwargs:
            change.add_change("owner", kwargs["owner"])

        for key, value in kwargs.items():
            if key != "owner":
                change.add_change(key, value)

        commit.add_change(change)

        self._conn.create_commit(self._project_id, commit.to_json())
        self._reload_project()

        element = self._extract_created_element(element_type, existing_elements)
        if "value" in kwargs.keys():
            element.set_value(kwargs.get("value"))
        elif "expression" in kwargs.keys():
            element.parse_and_set_value(kwargs.get("expression"))
        return element

    def _extract_created_element(self, element_type: str, existing_elements: set):
        """Extract the newly created element.

        Parameters
        ----------
        element_type : str
            Type of the element.
        existing_elements : set
            Elements contained in the project environment.

        Returns
        -------
        SysMLElement
            Created element.
        """
        from ansys.sam.sysml2.tools import SysMLTools

        diff_elements = set(self._project._env.keys()).difference(existing_elements)

        new_elements_ids = list(
            x for x in diff_elements if SysMLTools.isinstance(self._project._env[x], element_type)
        )

        if len(new_elements_ids) > 1:
            raise ValueError("Too many elements of this type found on reload")

        return self._project._env[new_elements_ids[0]]

    def _reload_project(self):
        """Reload the project."""
        from ansys.sam.sysml2.builder.sysml2_project_builder import SysML2ProjectBuilder

        builder = SysML2ProjectBuilder(self._conn)
        observer = self._project.get_root_package()._observer
        builder.reload_project(observer, self._project)
