"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.concern_usage import ConcernUsage


class TestConcernUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ConcernUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ConcernUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_concern_definition(self, element):
        """Test getter and setter for concern definition property."""
        value = "test_value"
        element.concern_definition = value
        assert element.concern_definition == value
