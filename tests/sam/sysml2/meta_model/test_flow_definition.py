"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.flow_definition import FlowDefinition


class TestFlowDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.FlowDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FlowDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_flow_end(self, element):
        """Test getter for flow end property."""
        _ = element.flow_end
