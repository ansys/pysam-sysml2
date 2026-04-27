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

"""Unit tests for SysML2ProjectManager using the mocked connector."""

import pytest

from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.classes.scripting_project import ScriptingProject
from ansys.sam.sysml2.exception.connector_exception import (
    ConnectorConnectionException,
    ProjectAlreadyExistsException,
    ProjectNotFoundException,
)
from tests.unit.const import PROJECT_ID_1


class TestSysML2ProjectManagerScripting:

    def test_get_projects(self, connector):
        manager = SysML2ProjectManager(connector)
        projects = manager.get_projects()
        assert isinstance(projects, list)
        assert len(projects) > 0

    def test_get_scripting_project(self, connector):
        manager = SysML2ProjectManager(connector)
        project = manager.get_scripting_project(PROJECT_ID_1)
        assert len(project.get_root()) == 1
        assert project.get_root()[0]._name == "PySAMSysML2TestProject-COMPLET"

    def test_get_scripting_project_cached(self, connector):
        manager = SysML2ProjectManager(connector)
        project_1 = manager.get_scripting_project(PROJECT_ID_1)
        project_2 = manager.get_scripting_project(PROJECT_ID_1)
        assert project_1 is project_2

    def test_create_scripting_project_duplicate(self, connector):
        manager = SysML2ProjectManager(connector)
        with pytest.raises(ProjectAlreadyExistsException):
            manager.create_scripting_project("PySAMSysML2TestProject-COMPLET")

    def test_delete_project(self, connector):
        manager = SysML2ProjectManager(connector)
        manager.get_scripting_project(PROJECT_ID_1)
        assert PROJECT_ID_1 in manager._scripting_projects

        result = manager.delete_project(PROJECT_ID_1)
        assert result["@id"] == PROJECT_ID_1
        assert PROJECT_ID_1 not in manager._scripting_projects

    def test_delete_project_not_found(self, connector):
        manager = SysML2ProjectManager(connector)
        with pytest.raises(ProjectNotFoundException):
            manager.delete_project("non_existent_id")

    def test_update_project(self, connector):
        manager = SysML2ProjectManager(connector)
        manager.get_scripting_project(PROJECT_ID_1)
        assert PROJECT_ID_1 in manager._scripting_projects

        result = manager.update_project(
            PROJECT_ID_1, name="NewName", description="NewDesc"
        )
        assert result["@id"] == PROJECT_ID_1
        assert result["name"] == "NewName"
        assert result["description"] == "NewDesc"
        assert PROJECT_ID_1 not in manager._scripting_projects

    def test_update_project_not_found(self, connector):
        manager = SysML2ProjectManager(connector)
        with pytest.raises(ProjectNotFoundException):
            manager.update_project("non_existent_id", name="NewName")


class TestSysML2ProjectManagerSysML:

    def test_get_sysml_project(self, connector):
        manager = SysML2ProjectManager(connector)
        project = manager.get_sysml_project(PROJECT_ID_1)
        assert isinstance(project, Project)
        assert len(project.get_root()) == 1
        assert project.get_root()[0].name == "PySAMSysML2TestProject-COMPLET"

    def test_get_sysml_project_cached(self, connector):
        manager = SysML2ProjectManager(connector)
        project_1 = manager.get_sysml_project(PROJECT_ID_1)
        project_2 = manager.get_sysml_project(PROJECT_ID_1)
        assert project_1 is project_2

    def test_create_sysml_project_duplicate(self, connector):
        manager = SysML2ProjectManager(connector)
        with pytest.raises(ProjectAlreadyExistsException):
            manager.create_sysml_project("PySAMSysML2TestProject-COMPLET")


class TestSysML2ProjectManagerEdgeCases:

    def test_dual_mode_cache_override(self, connector):
        """Loading same project as scripting then sysml must return different types."""
        manager = SysML2ProjectManager(connector)
        scripting = manager.get_scripting_project(PROJECT_ID_1)
        sysml = manager.get_sysml_project(PROJECT_ID_1)
        assert isinstance(scripting, ScriptingProject)
        assert isinstance(sysml, Project)
        assert type(scripting) != type(sysml)

    def test_get_scripting_after_delete(self, connector):
        manager = SysML2ProjectManager(connector)
        manager.get_scripting_project(PROJECT_ID_1)
        manager.delete_project(PROJECT_ID_1)
        with pytest.raises(ProjectNotFoundException):
            manager.get_scripting_project(PROJECT_ID_1)

    def test_get_sysml_after_delete(self, connector):
        manager = SysML2ProjectManager(connector)
        manager.get_sysml_project(PROJECT_ID_1)
        manager.delete_project(PROJECT_ID_1)
        with pytest.raises(ProjectNotFoundException):
            manager.get_sysml_project(PROJECT_ID_1)

    def test_update_invalidates_cache(self, connector):
        """After update, the cached project is evicted and must be rebuilt."""
        manager = SysML2ProjectManager(connector)
        original = manager.get_scripting_project(PROJECT_ID_1)
        assert PROJECT_ID_1 in manager._scripting_projects
        manager.update_project(PROJECT_ID_1, name="UpdatedName")
        assert PROJECT_ID_1 not in manager._scripting_projects
        rebuilt = manager.get_scripting_project(PROJECT_ID_1)
        assert rebuilt is not original

    def test_update_project_failure_preserves_cache(self, connector, mocker):
        manager = SysML2ProjectManager(connector)
        manager.get_scripting_project(PROJECT_ID_1)
        assert PROJECT_ID_1 in manager._scripting_projects

        mocker.patch.object(
            connector,
            "update_project",
            side_effect=ProjectNotFoundException("Project not found"),
        )
        with pytest.raises(ProjectNotFoundException):
            manager.update_project(PROJECT_ID_1, name="NewName")
        assert PROJECT_ID_1 in manager._scripting_projects

    def test_delete_project_propagates_error(self, connector, mocker):
        manager = SysML2ProjectManager(connector)
        manager.get_scripting_project(PROJECT_ID_1)
        assert PROJECT_ID_1 in manager._scripting_projects

        mocker.patch.object(
            connector,
            "delete_project",
            side_effect=ProjectNotFoundException("Project not found"),
        )
        with pytest.raises(ProjectNotFoundException):
            manager.delete_project(PROJECT_ID_1)
        assert PROJECT_ID_1 in manager._scripting_projects

    def test_get_projects_connection_error(self, connector, mocker):
        mocker.patch.object(
            connector,
            "get_projects",
            side_effect=ConnectorConnectionException("Connection failed"),
        )
        manager = SysML2ProjectManager(connector)
        with pytest.raises(ConnectorConnectionException):
            manager.get_projects()
