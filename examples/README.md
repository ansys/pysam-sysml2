# Example

Here is an example which presents several functionalities of the Python library.
```python
from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager
from ansys.sam.sysml2.tool import SysMLTools
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(
    InsecureRequestWarning
)

token = "eyJraWQi..."


conn = AnsysSysML2APIConnector(
    server_url="https://sam-testing.ansys.com:9050",
    organization_id="1485632895474126574525orgaid",
    token=token,
    use_ssl=False,
)


model_manager = SysML2ProjectManager(connector=conn)

project = model_manager.get_project("c22d73ac-470c-47c6-ad59-dbad31c600e1")

"""
replace by your server_url, organization_id, project_id and token
"""

realSystems = project._root[0].RealSystems


def assess_cost(element):
    if hasattr(element, "cost") and (
        SysMLTools.extract_value(element.cost) is not None):
        return int(SysMLTools.extract_value(element.cost))
    cost = 0
    for sub_element in element._ownedElement:
        if SysMLTools.isinstance(sub_element, "PartUsage"):
            cost += assess_cost(sub_element)
    return cost


for system in realSystems._ownedElement:
    print(system._name, " : ", assess_cost(system))
```

You can use it by loading this [model](Computer.xmi) in your SAM server.
For details about getting token, projectID and other stuff, see the [documentation](Documentation.pdf).
