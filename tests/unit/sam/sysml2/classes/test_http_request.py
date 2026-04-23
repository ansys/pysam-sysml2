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

"""Pure unit tests for HttpRequest dataclass."""

from ansys.sam.sysml2.classes.http_request import HttpRequest


class TestHttpRequest:

    def test_explode_renames_json_body(self):
        req = HttpRequest(url="http://test")
        req.json_body = {"key": "value"}
        exploded = req.to_dict()
        assert "json" in exploded
        assert "json_body" not in exploded
        assert exploded["json"] == {"key": "value"}

    def test_headers_default_empty(self):
        req = HttpRequest(url="http://test")
        assert req.headers == {}

    def test_url_set(self):
        req = HttpRequest(url="http://example.com/api")
        assert req.url == "http://example.com/api"
        exploded = req.to_dict()
        assert exploded["url"] == "http://example.com/api"
