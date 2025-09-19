"""Computer cost example for PySam SysML2."""

import requests
from urllib3.exceptions import InsecureRequestWarning

from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager
from ansys.sam.sysml2.tools import SysMLTools

# Used to disable warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ansyssysml2apiconnector = AnsysSysML2APIConnector(
    server_url="https://127.0.0.1:8443/",  # Your SSAMam server base URL
    organization_id="<Orga ID>",  # The organization ID
    token="<Token>",  # Your authorization token
    use_ssl=False,  # If the server has a valid SSL
)

project_manager = SysML2ProjectManager(connector=ansyssysml2apiconnector)

project = project_manager.get_project(
    "<Computer Project ID>"
)  # You can find your project ID in the URL of the editor.

real_systems = project.get_root_package().RealSystems


def assess_cost(element):
    """Calculate the cost of element."""
    if hasattr(element, "cost") and (element.cost.get_value() is not None):
        return element.cost.get_value()
    cost = 0
    for sub_element in element._ownedElement:
        if SysMLTools.isinstance(sub_element, "PartUsage"):
            cost += assess_cost(sub_element)
    return cost


for system in real_systems._ownedElement:
    print(system._name, " : ", assess_cost(system))
