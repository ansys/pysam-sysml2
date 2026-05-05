"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.interface_usage import InterfaceUsage


class TestInterfaceUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.InterfaceUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return InterfaceUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_interface_definition(self, element):
        """Test getter for interface definition property."""
        _ = element.interface_definition
