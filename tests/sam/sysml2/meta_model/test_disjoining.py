"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.disjoining import Disjoining


class TestDisjoining:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Disjoining'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Disjoining("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_disjoining_type(self, element):
        """Test getter and setter for disjoining type property."""
        value = "test_value"
        element.disjoining_type = value
        assert element.disjoining_type == value

    def test_owning_type(self, element):
        """Test getter and setter for owning type property."""
        value = "test_value"
        element.owning_type = value
        assert element.owning_type == value

    def test_type_disjoined(self, element):
        """Test getter and setter for type disjoined property."""
        value = "test_value"
        element.type_disjoined = value
        assert element.type_disjoined == value
