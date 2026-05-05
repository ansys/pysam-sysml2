"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.element_filter_membership import ElementFilterMembership


class TestElementFilterMembership:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ElementFilterMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ElementFilterMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_condition(self, element):
        """Test getter and setter for condition property."""
        value = "test_value"
        element.condition = value
        assert element.condition == value
