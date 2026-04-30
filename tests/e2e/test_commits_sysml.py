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

"""E2E tests for commit operations against a real SAM product instance."""

import pytest

from ansys.sam.sysml2.dto.commit.commit_class import Commit
from ansys.sam.sysml2.dto.commit.data_version import DataVersion
from ansys.sam.sysml2.exception.connector_exception import BadRequestConnectionException

from .conftest import load_sysml_project


@pytest.mark.e2e
class TestCommitsSysML:

    def test_create_commit_successful(self, connector, project_manager):
        """Create a valid commit (rename element) via sysml project."""
        project = load_sysml_project(connector, project_manager, "bike")
        bike = project.get_root_package().get("Structure").get("Bike")
        bike_front_wheel = bike.get("frontWheel")
        bike_front_wheel_id = bike_front_wheel.id
        bike_front_wheel_type = type(bike_front_wheel)

        commit = Commit(project._id)
        change = DataVersion()
        change.identify(bike_front_wheel_id)
        change.add_change("@type", bike_front_wheel_type)
        change.add_change("name", "RenamedByE2ESysML")
        commit.add_change(change)

        response = connector.create_commit(project._id, commit.to_json())

        assert response["@type"] == "Commit"
        assert response["owningProject"]["@id"] == project._id

        connector.delete_project(project._id)

    def test_create_commit_set_attribute_via_sysml(self, connector, project_manager):
        """Set attribute via sysml API (.get() navigation), verify roundtrip."""
        project = load_sysml_project(connector, project_manager, "bike")
        bike = project.get_root_package().get("Structure").get("Bike")
        bike_front_wheel = bike.get("frontWheel")
        bike_front_wheel_rim = bike_front_wheel.get("rim")
        bike_front_wheel_rim_weight = bike_front_wheel_rim.get("weight")

        original_bike_front_wheel_rim_weight = bike_front_wheel_rim_weight.get_value()
        bike_front_wheel_rim_weight.parse_and_set_value("500 [g]")
        updated_bike_front_wheel_rim_weight = bike_front_wheel_rim_weight.get_value()

        assert updated_bike_front_wheel_rim_weight != original_bike_front_wheel_rim_weight
        assert updated_bike_front_wheel_rim_weight == (500, ['g'])

        connector.delete_project(project._id)

    def test_create_commit_empty_change_sysml(self, connector, project_manager):
        """Commit with no DataVersion raises BadRequestConnectionException (sysml project)."""
        project = load_sysml_project(connector, project_manager, "bike")

        commit = Commit(project._id)

        with pytest.raises(BadRequestConnectionException):
            connector.create_commit(project._id, commit.to_json())

        connector.delete_project(project._id)
