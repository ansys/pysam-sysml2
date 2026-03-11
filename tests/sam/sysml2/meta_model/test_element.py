# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.element import Element


class TestElement:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Element'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Element("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_name(self, element):
        """Test getter and setter for name property."""
        value = ""
        element.name = value
        assert element.name == value

    def test_owner(self, element):
        """Test getter and setter for owner property."""
        value = "test_value"
        element.owner = value
        assert element.owner == value

    def test_comment(self, element):
        """Test getter for comment property."""
        _ = element.comment

    def test_short_name(self, element):
        """Test getter and setter for short name property."""
        value = None
        element.short_name = value
        assert element.short_name == value

    def test_documentation(self, element):
        """Test getter for documentation property."""
        _ = element.documentation

    def test_owning_namespace(self, element):
        """Test getter and setter for owning namespace property."""
        value = "test_value"
        element.owning_namespace = value
        assert element.owning_namespace == value

    def test_owned_element(self, element):
        """Test getter for owned element property."""
        _ = element.owned_element

    def test_owned_annotation(self, element):
        """Test getter for owned annotation property."""
        _ = element.owned_annotation

    def test_qualified_name(self, element):
        """Test getter for qualified name property."""
        _ = element.qualified_name

    def test_alias_ids(self, element):
        """Test getter for alias ids property."""
        _ = element.alias_ids

    def test_visibility(self, element):
        """Test getter and setter for visibility property."""
        value = None
        element.visibility = value
        assert element.visibility == value

    def test_owned_relationship(self, element):
        """Test getter for owned relationship property."""
        _ = element.owned_relationship

    def test_textual_representation(self, element):
        """Test getter for textual representation property."""
        _ = element.textual_representation

    def test_owned_inherited_relationship(self, element):
        """Test getter for owned inherited relationship property."""
        _ = element.owned_inherited_relationship
