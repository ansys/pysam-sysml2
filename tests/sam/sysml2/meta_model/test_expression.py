"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.expression import Expression


class TestExpression:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Expression'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Expression("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_function(self, element):
        """Test getter and setter for function property."""
        value = "test_value"
        element.function = value
        assert element.function == value

    def test_result(self, element):
        """Test getter and setter for result property."""
        value = None
        element.result = value
        assert element.result == value
