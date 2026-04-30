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

"""E2E tests for project CRUD operations against a real SAM product instance."""

import uuid

import pytest

from ansys.sam.sysml2.exception.connector_exception import (
    ProjectAlreadyExistsException,
    ProjectNotFoundException,
)


@pytest.fixture
def unique_project_name():
    return f"e2e-test-{uuid.uuid4().hex[:8]}"


@pytest.fixture
def created_project(connector, unique_project_name):
    """Create a project and clean it up after the test."""
    project = connector.create_project(unique_project_name, "E2E test project")
    yield project
    try:
        connector.delete_project(project["@id"])
    except ProjectNotFoundException:
        pass


@pytest.mark.e2e
class TestProjectCRUD:

    def test_create_project(self, created_project, unique_project_name):
        assert created_project["name"] == unique_project_name
        assert "@id" in created_project

    def test_create_duplicate_project(self, connector, created_project):
        with pytest.raises(ProjectAlreadyExistsException):
            connector.create_project(created_project["name"])

    def test_get_projects(self, connector, created_project):
        projects = connector.get_projects()
        assert isinstance(projects, list)
        assert any(p["@id"] == created_project["@id"] for p in projects)

    def test_get_project_by_id(self, connector, created_project):
        project = connector.get_project_by_id(created_project["@id"])
        assert project["@id"] == created_project["@id"]
        assert project["name"] == created_project["name"]

    def test_get_project_not_found(self, connector):
        with pytest.raises(ProjectNotFoundException):
            connector.get_project_by_id("non-existent-id")

    def test_update_project(self, connector, created_project):
        result = connector.update_project(
            created_project["@id"],
            project_name="UpdatedName",
            project_description="UpdatedDesc",
        )
        assert result["@id"] == created_project["@id"]
        assert result["name"] == "UpdatedName"
        assert result["description"] == "UpdatedDesc"

    def test_update_project_not_found(self, connector):
        with pytest.raises(ProjectNotFoundException):
            connector.update_project("non-existent-id", project_name="Name")

    def test_delete_project(self, connector, unique_project_name):
        project = connector.create_project(
            f"delete-{unique_project_name}", "to be deleted"
        )
        project_id = project["@id"]
        result = connector.delete_project(project_id)
        assert result["@id"] == project_id

        with pytest.raises(ProjectNotFoundException):
            connector.get_project_by_id(project_id)

    def test_delete_project_not_found(self, connector):
        with pytest.raises(ProjectNotFoundException):
            connector.delete_project("non-existent-id")
