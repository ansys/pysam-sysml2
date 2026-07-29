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

"""Unit tests for the unified dynamic notation (DynamicEObject) over the generated metamodel."""

import pytest

from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.dynamic_e_object import DynamicEObject
from ansys.sam.sysml2.meta_model.attribute_usage import AttributeUsage
from ansys.sam.sysml2.meta_model.e_object import EObject
from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.tools.factory import Factory
from ansys.sam.sysml2.tools.sysmltools import SysMLTools
from tests.unit.const import PROJECT_ID_2, PROJECT_ID_5


class TestDynamicEObjectNavigation:
    """Dot navigation and _camelCase access resolve over the generated metamodel."""

    @pytest.fixture
    def project(self, connector):
        return SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)

    def test_dot_navigation_matches_get(self, project):
        root = project.get_root_package()

        assert root.attribute is not None
        assert root.attribute is root.get("attribute")

    def test_camel_case_scalar_read(self, project):
        attribute = project.get_root_package().get("attribute")

        assert attribute._declaredName == attribute.declared_name
        assert attribute._id == attribute.id

    def test_camel_case_list_read_is_the_readonly_property(self, project):
        root = project.get_root_package()

        assert root._ownedElement is root.owned_element
        assert isinstance(list(root._ownedElement), list)

    def test_native_isinstance(self, project):
        attribute = project.get_root_package().get("attribute")

        assert isinstance(attribute, AttributeUsage)
        assert isinstance(attribute, Element)
        assert isinstance(attribute, EObject)
        assert isinstance(attribute, DynamicEObject)

    def test_dir_exposes_dynamic_notation(self, project):
        root = project.get_root_package()

        listing = dir(root)

        assert "_declaredName" in listing
        assert "_ownedElement" in listing
        assert "declared_name" not in listing
        assert "owned_element" not in listing
        assert "attribute" in listing
        assert "get" in listing


class TestDynamicEObjectWrite:
    """Writes through the dynamic notation route through the metamodel property setters."""

    def test_writable_camel_case_routes_through_observer(self, connector, mocker):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)
        attribute = project.get_root_package().get("attribute")
        mocker.patch.object(attribute._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        attribute._declaredName = "renamed_attribute"

        assert attribute._declared_name == "renamed_attribute"
        assert commit_spy.call_count == 1
        assert "renamed_attribute" in commit_spy.call_args.args[1]

    def test_read_only_camel_case_write_raises(self, connector):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)
        attribute = project.get_root_package().get("attribute")

        with pytest.raises(AttributeError):
            attribute._qualifiedName = "nope"


class TestDynamicEObjectValuesAndFactory:
    """Value access and Factory creation behave as on the unified model."""

    def test_get_and_set_value(self, connector, mocker):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)
        attribute = project.get_root_package().get("attribute")

        assert SysMLTools.serialize_expression(attribute.get_value()) == "5 + 5"

        mocker.patch.object(attribute._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        attribute.set_value("42")

        assert commit_spy.call_count >= 1

    def test_factory_creates_dynamic_element(self, connector):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_2)
        factory = Factory(project, connector)
        root = project.get_root_package()
        project.start_transactional_mode()

        attribute = factory.create_attribute_usage(declared_name="new_attribute", owner=root)

        project.stop_transactional_mode()

        assert isinstance(attribute, AttributeUsage)
        assert isinstance(attribute, DynamicEObject)
        assert attribute._declared_name == "new_attribute"
