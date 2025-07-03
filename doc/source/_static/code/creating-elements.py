import requests
from urllib3.exceptions import InsecureRequestWarning

from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager
from ansys.sam.sysml2.tools import Factory

# Used to disable warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Create your connector for the Sam Server
ansyssysml2apiconnector = AnsysSysML2APIConnector(
    server_url="https://127.0.0.1:8443/",  # Your Sam server base URL
    organization_id="<Orga ID>",  # The Organization ID
    token="<Token>",  # Your Auth Token (See section below)
    use_ssl=False,  # IF the server has a valid SSL
)

project_manager = SysML2ProjectManager(connector=ansyssysml2apiconnector)
project = project_manager.get_project("<Bike Project ID>")

bike = project.get_root_package().Structure.Bike

factory = Factory(project, ansyssysml2apiconnector)

new_bicycle_frame_length = factory.create_elements(
    element_type="AttributeUsage", name="length", owner=bike.frame
)

new_bicycle_frame_length.parse_and_set_value("60 [cm]")

print(project.get_root_package().Structure.Bike.frame.length.get_value())
