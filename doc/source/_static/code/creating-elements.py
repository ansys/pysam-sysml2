from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager
from ansys.sam.sysml2.tools import Factory

# Create your connector for the Sam Server
connector = AnsysSysML2APIConnector(
    server_url="https://127.0.0.1:8443/",  # Your Sam server base URL
    organization_id="<Orga ID>",  # The Organization ID
    token="<Token>",  # Your Auth Token (See section below)
    use_ssl=False,  # IF the server has a valid SSL
)

model_manager = SysML2ProjectManager(connector=connector)
project = model_manager.get_project("<Bike Project ID>")

bike = project.get_root_package().Structure.Bike

factory = Factory(project, connector)

new_bicycle_frame_length = factory.create_elements(
    "AttributeUsage", name="length", owner=bike.frame
)

new_bicycle_frame_length.parse_and_set_value("60 [cm]")

print(project.get_root_package().Structure.Bike.frame.length.get_value())
