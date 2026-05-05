"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.analysis_case_usage import AnalysisCaseUsage


class TestAnalysisCaseUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.AnalysisCaseUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AnalysisCaseUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_analysis_case_definition(self, element):
        """Test getter and setter for analysis case definition property."""
        value = "test_value"
        element.analysis_case_definition = value
        assert element.analysis_case_definition == value

    def test_result_expression(self, element):
        """Test getter and setter for result expression property."""
        value = "test_value"
        element.result_expression = value
        assert element.result_expression == value
