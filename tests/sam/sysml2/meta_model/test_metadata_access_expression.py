"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.metadata_access_expression import MetadataAccessExpression


class TestMetadataAccessExpression:
    """Test class for Java class 'com.ansys.metamodel.sysml2.MetadataAccessExpression'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return MetadataAccessExpression("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_referenced_element(self, element):
        """Test getter and setter for referenced element property."""
        value = "test_value"
        element.referenced_element = value
        assert element.referenced_element == value
