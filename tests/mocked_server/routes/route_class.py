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

"""File  created on Mon Dec 09 2024."""


class ServerRouteMapping:
    """Top class for Server route mapping."""

    def __init__(self, route: str, controller_function, accepted_http_methods: str):
        self.data = {
            "rule": route,
            "view_func": controller_function,
            "methods": [accepted_http_methods],
        }

    def get_data(self) -> dict:
        """
        Return the data to build Flask route

        Returns
        -------
        dict
            all the route data
        """
        return self.data


class ServerGetRouteMapping(ServerRouteMapping):
    """Get mapping for Flask Route."""

    def __init__(self, route: str, controller_function):
        super().__init__(route, controller_function, "GET")


class ServerDeleteRouteMapping(ServerRouteMapping):
    """Delete mapping for Flask Route."""

    def __init__(self, route: str, controller_function):
        super().__init__(route, controller_function, "DELETE")


class ServerPostRouteMapping(ServerRouteMapping):
    """Post mapping for Flask Route."""

    def __init__(self, route: str, controller_function):
        super().__init__(route, controller_function, "POST")


class ServerPutRouteMapping(ServerRouteMapping):
    """Put mapping for Flask Route."""

    def __init__(self, route: str, controller_function):
        super().__init__(route, controller_function, "PUT")
