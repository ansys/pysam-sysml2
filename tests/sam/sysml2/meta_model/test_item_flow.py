"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.item_flow import ItemFlow


class TestItemFlow:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ItemFlow'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ItemFlow("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_item_feature(self, element):
        """Test getter for item feature property."""
        _ = element.item_feature

    def test_item_flow_end(self, element):
        """Test getter for item flow end property."""
        _ = element.item_flow_end

    def test_item_type(self, element):
        """Test getter for item type property."""
        _ = element.item_type

    def test_target_input_feature(self, element):
        """Test getter for target input feature property."""
        _ = element.target_input_feature

    def test_source_output_feature(self, element):
        """Test getter for source output feature property."""
        _ = element.source_output_feature
