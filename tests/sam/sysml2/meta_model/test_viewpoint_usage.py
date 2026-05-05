"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.viewpoint_usage import ViewpointUsage


class TestViewpointUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ViewpointUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ViewpointUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_viewpoint_definition(self, element):
        """Test getter and setter for viewpoint definition property."""
        value = "test_value"
        element.viewpoint_definition = value
        assert element.viewpoint_definition == value

    def test_viewpoint_stakeholder(self, element):
        """Test getter for viewpoint stakeholder property."""
        _ = element.viewpoint_stakeholder
