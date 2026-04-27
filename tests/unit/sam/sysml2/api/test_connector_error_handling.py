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

"""Tests for HTTP status code error handling in the connector."""

import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.exception.connector_exception import (
    BadRequestConnectionException,
    ConnectorConnectionException,
    ElementNotFoundException,
    HTTPResponseException,
    InvalidElementJsonFoundException,
    ProjectAlreadyExistsException,
    ProjectNotFoundException,
    UnauthorizedConnectionException,
)
from tests.unit.const import VALID_ORGANIZATION, VALID_TOKEN


class _MockResponse:
    """Minimal mock HTTP response."""

    def __init__(self, status_code, content=b"", json_data=None):
        self.status_code = status_code
        self.content = content
        self._json_data = json_data

    def json(self):
        if self._json_data is not None:
            return self._json_data
        raise ValueError("No JSON")


@pytest.fixture
def connector():
    return AnsysSysML2APIConnector(
        server_url="http://fake-server",
        organization_id=VALID_ORGANIZATION,
        token=VALID_TOKEN,
        use_ssl=False,
    )


class TestConnectorErrorHandling:

    def test_get_project_200_returns_json(self, connector, mocker):
        mocker.patch(
            "requests.get",
            return_value=_MockResponse(200, content=b'{"@id": "1", "name": "P"}'),
        )
        result = connector.get_project_by_id("1")
        assert result["@id"] == "1"

    def test_get_project_200_invalid_json(self, connector, mocker):
        mocker.patch(
            "requests.get",
            return_value=_MockResponse(200, content=b"not json"),
        )
        with pytest.raises(InvalidElementJsonFoundException):
            connector.get_project_by_id("1")

    def test_get_project_401(self, connector, mocker):
        mocker.patch(
            "requests.get",
            return_value=_MockResponse(401),
        )
        with pytest.raises(UnauthorizedConnectionException):
            connector.get_project_by_id("1")

    def test_get_project_403(self, connector, mocker):
        mocker.patch(
            "requests.get",
            return_value=_MockResponse(
                403,
                json_data={
                    "message": "Accessing the resource you were trying to reach is forbidden"
                },
            ),
        )
        with pytest.raises(ConnectorConnectionException):
            connector.get_project_by_id("1")

    def test_get_project_404_project(self, connector, mocker):
        mocker.patch(
            "requests.get",
            return_value=_MockResponse(
                404, json_data={"message": "Project X not found"}
            ),
        )
        with pytest.raises(ProjectNotFoundException):
            connector.get_project_by_id("X")

    def test_get_element_404_element(self, connector, mocker):
        mocker.patch(
            "requests.get",
            return_value=_MockResponse(
                404,
                json_data={"message": "Element X not found in project Y"},
            ),
        )
        with pytest.raises(ElementNotFoundException):
            connector.get_element_by_id("Y", "X")

    def test_get_project_404_organization(self, connector, mocker):
        mocker.patch(
            "requests.get",
            return_value=_MockResponse(
                404, json_data={"message": "Organization Z not found"}
            ),
        )
        with pytest.raises(ConnectorConnectionException):
            connector.get_project_by_id("1")

    def test_create_project_409(self, connector, mocker):
        mocker.patch(
            "requests.post",
            return_value=_MockResponse(
                409,
                json_data={
                    "message": "A project with this name already exists in this space."
                },
            ),
        )
        with pytest.raises(ProjectAlreadyExistsException):
            connector.create_project("duplicate")

    def test_commit_400(self, connector, mocker):
        mocker.patch(
            "requests.post",
            return_value=_MockResponse(
                400, json_data={"message": "Change can't be empty"}
            ),
        )
        with pytest.raises(BadRequestConnectionException):
            connector.create_commit("1", '{"@type": "Commit", "change": []}')

    def test_get_project_500(self, connector, mocker):
        mocker.patch(
            "requests.get",
            return_value=_MockResponse(500),
        )
        with pytest.raises(ConnectorConnectionException, match="Internal Server Error"):
            connector.get_project_by_id("1")

    def test_get_project_unknown_status(self, connector, mocker):
        mocker.patch(
            "requests.get",
            return_value=_MockResponse(418),
        )
        with pytest.raises(HTTPResponseException):
            connector.get_project_by_id("1")

    def test_connection_error(self, connector, mocker):
        mocker.patch(
            "requests.get",
            side_effect=ConnectionError("Connection refused"),
        )
        with pytest.raises(ConnectorConnectionException):
            connector.get_project_by_id("1")
