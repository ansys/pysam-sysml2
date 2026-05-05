"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.relationship import Relationship


class TestRelationship:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Relationship'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Relationship("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owned_related_element(self, element):
        """Test getter for owned related element property."""
        _ = element.owned_related_element

    def test_owning_related_element(self, element):
        """Test getter and setter for owning related element property."""
        value = "test_value"
        element.owning_related_element = value
        assert element.owning_related_element == value

    def test_related_element(self, element):
        """Test getter for related element property."""
        _ = element.related_element

    def test_relationship_owner(self, element):
        """Test getter and setter for relationship owner property."""
        value = "test_value"
        element.relationship_owner = value
        assert element.relationship_owner == value

    def test_source(self, element):
        """Test getter for source property."""
        _ = element.source

    def test_target(self, element):
        """Test getter for target property."""
        _ = element.target

    def test_is_implied(self, element):
        """Test getter and setter for is implied property."""
        value = False
        element.is_implied = value
        assert element.is_implied == value
