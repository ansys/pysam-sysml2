"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.allocation_usage import AllocationUsage


class TestAllocationUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.AllocationUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AllocationUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_allocation_definition(self, element):
        """Test getter for allocation definition property."""
        _ = element.allocation_definition
