"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.association import Association


class TestAssociation:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Association'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Association("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_association_end(self, element):
        """Test getter for association end property."""
        _ = element.association_end

    def test_related_type(self, element):
        """Test getter for related type property."""
        _ = element.related_type

    def test_source_type(self, element):
        """Test getter and setter for source type property."""
        value = "test_value"
        element.source_type = value
        assert element.source_type == value

    def test_target_type(self, element):
        """Test getter for target type property."""
        _ = element.target_type
