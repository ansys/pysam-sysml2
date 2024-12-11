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

"""
File created on Tue Dec 03 2024.

Thanks to this class, we provide an interface for user.
This interface intent to protect user of this library of any
future changes in the code (New object or other ...)
"""
from ansys.sam.sysml2.auth.ansys_auth import AnsysAuth
from ansys.sam.sysml2.connector.sysml_connector import SysMLConnector
from ansys.sam.sysml2.routes.ansys_route_dispatcher import AnsysRouteDispatcher


class ConnectorFactory:
    """Interface for connector creation.For specific SysML Models tools."""

    @staticmethod
    def create_ansys_sysml_connector(
        server_url: str = "http://localhost:8443",
        organization_id: str = None,
        token: str = None,
        is_secure: bool = True,
    ) -> SysMLConnector:
        """
        Create a SysML Connector for Ansys Standard API.

        Parameters
        ----------
        server_url : str, optional
            The API base URL, by default "http://localhost:8443"
        organization_id : str, optional
            organization ID, by default None
        token : str, optional
            Your auth token, by default None

        Returns
        -------
        SysMLConnector
            The initialized Connector
        """
        route_dispatcher = AnsysRouteDispatcher(
            server_url=server_url, organization_id=organization_id
        )
        auth = AnsysAuth(token=token)
        return SysMLConnector(
            route_dispatcher=route_dispatcher, authenticator=auth, is_secure=is_secure
        )
