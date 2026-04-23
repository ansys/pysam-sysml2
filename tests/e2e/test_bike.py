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
class TestBike:

    def test_bike_weight(self, connector, project_manager):
        """Navigate model, calculate total weight, assert == 10 (weight-bike.py)."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike

        bike_weight = (
            bike.frontWheel.rim.weight.get_value()[0]
            + bike.frontWheel.tire.weight.get_value()[0]
            + bike.rearWheel.rim.weight.get_value()[0]
            + bike.rearWheel.tire.weight.get_value()[0]
            + bike.frame.weight.get_value()[0]
        )
        assert bike_weight == 10

        connector.delete_project(project._id)

    def test_bike_rim_weight_update(self, connector, project_manager):
        """Update rim weight, verify change (bike-rim-weight-update.py)."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike

        original_front = bike.frontWheel.rim.weight.get_value()[0]
        bike.frontWheel.rim.weight.parse_and_set_value("0.5 [kg]")
        updated_front = bike.frontWheel.rim.weight.get_value()[0]
        assert updated_front != original_front

        connector.delete_project(project._id)

    def test_bike_rim_weight_transaction(self, connector, project_manager):
        """Transactional mode: batch updates, verify after commit."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike

        project.start_transactional_mode()
        bike.frontWheel.rim.weight.parse_and_set_value("0.5 [kg]")
        bike.rearWheel.rim.weight.parse_and_set_value("0.8 [kg]")
        project.stop_transactional_mode()

        updated_front = bike.frontWheel.rim.weight.get_value()
        updated_rear = bike.rearWheel.rim.weight.get_value()
        assert updated_front[0] == 0.5
        assert updated_front[1] == "kg"
        assert updated_rear[0] == 0.8
        assert updated_rear[1] == "kg"

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

        bike_weight = (
            bike.get("frontWheel").get("rim").get("weight").get_value()[0]
            + bike.get("frontWheel").get("tire").get("weight").get_value()[0]
            + bike.get("rearWheel").get("rim").get("weight").get_value()[0]
            + bike.get("rearWheel").get("tire").get("weight").get_value()[0]
            + bike.get("frame").get("weight").get_value()[0]
        )
        assert bike_weight == 10

        connector.delete_project(project._id)

    def test_bike_delete_project(self, connector, project_manager):
        """Delete project and verify it raises ProjectNotFoundException."""
        project = load_scripting_project(connector, project_manager, "bike")
        project_id = project._id

        connector.delete_project(project_id)

        with pytest.raises(ProjectNotFoundException):
            connector.get_project_by_id(project_id)
