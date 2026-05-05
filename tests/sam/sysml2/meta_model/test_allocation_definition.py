"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.allocation_definition import AllocationDefinition


class TestAllocationDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.AllocationDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AllocationDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_allocation(self, element):
        """Test getter for allocation property."""
        _ = element.allocation
