"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.membership import Membership


class TestMembership:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Membership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Membership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_member_name(self, element):
        """Test getter and setter for member name property."""
        value = ""
        element.member_name = value
        assert element.member_name == value

    def test_member_element(self, element):
        """Test getter and setter for member element property."""
        value = None
        element.member_element = value
        assert element.member_element == value

    def test_owned_member_element(self, element):
        """Test getter and setter for owned member element property."""
        value = "test_value"
        element.owned_member_element = value
        assert element.owned_member_element == value

    def test_membership_owning_namespace(self, element):
        """Test getter and setter for membership owning namespace property."""
        value = None
        element.membership_owning_namespace = value
        assert element.membership_owning_namespace == value
