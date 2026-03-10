"""Generated  test class from metamodel."""


import pytest

from ansys.sam.sysml2.meta_model.attribute_usage import AttributeUsage


class TestAttributeUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.AttributeUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AttributeUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_attribute_definition(self, element):
        """Test getter for attribute definition property."""
        _ = element.attribute_definition
