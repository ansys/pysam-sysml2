"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.include_use_case_usage import IncludeUseCaseUsage


class TestIncludeUseCaseUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.IncludeUseCaseUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return IncludeUseCaseUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_use_case_included(self, element):
        """Test getter and setter for use case included property."""
        value = "test_value"
        element.use_case_included = value
        assert element.use_case_included == value
