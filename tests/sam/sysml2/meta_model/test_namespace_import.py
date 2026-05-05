"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.namespace_import import NamespaceImport


class TestNamespaceImport:
    """Test class for Java class 'com.ansys.metamodel.sysml2.NamespaceImport'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return NamespaceImport("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_imported_namespace(self, element):
        """Test getter and setter for imported namespace property."""
        value = "test_value"
        element.imported_namespace = value
        assert element.imported_namespace == value
