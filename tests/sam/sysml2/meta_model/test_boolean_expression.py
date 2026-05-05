"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.boolean_expression import BooleanExpression


class TestBooleanExpression:
    """Test class for Java class 'com.ansys.metamodel.sysml2.BooleanExpression'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return BooleanExpression("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_predicate(self, element):
        """Test getter and setter for predicate property."""
        value = "test_value"
        element.predicate = value
        assert element.predicate == value
