"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.part_usage import PartUsage


class TestPartUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.PartUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return PartUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_part_definition(self, element):
        """Test getter for part definition property."""
        _ = element.part_definition
