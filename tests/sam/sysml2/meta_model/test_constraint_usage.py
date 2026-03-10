"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.constraint_usage import ConstraintUsage


class TestConstraintUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ConstraintUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ConstraintUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_set_kind(self, element):
        """Test getter for set kind property."""
        _ = element.set_kind

    def test_kind(self, element):
        """Test getter and setter for kind property."""
        value = None
        element.kind = value
        assert element.kind == value

    def test_constraint_definition(self, element):
        """Test getter and setter for constraint definition property."""
        value = "test_value"
        element.constraint_definition = value
        assert element.constraint_definition == value

    def test_constraint_expression(self, element):
        """Test getter and setter for constraint expression property."""
        value = None
        element.constraint_expression = value
        assert element.constraint_expression == value

    def test_set_constraint_expression(self, element):
        """Test getter for set constraint expression property."""
        _ = element.set_constraint_expression
