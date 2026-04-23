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

from ansys.sam.sysml2.meta_model.state_usage import StateUsage


class TestStateUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.StateUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return StateUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_is_parallel(self, element):
        """Test getter and setter for is parallel property."""
        value = False
        element.is_parallel = value
        assert element.is_parallel == value

    def test_set_is_parallel(self, element):
        """Test getter for set is parallel property."""
        _ = element.set_is_parallel

    def test_do_action(self, element):
        """Test getter and setter for do action property."""
        value = "test_value"
        element.do_action = value
        assert element.do_action == value

    def test_entry_action(self, element):
        """Test getter and setter for entry action property."""
        value = "test_value"
        element.entry_action = value
        assert element.entry_action == value

    def test_set_do_action(self, element):
        """Test getter for set do action property."""
        _ = element.set_do_action

    def test_exit_action(self, element):
        """Test getter and setter for exit action property."""
        value = "test_value"
        element.exit_action = value
        assert element.exit_action == value

    def test_set_entry_action(self, element):
        """Test getter for set entry action property."""
        _ = element.set_entry_action

    def test_state_definition(self, element):
        """Test getter for state definition property."""
        _ = element.state_definition

    def test_set_exit_action(self, element):
        """Test getter for set exit action property."""
        _ = element.set_exit_action
