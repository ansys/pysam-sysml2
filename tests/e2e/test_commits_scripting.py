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
from ansys.sam.sysml2.tools.factory import Factory

from .conftest import load_scripting_project


@pytest.mark.e2e
class TestCommitsScripting:

    def test_create_commit_successful(self, connector, project_manager):
        """Create a valid commit (rename element), verify server accepts it."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike
        bike_front_wheel = bike.frontWheel
        bike_front_wheel_id = bike_front_wheel._id
        bike_front_wheel_type = type(bike_front_wheel)

        commit = Commit(project._id)
        change = DataVersion()
        change.identify(bike_front_wheel_id)
        change.add_change("@type", bike_front_wheel_type)
        change.add_change("name", "RenamedByE2E")
        commit.add_change(change)

        response = connector.create_commit(project._id, commit.to_json())

        assert response["@type"] == "Commit"
        assert response["owningProject"]["@id"] == project._id

        connector.delete_project(project._id)

    def test_create_commit_set_attribute(self, connector, project_manager):
        """Set attribute via scripting API, verify roundtrip."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike
        bike_front_wheel_rim_weight = bike.frontWheel.rim.weight
        original_front_wheel_rim_weight = bike_front_wheel_rim_weight.get_value()

        assert original_front_wheel_rim_weight == (1,['kg'])

        bike_front_wheel_rim_weight.parse_and_set_value("500 [g]")
        updated_front_wheel_rim_weight = bike_front_wheel_rim_weight.get_value()

        assert updated_front_wheel_rim_weight != original_front_wheel_rim_weight
        assert updated_front_wheel_rim_weight == (500,["g"])

        connector.delete_project(project._id)

    def test_create_commit_empty_change(self, connector, project_manager):
        """Commit with no DataVersion raises BadRequestConnectionException."""
        project = load_scripting_project(connector, project_manager, "bike")

        commit = Commit(project._id)

        with pytest.raises(BadRequestConnectionException):
            connector.create_commit(project._id, commit.to_json())

        connector.delete_project(project._id)

    def test_create_commit_none_type(self, connector, project_manager):
        """Commit for new element with None @type raises BadRequestConnectionException."""
        project = load_scripting_project(connector, project_manager, "bike")

        commit = Commit(project._id)
        change = DataVersion()
        change.add_change("@type", None)
        commit.add_change(change)

        with pytest.raises(BadRequestConnectionException):
            connector.create_commit(project._id, commit.to_json())

        connector.delete_project(project._id)

    def test_create_commit_missing_type(self, connector, project_manager):
        """Commit for new element without @type raises BadRequestConnectionException."""
        project = load_scripting_project(connector, project_manager, "bike")

        commit = Commit(project._id)
        change = DataVersion()
        commit.add_change(change)

        with pytest.raises(BadRequestConnectionException):
            connector.create_commit(project._id, commit.to_json())

        connector.delete_project(project._id)

    def test_create_commit_invalid_key(self, connector, project_manager):
        """Commit with invalid key raises BadRequestConnectionException."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike
        bike_front_wheel = bike.frontWheel
        bike_front_wheel_id = bike_front_wheel._id

        commit = Commit(project._id)
        change = DataVersion()
        change.identify(bike_front_wheel_id)
        change.add_change("invalidKey", "SomeValue")
        commit.add_change(change)

        with pytest.raises(BadRequestConnectionException):
            connector.create_commit(project._id, commit.to_json())

        connector.delete_project(project._id)

    def test_create_commit_invalid_attribute_type(self, connector, project_manager):
        """Commit with wrong value type raises BadRequestConnectionException."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike
        bike_front_wheel = bike.frontWheel
        bike_front_wheel_id = bike_front_wheel._id

        commit = Commit(project._id)
        change = DataVersion()
        change.identify(bike_front_wheel_id)
        change.add_change("name", ["NotAString"])
        commit.add_change(change)

        with pytest.raises(BadRequestConnectionException):
            connector.create_commit(project._id, commit.to_json())

        connector.delete_project(project._id)

    def test_create_commit_replace_list(self, connector, project_manager):
        """Create a RequirementUsage, set its _text list, then replace it."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike

        factory = Factory(project, connector)
        req = factory.create_requirement_usage(name="testReq", owner=bike)

        req._text.extend([
            "The bicycle shall not exceed 15 kg.",
            "Measured under standard conditions.",
            "Excludes accessories.",
        ])
        text_after_set = project.get_root_package().Structure.Bike.testReq._text
        assert len(text_after_set) == 3
        assert text_after_set[1] == "Measured under standard conditions."

        req._text.clear()
        req._text.extend([
            "The bicycle shall not exceed 15 kg.",
            "Measured under ISO conditions.",
            "Excludes accessories.",
        ])
        text_after_replace = project.get_root_package().Structure.Bike.testReq._text
        assert len(text_after_replace) == 3
        assert text_after_replace[1] == "Measured under ISO conditions."

        connector.delete_project(project._id)

    def test_create_commit_set_invalid_key_via_scripting(
        self, connector, project_manager
    ):
        """Setting invalid attribute via scripting API raises BadRequestConnectionException."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike

        with pytest.raises(BadRequestConnectionException):
            bike._invalidKey = "SomeValue"

        connector.delete_project(project._id)