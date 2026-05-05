"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.enumeration_definition import EnumerationDefinition


class TestEnumerationDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.EnumerationDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return EnumerationDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_enumerated_value(self, element):
        """Test getter for enumerated value property."""
        _ = element.enumerated_value
