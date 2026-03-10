"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.requirement_constraint_membership import RequirementConstraintMembership


class TestRequirementConstraintMembership:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.RequirementConstraintMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return RequirementConstraintMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_kind(self, element):
        """Test getter and setter for kind property."""
        value = None
        element.kind = value
        assert element.kind == value

    def test_constraint(self, element):
        """Test getter and setter for constraint property."""
        value = None
        element.constraint = value
        assert element.constraint == value
