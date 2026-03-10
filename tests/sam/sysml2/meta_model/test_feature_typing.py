"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.feature_typing import FeatureTyping


class TestFeatureTyping:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.FeatureTyping'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FeatureTyping("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_type_(self, element):
        """Test getter and setter for type property."""
        value = None
        element.type_ = value
        assert element.type_ == value

    def test_typed_feature(self, element):
        """Test getter and setter for typed feature property."""
        value = "test_value"
        element.typed_feature = value
        assert element.typed_feature == value

    def test_owning_feature(self, element):
        """Test getter and setter for owning feature property."""
        value = None
        element.owning_feature = value
        assert element.owning_feature == value
