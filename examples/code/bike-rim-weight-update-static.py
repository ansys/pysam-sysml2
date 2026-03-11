# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Bike rim weight update static example for PySAM SysML2."""

# Import connector and model manager
import requests
from urllib3.exceptions import InsecureRequestWarning

from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager

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

my_bike_project = project_manager.get_sysml_project("<Bike Project ID>")


# Then we can use the following code to get the PartDefinition of the bike
bike = my_bike_project.get_root_package().get("Structure").get("Bike")

rim = my_bike_project.get_root_package().get("Structure").get("Rim")
print(f"Default rim weight: {rim.get('weight').get_value()}")
print(
    f"Default frontWheel rim weight: {bike.get('frontWheel').get('rim').get('weight').get_value()}"
)
print(f"Default RearWheel rim weight: {bike.get('rearWheel').get('rim').get('weight').get_value()}")

bike.get("frontWheel").get("rim").get("weight").parse_and_set_value("0.5 [kg]")
bike.get("rearWheel").get("rim").get("weight").parse_and_set_value("0.8 [kg]")

print(f"Actual rim weight: {rim.get('weight').get_value()}")
print(f"New frontWheel rim weight: {bike.get('frontWheel').get('rim').get('weight').get_value()}")
print(f"New RearWheel rim weight: {bike.get('rearWheel').get('rim').get('weight').get_value()}")
