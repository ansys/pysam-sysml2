"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.feature_chain_expression import FeatureChainExpression


class TestFeatureChainExpression:
    """Test class for Java class 'com.ansys.metamodel.sysml2.FeatureChainExpression'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FeatureChainExpression("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_target_feature(self, element):
        """Test getter and setter for target feature property."""
        value = "test_value"
        element.target_feature = value
        assert element.target_feature == value
