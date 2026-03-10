"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.view_usage import ViewUsage


class TestViewUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ViewUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ViewUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_view_definition(self, element):
        """Test getter and setter for view definition property."""
        value = None
        element.view_definition = value
        assert element.view_definition == value
