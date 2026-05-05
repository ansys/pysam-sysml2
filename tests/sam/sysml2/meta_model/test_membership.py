"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.membership import Membership


class TestMembership:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Membership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Membership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_member_element(self, element):
        """Test getter and setter for member element property."""
        value = "test_value"
        element.member_element = value
        assert element.member_element == value

    def test_member_element_id(self, element):
        """Test getter and setter for member element id property."""
        value = ""
        element.member_element_id = value
        assert element.member_element_id == value

    def test_member_name(self, element):
        """Test getter and setter for member name property."""
        value = ""
        element.member_name = value
        assert element.member_name == value

    def test_member_short_name(self, element):
        """Test getter and setter for member short name property."""
        value = ""
        element.member_short_name = value
        assert element.member_short_name == value

    def test_membership_owning_namespace(self, element):
        """Test getter and setter for membership owning namespace property."""
        value = "test_value"
        element.membership_owning_namespace = value
        assert element.membership_owning_namespace == value

    def test_visibility(self, element):
        """Test getter and setter for visibility property."""
        value = "test_value"
        element.visibility = value
        assert element.visibility == value

    def test_distinguishable_from(self, element):
        """Test getter for distinguishable from property."""
        _ = element.distinguishable_from
