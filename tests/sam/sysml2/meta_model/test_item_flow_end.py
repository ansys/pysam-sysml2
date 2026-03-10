"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.item_flow_end import ItemFlowEnd


class TestItemFlowEnd:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ItemFlowEnd'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ItemFlowEnd("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
