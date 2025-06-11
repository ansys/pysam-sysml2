# Import Connector and Model Manager
from ansys.sam.sysml2 import SysML2ProjectManager, AnsysSysML2APIConnector

# Create your connector for the Sam Server
connector = AnsysSysML2APIConnector(
    server_url="https://127.0.0.1:8443/",  # Your Sam server base URL
    organization_id="<Orga ID>",  # The Organization ID
    token="<Token>",  # Your Auth Token (See section below)
    use_ssl=False,  # If the server has a valid SSL
)

project_manager = SysML2ProjectManager(connector=connector)

myBikeProject = project_manager.get_project("<Bike Project ID>")


# Then we can use the following code to get the PartDefinition of the bike
bike = myBikeProject.get_root_package().Structure.Bike

bike_weight = (
    bike.frontWheel.rim.weight.get_value()[0]
    + bike.frontWheel.tire.weight.get_value()[0]
    + bike.rearWheel.rim.weight.get_value()[0]
    + bike.rearWheel.tire.weight.get_value()[0]
    + bike.frame.weight.get_value()[0]
)
print(bike_weight)
