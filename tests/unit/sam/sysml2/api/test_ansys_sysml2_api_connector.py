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

"""Unit tests for AnsysSysML2APIConnector URL building and authentication."""

import json

import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.classes.http_request import HttpRequest
from ansys.sam.sysml2.exception.connector_exception import ConnectorConnectionException
from tests.unit.const import VALID_ORGANIZATION, VALID_TOKEN


class _MockResponse:
    """Minimal mock HTTP response."""

    def __init__(self, status_code, content=b""):
        self.status_code = status_code
        self.content = content


@pytest.fixture
def connector():
    return AnsysSysML2APIConnector(
        server_url="http://fake-server",
        organization_id=VALID_ORGANIZATION,
        token=VALID_TOKEN,
        use_ssl=False,
        check_version=False
    )


class TestAnsysSysML2APIConnector:

    def test_build_endpoint(self, connector):
        url = connector._build_endpoint("/projects")

        assert url == f"http://fake-server/api/spaces/{VALID_ORGANIZATION}/sysml2/projects"

    def test_build_endpoint_without_leading_slash(self, connector):
        url = connector._build_endpoint("projects")

        assert url == f"http://fake-server/api/spaces/{VALID_ORGANIZATION}/sysml2/projects"

    def test_add_authentication_field(self, connector):
        http_request = HttpRequest(url="http://test")
        http_request = connector._add_authentication_field(http_request)

        assert "Authorization" in http_request.headers
        assert http_request.headers["Authorization"] == f"Bearer {VALID_TOKEN}"

    def test_trailing_slash_stripped(self):
        c = AnsysSysML2APIConnector(
            server_url="http://fake-server/",
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
            check_version=False
        )

        assert c._server_url == "http://fake-server"

    def test_get_all_elements_query_params(self, connector, mocker):
        mock_get = mocker.patch(
            "requests.get",
            return_value=_MockResponse(200, content=b"[]"),
        )

        connector.get_all_elements(
            "project-1",
            includes_derived=False,
            includes_inherited=False,
        )

        mock_get.assert_called_once()
        assert mock_get.call_args.kwargs["params"] == {
            "includesDerived": "false",
            "includesInherited": "false",
        }

    def test_execute_query_query_params(self, connector, mocker):
        mock_post = mocker.patch(
            "requests.post",
            return_value=_MockResponse(200, content=b"[]"),
        )

        connector.execute_query(
            "project-1",
            "{}",
            includes_derived=False,
            includes_inherited=False,
        )

        mock_post.assert_called_once()
        assert mock_post.call_args.kwargs["params"] == {
            "includesDerived": "false",
            "includesInherited": "false",
        }

    def test_validated_check_version(self, connector, mocker):
            mock_get = mocker.patch(
                "requests.get",
                return_value=_MockResponse(200, content=json.dumps({"build": {"version": "27.1.0"}})),
            )

            connector._check_version()
            assert mock_get.call_count == 1
            assert mock_get.call_args.kwargs["url"] == "http://fake-server/api/status/info"


    def test_invalid_check_version(self, connector, mocker):
        mock_get = mocker.patch(
            "requests.get",
            return_value=_MockResponse(200, content=json.dumps({"build": {"version": "26.1.0"}})),
        )

        with pytest.raises(Exception) as excinfo:
            connector._check_version()

        assert "26.1.0" in str(excinfo.value)
        assert "Unsupported SAM server version" in str(excinfo.value)

    def test_check_version_request_failure(self, connector, mocker):
        mock_get = mocker.patch(
            "requests.get",
            return_value=_MockResponse(500, content=json.dumps({"error": "Internal Server Error"})),
        )

        with pytest.raises(ConnectorConnectionException) as excinfo:
            connector._check_version()

        assert "Internal Server Error" in str(excinfo.value)

    def test_check_version_invalid_format(self, connector, mocker):
            mock_get = mocker.patch(
                "requests.get",
                return_value=_MockResponse(200, content=json.dumps({"build": {"server_version": "26.1.0"}})),
            )

            with pytest.raises(ConnectorConnectionException) as excinfo:
                connector._check_version()

            assert "Failed to check SAM server version" in str(excinfo.value)