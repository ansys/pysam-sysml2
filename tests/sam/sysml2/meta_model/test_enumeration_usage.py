"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.enumeration_usage import EnumerationUsage


class TestEnumerationUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.EnumerationUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return EnumerationUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_enumeration_definition(self, element):
        """Test getter and setter for enumeration definition property."""
        value = "test_value"
        element.enumeration_definition = value
        assert element.enumeration_definition == value
