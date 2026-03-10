"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.step import Step


class TestStep:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Step'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Step("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_parameter(self, element):
        """Test getter for parameter property."""
        _ = element.parameter

    def test_behavior(self, element):
        """Test getter for behavior property."""
        _ = element.behavior

    def test_general_parameter(self, element):
        """Test getter for general parameter property."""
        _ = element.general_parameter

    def test_transition_feature_kind(self, element):
        """Test getter and setter for transition feature kind property."""
        value = None
        element.transition_feature_kind = value
        assert element.transition_feature_kind == value
