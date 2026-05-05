"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.objective_membership import ObjectiveMembership


class TestObjectiveMembership:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ObjectiveMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ObjectiveMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owned_objective_requirement(self, element):
        """Test getter and setter for owned objective requirement property."""
        value = "test_value"
        element.owned_objective_requirement = value
        assert element.owned_objective_requirement == value
