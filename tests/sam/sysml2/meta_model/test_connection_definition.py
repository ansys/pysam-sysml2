"""Generated  test class from metamodel."""


import pytest

from ansys.sam.sysml2.meta_model.connection_definition import ConnectionDefinition


class TestConnectionDefinition:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ConnectionDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ConnectionDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_connection_end(self, element):
        """Test getter for connection end property."""
        _ = element.connection_end
