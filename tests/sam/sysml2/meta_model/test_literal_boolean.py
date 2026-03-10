"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.literal_boolean import LiteralBoolean


class TestLiteralBoolean:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.LiteralBoolean'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return LiteralBoolean("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_value(self, element):
        """Test getter and setter for value property."""
        value = None
        element.value = value
        assert element.value == value
