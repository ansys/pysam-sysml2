"""Ansys SysML2 project example for PySAM SysML2."""

import requests
from urllib3.exceptions import InsecureRequestWarning

from ansys.sam.sysml2.tools.ansys_scripting_project import AnsysScriptingProject

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

project = AnsysScriptingProject(
    server_url="<SAM Server URL>",  # Your SAM server base URL
    organization_id="<Orga ID>",  # The organization ID
    token="<Token>",  # Your authorization token
    use_ssl=False,  # If the server hasn't a valid SSL
    project_id="<Bike Project ID>",  # The project ID
)

diagrams_status = project.is_diagrams_available()
print(f"Diagrams Status : {'Available' if diagrams_status else 'Unavailable'}", end="\n\n")

SAVE_IMAGE_PATH = "C:/Diagrams/Images/"
first_diagram = project.get_root_package().__diagram[0]
first_diagram_id = first_diagram._id

# -----------------------------------------
# Download ZIP file containing diagrams
# -----------------------------------------

response = project.download_all_diagrams(path=SAVE_IMAGE_PATH, file_format="png", filename="png")
print(f"> ZIP saved at: {response}\n")

# -----------------------------------------
# Download single diagram
# -----------------------------------------

path = project.download_diagram(
    diagram_id=first_diagram_id,
    filename="CUSTOM_FILENAME",
    file_format="png",
    path=SAVE_IMAGE_PATH,
)
print(f"> Diagram saved at: {path}\n")

usage_diagrams = project.get_root_package().Usage.__diagram
for i, diagram in enumerate(usage_diagrams, 1):
    project.download_diagram(
        diagram_id=diagram._id, file_format="png", path="C:/Diagrams/Images/Usage"
    )
    print(f"> Saved Usage diagram #{i}: {diagram._plane._model_element._name}\n")

# -----------------------------------------
# Navigate through diagrams
# -----------------------------------------

print(first_diagram._plane._model_element._name, end="\n")

for diagram in project.get_root_package().Usage.__diagram:
    print("Diagram name:", diagram._name, end="\n")

# -----------------------------------------
# Create element
# -----------------------------------------

project.factory.create_attribute_usage(name="NewAttr")

# -----------------------------------------
# Get diagrams information
# -----------------------------------------

print(project.get_project_diagrams_info(), end="\n\n")

print(project.get_single_diagram_info(first_diagram_id))
