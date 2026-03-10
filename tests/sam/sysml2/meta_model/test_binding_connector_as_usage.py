"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.binding_connector_as_usage import BindingConnectorAsUsage


class TestBindingConnectorAsUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.BindingConnectorAsUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return BindingConnectorAsUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
