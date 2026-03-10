"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.feature_chain_expression import FeatureChainExpression


class TestFeatureChainExpression:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.FeatureChainExpression'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FeatureChainExpression("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_target_feature(self, element):
        """Test getter for target feature property."""
        _ = element.target_feature
