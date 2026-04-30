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
from ansys.sam.sysml2.tools.sysmltools import SysMLTools

from .conftest import load_scripting_project, load_sysml_project


def _assess_cost(element):
    """Recursively calculate cost from the model tree."""
    if getattr(element, "cost"):
        try:
            cost = element.cost.get_value()
        except UnsupportedValueExpression:
            cost = None
        if cost is not None:
            if isinstance(cost,int):
                return cost
            elif isinstance(cost,tuple):
                return cost[0]
            else:
                raise ValueError(
                    f"Problem of value type for the cost of {element._name}"
                )
    cost = 0
    for sub_element in element._ownedElement:
        if SysMLTools.isinstance(sub_element, "PartUsage"):
            cost += _assess_cost(sub_element)
    return cost


@pytest.mark.e2e
class TestComputer:

    def test_computer_cost(self, connector, project_manager):
        """Load computer model, compute cost for each real system."""
        project = load_scripting_project(connector, project_manager, "computer")
        real_systems = project.get_root_package().RealSystems

        total_cost = 0
        for system in real_systems._ownedElement:
            system_cost = _assess_cost(system)
            assert system_cost >= 0
            total_cost += system_cost
        assert total_cost == 2900

        connector.delete_project(project._id)
