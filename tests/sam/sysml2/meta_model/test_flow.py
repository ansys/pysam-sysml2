"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.flow import Flow


class TestFlow:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Flow'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Flow("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_flow_end(self, element):
        """Test getter for flow end property."""
        _ = element.flow_end

    def test_interaction(self, element):
        """Test getter for interaction property."""
        _ = element.interaction

    def test_payload_feature(self, element):
        """Test getter and setter for payload feature property."""
        value = "test_value"
        element.payload_feature = value
        assert element.payload_feature == value

    def test_payload_type(self, element):
        """Test getter for payload type property."""
        _ = element.payload_type

    def test_source_output_feature(self, element):
        """Test getter and setter for source output feature property."""
        value = "test_value"
        element.source_output_feature = value
        assert element.source_output_feature == value

    def test_target_input_feature(self, element):
        """Test getter and setter for target input feature property."""
        value = "test_value"
        element.target_input_feature = value
        assert element.target_input_feature == value
