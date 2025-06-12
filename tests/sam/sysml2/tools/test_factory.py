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

from mocked_server.mocked_server import MockedServer
from mocked_server.routes.const import PROJECT_ID_2, VALID_ORGANIZATION, VALID_TOKEN
import pytest

from ansys.sam.sysml2 import SysML2ProjectManager
from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.tools import Factory


class TestFactory:
    @pytest.fixture
    def project_manager(self) -> SysML2ProjectManager:
        return SysML2ProjectManager(
            AnsysSysML2APIConnector(
                server_url=MockedServer.get_url(),
                organization_id=VALID_ORGANIZATION,
                token=VALID_TOKEN,
            )
        )

    def test_create_element(self, project_manager: SysML2ProjectManager):
        project = project_manager.get_project(PROJECT_ID_2)

        factory = Factory(project, project_manager._connector)

        project_root = project.get_root_package()

        new_attribute = factory.create_element(
            element_type="AttributeUsage", name="new_attribute", owner=project_root
        )

        assert project_root.new_attribute._name == "new_attribute"

        new_attribute._name = "NewAttr"

        assert project_root.NewAttr._name == "NewAttr"

        with pytest.raises(AttributeError):
            project_root.new_attribute
