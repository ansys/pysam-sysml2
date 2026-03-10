"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.assert_constraint_usage import AssertConstraintUsage


class TestAssertConstraintUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.AssertConstraintUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AssertConstraintUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_asserted_constraint(self, element):
        """Test getter and setter for asserted constraint property."""
        value = "test_value"
        element.asserted_constraint = value
        assert element.asserted_constraint == value
