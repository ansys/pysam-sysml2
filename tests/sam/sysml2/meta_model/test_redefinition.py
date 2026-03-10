"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.redefinition import Redefinition


class TestRedefinition:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Redefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Redefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_redefined_feature(self, element):
        """Test getter and setter for redefined feature property."""
        value = "test_value"
        element.redefined_feature = value
        assert element.redefined_feature == value

    def test_redefining_feature(self, element):
        """Test getter and setter for redefining feature property."""
        value = "test_value"
        element.redefining_feature = value
        assert element.redefining_feature == value
