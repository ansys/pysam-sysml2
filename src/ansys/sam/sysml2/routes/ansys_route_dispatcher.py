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

from typing import Optional

from overrides import overrides

from ansys.sam.sysml2.exception.route_exception import InvalidAnsysOrganizationIdException

from .route_dispatcher import RouteDispatcher


class AnsysRouteDispatcher(RouteDispatcher):
    """Class dedicated to Ansys specific API route."""

    _organization_id: Optional[str] = None

    def __init__(self, server_url: str, organization_id: str = None) -> None:
        super().__init__(server_url)
        self._organization_id = organization_id

    @overrides
    def build_endpoint(self, endpoint: str) -> str:
        """
        build_endpoint create the full URL using the given API endpoint.

        Parameters
        ----------
        endpoint : str
            The endpoint

        Returns
        -------
        str
            Full url
        """
        if self._organization_id is None:
            raise InvalidAnsysOrganizationIdException("Organization id is not provided!")
        if endpoint.startswith("/"):
            endpoint = endpoint[1:]
        return f"{self._server_url}/api/spaces/{self._organization_id}/sysml2/{endpoint}"

    def set_organization(self, organization_id: str):
        """
        set_organization update the organization Id.

        Parameters
        ----------
        organization_id : str
            New organization Id
        """
        self._organization_id = organization_id
