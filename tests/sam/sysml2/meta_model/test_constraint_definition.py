"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.constraint_definition import ConstraintDefinition


class TestConstraintDefinition:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ConstraintDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ConstraintDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_constraint_expression(self, element):
        """Test getter and setter for constraint expression property."""
        value = None
        element.constraint_expression = value
        assert element.constraint_expression == value

    def test_set_constraint_expression(self, element):
        """Test getter for set constraint expression property."""
        _ = element.set_constraint_expression
