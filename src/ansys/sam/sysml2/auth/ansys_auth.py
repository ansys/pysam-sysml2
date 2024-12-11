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

"""File created on Tue Dec 03 2024."""

from __future__ import annotations

from overrides import overrides

from ansys.sam.sysml2.core.http_request import HttpRequest

from .sysml_auth import SysMLAuth


class AnsysAuth(SysMLAuth):
    """AnsysAuth provide the correct authentication for Ansys Standard API implementation."""

    _token: str

    def __init__(self, token: str) -> None:
        self._token = token
        super().__init__()

    @overrides
    def update_request(self, request: HttpRequest) -> HttpRequest:
        """
        update_request Implement the `SysMLAuth` method, for the needs of Ansys security.

        Parameters
        ----------
        request : HttpRequest
            The update to update
        Returns
        -------
        HttpRequest
            Updated Request
        """
        request.headers["Authorization"] = "Bearer " + self._token
        return request

    def update_token(self, token: str) -> None:
        """
        update_token take the new token and update it.

        Parameters
        ----------
        token : str
            The new token
        """
        self._token = token
