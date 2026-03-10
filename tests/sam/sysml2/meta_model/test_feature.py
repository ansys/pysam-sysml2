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

from ansys.sam.sysml2.meta_model.feature import Feature


class TestFeature:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Feature'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Feature("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_inherited(self, element):
        """Test getter for inherited property."""
        _ = element.inherited

    def test_type_(self, element):
        """Test getter for type property."""
        _ = element.type_

    def test_default_value(self, element):
        """Test getter and setter for default value property."""
        value = "test_value"
        element.default_value = value
        assert element.default_value == value

    def test_inherited_type(self, element):
        """Test getter for inherited type property."""
        _ = element.inherited_type

    def test_inheriting_type(self, element):
        """Test getter and setter for inheriting type property."""
        value = "test_value"
        element.inheriting_type = value
        assert element.inheriting_type == value

    def test_is_composite(self, element):
        """Test getter and setter for is composite property."""
        value = False
        element.is_composite = value
        assert element.is_composite == value

    def test_is_end(self, element):
        """Test getter and setter for is end property."""
        value = False
        element.is_end = value
        assert element.is_end == value

    def test_declaration(self, element):
        """Test getter for declaration property."""
        _ = element.declaration

    def test_owned_subsetting(self, element):
        """Test getter for owned subsetting property."""
        _ = element.owned_subsetting

    def test_direction(self, element):
        """Test getter and setter for direction property."""
        value = "test_value"
        element.direction = value
        assert element.direction == value

    def test_chaining_feature(self, element):
        """Test getter for chaining feature property."""
        _ = element.chaining_feature

    def test_valuation(self, element):
        """Test getter and setter for valuation property."""
        value = "test_value"
        element.valuation = value
        assert element.valuation == value

    def test_owned_typing(self, element):
        """Test getter for owned typing property."""
        _ = element.owned_typing

    def test_set_is_composite(self, element):
        """Test getter for set is composite property."""
        _ = element.set_is_composite

    def test_set_direction(self, element):
        """Test getter for set direction property."""
        _ = element.set_direction

    def test_is_ordered(self, element):
        """Test getter and setter for is ordered property."""
        value = None
        element.is_ordered = value
        assert element.is_ordered == value

    def test_is_unique(self, element):
        """Test getter and setter for is unique property."""
        value = False
        element.is_unique = value
        assert element.is_unique == value

    def test_set_is_ordered(self, element):
        """Test getter for set is ordered property."""
        _ = element.set_is_ordered

    def test_set_is_unique(self, element):
        """Test getter for set is unique property."""
        _ = element.set_is_unique

    def test_set_default_value(self, element):
        """Test getter for set default value property."""
        _ = element.set_default_value

    def test_set_valuation(self, element):
        """Test getter for set valuation property."""
        _ = element.set_valuation

    def test_referenced_feature(self, element):
        """Test getter for referenced feature property."""
        _ = element.referenced_feature

    def test_feature_value_expression(self, element):
        """Test getter and setter for feature value expression property."""
        value = "test_value"
        element.feature_value_expression = value
        assert element.feature_value_expression == value

    def test_owned_reference_subsetting(self, element):
        """Test getter for owned reference subsetting property."""
        _ = element.owned_reference_subsetting

    def test_owned_redefinition(self, element):
        """Test getter for owned redefinition property."""
        _ = element.owned_redefinition

    def test_owned_type_featuring(self, element):
        """Test getter for owned type featuring property."""
        _ = element.owned_type_featuring

    def test_owning_feature_membership(self, element):
        """Test getter and setter for owning feature membership property."""
        value = "test_value"
        element.owning_feature_membership = value
        assert element.owning_feature_membership == value

    def test_subsetted_feature(self, element):
        """Test getter for subsetted feature property."""
        _ = element.subsetted_feature

    def test_redefined_feature(self, element):
        """Test getter for redefined feature property."""
        _ = element.redefined_feature

    def test_set_feature_value_expression(self, element):
        """Test getter for set feature value expression property."""
        _ = element.set_feature_value_expression

    def test_all_redefinitions(self, element):
        """Test getter for all redefinitions property."""
        _ = element.all_redefinitions
