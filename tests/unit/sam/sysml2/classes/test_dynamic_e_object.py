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

"""Unit tests for the unified scripting notation (DynamicEObject) over the generated metamodel."""

import pytest

from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.dynamic_e_object import DynamicEObject
from ansys.sam.sysml2.classes.sysml_inherited_element import SysMLInheritedElement
from ansys.sam.sysml2.exception.connector_exception import BadRequestConnectionException
from ansys.sam.sysml2.meta_model.attribute_usage import AttributeUsage
from ansys.sam.sysml2.meta_model.e_object import EObject
from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.tools.factory import Factory
from ansys.sam.sysml2.tools.sysmltools import SysMLTools
from tests.unit.const import PROJECT_ID_1, PROJECT_ID_2, PROJECT_ID_3, PROJECT_ID_5


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

    def test_dir_exposes_scripting_notation(self, project):
        root = project.get_root_package()

        listing = dir(root)

        assert "_declaredName" in listing
        assert "_ownedElement" in listing
        assert "declared_name" not in listing
        assert "owned_element" not in listing
        assert "attribute" in listing
        assert "get" in listing


class TestDynamicEObjectWrite:
    """Writes through the scripting notation route through the metamodel property setters."""

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

    def test_read_only_single_word_write_raises(self):
        element = SysMLUtil.get_scripting_constructor("PartUsage")("element_id")

        with pytest.raises(AttributeError):
            element._name = "nope"

    def test_read_only_source_and_target_write_raises(self):
        relationship = SysMLUtil.get_scripting_constructor("Relationship")("element_id")

        with pytest.raises(AttributeError):
            relationship._source = []
        with pytest.raises(AttributeError):
            relationship._target = []

    def test_snake_case_read_only_write_raises_like_sysml(self):
        element = SysMLUtil.get_scripting_constructor("PartUsage")("element_id")

        with pytest.raises(AttributeError):
            element.name = "nope"

    def test_writable_single_word_routes_through_setter(self):
        transition = SysMLUtil.get_scripting_constructor("TransitionUsage")("element_id")
        end = SysMLUtil.get_scripting_constructor("PartUsage")("end_id")

        transition._source = end

        assert transition.source is end


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

    def test_factory_creates_scripting_element(self, connector):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_2)
        factory = Factory(project, connector)
        root = project.get_root_package()
        project.start_transactional_mode()

        attribute = factory.create_attribute_usage(declared_name="new_attribute", owner=root)

        project.stop_transactional_mode()

        assert isinstance(attribute, AttributeUsage)
        assert isinstance(attribute, DynamicEObject)
        assert attribute._declared_name == "new_attribute"


class TestSysMLElementGet:
    """``get(name)`` reaches scripting children whose names dot access cannot express."""

    def _build_parent_with_spaced_child(self):
        child = SysMLUtil.get_scripting_constructor("PartDefinition")("child-id")
        child._declaredName = "Part Definition"
        parent = SysMLUtil.get_scripting_constructor("Package")("parent-id")
        parent._element_hash_map = {"Part Definition": child}
        parent._owned_names = {"Part Definition"}
        return parent, child

    def test_get_returns_owned_child_with_spaced_name(self):
        parent, child = self._build_parent_with_spaced_child()

        assert parent.get("Part Definition") is child

    def test_get_returns_none_for_missing_name(self):
        parent, _ = self._build_parent_with_spaced_child()

        assert parent.get("missing") is None

    def test_get_through_inherited_element_proxy(self):
        parent, _ = self._build_parent_with_spaced_child()
        owner = SysMLUtil.get_scripting_constructor("Package")("owner-id")
        proxy = SysMLInheritedElement(owner, parent)

        resolved = proxy.get("Part Definition")

        assert resolved is not None
        assert resolved._declaredName == "Part Definition"
        assert proxy.get("missing") is None

    def test_inherited_element_proxy_exposes_real_uuid(self):
        parent, _ = self._build_parent_with_spaced_child()
        owner = SysMLUtil.get_scripting_constructor("Package")("owner-id")
        proxy = SysMLInheritedElement(owner, parent)

        assert proxy._id == parent._id
        assert "/?" not in proxy._id


class TestSysMLElement:
    """Scripting value get/set and name updates using the ``_camelCase`` notation."""

    @pytest.fixture
    def project(self, connector):
        manager = SysML2ProjectManager(connector)
        return manager.get_scripting_project(PROJECT_ID_3)

    def test_update_element_name(self, connector, mocker):
        manager = SysML2ProjectManager(connector)
        project = manager.get_scripting_project(PROJECT_ID_1)
        root = project.get_root_package()
        mocker.patch.object(root._observer, "reload_project")
        attr = root.PartDefinition.attribute

        attr._declaredName = "NewAttr"

        assert attr._declaredName == "NewAttr"

    def test_expression_get_value(self, project):
        package = project.get_root_package()

        value = package.Feature.myExpressionFeature.get_value()
        assert SysMLTools.serialize_expression(value) == "10 [kg]"

    def test_expression_set_value(self, connector, project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        SysMLTools.parse_and_set_value(package.Feature.myExpressionFeature, "20 [kg]")

        assert commit_spy.call_count == 2

    def test_expression_complex_value_renders_as_text(self, project):
        package = project.get_root_package()

        value = package.Feature.myComplexExpressionFeature.get_value()
        assert SysMLTools.serialize_expression(value) == "10 [kg] + 6 [kg]"

    def test_int_get_set_value(self, connector, project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        assert package.Feature.myIntFeature.get_value()._value == 10

        package.Feature.myIntFeature.set_value(20)

        assert commit_spy.call_count == 1

    def test_string_get_set_value(self, connector, project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        assert package.Feature.myStringFeature.get_value()._value == "Hello"

        package.Feature.myStringFeature.set_value("World")

        assert commit_spy.call_count == 1

    def test_bool_get_set_value(self, connector, project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        assert package.Feature.myBoolFeature.get_value()._value is False

        package.Feature.myBoolFeature.set_value(True)

        assert commit_spy.call_count == 1

    def test_float_get_set_value(self, connector, project, mocker):
        package = project.get_root_package()
        mocker.patch.object(package._observer, "reload_project")
        commit_spy = mocker.spy(connector, "create_commit")

        assert package.Feature.myFloatFeature.get_value()._value == pytest.approx(10.56)

        package.Feature.myFloatFeature.set_value(20.5)

        assert commit_spy.call_count == 1

    def test_setattr_commit_rejected(self, connector, mocker):
        manager = SysML2ProjectManager(connector)
        project = manager.get_scripting_project(PROJECT_ID_1)
        root = project.get_root_package()
        mocker.patch.object(
            connector,
            "create_commit",
            side_effect=BadRequestConnectionException("Invalid key"),
        )

        with pytest.raises(BadRequestConnectionException):
            root._declaredName = ["ShouldFail"]


class TestSysMLElementDir:
    """dir() lists value and connection helpers only when applicable."""

    def test_value_methods_hidden_on_non_feature(self):
        element = SysMLUtil.get_scripting_constructor("Comment")("element_id")

        listing = dir(element)
        assert "get_value" not in listing
        assert "set_value" not in listing
        assert "parse_and_set_value" not in listing

    def test_value_methods_listed_on_feature_descendant(self):
        element = SysMLUtil.get_scripting_constructor("PartUsage")("element_id")

        listing = dir(element)
        assert "get_value" in listing
        assert "set_value" in listing
        assert "parse_and_set_value" not in listing
