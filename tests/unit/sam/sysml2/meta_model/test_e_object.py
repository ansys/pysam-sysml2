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

"""Unit tests for EObject (SysML project element) get/set using the mocked connector."""

import pytest

from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.classes.sysml_inherited_element import SysMLInheritedElement
from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.meta_model.feature import Feature
from ansys.sam.sysml2.meta_model.part_usage import PartUsage
from ansys.sam.sysml2.tools.sysmltools import SysMLTools
from tests.unit.const import PROJECT_ID_1, PROJECT_ID_3


class TestEObject:

    @pytest.fixture
    def project(self, connector) -> Project:
        model_manager = SysML2ProjectManager(connector=connector)
        return model_manager.get_sysml_project(PROJECT_ID_3)

    def test_update_element(self, connector, mocker):
        project_manager = SysML2ProjectManager(connector)
        project = project_manager.get_sysml_project(PROJECT_ID_1)
        root = project.get_root_package()
        mocker.patch.object(root._observer, "reload_project")
        elem = root.get("PartDefinition").get("attribute")
        elem.declared_name = "NewAttr"
        assert elem.declared_name == "NewAttr"

    def test_expression_get_values(self, project: Project):
        package = project.get_root_package()
        value = package.get("Feature").get("myExpressionFeature").get_value()
        assert SysMLTools.serialize_expression(value) == "10 [kg]"

    def test_expression_set_value(self, project: Project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        package.get("Feature").get("myExpressionFeature").parse_and_set_value("20 [kg]")
        value = package.get("Feature").get("myExpressionFeature").get_value()
        assert value is not None

    def test_expression_complex_value_renders_as_text(self, project: Project):
        package = project.get_root_package()
        value = package.get("Feature").get("myComplexExpressionFeature").get_value()
        assert SysMLTools.serialize_expression(value) == "10 [kg] + 6 [kg]"

    def test_int_get_values(self, project: Project):
        package = project.get_root_package()
        assert package.get("Feature").get("myIntFeature").get_value().value == 10

    def test_int_set_value(self, connector, project: Project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")
        package.get("Feature").get("myIntFeature").set_value(20)
        assert commit_spy.call_count == 1

    def test_string_get_values(self, project: Project):
        package = project.get_root_package()
        assert package.get("Feature").get("myStringFeature").get_value().value == "Hello"

    def test_string_set_value(self, connector, project: Project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")
        package.get("Feature").get("myStringFeature").set_value("World")
        assert commit_spy.call_count == 1

    def test_bool_get_values(self, project: Project):
        package = project.get_root_package()
        assert package.get("Feature").get("myBoolFeature").get_value().value is False

    def test_bool_set_value(self, connector, project: Project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")
        package.get("Feature").get("myBoolFeature").set_value(True)
        assert commit_spy.call_count == 1

    def test_float_get_values(self, project: Project):
        package = project.get_root_package()
        assert package.get("Feature").get(
            "myFloatFeature"
        ).get_value().value == pytest.approx(10.56)

    def test_float_set_value(self, connector, project: Project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")
        package.get("Feature").get("myFloatFeature").set_value(20.5)
        assert commit_spy.call_count == 1


class TestSysMLInheritedElement:
    """The inherited-element proxy exposes the wrapped element's real UUID."""

    def test_proxy_exposes_real_uuid(self):
        element = Element("base-uuid")
        owner = Element("owner-uuid")
        proxy = SysMLInheritedElement(owner, element)

        assert proxy.id == element.id
        assert "/?" not in proxy.id


class TestEObjectDir:
    """dir() lists value and connection helpers only when applicable."""

    def test_value_methods_hidden_on_non_feature(self):
        element = Element("element_id")

        listing = dir(element)
        assert "get_value" not in listing
        assert "set_value" not in listing
        assert "parse_and_set_value" not in listing

    def test_value_methods_listed_on_feature(self):
        element = Feature("element_id")

        listing = dir(element)
        assert "get_value" in listing
        assert "set_value" in listing
        assert "parse_and_set_value" in listing

    def test_value_methods_listed_on_feature_descendant(self):
        element = PartUsage("element_id")

        listing = dir(element)
        assert "get_value" in listing
        assert "set_value" in listing
        assert "parse_and_set_value" in listing

    def test_source_target_hidden_without_ends(self):
        element = Element("element_id")

        listing = dir(element)
        assert "get_source" not in listing
        assert "get_target" not in listing

    def test_get_source_listed_when_source_populated(self):
        element = Element("element_id")
        element.source = [Element("end_id")]

        assert "get_source" in dir(element)
        assert "get_target" not in dir(element)

    def test_get_target_listed_when_target_populated(self):
        element = Element("element_id")
        element.target = [Element("end_id")]

        assert "get_target" in dir(element)
        assert "get_source" not in dir(element)


class TestEObjectDirPublicOnly:
    """dir() exposes the public SysML API only, hiding single-underscore backing fields."""

    def test_public_properties_listed(self):
        element = PartUsage("element_id")

        listing = dir(element)
        assert "declared_name" in listing
        assert "name" in listing
        assert "id" in listing
        assert "owned_element" in listing

    def test_single_underscore_backing_fields_hidden(self):
        element = PartUsage("element_id")

        listing = dir(element)
        assert "_declared_name" not in listing
        assert "_name" not in listing
        assert "_owner" not in listing
        assert "_id" not in listing
        assert "_proxy_cache" not in listing

    def test_no_single_underscore_names_at_all(self):
        element = PartUsage("element_id")

        private = [
            a for a in dir(element) if a.startswith("_") and not a.startswith("__")
        ]
        assert private == []

    def test_dunders_still_listed(self):
        element = PartUsage("element_id")

        assert "__class__" in dir(element)
