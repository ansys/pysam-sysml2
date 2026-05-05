"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.result_expression_membership import ResultExpressionMembership


class TestResultExpressionMembership:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ResultExpressionMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ResultExpressionMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owned_result_expression(self, element):
        """Test getter and setter for owned result expression property."""
        value = "test_value"
        element.owned_result_expression = value
        assert element.owned_result_expression == value
