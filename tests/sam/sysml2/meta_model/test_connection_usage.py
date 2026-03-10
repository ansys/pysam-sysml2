"""Generated  test class from metamodel."""


import pytest

from ansys.sam.sysml2.meta_model.connection_usage import ConnectionUsage


class TestConnectionUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ConnectionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ConnectionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_connection_definition(self, element):
        """Test getter for connection definition property."""
        _ = element.connection_definition
