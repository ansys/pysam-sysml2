# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
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

from ansys.sam.sysml2 import ConnectorFactory
from ansys.sam.sysml2.connector.sysml_connector import SysMLConnector
from ansys.sam.sysml2.exception.connector_exception import (
    ElementNotFoundException,
    ProjectNotFoundException,
)
from mocked_server.mocked_server import MockedServer
from mocked_server.routes.const import (
    PROJECT_1_ATTR_ID,
    PROJECT_1_PART_ID,
    PROJECT_ID_1,
    PROJECT_ID_2,
    VALID_ORGANIZATION,
    VALID_TOKEN,
)


class TestEndPointSysMLConnector:

    RANDOM_PROJECT_ID = "Tim"
    RANDOM_ELEMENT_ID = "Oleon"

    @pytest.fixture
    def valid_source(self) -> SysMLConnector:
        return ConnectorFactory.create_ansys_sysml_connector(
            server_url=MockedServer.get_url(), organization_id=VALID_ORGANIZATION, token=VALID_TOKEN
        )

    def test_get_project_data(self, valid_source: SysMLConnector):
        project_data = valid_source.get_project_data(PROJECT_ID_1)
        assert project_data is not None
        assert "elements" in project_data
        assert project_data["@id"] == PROJECT_ID_1

    def test_get_projects(self, valid_source: SysMLConnector):
        projects = valid_source.get_projects()
        assert projects is not None
        assert type(projects) == list
        assert len(projects) > 0
        assert all(type(project) == dict for project in projects)

    def test_get_project(self, valid_source: SysMLConnector):
        project_1 = valid_source.get_project(PROJECT_ID_1)
        project_2 = valid_source.get_project(PROJECT_ID_2)

        assert project_1 is not None and project_2 is not None
        assert project_1["@id"] == PROJECT_ID_1
        assert project_2["@id"] == PROJECT_ID_2
        assert project_1["@id"] != project_2["@id"]

    def test_get_not_found_project(self, valid_source: SysMLConnector):
        with pytest.raises(ProjectNotFoundException):
            valid_source.get_project(TestEndPointSysMLConnector.RANDOM_PROJECT_ID)

    def test_get_elements(self, valid_source: SysMLConnector):
        elements = valid_source.get_elements(PROJECT_ID_1)

        assert elements is not None
        assert len(elements) > 0
        assert all(type(element) == dict for element in elements)

    def test_get_elements_invalid_project(self, valid_source: SysMLConnector):
        with pytest.raises(ProjectNotFoundException):
            valid_source.get_elements(TestEndPointSysMLConnector.RANDOM_PROJECT_ID)

    def test_get_element(self, valid_source: SysMLConnector):
        partUsageElement = valid_source.get_element(PROJECT_ID_1, PROJECT_1_PART_ID)

        assert partUsageElement is not None
        assert partUsageElement["@type"] == "PartUsage"

        attributeUsageElement = valid_source.get_element(PROJECT_ID_1, PROJECT_1_ATTR_ID)
        assert attributeUsageElement is not None
        assert attributeUsageElement["@type"] == "AttributeUsage"

    def test_get_element_invalid_id(self, valid_source: SysMLConnector):
        with pytest.raises(ElementNotFoundException):
            valid_source.get_element(PROJECT_ID_1, TestEndPointSysMLConnector.RANDOM_ELEMENT_ID)

    def test_get_element_invalid_project(self, valid_source: SysMLConnector):
        with pytest.raises(ElementNotFoundException):
            valid_source.get_element(
                TestEndPointSysMLConnector.RANDOM_PROJECT_ID, PROJECT_1_PART_ID
            )
