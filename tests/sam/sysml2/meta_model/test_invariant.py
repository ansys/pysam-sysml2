"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.invariant import Invariant


class TestInvariant:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Invariant'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Invariant("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_is_negated(self, element):
        """Test getter and setter for is negated property."""
        value = False
        element.is_negated = value
        assert element.is_negated == value
