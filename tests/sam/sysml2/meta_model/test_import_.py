"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.import_ import Import


class TestImport:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Import'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Import("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_is_recursive(self, element):
        """Test getter and setter for is recursive property."""
        value = False
        element.is_recursive = value
        assert element.is_recursive == value

    def test_imported_namespace(self, element):
        """Test getter and setter for imported namespace property."""
        value = "test_value"
        element.imported_namespace = value
        assert element.imported_namespace == value
