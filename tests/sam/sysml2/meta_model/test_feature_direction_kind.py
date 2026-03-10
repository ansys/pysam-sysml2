"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.feature_direction_kind import FeatureDirectionKind


class TestFeatureDirectionKind:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.FeatureDirectionKind'."""

    @pytest.fixture
    def element(self):
        """Create test element."""
        return FeatureDirectionKind()

    def test_name(self, element):
        """Test getter for name property."""
        _ = element.name

    def test_value(self, element):
        """Test getter for value property."""
        _ = element.value

    def test_by_name(self, element):
        """Test getter for by name property."""
        _ = element.by_name

    def test_literal(self, element):
        """Test getter for literal property."""
        _ = element.literal
