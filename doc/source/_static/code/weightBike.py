"""Sample file."""

from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager

token = ""


conn = AnsysSysML2APIConnector(
    server_url="https://127.0.0.1:8443",
    organization_id="<orgaId>",
    token=token,
    use_ssl=False,
)

model_manager = SysML2ProjectManager(connector=conn)

project = model_manager.get_project("<Project ID>")

bike = project.get_root_package().Structure.Bike


bike_weight = (
    bike.frontWheel.rim.weight.get_value()[0]
    + bike.frontWheel.tire.weight.get_value()[0]
    + bike.rearWheel.rim.weight.get_value()[0]
    + bike.rearWheel.tire.weight.get_value()[0]
    + bike.frame.weight.get_value()[0]
)
print("Bike weight: ", bike_weight)
