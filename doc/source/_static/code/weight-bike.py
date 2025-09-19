"""Weight Bike Example for PySam."""

# Import connector and model manager
import requests
from urllib3.exceptions import InsecureRequestWarning

from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager

# Used to disable warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Create your connector for the SAM Server
ansyssysml2apiconnector = AnsysSysML2APIConnector(
    server_url="https://127.0.0.1:8443/",  # Your SAM server base URL
    organization_id="<Orga ID>",  # The organization ID
    token="<Token>",  # Your authorization token
    use_ssl=False,  # If the server has a valid SSL
)

project_manager = SysML2ProjectManager(connector=ansyssysml2apiconnector)

my_bike_project = project_manager.get_project("<Bike Project ID>")


# Then we can use the following code to get the PartDefinition of the bike
bike = my_bike_project.get_root_package().Structure.Bike

bike_weight = (
    bike.frontWheel.rim.weight.get_value()[0]
    + bike.frontWheel.tire.weight.get_value()[0]
    + bike.rearWheel.rim.weight.get_value()[0]
    + bike.rearWheel.tire.weight.get_value()[0]
    + bike.frame.weight.get_value()[0]
)
print(bike_weight)
