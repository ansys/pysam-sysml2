"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.relationship import Relationship


class TestRelationship:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Relationship'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Relationship("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_target(self, element):
        """Test getter for target property."""
        _ = element.target

    def test_source(self, element):
        """Test getter for source property."""
        _ = element.source

    def test_related_element(self, element):
        """Test getter for related element property."""
        _ = element.related_element

    def test_owned_related_element(self, element):
        """Test getter for owned related element property."""
        _ = element.owned_related_element

    def test_owning_related_element(self, element):
        """Test getter and setter for owning related element property."""
        value = None
        element.owning_related_element = value
        assert element.owning_related_element == value

    def test_inheriting_element(self, element):
        """Test getter and setter for inheriting element property."""
        value = "test_value"
        element.inheriting_element = value
        assert element.inheriting_element == value
