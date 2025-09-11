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

import json
from pathlib import Path

import pytest

from ansys.sam.sysml2 import SysML2ProjectManager
from ansys.sam.sysml2.exception.connector_exception import (
    BadRequestConnectionException,
    DiagramNotAvailableException,
)
from ansys.sam.sysml2.tools.ansys_sysml2_project import AnsysSysML2Project
from conftest import tmp_dir
from mocked_server.routes.const import PROJECT_ID_2, PROJECT_ID_5, VALID_ORGANIZATION, VALID_TOKEN
from parent_test_class import ParentTestClass
from mocked_server.mocked_server import MockedServer


def get_diagrams(element):
    return element.__diagram


dl_path = tmp_dir / "images"


class TestAnsysSysml2Project(ParentTestClass):

    @pytest.fixture
    def ansyssysml2project_5(self) -> AnsysSysML2Project:
        project = AnsysSysML2Project(
            server_url=MockedServer.get_url(),
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
            use_ssl=False,
            project_id=PROJECT_ID_5,
        )
        return project

    def test_create_element(self, ansyssysml2project_5: SysML2ProjectManager):

        project_root = ansyssysml2project_5.get_root_package()
        new_attribute = ansyssysml2project_5.create_element(
            element_type="AttributeUsage", name="new_attribute", owner=project_root
        )

        assert project_root.new_attribute._name == "new_attribute"

        new_attribute._name = "NewAttr"

        assert project_root.NewAttr._name == "NewAttr"

        with pytest.raises(AttributeError):
            project_root.new_attribute

    def test_create_element_with_no_type(self, ansyssysml2project_5: SysML2ProjectManager):

        with pytest.raises(BadRequestConnectionException) as exception:
            ansyssysml2project_5.create_element(element_type=None, name="new_attribute")
        assert "Bad Request : No Type for New Element" == exception.value.args[0]

    def test_working_dowload_diagram_in_png(self, ansyssysml2project_5: SysML2ProjectManager):
        package = ansyssysml2project_5.get_root_package()

        expected_file_format = "png"
        expected_filename = f"ae11d5ed-0f61-44a1-b4a7-f727d5bddccd.{expected_file_format}"
        expected_file_path = dl_path / expected_filename

        assert ansyssysml2project_5.is_diagrams_available() == True

        diagram = get_diagrams(package)[0]
        response = ansyssysml2project_5.download_diagram(
            diagram_id=diagram._id, file_format=expected_file_format, path=dl_path
        )

        response_path = Path(response)

        assert response_path == expected_file_path
        assert expected_file_path.exists()
        assert response_path.name == expected_filename

    def test_download_all_diagrams_without_args(self, ansyssysml2project_5: SysML2ProjectManager):
        expected_file_format = "svg"
        expected_filename = f"{ansyssysml2project_5._id}_{expected_file_format}_diagrams.zip"
        expected_file_path = dl_path / expected_filename

        assert ansyssysml2project_5.is_diagrams_available() == True

        response = ansyssysml2project_5.download_all_diagrams(path=dl_path)

        response_path = Path(response)

        assert response_path == expected_file_path
        assert expected_file_path.exists()
        assert response_path.name == expected_filename

        with open(expected_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        expected_data = {
            "success": 200,
            "project_id": PROJECT_ID_5,
            "number_diagrams": 2,
            "file_format": expected_file_format,
        }

        assert data == expected_data

    def test_get_diagrams_info(self, ansyssysml2project_5: SysML2ProjectManager):
        diagrams_info = ansyssysml2project_5.get_project_diagrams_info()

        expected_diagrams = [
            {"name": "Bike", "numberOfElements": 22, "kind": "SimpleDiagram"},
            {"name": "myBikeInheritance", "numberOfElements": 3, "kind": "SimpleDiagram"},
            {"name": "myBikeRedef", "numberOfElements": 5, "kind": "SimpleDiagram"},
            {"name": "Redef & inheritance", "numberOfElements": 12, "kind": "SimpleDiagram"},
        ]

        assert len(diagrams_info) == len(expected_diagrams)

        for i, expected in enumerate(expected_diagrams):
            actual = diagrams_info[i]
            assert actual["name"] == expected["name"]
            assert actual["numberOfElements"] == expected["numberOfElements"]
            assert actual["kind"] == expected["kind"]

    def test_get_single_diagram_info(self, ansyssysml2project_5: SysML2ProjectManager):
        diagram_id = "85f84746-3bbc-4b65-8b9c-503d736655eb"

        diagram_info = ansyssysml2project_5.get_single_diagram_info(diagram_id)

        assert isinstance(diagram_info, dict), "Single diagram info should be a dictionary"

        expected_data = {
            "projectId": "dd2e4b9b-a290-4511-a892-aafd0ede597a",
            "diagramId": "85f84746-3bbc-4b65-8b9c-503d736655eb",
            "name": "Bike",
            "kind": "SimpleDiagram",
            "numberOfElements": 0,
        }

        assert diagram_info["projectId"] == expected_data["projectId"]
        assert diagram_info["diagramId"] == expected_data["diagramId"]
        assert diagram_info["name"] == expected_data["name"]
        assert diagram_info["kind"] == expected_data["kind"]
        assert diagram_info["numberOfElements"] == expected_data["numberOfElements"]

    def test_no_diagrams_found_in_project(self):
        project = AnsysSysML2Project(
            server_url=MockedServer.get_url(),
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
            use_ssl=False,
            project_id=PROJECT_ID_2,
        )

        assert project.is_diagrams_available() == False

        with pytest.raises(DiagramNotAvailableException):
            project.download_all_diagrams(path=dl_path)

        with pytest.raises(DiagramNotAvailableException):
            project.download_diagram(path=dl_path, diagram_id="unknown")

        with pytest.raises(DiagramNotAvailableException):
            project.get_project_diagrams_info()

        with pytest.raises(DiagramNotAvailableException):
            project.get_single_diagram_info(diagram_id="unknown")
