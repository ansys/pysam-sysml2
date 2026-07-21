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

"""E2E tests based on the computer cost model example (computer-cost.py)."""

import pytest

from ansys.sam.sysml2.exception.runtime_exception import UnsupportedValueExpression
from ansys.sam.sysml2.meta_model.part_usage import PartUsage
from ansys.sam.sysml2.tools.sysmltools import SysMLTools


def _cost_amount(value):
    """Return the integer cost from a value element (plain literal or ``N [unit]``)."""
    try:
        rendered = SysMLTools.serialize_expression(value)
    except UnsupportedValueExpression:
        return None
    return int(rendered.split()[0]) if rendered else None


def _assess_cost_scripting(element):
    """Recursively calculate cost from the model tree."""
    if getattr(element, "cost", None):
        amount = _cost_amount(element.cost.get_value())
        if amount is not None:
            return amount
    cost = 0
    for sub_element in element._ownedElement:
        if SysMLTools.isinstance(sub_element, "PartUsage"):
            cost += _assess_cost_scripting(sub_element)
    return cost


def _assess_cost_sysml(element):
    """Recursively calculate cost from the model tree."""
    cost_feature = element.get("cost")
    if cost_feature is not None:
        amount = _cost_amount(cost_feature.get_value())
        if amount is not None:
            return amount
    cost = 0
    for sub_element in element.owned_element:
        if isinstance(sub_element, PartUsage):
            cost += _assess_cost_sysml(sub_element)
    return cost


@pytest.mark.e2e
class TestComputer:

    def test_computer_cost_scripting(self, project_factory):
        """Load computer model via scripting, compute cost for each real system."""
        project = project_factory(model="computer", kind="scripting")
        real_systems = project.get_root_package().RealSystems

        total_cost = 0
        for system in real_systems._ownedElement:
            system_cost = _assess_cost_scripting(system)
            assert system_cost >= 0
            total_cost += system_cost

        assert total_cost == 2900

    def test_computer_cost_sysml(self, project_factory):
        """Load computer model via sysml, compute cost for each real system."""
        project = project_factory(model="computer", kind="sysml")
        real_systems = project.get_root_package().get("RealSystems")

        total_cost = 0
        for system in real_systems.owned_element:
            system_cost = _assess_cost_sysml(system)
            assert system_cost >= 0
            total_cost += system_cost

        assert total_cost == 2900
