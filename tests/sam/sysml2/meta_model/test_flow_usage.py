"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.flow_usage import FlowUsage


class TestFlowUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.FlowUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FlowUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_flow_definition(self, element):
        """Test getter for flow definition property."""
        _ = element.flow_definition
