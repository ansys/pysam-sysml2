"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.variant_membership import VariantMembership


class TestVariantMembership:
    """Test class for Java class 'com.ansys.metamodel.sysml2.VariantMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return VariantMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owned_variant_usage(self, element):
        """Test getter and setter for owned variant usage property."""
        value = "test_value"
        element.owned_variant_usage = value
        assert element.owned_variant_usage == value
