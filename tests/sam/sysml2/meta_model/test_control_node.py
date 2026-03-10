"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.control_node import ControlNode


class TestControlNode:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ControlNode'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ControlNode("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
