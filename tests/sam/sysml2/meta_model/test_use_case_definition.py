"""Generated  test class from metamodel."""


import pytest

from ansys.sam.sysml2.meta_model.use_case_definition import UseCaseDefinition


class TestUseCaseDefinition:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.UseCaseDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return UseCaseDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_included_use_case(self, element):
        """Test getter for included use case property."""
        _ = element.included_use_case
