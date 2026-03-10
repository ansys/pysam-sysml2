"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.literal_integer import LiteralInteger


class TestLiteralInteger:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.LiteralInteger'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return LiteralInteger("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_value(self, element):
        """Test getter and setter for value property."""
        value = 0
        element.value = value
        assert element.value == value
