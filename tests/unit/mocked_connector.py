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


_DERIVED_ELEMENT_KEYS = frozenset(
    {
        "ownedElement",
        "ownedMembership",
        "ownedMember",
        "ownedImport",
        "ownedAnnotation",
        "documentation",
        "ownedFeature",
        "ownedFeatureMembership",
        "feature",
        "featureMembership",
        "inheritedFeature",
        "inheritedMembership",
        "inheritedMembershipExcludeImplied",
        "ownedSpecialization",
        "ownedTyping",
        "ownedSubsetting",
        "ownedRedefinition",
        "chainingFeature",
        "type",
        "definition",
        "attributeDefinition",
        "partDefinition",
        "itemDefinition",
        "portDefinition",
        "occurrenceDefinition",
        "actionDefinition",
        "allocationDefinition",
        "connectionDefinition",
        "stateDefinition",
        "flowDefinition",
        "interfaceDefinition",
        "enumerationDefinition",
        "requirementDefinition",
        "constraintDefinition",
        "calculationDefinition",
        "caseDefinition",
        "analysisCaseDefinition",
        "verificationCaseDefinition",
        "useCaseDefinition",
        "concernDefinition",
        "viewpointDefinition",
        "viewDefinition",
        "renderingDefinition",
        "metadataDefinition",
    }
)


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

    @staticmethod
    def _strip_derived_properties(elements: list) -> list:
        stripped = []
        for element in elements:
            cleaned = {
                key: value
                for key, value in element.items()
                if key not in _DERIVED_ELEMENT_KEYS
            }
            stripped.append(cleaned)
        return stripped

    def _load_library_elements(self, project_id: str) -> list:
        lib_file = MODELTESTSET / f"project_{project_id}" / "library_elements.json"
        if not lib_file.exists():
            return []
        return json.loads(lib_file.read_text(encoding="utf-8"))

    def _extract_ids(self, query: dict) -> set:
        """Collect every value whose constraint targets the ``@id`` property."""
        ids: set = set()
        if isinstance(query, dict):
            if query.get("property") == "@id" and "value" in query:
                ids.add(query["value"])
            for value in query.values():
                ids |= self._extract_ids(value)
        elif isinstance(query, list):
            for item in query:
                ids |= self._extract_ids(item)
        return ids

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

    def get_all_elements(self, project_id: str, **kwargs) -> list:
        """Get all elements of a project."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        elements = self._load_elements(project_id)
        if not kwargs.get("includes_derived", True):
            elements = self._strip_derived_properties(elements)
        return elements

    def get_element_by_id(self, project_id: str, element_id: str) -> dict:
        """Get a single element by ID."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        elements = self._load_elements(project_id) + self._load_library_elements(project_id)
        for el in elements:
            if el.get("@id") == element_id:
                return el
        raise ElementNotFoundException(
            f"Element {element_id} not found in project {project_id}"
        )

    def get_root_elements(self, project_id: str) -> list:
        """Get the root Namespace, its owned members, and the root imports."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        elements = self._load_elements(project_id)
        by_id = {element["@id"]: element for element in elements}
        roots = {}
        for element in elements:
            if element.get("owner") is not None:
                continue
            if element.get("@type") == "Namespace":
                roots[element["@id"]] = element
                for ref in element.get("ownedMember", []):
                    if ref["@id"] in by_id:
                        roots[ref["@id"]] = by_id[ref["@id"]]
            elif element.get("@type") == "NamespaceImport":
                roots[element["@id"]] = element
        return list(roots.values())

    def execute_query(self, project_id: str, query: str) -> dict:
        """Return the library elements matching the query's @id constraints."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        wanted = self._extract_ids(json.loads(query))
        return [el for el in self._load_library_elements(project_id) if el.get("@id") in wanted]

    def create_commit(self, project_id: str, commit: str) -> dict:
        """Return a realistic CommitDto response."""
        if project_id not in self._projects:
            raise ProjectNotFoundException(f"Project {project_id} not found")
        return {
            "@type": "Commit",
            "owningProject": {"@id": project_id},
            "timestamp": 0,
        }
