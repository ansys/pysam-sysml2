from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager
from ansys.sam.sysml2.tools import SysMLTools
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

conn = AnsysSysML2APIConnector(
    server_url="https://127.0.0.1:8443/",  # Your Sam server base URL
    organization_id="<Orga ID>",  # The Organization ID
    token="<Token>",  # Your Auth Token (See section below)
    use_ssl=False,  # If the server has a valid SSL
)

model_manager = SysML2ProjectManager(connector=conn)

project = model_manager.get_project(
    "<Computer Project ID>"
)  # You can find it in the URL of the Editor

realSystems = project.get_root_package().RealSystems


def assess_cost(element):
    if hasattr(element, "cost") and (element.cost.get_value() is not None):
        return element.cost.get_value()
    cost = 0
    for sub_element in element._ownedElement:
        if SysMLTools.isinstance(sub_element, "PartUsage"):
            cost += assess_cost(sub_element)
    return cost


for system in realSystems._ownedElement:
    print(system._name, " : ", assess_cost(system))
