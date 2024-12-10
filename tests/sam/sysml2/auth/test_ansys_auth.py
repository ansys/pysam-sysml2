# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
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

"""File  created on Tue Dec 10 2024."""

import pytest

from ansys.sam.sysml2.auth.ansys_auth import AnsysAuth
from ansys.sam.sysml2.core.http_request import HttpRequest


class TestAnsysSysMLAuth:

    TOKEN: str = "ASuperToken"

    @pytest.fixture
    def http_request(self):
        return HttpRequest(url="localhost")

    def test_initialization(self, http_request: HttpRequest):
        auth = AnsysAuth(token=self.TOKEN)

        auth.update_request(request=http_request)

        assert "Bearer Token" in http_request.headers
        assert http_request.headers["Bearer Token"] == self.TOKEN

    def test_update_token(self, http_request: HttpRequest):
        auth = AnsysAuth(token=self.TOKEN)

        auth.update_request(request=http_request)
        assert http_request.headers["Bearer Token"] == self.TOKEN

        auth.update_token(token="A")
        auth.update_request(request=http_request)

        assert http_request.headers["Bearer Token"] != self.TOKEN
        assert http_request.headers["Bearer Token"] == "A"
