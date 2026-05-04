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

"""Unit tests for AnsysSysML2Project using mocker to inject MockedConnectors."""

from ansys.sam.sysml2.diagrams.api.sam_rest_api_connector import SamRestApiConnector
from ansys.sam.sysml2.meta_model.package import Package
from ansys.sam.sysml2.tools.ansys_sysml2_project import AnsysSysML2Project
from ansys.sam.sysml2.tools.factory import Factory
from tests.unit.const import PROJECT_ID_1, VALID_ORGANIZATION, VALID_TOKEN
from tests.unit.mocked_connector import MockedSysML2APIConnector


class TestAnsysSysML2Project:

    def test_streamlined_project_factory_initialization(self, mocker):
        mocker.patch(
            "ansys.sam.sysml2.tools.ansys_project.AnsysSysML2APIConnector",
            return_value=MockedSysML2APIConnector(),
        )
        mocker.patch.object(
            SamRestApiConnector,
            "get_project_data",
            side_effect=RuntimeError("diagrams not available in unit tests"),
        )

        project = AnsysSysML2Project(
            server_url="http://fake",
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
            use_ssl=False,
            project_id=PROJECT_ID_1,
        )

        assert project._project_id == PROJECT_ID_1
        root = project.get_root_package()
        assert root is not None
        assert root.name == "project-1"

        assert isinstance(project._factory, Factory)
        assert project._factory._project is project
        assert project._factory._project_id == PROJECT_ID_1

        project.start_transactional_mode()
        new_pkg = project._factory.create_package(name="my_package", owner=root)
        project.stop_transactional_mode()
        assert isinstance(new_pkg, Package)
        assert new_pkg.name == "my_package"

        assert project.is_diagrams_available() is False
        assert project._downloader is None
