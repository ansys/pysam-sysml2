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

# -*- coding: utf-8 -*-
"""
 Copyright (c) 2024 ANSYS, Inc.
 Unauthorized use, distribution, or duplication is prohibited.

File <test_ansys_sysml_source.py> created on Thu Nov 28 2024
"""

import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.dto.commit.commit_class import Commit
from ansys.sam.sysml2.dto.commit.data_version import DataVersion
from ansys.sam.sysml2.dto.query.constraints_classes import CompositeConstraint, PrimitiveConstraint
from ansys.sam.sysml2.dto.query.query_class import Query
from ansys.sam.sysml2.dto.query.query_enum import JoinOperator
from ansys.sam.sysml2.exception.connector_exception import (
    BadRequestConnectionException,
    ConnectorConnectionException,
    ElementNotFoundException,
    InvalidProjectNameException,
    ProjectNotFoundException,
)
from ansys.sam.sysml2.exception.query_exception import InvalidQuery
from mocked_server.mocked_server import MockedServer
from mocked_server.routes.const import (
    PROJECT_1_ATTR_ID,
    PROJECT_1_PART_ID,
    PROJECT_ID_1,
    PROJECT_ID_2,
    VALID_ORGANIZATION,
    VALID_TOKEN,
)


class TestSysML2APIConnector:

    RANDOM_PROJECT_ID = "Tim"
    RANDOM_ELEMENT_ID = "Oleon"

    @pytest.fixture
    def valid_source(self) -> AnsysSysML2APIConnector:
        return AnsysSysML2APIConnector(
            server_url=MockedServer.get_url(),
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
        )

    def test_create_project(self, valid_source: AnsysSysML2APIConnector):
        project_data = valid_source.create_project("newProjectName", "newProjectDescription")
        assert project_data is not None
        assert project_data["name"] == "newProjectName"
        assert project_data["description"] == "newProjectDescription"

    def test_create_unnamed_project(self, valid_source: AnsysSysML2APIConnector):
        with pytest.raises(InvalidProjectNameException):
            valid_source.create_project("")

    def test_get_projects(self, valid_source: AnsysSysML2APIConnector):
        projects = valid_source.get_projects()
        assert projects is not None
        assert isinstance(projects, list)
        assert len(projects) > 0
        assert all(isinstance(project, dict) for project in projects)

    def test_get_project(self, valid_source: AnsysSysML2APIConnector):
        project_1 = valid_source.get_project_by_id(PROJECT_ID_1)
        project_2 = valid_source.get_project_by_id(PROJECT_ID_2)

        assert project_1 is not None and project_2 is not None
        assert project_1["@id"] == PROJECT_ID_1
        assert project_2["@id"] == PROJECT_ID_2
        assert project_1["@id"] != project_2["@id"]

    def test_get_not_found_project(self, valid_source: AnsysSysML2APIConnector):
        with pytest.raises(ProjectNotFoundException):
            valid_source.get_project_by_id(TestSysML2APIConnector.RANDOM_PROJECT_ID)

    def test_get_elements(self, valid_source: AnsysSysML2APIConnector):
        elements = valid_source.get_all_elements(PROJECT_ID_1)

        assert elements is not None
        assert len(elements) > 0
        assert all(isinstance(element, dict) for element in elements)

    def test_get_elements_invalid_project(self, valid_source: AnsysSysML2APIConnector):
        with pytest.raises(ProjectNotFoundException):
            valid_source.get_all_elements(TestSysML2APIConnector.RANDOM_PROJECT_ID)

    def test_get_element(self, valid_source: AnsysSysML2APIConnector):
        part_usage_element = valid_source.get_element_by_id(PROJECT_ID_1, PROJECT_1_PART_ID)

        assert part_usage_element is not None
        assert part_usage_element["@type"] == "PartUsage"

        attribute_usage_element = valid_source.get_element_by_id(PROJECT_ID_1, PROJECT_1_ATTR_ID)
        assert attribute_usage_element is not None
        assert attribute_usage_element["@type"] == "AttributeUsage"

    def test_get_element_invalid_id(self, valid_source: AnsysSysML2APIConnector):
        with pytest.raises(ElementNotFoundException):
            valid_source.get_element_by_id(
                PROJECT_ID_1,
                TestSysML2APIConnector.RANDOM_ELEMENT_ID,
            )

    def test_get_element_invalid_project(self, valid_source: AnsysSysML2APIConnector):
        with pytest.raises(ProjectNotFoundException):
            valid_source.get_element_by_id(
                TestSysML2APIConnector.RANDOM_PROJECT_ID,
                PROJECT_1_PART_ID,
            )

    def test_get_root_elements(self, valid_source: AnsysSysML2APIConnector):
        roots = valid_source.get_root_elements(PROJECT_ID_1)

        assert roots is not None
        assert len(roots) == 1
        assert not any("owner" in element for element in roots)

    def test_get_root_elements_invalid_project(self, valid_source: AnsysSysML2APIConnector):
        with pytest.raises(ProjectNotFoundException):
            valid_source.get_root_elements(TestSysML2APIConnector.RANDOM_PROJECT_ID)

    def test_query_primitive_constraint_valid(self, valid_source: AnsysSysML2APIConnector):
        query = Query()
        query.where = PrimitiveConstraint("@id", PROJECT_1_PART_ID)

        result = valid_source.execute_query(PROJECT_ID_1, query.to_json())

        assert len(result) == 1
        assert result[0]["@id"] == PROJECT_1_PART_ID

    def test_query_composite_constraint_valid(self, valid_source: AnsysSysML2APIConnector):
        query = Query()
        pc_1 = PrimitiveConstraint("@id", PROJECT_1_PART_ID)
        pc_2 = PrimitiveConstraint("@id", PROJECT_1_ATTR_ID)
        cc = CompositeConstraint(operator=JoinOperator.OR)
        cc.constraint.append(pc_1)
        cc.constraint.append(pc_2)
        query.where = cc

        result = valid_source.execute_query(PROJECT_ID_1, query.to_json())

        assert len(result) == 2
        assert any(x["@id"] == PROJECT_1_ATTR_ID for x in result)
        assert any(x["@id"] == PROJECT_1_PART_ID for x in result)

    def test_query_primitive_constraint_invalid(self, valid_source: AnsysSysML2APIConnector):
        query = Query()
        query.where = PrimitiveConstraint("NoSysMLMethod", "value")

        with pytest.raises(ConnectorConnectionException):
            valid_source.execute_query(PROJECT_ID_1, query.to_json())

    def test_query_composite_constraint_invalid_count(self, valid_source: AnsysSysML2APIConnector):
        query = Query()
        pc_1 = PrimitiveConstraint("@id", PROJECT_1_PART_ID)
        cc = CompositeConstraint(operator=JoinOperator.OR)
        cc.constraint.append(pc_1)
        query.where = cc

        with pytest.raises(InvalidQuery):
            valid_source.execute_query(PROJECT_ID_1, query.to_json())

    def test_create_commit_successfull(self, valid_source: AnsysSysML2APIConnector):
        commit = Commit(PROJECT_ID_1)
        change = DataVersion()
        change.identify("61ac5435-8537-4f46-aec7-43636dcbb36f")
        change.add_change("name", "NewAttribute")
        commit.add_change(change)

        response = valid_source.create_commit(PROJECT_ID_1, commit.to_json())
        assert response.get("message") == "Commit Successful"

    def test_create_commit_with_invalid_identity(self, valid_source: AnsysSysML2APIConnector):
        commit = Commit(PROJECT_ID_1)
        change = DataVersion()
        change.identify("12345678-1234-1234-1234-123456789012")
        change.add_change("name", "NewAttribute")
        commit.add_change(change)

        with pytest.raises(BadRequestConnectionException) as exception:
            valid_source.create_commit(PROJECT_ID_1, commit.to_json())
        assert "Bad Request : Invalid Identity Id" == exception.value.args[0]

    def test_create_commit_with_missing_type(self, valid_source: AnsysSysML2APIConnector):
        commit = Commit(PROJECT_ID_1)
        change = DataVersion()
        change.add_change("@type", None)
        commit.add_change(change)

        with pytest.raises(BadRequestConnectionException) as exception:
            valid_source.create_commit(PROJECT_ID_1, commit.to_json())
        assert "Bad Request : No Type for New Element" == exception.value.args[0]

    def test_create_commit_with_missing_payload(self, valid_source: AnsysSysML2APIConnector):
        commit = Commit(PROJECT_ID_1)
        change = DataVersion()
        commit.add_change(change)

        with pytest.raises(BadRequestConnectionException) as exception:
            valid_source.create_commit(PROJECT_ID_1, commit.to_json())
        assert "Bad Request : Invalid change data" == exception.value.args[0]

    def test_create_commit_with_missing_dataversion(self, valid_source: AnsysSysML2APIConnector):
        commit = Commit(PROJECT_ID_1)

        with pytest.raises(BadRequestConnectionException) as exception:
            valid_source.create_commit(PROJECT_ID_1, commit.to_json())
        assert "Bad Request : Change can't be empty" == exception.value.args[0]

    def test_create_commit_with_invalid_key(self, valid_source: AnsysSysML2APIConnector):
        commit = Commit(PROJECT_ID_1)
        change = DataVersion()
        change.identify("61ac5435-8537-4f46-aec7-43636dcbb36f")
        invalid_key = "zadazdazd"
        change.add_change(invalid_key, "NewAttribute")
        commit.add_change(change)

        with pytest.raises(BadRequestConnectionException) as exception:
            valid_source.create_commit(PROJECT_ID_1, commit.to_json())
        assert f"Bad Request : Element: Invalid {invalid_key}" == exception.value.args[0]

    def test_create_commit_with_invalid_type(self, valid_source: AnsysSysML2APIConnector):
        commit = Commit(PROJECT_ID_1)
        change = DataVersion()
        change.identify("61ac5435-8537-4f46-aec7-43636dcbb36f")
        key = "name"
        change.add_change(key, ["NewAttribute"])
        commit.add_change(change)

        with pytest.raises(BadRequestConnectionException) as exception:
            valid_source.create_commit(PROJECT_ID_1, commit.to_json())
        assert f"Bad Request : Element: Invalid Type for {key}" == exception.value.args[0]
