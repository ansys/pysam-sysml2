"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.calculation_definition import CalculationDefinition


class TestCalculationDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.CalculationDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return CalculationDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_calculation(self, element):
        """Test getter for calculation property."""
        _ = element.calculation
