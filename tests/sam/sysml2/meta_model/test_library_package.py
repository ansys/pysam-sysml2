"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.library_package import LibraryPackage


class TestLibraryPackage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.LibraryPackage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return LibraryPackage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_is_standard(self, element):
        """Test getter and setter for is standard property."""
        value = False
        element.is_standard = value
        assert element.is_standard == value
