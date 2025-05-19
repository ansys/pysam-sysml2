# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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

import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.diagrams.api import AnsysRestApiConnector
from mocked_server.mocked_server import MockedServer
from mocked_server.routes.const import PROJECT_ID_3, VALID_ORGANIZATION, VALID_TOKEN


class TestAnsysRestApiConnector:

    @pytest.fixture
    def connector(self) -> AnsysRestApiConnector:
        connector = AnsysSysML2APIConnector(
            server_url=MockedServer.get_url() + "/",
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
        )
        return AnsysRestApiConnector(connector)

    def test_get_project_data(self, connector: AnsysRestApiConnector):
        data = connector.get_project_data(PROJECT_ID_3)
        assert len(data) > 0
        assert "eClass" in data

    def test_build_end_point(self, connector: AnsysRestApiConnector):
        url = connector._build_endpoint(f"/projects/{PROJECT_ID_3}/json")
        assert url.endswith("/json")
