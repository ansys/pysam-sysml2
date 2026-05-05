"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.stakeholder_membership import StakeholderMembership


class TestStakeholderMembership:
    """Test class for Java class 'com.ansys.metamodel.sysml2.StakeholderMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return StakeholderMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owned_stakeholder_parameter(self, element):
        """Test getter and setter for owned stakeholder parameter property."""
        value = "test_value"
        element.owned_stakeholder_parameter = value
        assert element.owned_stakeholder_parameter == value
