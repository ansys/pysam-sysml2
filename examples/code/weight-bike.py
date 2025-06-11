# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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
