"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.metadata_usage import MetadataUsage


class TestMetadataUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.MetadataUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return MetadataUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_metadata_definition(self, element):
        """Test getter and setter for metadata definition property."""
        value = None
        element.metadata_definition = value
        assert element.metadata_definition == value
