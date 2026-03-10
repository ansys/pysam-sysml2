"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.feature_reference_expression import FeatureReferenceExpression


class TestFeatureReferenceExpression:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.FeatureReferenceExpression'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FeatureReferenceExpression("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_referent(self, element):
        """Test getter for referent property."""
        _ = element.referent
