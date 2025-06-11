# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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

import pytest

from ansys.sam.sysml2.builder.classes.derived_list import DerivedList
from ansys.sam.sysml2.classes.sysml_element import SysMLElement


class TestDerivedList:
    @pytest.fixture
    def element(self):
        element = SysMLElement("")
        element.data = DerivedList(element, "data", *[1, 2, 3])
        element._IS_READ_ONLY = True
        return element

    #
    # These tests check if the list attribute is protected in read-only mode
    #

    def test_direct_assignment(self, element):
        element.data = [4, 5, 6]
        # Should be unchanged
        assert element.data == [1, 2, 3]

    def test_setattr(self, element):
        setattr(element, "data", [99])
        assert element.data == [1, 2, 3]

    def test_mutation_append(self, element):
        assert len(element.data) == 3
        element.data.append(4)
        assert len(element.data) == 3

    def test_mutation_setitem(self, element):
        assert element.data[0] == 1
        element.data[0] = 10
        assert element.data[0] == 1

    def test_mutation_delitem(self, element):
        assert len(element.data) == 3
        del element.data[1]
        assert len(element.data) == 3
