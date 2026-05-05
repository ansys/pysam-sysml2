"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.connector import Connector


class TestConnector:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Connector'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Connector("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_association(self, element):
        """Test getter for association property."""
        _ = element.association

    def test_connector_end(self, element):
        """Test getter for connector end property."""
        _ = element.connector_end

    def test_default_featuring_type(self, element):
        """Test getter and setter for default featuring type property."""
        value = "test_value"
        element.default_featuring_type = value
        assert element.default_featuring_type == value

    def test_related_feature(self, element):
        """Test getter for related feature property."""
        _ = element.related_feature

    def test_source_feature(self, element):
        """Test getter and setter for source feature property."""
        value = "test_value"
        element.source_feature = value
        assert element.source_feature == value

    def test_target_feature(self, element):
        """Test getter for target feature property."""
        _ = element.target_feature
