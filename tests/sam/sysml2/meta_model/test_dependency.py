"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.dependency import Dependency


class TestDependency:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Dependency'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Dependency("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_client(self, element):
        """Test getter for client property."""
        _ = element.client

    def test_supplier(self, element):
        """Test getter for supplier property."""
        _ = element.supplier
