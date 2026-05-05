"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.namespace import Namespace


class TestNamespace:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Namespace'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Namespace("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_imported_membership(self, element):
        """Test getter for imported membership property."""
        _ = element.imported_membership

    def test_member(self, element):
        """Test getter for member property."""
        _ = element.member

    def test_membership(self, element):
        """Test getter for membership property."""
        _ = element.membership

    def test_owned_import(self, element):
        """Test getter for owned import property."""
        _ = element.owned_import

    def test_owned_member(self, element):
        """Test getter for owned member property."""
        _ = element.owned_member

    def test_owned_membership(self, element):
        """Test getter for owned membership property."""
        _ = element.owned_membership
