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

from ansys.sam.sysml2 import ConnectorFactory


class TestConnectorFactory:

    URL: str = "localhost"
    ORGANIZATION: str = "org_id"
    TOKEN: str = "TOKEN"

    def test_sysml_initialization(self):
        conn = ConnectorFactory.create_ansys_sysml_connector(
            server_url=self.URL, organization_id=self.ORGANIZATION, token=self.TOKEN
        )

        assert conn is not None
        assert hasattr(conn._authenticator, "_token")
        assert self.ORGANIZATION in conn._route_dispatcher.build_endpoint("")
        assert conn._route_dispatcher.build_endpoint("").startswith(self.URL)
