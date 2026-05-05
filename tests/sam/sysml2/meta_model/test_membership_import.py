"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.membership_import import MembershipImport


class TestMembershipImport:
    """Test class for Java class 'com.ansys.metamodel.sysml2.MembershipImport'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return MembershipImport("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_imported_membership(self, element):
        """Test getter and setter for imported membership property."""
        value = "test_value"
        element.imported_membership = value
        assert element.imported_membership == value
