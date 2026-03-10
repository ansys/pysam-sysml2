"""Generated  test class from metamodel."""


import pytest

from ansys.sam.sysml2.meta_model.view_definition import ViewDefinition


class TestViewDefinition:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ViewDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ViewDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_view(self, element):
        """Test getter for view property."""
        _ = element.view

    def test_view_condition(self, element):
        """Test getter for view condition property."""
        _ = element.view_condition
