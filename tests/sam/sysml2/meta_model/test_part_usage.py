"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.part_usage import PartUsage


class TestPartUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.PartUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return PartUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_all_part_definition(self, element):
        """Test getter for all part definition property."""
        _ = element.all_part_definition

    def test_part_definition(self, element):
        """Test getter for part definition property."""
        _ = element.part_definition

    def test_is_actor(self, element):
        """Test getter and setter for is actor property."""
        value = False
        element.is_actor = value
        assert element.is_actor == value

    def test_is_stakeholder(self, element):
        """Test getter and setter for is stakeholder property."""
        value = False
        element.is_stakeholder = value
        assert element.is_stakeholder == value
