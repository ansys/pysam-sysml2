"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.viewpoint_definition import ViewpointDefinition


class TestViewpointDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ViewpointDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ViewpointDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_viewpoint_stakeholder(self, element):
        """Test getter for viewpoint stakeholder property."""
        _ = element.viewpoint_stakeholder
