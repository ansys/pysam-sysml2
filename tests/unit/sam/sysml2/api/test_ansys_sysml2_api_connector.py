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

import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.classes.http_request import HttpRequest
from tests.unit.const import VALID_ORGANIZATION, VALID_TOKEN


@pytest.fixture
def connector():
    return AnsysSysML2APIConnector(
        server_url="http://fake-server",
        organization_id=VALID_ORGANIZATION,
        token=VALID_TOKEN,
        use_ssl=False,
    )


class TestAnsysSysML2APIConnector:

    def test_build_endpoint(self, connector):
        url = connector._build_endpoint("/projects")
        assert VALID_ORGANIZATION in url
        assert url.endswith("/projects")
        assert url.startswith("http://fake-server/api/spaces/")

    def test_build_endpoint_without_leading_slash(self, connector):
        url = connector._build_endpoint("projects")
        assert url.endswith("/projects")
        assert "/sysml2/" in url

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
        )
        assert not c._server_url.endswith("/")
