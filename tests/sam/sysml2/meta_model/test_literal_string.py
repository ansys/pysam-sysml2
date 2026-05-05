"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.literal_string import LiteralString


class TestLiteralString:
    """Test class for Java class 'com.ansys.metamodel.sysml2.LiteralString'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return LiteralString("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_value(self, element):
        """Test getter and setter for value property."""
        value = ""
        element.value = value
        assert element.value == value
