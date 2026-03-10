"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.multiplicity_range import MultiplicityRange


class TestMultiplicityRange:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.MultiplicityRange'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return MultiplicityRange("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_lower_bound(self, element):
        """Test getter and setter for lower bound property."""
        value = "test_value"
        element.lower_bound = value
        assert element.lower_bound == value

    def test_upper_bound(self, element):
        """Test getter and setter for upper bound property."""
        value = "test_value"
        element.upper_bound = value
        assert element.upper_bound == value

    def test_bound(self, element):
        """Test getter for bound property."""
        _ = element.bound
