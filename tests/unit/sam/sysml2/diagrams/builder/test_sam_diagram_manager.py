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

"""Unit tests for SAMDiagramManager using MockedConnector + MockedSamApiConnector."""

import pytest

from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.scripting_project import ScriptingProject
from ansys.sam.sysml2.diagrams.sam_diagram_manager import SAMDiagramManager
from tests.unit.const import PROJECT_ID_5


def get_diagrams(element):
    return element.__diagram


class TestSAMDiagramManager:

    @pytest.fixture
    def project_5(self, connector) -> ScriptingProject:
        manager = SysML2ProjectManager(connector)
        return manager.get_scripting_project(PROJECT_ID_5)

    def test_load_diagrams(self, sam_connector, project_5):
        with SAMDiagramManager(sam_connector) as diagrams:
            diagrams.load_diagrams(project_5)

        package = project_5.get_root_package()
        bike = package.Bike
        assert len(get_diagrams(package)) == 1
        assert len(get_diagrams(bike)) == 1

        diagram = get_diagrams(package)[0]
        diagram_bike = get_diagrams(bike)[0]
        assert hasattr(diagram, "_name")
        assert hasattr(diagram_bike, "_name")
        assert diagram._name == "general diagram"
        assert diagram_bike._name == "general diagram"

    def test_navigation_through_diagrams(self, sam_connector, project_5):
        with SAMDiagramManager(sam_connector) as diagrams:
            diagrams.load_diagrams(project_5)

        package = project_5.get_root_package()
        diagram = get_diagrams(package)[0]
        owned = diagram._plane._owned_diagram_elements
        assert len(owned) == 10
        simple_nodes = [x for x in owned if x.__class__.__name__ == "SimpleNode"]
        for node in simple_nodes:
            assert hasattr(node, "_model_element")
        assert len(simple_nodes) == 5

    def test_points_correctly_typed(self, sam_connector, project_5):
        with SAMDiagramManager(sam_connector) as diagrams:
            diagrams.load_diagrams(project_5)

        package = project_5.get_root_package()
        diagram = get_diagrams(package)[0]
        owned = diagram._plane._owned_diagram_elements
        path_elements = [x for x in owned if x.__class__.__name__ == "Path"]
        assert len(path_elements) > 0

        point_elements = []
        for path in path_elements:
            if hasattr(path, "_points") and path._points:
                point_elements.extend(path._points)
        assert len(point_elements) > 0
        actual_points = [p for p in point_elements if p.__class__.__name__ == "Point"]
        assert len(actual_points) > 0
