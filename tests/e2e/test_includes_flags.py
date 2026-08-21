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

"""E2E tests for client-side reconstitution when includes_derived is False."""

import pytest

from ansys.sam.sysml2.meta_model.part_definition import PartDefinition
from ansys.sam.sysml2.meta_model.part_usage import PartUsage
from ansys.sam.sysml2.meta_model.requirement_usage import RequirementUsage
from ansys.sam.sysml2.tools.sysmltools import SysMLTools

_BIKE_WEIGHT_TEXT = "Weight of bike shall be less than 12 kg."


@pytest.mark.e2e
class TestIncludesFlags:

    @pytest.mark.parametrize("kind", ["sysml", "scripting"])
    def test_bike_navigation_without_derived(self, connector, project_factory, kind):
        """Navigate Structure.Bike with includes_derived=False and check reconstitution."""
        project = project_factory(
            model="bike",
            kind=kind,
            includes_derived=False,
            includes_inherited=True,
        )

        if kind == "sysml":
            structure = project.get_root_package().get("Structure")
            bike = structure.get("Bike")
            front_wheel = bike.get("frontWheel")
            rim = front_wheel.get("rim")

            assert structure.declared_name == "Structure"
            assert isinstance(bike, PartDefinition)
            assert bike.declared_name == "Bike"
            assert isinstance(front_wheel, PartUsage)
            assert front_wheel.declared_name == "frontWheel"
            assert isinstance(rim, PartUsage)
            assert rim.declared_name == "rim"
            assert len(bike.owned_element) > 0

            bike_id = bike.id
            front_wheel_id = front_wheel.id
            owned_child_ids = {child.id for child in bike.owned_element}
        else:
            bike = project.get_root_package().Structure.Bike
            front_wheel = bike.frontWheel
            rim = front_wheel.rim

            assert SysMLTools.isinstance(bike, "PartDefinition")
            assert bike._declaredName == "Bike"
            assert SysMLTools.isinstance(front_wheel, "PartUsage")
            assert front_wheel._declaredName == "frontWheel"
            assert SysMLTools.isinstance(rim, "PartUsage")
            assert rim._declaredName == "rim"
            assert len(bike._ownedElement) > 0

            bike_id = bike._id
            front_wheel_id = front_wheel._id
            owned_child_ids = {child._id for child in bike._ownedElement}

        lite = connector.get_all_elements(
            project.get_id(),
            includes_derived=False,
            includes_inherited=True,
        )
        bike_json = next(element for element in lite if element["@id"] == bike_id)
        assert "ownedElement" not in bike_json
        assert front_wheel_id in owned_child_ids

    @pytest.mark.parametrize("kind", ["sysml", "scripting"])
    def test_requirement_text_without_derived(self, connector, project_factory, kind):
        """Read BikeWeightValuesRedefined text/documentation with includes_derived=False."""
        project = project_factory(
            model="bike",
            kind=kind,
            includes_derived=False,
            includes_inherited=True,
        )

        if kind == "sysml":
            req = project.get_root_package().get("Requirements").get(
                "BikeWeightValuesRedefined"
            )
            assert isinstance(req, RequirementUsage)
            assert req.declared_name == "BikeWeightValuesRedefined"
            assert req.documentation[0].body == _BIKE_WEIGHT_TEXT
            assert _BIKE_WEIGHT_TEXT in req.text
            req_id = req.id
        else:
            req = project.get_root_package().Requirements.BikeWeightValuesRedefined
            assert SysMLTools.isinstance(req, "RequirementUsage")
            assert req._declaredName == "BikeWeightValuesRedefined"
            assert req._documentation[0]._body == _BIKE_WEIGHT_TEXT
            assert _BIKE_WEIGHT_TEXT in req._text
            req_id = req._id

        lite = connector.get_all_elements(
            project.get_id(),
            includes_derived=False,
            includes_inherited=True,
        )
        req_json = next(element for element in lite if element["@id"] == req_id)
        assert "text" not in req_json
