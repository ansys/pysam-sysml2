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

"""E2E tests based on the bike model examples (weight, update, transaction, create element)."""

import pytest

from ansys.sam.sysml2.exception.connector_exception import ProjectNotFoundException
from ansys.sam.sysml2.tools.factory import Factory
from ansys.sam.sysml2.tools.sysmltools import SysMLTools


@pytest.mark.e2e
class TestValues:

    def test_bike_weight_and_unit(self, project_factory):
        """Navigate model, calculate total weight, checks weight and unit."""
        project = project_factory(model="bike", kind="scripting")
        bike = project.get_root_package().Structure.Bike
        bike_parts = [
            SysMLTools.serialize_expression(bike.frontWheel.rim.weight.get_value()),
            SysMLTools.serialize_expression(bike.frontWheel.tire.weight.get_value()),
            SysMLTools.serialize_expression(bike.rearWheel.rim.weight.get_value()),
            SysMLTools.serialize_expression(bike.rearWheel.tire.weight.get_value()),
            SysMLTools.serialize_expression(bike.frame.weight.get_value()),
        ]

        total_bike_weight = sum(int(part.split()[0]) for part in bike_parts)
        bike_parts_weight_unit_all_same = all(p.endswith(" [kg]") for p in bike_parts)

        assert total_bike_weight == 10
        assert bike_parts[0].endswith(" [kg]")
        assert bike_parts_weight_unit_all_same

    def test_bike_rim_weight_and_unit_update(self, project_factory):
        """Update rim weight and unit, verify change."""
        project = project_factory(model="bike", kind="scripting")
        bike = project.get_root_package().Structure.Bike
        original_front_weight = SysMLTools.serialize_expression(
            bike.frontWheel.rim.weight.get_value()
        )

        assert original_front_weight == "1 [kg]"

        bike.frontWheel.rim.weight.parse_and_set_value("500 [g]")
        updated_front_weight = SysMLTools.serialize_expression(
            bike.frontWheel.rim.weight.get_value()
        )

        assert updated_front_weight != original_front_weight
        assert updated_front_weight == "500 [g]"

    def test_bike_rim_weight_transaction(self, project_factory):
        """Transactional mode: batch updates, verify after commit."""
        project = project_factory(model="bike", kind="scripting")
        bike = project.get_root_package().Structure.Bike
        original_front_weight = SysMLTools.serialize_expression(
            bike.frontWheel.rim.weight.get_value()
        )
        original_rear_weight = SysMLTools.serialize_expression(
            bike.rearWheel.rim.weight.get_value()
        )

        assert original_front_weight == "1 [kg]"
        assert original_rear_weight == "1 [kg]"

        project.start_transactional_mode()
        bike.frontWheel.rim.weight.parse_and_set_value("500 [g]")
        bike.rearWheel.rim.weight.parse_and_set_value("750 [g]")
        project.stop_transactional_mode()

        updated_front_weight = SysMLTools.serialize_expression(
            bike.frontWheel.rim.weight.get_value()
        )
        updated_rear_weight = SysMLTools.serialize_expression(bike.rearWheel.rim.weight.get_value())

        assert updated_front_weight == "500 [g]"
        assert updated_rear_weight == "750 [g]"

    def test_bike_create_element(self, connector, project_factory):
        """Create attribute on bike.frame, set value, verify roundtrip."""
        project = project_factory(model="bike", kind="scripting")
        bike = project.get_root_package().Structure.Bike
        factory = Factory(project, connector)
        factory.create_attribute_usage(declared_name="length", owner=bike.frame)

        bike.frame.length.parse_and_set_value("60 [cm]")
        value = SysMLTools.serialize_expression(bike.frame.length.get_value())

        assert value == "60 [cm]"

    def test_bike_sysml_project(self, project_factory):
        """Load bike via sysml project, navigate with .get(), verify structure (weight-bike-static.py)."""
        project = project_factory(model="bike", kind="sysml")
        bike = project.get_root_package().get("Structure").get("Bike")
        front_wheel = bike.get("frontWheel")
        rear_wheel = bike.get("rearWheel")
        bike_parts = [
            SysMLTools.serialize_expression(front_wheel.get("rim").get("weight").get_value()),
            SysMLTools.serialize_expression(front_wheel.get("tire").get("weight").get_value()),
            SysMLTools.serialize_expression(rear_wheel.get("rim").get("weight").get_value()),
            SysMLTools.serialize_expression(rear_wheel.get("tire").get("weight").get_value()),
            SysMLTools.serialize_expression(bike.get("frame").get("weight").get_value()),
        ]

        total_bike_weight = sum(int(part.split()[0]) for part in bike_parts)
        bike_parts_weight_unit_all_same = all(p.endswith(" [kg]") for p in bike_parts)

        assert total_bike_weight == 10
        assert bike_parts[0].endswith(" [kg]")
        assert bike_parts_weight_unit_all_same

    def test_bike_delete_project(self, connector, project_factory):
        """Delete project and verify it raises ProjectNotFoundException."""
        project = project_factory(model="bike", kind="scripting")
        project_id = project.get_id()

        connector.delete_project(project_id)

        with pytest.raises(ProjectNotFoundException):
            connector.get_project_by_id(project_id)

    def test_create_attribute_arithmetic_expression(self, connector, project_factory):
        """Create an attribute, set an arithmetic complex expression, verify roundtrip."""
        project = project_factory(model="bike", kind="scripting")
        bike = project.get_root_package().Structure.Bike
        factory = Factory(project, connector)
        factory.create_attribute_usage(declared_name="complexArithmetic", owner=bike.frame)

        bike.frame.complexArithmetic.parse_and_set_value("5 + 5 + 5")

        assert (
            SysMLTools.serialize_expression(bike.frame.complexArithmetic.get_value()) == "5 + 5 + 5"
        )

    def test_create_attribute_reference_expression(self, connector, project_factory):
        """Reference an already-created attribute from a second attribute's expression."""
        project = project_factory(model="bike", kind="scripting")
        bike = project.get_root_package().Structure.Bike
        factory = Factory(project, connector)
        factory.create_attribute_usage(declared_name="baseValue", owner=bike.frame)
        bike.frame.baseValue.parse_and_set_value("5 + 5")
        factory.create_attribute_usage(declared_name="refValue", owner=bike.frame)

        bike.frame.refValue.parse_and_set_value("baseValue + baseValue")

        assert SysMLTools.serialize_expression(bike.frame.baseValue.get_value()) == "5 + 5"
        assert (
            SysMLTools.serialize_expression(bike.frame.refValue.get_value())
            == "baseValue + baseValue"
        )

    def test_create_attribute_usage_with_expression_tag(self, connector, project_factory):
        """Create an attribute usage with the expression already set at creation time."""
        project = project_factory(model="bike", kind="scripting")
        bike = project.get_root_package().Structure.Bike
        factory = Factory(project, connector)

        factory.create_attribute_usage(
            declared_name="preSetExpr", owner=bike.frame, expression="5 + 5 + 5"
        )

        assert SysMLTools.serialize_expression(bike.frame.preSetExpr.get_value()) == "5 + 5 + 5"

    def test_create_attribute_expression_sysml(self, connector, project_factory):
        """SysML-kind: create an attribute, set an arithmetic expression, read it via .get()."""
        project = project_factory(model="bike", kind="sysml")
        bike = project.get_root_package().get("Structure").get("Bike")
        frame = bike.get("frame")
        factory = Factory(project, connector)
        factory.create_attribute_usage(declared_name="complexArithmetic", owner=frame)

        frame.get("complexArithmetic").parse_and_set_value("5 + 5 + 5")

        assert (
            SysMLTools.serialize_expression(frame.get("complexArithmetic").get_value())
            == "5 + 5 + 5"
        )

    def test_create_attribute_with_value_kwarg(self, connector, project_factory):
        """Create attributes with an initial literal value; read them back as native ints."""
        project = project_factory(model="bike", kind="scripting")
        root = project.get_root_package()
        factory = Factory(project, connector)
        factory.create_attribute_usage(declared_name="second", owner=root, value=1)
        factory.create_attribute_usage(declared_name="third", owner=root, value=5)

        assert root.second.get_value()._value == 1
        assert root.third.get_value()._value == 5

    def test_create_attribute_with_expression_kwarg(self, connector, project_factory):
        """Create an attribute with an expression set at creation time (unary not)."""
        project = project_factory(model="bike", kind="scripting")
        root = project.get_root_package()
        factory = Factory(project, connector)

        factory.create_attribute_usage(declared_name="notAttr", owner=root, expression="not false")

        assert SysMLTools.serialize_expression(root.notAttr.get_value()) == "not false"

    def test_set_value_stores_string_verbatim(self, connector, project_factory):
        """set_value stores a string literal returned verbatim, without spacing changes."""
        project = project_factory(model="bike", kind="scripting")
        root = project.get_root_package()
        factory = Factory(project, connector)
        factory.create_attribute_usage(declared_name="first", owner=root)

        root.first.set_value("1+2+3+4+5")

        assert root.first.get_value()._value == "1+2+3+4+5"

    def test_parse_and_set_value_renders_expression(self, connector, project_factory):
        """parse_and_set_value builds an expression re-rendered with normalized spacing."""
        project = project_factory(model="bike", kind="scripting")
        root = project.get_root_package()
        factory = Factory(project, connector)
        factory.create_attribute_usage(declared_name="first", owner=root)

        root.first.parse_and_set_value("1+2+3+4+5")

        assert SysMLTools.serialize_expression(root.first.get_value()) == "1 + 2 + 3 + 4 + 5"

    def test_reference_expression_across_siblings(self, connector, project_factory):
        """Reference sibling attributes by name inside a nested arithmetic expression."""
        project = project_factory(model="bike", kind="scripting")
        root = project.get_root_package()
        factory = Factory(project, connector)
        factory.create_attribute_usage(declared_name="second", owner=root, value=1)
        factory.create_attribute_usage(declared_name="third", owner=root, value=5)
        factory.create_attribute_usage(declared_name="first", owner=root)

        root.first.set_value("first_value")
        assert root.first.get_value()._value == "first_value"

        root.first.parse_and_set_value("second + third * 3")

        assert SysMLTools.serialize_expression(root.first.get_value()) == "second + third * 3"

    def test_unary_not_expression(self, connector, project_factory):
        """Unary not renders with a lowercased boolean, both at creation and after update."""
        project = project_factory(model="bike", kind="scripting")
        root = project.get_root_package()
        factory = Factory(project, connector)
        factory.create_attribute_usage(declared_name="flag", owner=root, expression="not false")

        assert SysMLTools.serialize_expression(root.flag.get_value()) == "not false"

        root.flag.parse_and_set_value("not true")

        assert SysMLTools.serialize_expression(root.flag.get_value()) == "not true"

    def test_switch_string_value_to_expression_and_back(self, connector, project_factory):
        """Switch a value between a string literal and an operator expression both ways."""
        project = project_factory(model="bike", kind="scripting")
        root = project.get_root_package()
        factory = Factory(project, connector)
        factory.create_attribute_usage(declared_name="second", owner=root, value=1)
        factory.create_attribute_usage(declared_name="notAttrStr", owner=root, value="not false")

        assert root.notAttrStr.get_value()._value == "not false"

        root.notAttrStr.parse_and_set_value("second * 3")
        assert SysMLTools.serialize_expression(root.notAttrStr.get_value()) == "second * 3"

        root.notAttrStr.set_value("not true")
        assert root.notAttrStr.get_value()._value == "not true"

    def test_update_existing_attribute_value(self, connector, project_factory):
        """Update an already-created attribute value twice (same-type in place)."""
        project = project_factory(model="bike", kind="scripting")
        root = project.get_root_package()
        factory = Factory(project, connector)
        factory.create_attribute_usage(declared_name="first", owner=root)

        root.first.set_value("first_value")
        assert root.first.get_value()._value == "first_value"

        root.first.set_value("second_value")

        assert root.first.get_value()._value == "second_value"
