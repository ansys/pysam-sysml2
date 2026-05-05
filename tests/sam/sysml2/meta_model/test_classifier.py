"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.classifier import Classifier


class TestClassifier:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Classifier'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Classifier("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owned_subclassification(self, element):
        """Test getter for owned subclassification property."""
        _ = element.owned_subclassification
