"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.function import Function


class TestFunction:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Function'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Function("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_expression(self, element):
        """Test getter for expression property."""
        _ = element.expression

    def test_result(self, element):
        """Test getter and setter for result property."""
        value = "test_value"
        element.result = value
        assert element.result == value

    def test_is_model_level_evaluable(self, element):
        """Test getter and setter for is model level evaluable property."""
        value = False
        element.is_model_level_evaluable = value
        assert element.is_model_level_evaluable == value
