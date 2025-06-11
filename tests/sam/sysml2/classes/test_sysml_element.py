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
from mocked_server.routes.const import PROJECT_ID_1, VALID_ORGANIZATION, VALID_TOKEN
import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.sysml_element import SysMLElement


class TestSysMLElement:
    @pytest.fixture
    def element(self):
        element = SysMLElement("")
        element._IS_READ_ONLY = True
        return element

    #
    # functions below are testing the write access elements
    #

    def test_direct_assignment(self, element):
        element.value = 42
        assert not hasattr(element, "value")

    def test_setattr(self, element):
        setattr(element, "value", 99)
        assert not hasattr(element, "value")

    def test_update_element(self):
        project_manager = SysML2ProjectManager(
            AnsysSysML2APIConnector(
                server_url=MockedServer.get_url(),
                organization_id=VALID_ORGANIZATION,
                token=VALID_TOKEN,
            )
        )

        project = project_manager.get_project(PROJECT_ID_1)

        project_root = project.get_root_package()

        project_root.myPartUsage.Attribute._name = "NewAttr"

        assert project_root.myPartUsage.NewAttr._name == "NewAttr"

        with pytest.raises(AttributeError):
            project_root.myPartUsage.Attribute
