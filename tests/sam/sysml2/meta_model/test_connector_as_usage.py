"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.connector_as_usage import ConnectorAsUsage


class TestConnectorAsUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ConnectorAsUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ConnectorAsUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
