"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.intersecting import Intersecting


class TestIntersecting:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Intersecting'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Intersecting("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_intersecting_type(self, element):
        """Test getter and setter for intersecting type property."""
        value = "test_value"
        element.intersecting_type = value
        assert element.intersecting_type == value

    def test_type_intersected(self, element):
        """Test getter and setter for type intersected property."""
        value = "test_value"
        element.type_intersected = value
        assert element.type_intersected == value
