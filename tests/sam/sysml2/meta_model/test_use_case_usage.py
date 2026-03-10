"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.use_case_usage import UseCaseUsage


class TestUseCaseUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.UseCaseUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return UseCaseUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_included_use_case(self, element):
        """Test getter for included use case property."""
        _ = element.included_use_case

    def test_use_case_definition(self, element):
        """Test getter and setter for use case definition property."""
        value = "test_value"
        element.use_case_definition = value
        assert element.use_case_definition == value
