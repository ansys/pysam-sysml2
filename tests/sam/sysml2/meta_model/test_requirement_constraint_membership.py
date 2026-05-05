"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.requirement_constraint_membership import RequirementConstraintMembership


class TestRequirementConstraintMembership:
    """Test class for Java class 'com.ansys.metamodel.sysml2.RequirementConstraintMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return RequirementConstraintMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_kind(self, element):
        """Test getter and setter for kind property."""
        value = "test_value"
        element.kind = value
        assert element.kind == value

    def test_owned_constraint(self, element):
        """Test getter and setter for owned constraint property."""
        value = "test_value"
        element.owned_constraint = value
        assert element.owned_constraint == value

    def test_referenced_constraint(self, element):
        """Test getter and setter for referenced constraint property."""
        value = "test_value"
        element.referenced_constraint = value
        assert element.referenced_constraint == value
