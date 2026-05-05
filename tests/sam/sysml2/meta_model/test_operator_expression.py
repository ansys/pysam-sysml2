"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.operator_expression import OperatorExpression


class TestOperatorExpression:
    """Test class for Java class 'com.ansys.metamodel.sysml2.OperatorExpression'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return OperatorExpression("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_operator(self, element):
        """Test getter and setter for operator property."""
        value = ""
        element.operator = value
        assert element.operator == value
