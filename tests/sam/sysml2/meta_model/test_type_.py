"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.type_ import Type


class TestType:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Type'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Type("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_multiplicity(self, element):
        """Test getter and setter for multiplicity property."""
        value = "test_value"
        element.multiplicity = value
        assert element.multiplicity == value

    def test_set_multiplicity(self, element):
        """Test getter for set multiplicity property."""
        _ = element.set_multiplicity

    def test_owned_end_feature(self, element):
        """Test getter for owned end feature property."""
        _ = element.owned_end_feature

    def test_is_sufficient(self, element):
        """Test getter and setter for is sufficient property."""
        value = False
        element.is_sufficient = value
        assert element.is_sufficient == value

    def test_is_abstract(self, element):
        """Test getter and setter for is abstract property."""
        value = False
        element.is_abstract = value
        assert element.is_abstract == value

    def test_owned_feature(self, element):
        """Test getter for owned feature property."""
        _ = element.owned_feature

    def test_set_is_abstract(self, element):
        """Test getter for set is abstract property."""
        _ = element.set_is_abstract

    def test_all_feature(self, element):
        """Test getter for all feature property."""
        _ = element.all_feature

    def test_directed_feature(self, element):
        """Test getter for directed feature property."""
        _ = element.directed_feature

    def test_feature(self, element):
        """Test getter for feature property."""
        _ = element.feature

    def test_owned_specialization(self, element):
        """Test getter for owned specialization property."""
        _ = element.owned_specialization

    def test_owned_inherited_feature(self, element):
        """Test getter for owned inherited feature property."""
        _ = element.owned_inherited_feature

    def test_owned_feature_membership(self, element):
        """Test getter for owned feature membership property."""
        _ = element.owned_feature_membership
