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

"""Unit tests for SysMLTools connection-end resolution on the Vehicle model."""

import pytest

from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.meta_model.connection_usage import ConnectionUsage
from ansys.sam.sysml2.meta_model.package import Package
from ansys.sam.sysml2.tools import SysMLTools
from tests.unit.const import PROJECT_ID_7


class TestFeatureChainingStatic:
    """resolve_feature_chaining on the metamodel (static) representation."""

    @pytest.fixture
    def project(self, connector):
        return SysML2ProjectManager(connector=connector).get_sysml_project(PROJECT_ID_7)

    def test_authoring_context_resolves_base_features(self, project):
        vehicle = project.get_root_package().get("Vehicle")
        connection = vehicle.get("ConnectionUsage::cac44166-105a-412b-ae47-b7fe2d1adb4c")

        source = SysMLTools().resolve_feature_chaining(connection, "source")
        target = SysMLTools().resolve_feature_chaining(connection, "target")

        assert source.declared_name == "chamber"
        assert target.declared_name == "fuel"

    def test_transit_context_resolves_renamed_redefinitions(self, project):
        transit = project.get_root_package().get("Transit")
        connection = transit.get("ConnectionUsage::cac44166-105a-412b-ae47-b7fe2d1adb4c")

        source = SysMLTools().resolve_feature_chaining(connection, "source")
        target = SysMLTools().resolve_feature_chaining(connection, "target")

        assert source.declared_name == "transitChamber"
        assert target.declared_name == "transitFuel"

    def test_electric_transit_context_resolves_deepest_redefinitions(self, project):
        electric = project.get_root_package().get("ElectricTransit")
        connection = electric.get("ConnectionUsage::cac44166-105a-412b-ae47-b7fe2d1adb4c")

        source, target = SysMLTools().get_connector_ends(connection)

        assert source.declared_name == "eChamber"
        assert target.declared_name == "eFuel"


class TestFeatureChainingScripting:
    """resolve_feature_chaining on the scripting representation."""

    @pytest.fixture
    def project(self, connector):
        return SysML2ProjectManager(connector=connector).get_scripting_project(PROJECT_ID_7)

    def test_authoring_context_resolves_base_features(self, project):
        vehicle = project.get_root_package().get("Vehicle")
        connection = vehicle.get("ConnectionUsage_cac44166_105a_412b_ae47_b7fe2d1adb4c")

        source = SysMLTools().resolve_feature_chaining(connection, "source")
        target = SysMLTools().resolve_feature_chaining(connection, "target")

        assert source._declaredName == "chamber"
        assert target._declaredName == "fuel"

    def test_transit_context_resolves_renamed_redefinitions(self, project):
        transit = project.get_root_package().get("Transit")
        connection = transit.get("ConnectionUsage_cac44166_105a_412b_ae47_b7fe2d1adb4c")

        source = SysMLTools().resolve_feature_chaining(connection, "source")
        target = SysMLTools().resolve_feature_chaining(connection, "target")

        assert source._declaredName == "transitChamber"
        assert target._declaredName == "transitFuel"

    def test_electric_transit_context_resolves_deepest_redefinitions(self, project):
        electric = project.get_root_package().get("ElectricTransit")
        connection = electric.get("ConnectionUsage_cac44166_105a_412b_ae47_b7fe2d1adb4c")

        source, target = SysMLTools().get_connector_ends(connection)

        assert source._declaredName == "eChamber"
        assert target._declaredName == "eFuel"


class TestFeatureChainingValidation:
    """Edge guards that need no project."""

    def test_invalid_end_raises(self):
        with pytest.raises(ValueError):
            SysMLTools().resolve_feature_chaining(ConnectionUsage("conn"), end="middle")

    def test_missing_end_returns_none(self):
        connection = ConnectionUsage("conn")
        connection._owner = Package("pkg")

        assert SysMLTools().resolve_feature_chaining(connection) is None
