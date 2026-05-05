"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.rendering_definition import RenderingDefinition


class TestRenderingDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.RenderingDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return RenderingDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_rendering(self, element):
        """Test getter for rendering property."""
        _ = element.rendering
