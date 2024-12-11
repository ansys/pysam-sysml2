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
from ansys.sam.sysml2.exception.connector_exception import ConnectorConnectionException
from mocked_server.mocked_server import MockedServer
from mocked_server.routes.const import VALID_ORGANIZATION, VALID_TOKEN


class TestConfigAnsysSysMLSource:

    def test_constructor_valid_configuration(self):
        source = ConnectorFactory.create_ansys_sysml_connector(
            server_url=MockedServer.get_url(), organization_id=VALID_ORGANIZATION, token=VALID_TOKEN
        )
        projects = source.get_projects()
        assert projects is not None
        assert len(projects) > 0

    def test_constructor_invalid_organization_configuration(self):
        source = ConnectorFactory.create_ansys_sysml_connector(
            server_url=MockedServer.get_url(),
            organization_id="RandOmOrganization",
            token=VALID_TOKEN,
        )
        with pytest.raises(ConnectorConnectionException):
            source.get_projects()

    def test_constructor_invalid_token_configuration(self):
        source = ConnectorFactory.create_ansys_sysml_connector(
            server_url=MockedServer.get_url(),
            organization_id=VALID_ORGANIZATION,
            token="RandomTOken",
        )
        with pytest.raises(ConnectorConnectionException):
            source.get_projects()
