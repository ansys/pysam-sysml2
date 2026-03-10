"""Generated  test class from metamodel."""


import pytest

from ansys.sam.sysml2.meta_model.flow_connection_usage import FlowConnectionUsage


class TestFlowConnectionUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.FlowConnectionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FlowConnectionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_flow_connection_definition(self, element):
        """Test getter for flow connection definition property."""
        _ = element.flow_connection_definition
