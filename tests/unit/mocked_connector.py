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

"""Mocked SysML2 API connector returning canned JSON from modeltestset/."""

import json
from pathlib import Path
from uuid import uuid4

from ansys.sam.sysml2.api.sysml2_api_connector import SysML2APIConnector
from ansys.sam.sysml2.exception.connector_exception import (
    ElementNotFoundException,
    ProjectAlreadyExistsException,
    ProjectNotFoundException,
)

MODELTESTSET = Path(__file__).resolve().parent / "modeltestset"


class MockedSysML2APIConnector(SysML2APIConnector):
    """Returns canned JSON responses from modeltestset/ fixtures."""

    def __init__(self):
        super().__init__()
        self._projects = {}
        for project_dir in sorted(MODELTESTSET.iterdir()):
            project_file = project_dir / "project.json"
            if project_file.exists():
                data = json.loads(project_file.read_text(encoding="utf-8"))
                self._projects[data["@id"]] = data

    def _load_elements(self, project_id: str) -> list:
        elements_file = MODELTESTSET / f"project_{project_id}" / "elements.json"
        if not elements_file.exists():
            raise ProjectNotFoundException(f"Project {project_id} not found")
        return json.loads(elements_file.read_text(encoding="utf-8"))

    def get_projects(self) -> list:
        """Get all projects."""
        return list(self._projects.values())

    def get_project_by_id(self, project_id: str) -> dict:
        """Get project by ID."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        return self._projects[project_id].copy()

    def create_project(
        self,
        project_name: str,
        project_description: str = "Project description",
    ) -> dict:
        """Create a new project."""
        for p in self._projects.values():
            if p["name"] == project_name:
                raise ProjectAlreadyExistsException(
                    "A project with this name already exists in this space."
                )
        new_id = str(uuid4())
        project = {
            "@type": "Project",
            "@id": new_id,
            "name": project_name,
            "description": project_description,
            "defaultBranch": {"@id": "defaultBranch"},
        }
        self._projects[new_id] = project
        return project

    def delete_project(self, project_id: str) -> dict:
        """Delete a project."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        self._projects.pop(project_id)
        return {"@type": "Project", "@id": project_id}

    def update_project(
        self,
        project_id: str,
        project_name: str = None,
        project_description: str = None,
    ) -> dict:
        """Update a project."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        project = self._projects[project_id]
        if project_name is not None:
            project["name"] = project_name
        if project_description is not None:
            project["description"] = project_description
        return project.copy()

    def get_all_elements(self, project_id: str) -> list:
        """Get all elements of a project."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        return self._load_elements(project_id)

    def get_element_by_id(self, project_id: str, element_id: str) -> dict:
        """Get a single element by ID."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        elements = self._load_elements(project_id)
        for el in elements:
            if el.get("@id") == element_id:
                return el
        raise ElementNotFoundException(
            f"Element {element_id} not found in project {project_id}"
        )

    def get_root_elements(self, project_id: str) -> list:
        """Get root elements."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        elements = self._load_elements(project_id)
        return [el for el in elements if el.get("owner") is None]

    def execute_query(self, project_id: str, query: str) -> dict:
        """Return all elements."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        return self._load_elements(project_id)

    def create_commit(self, project_id: str, commit: str) -> dict:
        """Return a realistic CommitDto response."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        return {
            "@type": "Commit",
            "owningProject": {"@id": project_id},
            "timestamp": 0,
        }
