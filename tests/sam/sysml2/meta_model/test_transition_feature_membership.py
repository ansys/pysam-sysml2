"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.transition_feature_membership import TransitionFeatureMembership


class TestTransitionFeatureMembership:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.TransitionFeatureMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return TransitionFeatureMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_transition_feature(self, element):
        """Test getter and setter for transition feature property."""
        value = None
        element.transition_feature = value
        assert element.transition_feature == value

    def test_kind(self, element):
        """Test getter and setter for kind property."""
        value = None
        element.kind = value
        assert element.kind == value
