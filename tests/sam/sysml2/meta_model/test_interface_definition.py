"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.interface_definition import InterfaceDefinition


class TestInterfaceDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.InterfaceDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return InterfaceDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_interface_end(self, element):
        """Test getter for interface end property."""
        _ = element.interface_end
