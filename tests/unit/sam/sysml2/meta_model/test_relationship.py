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

from ansys.sam.sysml2.meta_model.relationship import Relationship


class TestRelationship:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Relationship'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Relationship("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_target(self, element):
        """Test getter for target property."""
        _ = element.target

    def test_source(self, element):
        """Test getter for source property."""
        _ = element.source

    def test_related_element(self, element):
        """Test getter for related element property."""
        _ = element.related_element

    def test_inheriting_element(self, element):
        """Test getter and setter for inheriting element property."""
        value = "test_value"
        element.inheriting_element = value
        assert element.inheriting_element == value

    def test_owned_related_element(self, element):
        """Test getter for owned related element property."""
        _ = element.owned_related_element

    def test_owning_related_element(self, element):
        """Test getter and setter for owning related element property."""
        value = "test_value"
        element.owning_related_element = value
        assert element.owning_related_element == value
