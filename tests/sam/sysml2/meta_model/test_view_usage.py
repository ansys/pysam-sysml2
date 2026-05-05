"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.view_usage import ViewUsage


class TestViewUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ViewUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ViewUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_exposed_element(self, element):
        """Test getter for exposed element property."""
        _ = element.exposed_element

    def test_satisfied_viewpoint(self, element):
        """Test getter for satisfied viewpoint property."""
        _ = element.satisfied_viewpoint

    def test_view_condition(self, element):
        """Test getter for view condition property."""
        _ = element.view_condition

    def test_view_definition(self, element):
        """Test getter and setter for view definition property."""
        value = "test_value"
        element.view_definition = value
        assert element.view_definition == value

    def test_view_rendering(self, element):
        """Test getter and setter for view rendering property."""
        value = "test_value"
        element.view_rendering = value
        assert element.view_rendering == value
