"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.metadata_feature import MetadataFeature


class TestMetadataFeature:
    """Test class for Java class 'com.ansys.metamodel.sysml2.MetadataFeature'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return MetadataFeature("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_metaclass(self, element):
        """Test getter and setter for metaclass property."""
        value = "test_value"
        element.metaclass = value
        assert element.metaclass == value

    def test_semantic(self, element):
        """Test getter for semantic property."""
        _ = element.semantic

    def test_syntactic(self, element):
        """Test getter for syntactic property."""
        _ = element.syntactic
