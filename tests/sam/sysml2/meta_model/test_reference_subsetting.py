"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.reference_subsetting import ReferenceSubsetting


class TestReferenceSubsetting:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ReferenceSubsetting'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ReferenceSubsetting("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_referenced_feature(self, element):
        """Test getter and setter for referenced feature property."""
        value = "test_value"
        element.referenced_feature = value
        assert element.referenced_feature == value

    def test_referencing_feature(self, element):
        """Test getter and setter for referencing feature property."""
        value = "test_value"
        element.referencing_feature = value
        assert element.referencing_feature == value
