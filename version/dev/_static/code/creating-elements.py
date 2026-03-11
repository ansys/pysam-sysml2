"""Creating element example for PySAM SysML2."""

import requests
from urllib3.exceptions import InsecureRequestWarning

from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager
from ansys.sam.sysml2.tools import Factory

# Used to disable warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Create your connector for the SAM server
ansyssysml2apiconnector = AnsysSysML2APIConnector(
    server_url="<SAM Server URL>",  # Your SAM server base URL
    organization_id="<Orga ID>",  # The organization ID
    token="<Token>",  # Your authorization token
    use_ssl=False,  # If the server hasn't a valid SSL
)

project_manager = SysML2ProjectManager(connector=ansyssysml2apiconnector)
project = project_manager.get_scripting_project("<Bike Project ID>")

bike = project.get_root_package().Structure.Bike

factory = Factory(project, ansyssysml2apiconnector)

new_bicycle_frame_length = factory.create_attribute_usage(name="length", owner=bike.frame)

new_bicycle_frame_length.parse_and_set_value("60 [cm]")

print(project.get_root_package().Structure.Bike.frame.length.get_value())
