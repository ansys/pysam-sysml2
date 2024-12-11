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
File  created on Mon Dec 09 2024.

You can define here your own path on the mocked server.

Step to define your route:

=> Create the render function in the file ``route_functions.py``
=> Add a new entry in the ``routes_list`` list
=> Select the methods with the correct mapping:
    -ex:  If GET method -> Use ``ServerGetRouteMapping``
=> Setup your route in the constructor params of the mapping class.

Example:

If i want to create a route "/hello/<name>"
That return an HTML who says "Hello <name> !"
First create the function hello in ``route_functions.py``
.. code-block:: pycon
    >>> def hello(name:str)->str:
    >>> ...     return f"Hello {name} !"

Then, in this file ``__init__.py``, we add an new entry
to ``routes_list``.
The method is GET, the path is "/hello/<name>" and the
associated method is ``hello``
So we got:
.. code-block:: pycon
    >>> routes_list = [
    >>> ... # Other entry
    >>> ServerGetRouteMapping(
    route="/hello/<string:name>",
    controller_function=hello
    ),]

And all good!

To pass params in url, use ``<type:name>``


"""

from .route_class import (
    ServerDeleteRouteMapping,
    ServerGetRouteMapping,
    ServerPostRouteMapping,
    ServerPutRouteMapping,
)
from .route_functions import *

ANSYS_BASE_URI = "/api/spaces/<string:organization>/sysml2/"


# Add HERE your new route
routes_list = [
    ServerGetRouteMapping(
        route=ANSYS_BASE_URI + "/projects", controller_function=route_get_projects
    ),
    ServerGetRouteMapping(
        route=ANSYS_BASE_URI + "/projects/<string:project_id>",
        controller_function=route_get_project,
    ),
    ServerGetRouteMapping(
        route=ANSYS_BASE_URI + "/projects/<string:project_id>/commits/head/elements",
        controller_function=route_get_elements,
    ),
    ServerGetRouteMapping(
        route=ANSYS_BASE_URI
        + "/projects/<string:project_id>/commits/head/elements/<string:element_id>",
        controller_function=route_get_element,
    ),
]
