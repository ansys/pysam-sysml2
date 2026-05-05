"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.comment import Comment


class TestComment:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Comment'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Comment("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_body(self, element):
        """Test getter and setter for body property."""
        value = ""
        element.body = value
        assert element.body == value

    def test_locale(self, element):
        """Test getter and setter for locale property."""
        value = ""
        element.locale = value
        assert element.locale == value
