"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.flow_connection_definition import FlowConnectionDefinition


class TestFlowConnectionDefinition:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.FlowConnectionDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FlowConnectionDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
