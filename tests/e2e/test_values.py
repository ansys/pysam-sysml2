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

from .conftest import load_scripting_project, load_sysml_project


@pytest.mark.e2e
class TestValues:

    def test_bike_weight_and_unit(self, connector, project_manager):
        """Navigate model, calculate total weight, checks weight and unit."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike
        bike_parts = [bike.frontWheel.rim.weight.get_value(), bike.frontWheel.tire.weight.get_value(), bike.rearWheel.rim.weight.get_value(), bike.rearWheel.tire.weight.get_value(), bike.frame.weight.get_value()]

        total_bike_weight = sum(bike_parts[part][0] for part in bike_parts)
        bike_first_part_weight_unit = bike_parts[0][1]
        bike_parts_weight_unit_all_same = all(x == bike_parts[1] for x in bike_parts)

        assert total_bike_weight == 10
        assert bike_first_part_weight_unit == "kg"
        assert bike_parts_weight_unit_all_same== True

        connector.delete_project(project._id)

    def test_bike_rim_weight_and_unit_update(self, connector, project_manager):
        """Update rim weight and unit, verify change."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike
        original_front_weight = bike.frontWheel.rim.weight.get_value()

        assert original_front_weight == (1, 'kg')

        bike.frontWheel.rim.weight.parse_and_set_value("500 [g]")
        updated_front_weight = bike.frontWheel.rim.weight.get_value()

        assert updated_front_weight != original_front_weight
        assert updated_front_weight == (500, 'g')

        connector.delete_project(project._id)

    def test_bike_rim_weight_transaction(self, connector, project_manager):
        """Transactional mode: batch updates, verify after commit."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike
        original_front_weight = bike.frontWheel.rim.weight.get_value()
        original_rear_weight = bike.rearWheel.rim.weight.get_value()

        assert original_front_weight == (1, 'kg')
        assert original_rear_weight == (1, 'kg')

        project.start_transactional_mode()
        bike.frontWheel.rim.weight.parse_and_set_value("500 [g]")
        bike.rearWheel.rim.weight.parse_and_set_value("750 [g]")
        project.stop_transactional_mode()

        updated_front_weight = bike.frontWheel.rim.weight.get_value()
        updated_rear_weight = bike.rearWheel.rim.weight.get_value()

        assert updated_front_weight == (500, 'g')
        assert updated_rear_weight == (750, 'g')

        connector.delete_project(project._id)

    def test_bike_create_element(self, connector, project_manager):
        """Create attribute on bike.frame, set value, verify roundtrip."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike
        factory = Factory(project, connector)
        factory.create_attribute_usage(name="length", owner=bike.frame)

        bike.frame.length.parse_and_set_value("60 [cm]")
        value = bike.frame.length.get_value()
        assert value == (60, "cm")

        connector.delete_project(project._id)

    def test_bike_sysml_project(self, connector, project_manager):
        """Load bike via load_sysml_project, navigate with .get(), verify structure (weight-bike-static.py)."""
        project = load_sysml_project(connector, project_manager, "bike")
        bike = project.get_root_package().get("Structure").get("Bike")
        bike_front_wheel = bike.get("frontWheel")
        bike_front_wheel_rim = bike_front_wheel.get("rim")
        bike_front_wheel_tire = bike_front_wheel.get("tire")
        bike_front_wheel_rim_weight = bike_front_wheel_rim.get("weight")
        bike_front_wheel_tire_weight = bike_front_wheel_tire.get("weight")
        bike_rear_wheel = bike.get("rearWheel")
        bike_rear_wheel_rim = bike_rear_wheel.get("rim")
        bike_rear_wheel_tire = bike_rear_wheel.get("tire")
        bike_rear_wheel_rim_weight = bike_rear_wheel_rim.get("weight")
        bike_rear_wheel_tire_weight = bike_rear_wheel_tire.get("weight")
        bike_parts = [bike_front_wheel_rim_weight, bike_front_wheel_tire_weight, bike_rear_wheel_rim_weight, bike_rear_wheel_tire_weight]

        total_bike_weight = sum(bike_parts[part][0] for part in bike_parts)
        bike_first_part_weight_unit = bike_parts[0][1]
        bike_parts_weight_unit_all_same = all(x == bike_parts[1] for x in bike_parts)

        assert total_bike_weight == 10
        assert bike_first_part_weight_unit == "kg"
        assert bike_parts_weight_unit_all_same== True

        connector.delete_project(project._id)

    def test_bike_delete_project(self, connector, project_manager):
        """Delete project and verify it raises ProjectNotFoundException."""
        project = load_scripting_project(connector, project_manager, "bike")
        project_id = project._id

        connector.delete_project(project_id)

        with pytest.raises(ProjectNotFoundException):
            connector.get_project_by_id(project_id)
