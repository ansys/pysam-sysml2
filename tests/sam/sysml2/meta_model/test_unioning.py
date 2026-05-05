"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.unioning import Unioning


class TestUnioning:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Unioning'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Unioning("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_type_unioned(self, element):
        """Test getter and setter for type unioned property."""
        value = "test_value"
        element.type_unioned = value
        assert element.type_unioned == value

    def test_unioning_type(self, element):
        """Test getter and setter for unioning type property."""
        value = "test_value"
        element.unioning_type = value
        assert element.unioning_type == value
