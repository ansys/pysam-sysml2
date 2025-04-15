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

from ansys.sam.sysml2.classes.feature_helper import FeatureHelper


class TestFeatureHelper:

    def test_adapt_bool_value(self):
        assert FeatureHelper._adapt_value(True) == "true"
        assert FeatureHelper._adapt_value(False) == "false"

    def test_adapt_string_value(self):
        assert FeatureHelper._adapt_value("hello") == '"hello"'
        assert FeatureHelper._adapt_value("") == '""'

    def test_adapt_numbers_value(self):
        assert FeatureHelper._adapt_value(42) == "42"
        assert FeatureHelper._adapt_value(3.14) == "3.14"

    def test_adapt_none_value(self):
        assert FeatureHelper._adapt_value(None) == "None"

    def test_adapt_structure_value(self):
        assert FeatureHelper._adapt_value([1, 2, 3]) == "[1, 2, 3]"
        assert FeatureHelper._adapt_value({"a": 1}) == "{'a': 1}"
