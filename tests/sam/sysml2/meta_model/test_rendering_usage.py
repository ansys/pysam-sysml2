"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.rendering_usage import RenderingUsage


class TestRenderingUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.RenderingUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return RenderingUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_rendering_definition(self, element):
        """Test getter and setter for rendering definition property."""
        value = "test_value"
        element.rendering_definition = value
        assert element.rendering_definition == value
