"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.calculation_usage import CalculationUsage


class TestCalculationUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.CalculationUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return CalculationUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_calculation_definition(self, element):
        """Test getter and setter for calculation definition property."""
        value = "test_value"
        element.calculation_definition = value
        assert element.calculation_definition == value
