"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.literal_rational import LiteralRational


class TestLiteralRational:
    """Test class for Java class 'com.ansys.metamodel.sysml2.LiteralRational'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return LiteralRational("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_value(self, element):
        """Test getter and setter for value property."""
        value = 0.0
        element.value = value
        assert element.value == value
