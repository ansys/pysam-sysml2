"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.decision_node import DecisionNode


class TestDecisionNode:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.DecisionNode'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return DecisionNode("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
