"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.framed_concern_membership import FramedConcernMembership


class TestFramedConcernMembership:
    """Test class for Java class 'com.ansys.metamodel.sysml2.FramedConcernMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FramedConcernMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owned_concern(self, element):
        """Test getter and setter for owned concern property."""
        value = "test_value"
        element.owned_concern = value
        assert element.owned_concern == value

    def test_referenced_concern(self, element):
        """Test getter and setter for referenced concern property."""
        value = "test_value"
        element.referenced_concern = value
        assert element.referenced_concern == value
