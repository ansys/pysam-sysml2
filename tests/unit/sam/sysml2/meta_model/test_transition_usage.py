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

from ansys.sam.sysml2.meta_model.transition_usage import TransitionUsage


class TestTransitionUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.TransitionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return TransitionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_target(self, element):
        """Test getter and setter for target property."""
        value = "test_value"
        element.target = value
        assert element.target == value

    def test_source(self, element):
        """Test getter and setter for source property."""
        value = "test_value"
        element.source = value
        assert element.source == value

    def test_inherited_guard_expression(self, element):
        """Test getter for inherited guard expression property."""
        _ = element.inherited_guard_expression

    def test_inherited_trigger_action(self, element):
        """Test getter for inherited trigger action property."""
        _ = element.inherited_trigger_action

    def test_inherited_effect_action(self, element):
        """Test getter for inherited effect action property."""
        _ = element.inherited_effect_action

    def test_succession(self, element):
        """Test getter and setter for succession property."""
        value = "test_value"
        element.succession = value
        assert element.succession == value

    def test_guard_expression(self, element):
        """Test getter for guard expression property."""
        _ = element.guard_expression

    def test_trigger_action(self, element):
        """Test getter for trigger action property."""
        _ = element.trigger_action

    def test_effect_action(self, element):
        """Test getter for effect action property."""
        _ = element.effect_action
