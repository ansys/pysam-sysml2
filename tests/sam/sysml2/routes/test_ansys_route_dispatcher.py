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

"""File  created on Tue Dec 10 2024."""

import pytest

from ansys.sam.sysml2.exception.route_exception import InvalidAnsysOrganizationIdException
from ansys.sam.sysml2.routes.ansys_route_dispatcher import AnsysRouteDispatcher


class TestAnsysRouteDispatcher:
    """Test class for route SysML dispatcher"""

    URL_1: str = "http://localhost:8443"
    URL_2: str = "https://sam-testing.ansys.com:9050"
    ORG_ID_1: str = "RandDomId"
    ORG_ID_2: str = "RandDomOtherId"

    def test_valid_initialization(self):
        routes = AnsysRouteDispatcher(server_url=self.URL_1, organization_id=self.ORG_ID_1)

        assert routes.build_endpoint("") is not None
        assert routes.build_endpoint("test").startswith(self.URL_1)
        assert self.ORG_ID_1 in routes.build_endpoint("")

    def test_invalid_initialization(self):
        routes = AnsysRouteDispatcher(server_url=self.URL_1)
        with pytest.raises(InvalidAnsysOrganizationIdException):
            routes.build_endpoint("")
        routes = AnsysRouteDispatcher(server_url=self.URL_1 + "/", organization_id=self.ORG_ID_1)

        assert not routes._server_url.endswith("/")

    def test_update_organization_id(self):
        routes = AnsysRouteDispatcher(server_url=self.URL_1, organization_id=self.ORG_ID_1)
        assert self.ORG_ID_1 in routes.build_endpoint("")

        routes.set_organization(self.ORG_ID_2)

        assert not self.ORG_ID_1 in routes.build_endpoint("")
        assert self.ORG_ID_2 in routes.build_endpoint("")
