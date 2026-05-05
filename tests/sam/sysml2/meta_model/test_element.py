"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.element import Element


class TestElement:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Element'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Element("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_alias_ids(self, element):
        """Test getter for alias ids property."""
        _ = element.alias_ids

    def test_declared_name(self, element):
        """Test getter and setter for declared name property."""
        value = ""
        element.declared_name = value
        assert element.declared_name == value

    def test_declared_short_name(self, element):
        """Test getter and setter for declared short name property."""
        value = ""
        element.declared_short_name = value
        assert element.declared_short_name == value

    def test_documentation(self, element):
        """Test getter for documentation property."""
        _ = element.documentation

    def test_element_id(self, element):
        """Test getter and setter for element id property."""
        value = ""
        element.element_id = value
        assert element.element_id == value

    def test_name(self, element):
        """Test getter for name property."""
        _ = element.name

    def test_owned_annotation(self, element):
        """Test getter for owned annotation property."""
        _ = element.owned_annotation

    def test_owned_element(self, element):
        """Test getter for owned element property."""
        _ = element.owned_element

    def test_owned_relationship(self, element):
        """Test getter for owned relationship property."""
        _ = element.owned_relationship

    def test_owner(self, element):
        """Test getter and setter for owner property."""
        value = "test_value"
        element.owner = value
        assert element.owner == value

    def test_owning_membership(self, element):
        """Test getter and setter for owning membership property."""
        value = "test_value"
        element.owning_membership = value
        assert element.owning_membership == value

    def test_owning_namespace(self, element):
        """Test getter and setter for owning namespace property."""
        value = "test_value"
        element.owning_namespace = value
        assert element.owning_namespace == value

    def test_owning_relationship(self, element):
        """Test getter and setter for owning relationship property."""
        value = "test_value"
        element.owning_relationship = value
        assert element.owning_relationship == value

    def test_qualified_name(self, element):
        """Test getter for qualified name property."""
        _ = element.qualified_name

    def test_short_name(self, element):
        """Test getter for short name property."""
        _ = element.short_name

    def test_textual_representation(self, element):
        """Test getter for textual representation property."""
        _ = element.textual_representation

    def test_is_implied_included(self, element):
        """Test getter and setter for is implied included property."""
        value = False
        element.is_implied_included = value
        assert element.is_implied_included == value

    def test_is_library_element(self, element):
        """Test getter and setter for is library element property."""
        value = False
        element.is_library_element = value
        assert element.is_library_element == value
