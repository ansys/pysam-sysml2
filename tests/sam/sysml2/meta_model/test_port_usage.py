"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.port_usage import PortUsage


class TestPortUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.PortUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return PortUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_port_definition(self, element):
        """Test getter for port definition property."""
        _ = element.port_definition
