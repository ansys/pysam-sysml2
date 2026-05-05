"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.item_usage import ItemUsage


class TestItemUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ItemUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ItemUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_item_definition(self, element):
        """Test getter for item definition property."""
        _ = element.item_definition
