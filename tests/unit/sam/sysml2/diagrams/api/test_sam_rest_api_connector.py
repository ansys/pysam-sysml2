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

"""Unit tests for SamRestApiConnector using MockedSamApiConnector + mocker."""

import pytest

from ansys.sam.sysml2.diagrams.api.sam_rest_api_connector import SamRestApiConnector
from ansys.sam.sysml2.exception.connector_exception import ConnectorConnectionException
from tests.unit.const import PROJECT_ID_5, VALID_TOKEN


class TestSamRestApiConnectorMocked:
    """Tests using the mocked SAM API connector."""

    def test_get_project_data(self, sam_connector):
        data = sam_connector.get_project_data(PROJECT_ID_5)
        assert len(data) > 0
        assert "eClass" in data

    def test_get_diagrams_info(self, sam_connector):
        diagrams_info = sam_connector.get_diagrams_info(PROJECT_ID_5)
        assert len(diagrams_info) == 4
        assert diagrams_info[0]["name"] == "Bike"

    def test_get_single_diagram_info(self, sam_connector):
        diagram_id = "85f84746-3bbc-4b65-8b9c-503d736655eb"
        info = sam_connector.get_single_diagram_info(PROJECT_ID_5, diagram_id)
        assert isinstance(info, dict)
        assert info["name"] == "Bike"
        assert info["diagramId"] == diagram_id

    def test_get_single_diagram_info_unknown(self, sam_connector):
        with pytest.raises(ConnectorConnectionException):
            sam_connector.get_single_diagram_info(PROJECT_ID_5, "unknown")


class TestSamRestApiConnectorEndpoints:
    """Tests for URL building on SamRestApiConnector."""

    @pytest.fixture
    def real_connector(self):
        return SamRestApiConnector(
            server_url="http://fake-server/",
            token=VALID_TOKEN,
        )

    def test_build_rest_endpoint(self, real_connector):
        url = real_connector._build_rest_endpoint(f"/projects/{PROJECT_ID_5}/json")
        assert url.endswith("/json")
        assert "/api/rest/latest/" in url

    def test_build_image_endpoint(self, real_connector):
        url = real_connector._build_image_endpoint("/svg")
        assert url.endswith("/svg")
        assert "/api/" in url

    def test_build_rest_endpoint_without_slash(self, real_connector):
        url = real_connector._build_rest_endpoint(f"projects/{PROJECT_ID_5}/json")
        assert url.endswith("/json")

    def test_unknown_diagram_error(self, real_connector, mocker):
        mock_response = type(
            "MockResponse",
            (),
            {"status_code": 404, "content": b"Not found"},
        )()
        mocker.patch("requests.get", return_value=mock_response)
        from ansys.sam.sysml2.exception.connector_exception import (
            DiagramConnectorException,
        )

        with pytest.raises(DiagramConnectorException):
            real_connector.get_single_diagram_info(PROJECT_ID_5, "unknown")
