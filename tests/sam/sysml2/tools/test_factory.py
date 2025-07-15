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

from ansys.sam.sysml2 import SysML2ProjectManager
from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.exception.connector_exception import BadRequestConnectionException
from ansys.sam.sysml2.tools.factory import Factory
from mocked_server.routes.const import PROJECT_ID_2
from parent_test_class import ParentTestClass


class TestFactory(ParentTestClass):

    @pytest.fixture
    def project_manager(self, valid_source: AnsysSysML2APIConnector) -> SysML2ProjectManager:
        return SysML2ProjectManager(valid_source)

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

    def test_create_element_with_no_type(self, project_manager: SysML2ProjectManager):
        project = project_manager.get_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)

        with pytest.raises(BadRequestConnectionException) as exception:
            factory.create_element(element_type=None, name="new_attribute")
        assert "Bad Request : No Type for New Element" == exception.value.args[0]

    def test_create_element_with_unknown_owner(self, project_manager: SysML2ProjectManager):
        project = project_manager.get_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)

        with pytest.raises(BadRequestConnectionException) as exception:
            factory.create_element(element_type="AttributeUsage", name="new_attribute")
        assert "Bad Request : No Valid Owner Specified" == exception.value.args[0]

    def test_create_element_with_invalid_owner(self, project_manager: SysML2ProjectManager):
        project = project_manager.get_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)

        with pytest.raises(BadRequestConnectionException) as exception:
            factory.create_element(
                element_type="AttributeUsage", name="new_attribute", owner="INVALID_OWNER"
            )
        assert "Bad Request : No Valid Owner Specified" == exception.value.args[0]

    def test_create_element_with_invalid_owner_attr(self, project_manager: SysML2ProjectManager):
        project = project_manager.get_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)

        project_root = project.get_root_package()

        with pytest.raises(AttributeError) as error:
            factory.create_element(
                element_type="AttributeUsage",
                name="new_attribute",
                owner=project_root.UNDEFINED_ELEMENT,
            )
        assert "'Package' object has no attribute 'UNDEFINED_ELEMENT'" == error.value.args[0]

    def test_create_element_with_owned_element(self, project_manager: SysML2ProjectManager):
        project = project_manager.get_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)

        project_root = project.get_root_package()

        new_attribute = factory.create_element(
            element_type="AttributeUsage", name="new_attribute", owner=project_root
        )

        new_part_definition = factory.create_element(
            element_type="PartDefinition",
            name="new_part_def",
            owner=project_root,
            owned_elements=[new_attribute],
        )

        assert len(new_part_definition._owned_elements) == 1
        assert new_part_definition._owned_elements[0]._name == new_attribute._name

    def test_create_element_with_invalid_type(self, project_manager: SysML2ProjectManager):
        project = project_manager.get_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)

        project_root = project.get_root_package()

        with pytest.raises(TypeError) as error:
            factory.create_element(
                element_type="AttributeUsage", name=["new_attribute"], owner=project_root
            )

        assert error.value.args[0].startswith("attribute name must be string")
