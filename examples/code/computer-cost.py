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

"""Computer cost example for PySAM SysML2."""

import requests
from urllib3.exceptions import InsecureRequestWarning

from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager
from ansys.sam.sysml2.tools import SysMLTools

# Used to disable warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ansyssysml2apiconnector = AnsysSysML2APIConnector(
    server_url="https://127.0.0.1:8443/",  # Your SAM server base URL
    organization_id="<Orga ID>",  # The organization ID
    token="<Token>",  # Your authorization token
    use_ssl=False,  # If the server has a valid SSL
)

project_manager = SysML2ProjectManager(connector=ansyssysml2apiconnector)

project = project_manager.get_scripting_project(
    "<Computer Project ID>"
)  # You can find your project ID in the URL of the editor.

real_systems = project.get_root_package().RealSystems


def assess_cost(element):
    """Calculate the cost of element."""
    if hasattr(element, "cost") and (element.cost.get_value() is not None):
        cost = element.cost.get_value()
        if type(cost) is int:
            return cost
        elif type(cost) is tuple:  # a tuple means an int value and a unit
            return cost[0]
        raise ValueError(f"Problem of value type for the cost of {element._name}")
    cost = 0
    for sub_element in element._ownedElement:
        if SysMLTools.isinstance(sub_element, "PartUsage"):
            cost += assess_cost(sub_element)
    return cost


for system in real_systems._ownedElement:
    print(system._name, " : ", assess_cost(system))
