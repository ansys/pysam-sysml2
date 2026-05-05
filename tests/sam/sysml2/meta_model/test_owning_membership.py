"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.owning_membership import OwningMembership


class TestOwningMembership:
    """Test class for Java class 'com.ansys.metamodel.sysml2.OwningMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return OwningMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owned_member_element(self, element):
        """Test getter and setter for owned member element property."""
        value = "test_value"
        element.owned_member_element = value
        assert element.owned_member_element == value

    def test_owned_member_element_id(self, element):
        """Test getter and setter for owned member element id property."""
        value = ""
        element.owned_member_element_id = value
        assert element.owned_member_element_id == value

    def test_owned_member_name(self, element):
        """Test getter and setter for owned member name property."""
        value = ""
        element.owned_member_name = value
        assert element.owned_member_name == value

    def test_owned_member_short_name(self, element):
        """Test getter and setter for owned member short name property."""
        value = ""
        element.owned_member_short_name = value
        assert element.owned_member_short_name == value
