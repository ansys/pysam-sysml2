"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.subject_membership import SubjectMembership


class TestSubjectMembership:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.SubjectMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return SubjectMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owned_subject_parameter(self, element):
        """Test getter and setter for owned subject parameter property."""
        value = None
        element.owned_subject_parameter = value
        assert element.owned_subject_parameter == value
