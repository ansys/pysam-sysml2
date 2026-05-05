"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.succession_flow_usage import SuccessionFlowUsage


class TestSuccessionFlowUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.SuccessionFlowUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return SuccessionFlowUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
