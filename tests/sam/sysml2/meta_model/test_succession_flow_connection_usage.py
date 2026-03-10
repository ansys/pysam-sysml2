"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.succession_flow_connection_usage import SuccessionFlowConnectionUsage


class TestSuccessionFlowConnectionUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.SuccessionFlowConnectionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return SuccessionFlowConnectionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
