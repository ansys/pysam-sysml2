"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.view_rendering_membership import ViewRenderingMembership


class TestViewRenderingMembership:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ViewRenderingMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ViewRenderingMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owned_rendering(self, element):
        """Test getter and setter for owned rendering property."""
        value = "test_value"
        element.owned_rendering = value
        assert element.owned_rendering == value

    def test_referenced_rendering(self, element):
        """Test getter and setter for referenced rendering property."""
        value = "test_value"
        element.referenced_rendering = value
        assert element.referenced_rendering == value
