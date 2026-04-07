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

import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.exception.connector_exception import ProjectNotFoundException
from conftest import restore_projects_backup_between_tests
from mocked_server.routes.const import PROJECT_ID_1
from parent_test_class import ParentTestClass


class TestSysML2ProjectManager(ParentTestClass):

    @pytest.fixture(scope="function", autouse=True)
    def restore_jsons(self):
        restore_projects_backup_between_tests()

    def test_load_project(self, valid_source: AnsysSysML2APIConnector):
        manager = SysML2ProjectManager(valid_source)
        project = manager.get_scripting_project("1")
        assert len(project.get_root()) == 1
        assert project.get_root()[0]._name == "PySAMSysML2TestProject-COMPLET"

    def test_get_projects(self, valid_source: AnsysSysML2APIConnector):
        manager = SysML2ProjectManager(valid_source)
        projects = manager.get_projects()
        assert projects is not None
        assert isinstance(projects, list)
        assert len(projects) > 0

    def test_delete_project(self, valid_source: AnsysSysML2APIConnector):
        manager = SysML2ProjectManager(valid_source)
        manager.get_scripting_project(PROJECT_ID_1)
        assert PROJECT_ID_1 in manager._constructed_project

        result = manager.delete_project(PROJECT_ID_1)
        assert result is not None
        assert result["@id"] == PROJECT_ID_1
        assert PROJECT_ID_1 not in manager._constructed_project

    def test_delete_project_not_found(self, valid_source: AnsysSysML2APIConnector):
        manager = SysML2ProjectManager(valid_source)
        with pytest.raises(ProjectNotFoundException):
            manager.delete_project("non_existent_id")

    def test_update_project(self, valid_source: AnsysSysML2APIConnector):
        manager = SysML2ProjectManager(valid_source)
        manager.get_scripting_project(PROJECT_ID_1)
        assert PROJECT_ID_1 in manager._constructed_project

        result = manager.update_project(
            PROJECT_ID_1, name="NewName", description="NewDesc"
        )
        assert result is not None
        assert result["@id"] == PROJECT_ID_1
        assert result["name"] == "NewName"
        assert result["description"] == "NewDesc"
        assert PROJECT_ID_1 not in manager._constructed_project

    def test_update_project_not_found(self, valid_source: AnsysSysML2APIConnector):
        manager = SysML2ProjectManager(valid_source)
        with pytest.raises(ProjectNotFoundException):
            manager.update_project("non_existent_id", name="NewName")
