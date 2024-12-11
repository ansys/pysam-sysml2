# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
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

# -*- coding: utf-8 -*-
"""
  Copyright (c) 2024 ANSYS, Inc.
  Unauthorized use, distribution, or duplication is prohibited.

 File <server_route.py> created on Tue Nov 26 2024
"""

from functools import wraps
from json import dumps, loads
import os

from flask import abort, request

from .const import VALID_ORGANIZATION, VALID_TOKEN

"""

This section declare helper function for all render functions.

For function declaration, go to the next section .

"""


def return_json(function):
    """
    Create a JSON wrapper for render function.

    Convert the return the function into a json.

    Parameters
    ----------
    function : function
        The Function

    Returns
    -------
    str
        JSON
    """

    @wraps(function)
    def wrapper(**args):
        return dumps(function(**args))

    return wrapper


def authenticate(function):
    """
    authenticate is a decorator who check the Bearer Token in headers.

    Parameters
    ----------
    function : Callable
        The function to protect
    Returns
    -------
    object
        the result of the function

    Exception
    ---------
    Throw a 403 error if no token or invalid token provided
    """

    @wraps(function)
    def auth_wrapper(**args):
        token = request.headers.get("Authorization", "")
        if token != "Bearer " + VALID_TOKEN:
            return create_http_error(
                code=403, title="Forbidden", description="You don't have access to this resource"
            )
        return function(**args)

    return auth_wrapper


def space_route(function):
    """
    Create a wrapper for render function.

    This wrapper check if there is a organization id
    in the url and check is validity.

    Parameters
    ----------
    function : function
        The Function

    Returns
    -------
    object
        the result of the function

    Exception
    ---------
    Throw a 404 error if the given Id is invalid
    """

    @wraps(function)
    def space_wrapper(organization, **args):
        if organization != VALID_ORGANIZATION:
            return create_http_error(
                code=404, title="Not Found", description="Organization not found"
            )
        return function(**args)

    return space_wrapper


def get_project_path(path: str = "") -> str:
    """
    Return the full path of the json folder

    Parameters
    ----------
    path : str, optional
        path in json, by default ""

    Returns
    -------
    str
        full path
    """
    local_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(local_path, "..", "json", path)


def load_project(id: str) -> dict:
    """
    Use this function to load project data.

    Parameters
    ----------
    id : str
        project id

    Returns
    -------
    str
        Project data
    """
    path = get_project_path(os.path.join(f"project_{id}", "elements.json"))
    try:
        with open(path, "r") as file:
            return loads(file.read())
    except Exception:
        create_http_error(
            code=500,
            title="JSON not found",
            description="Make sure the file is named : project_<id>/elements.json",
        )


def create_http_error(code: int = 404, title: str = "Error", description: str = ""):
    """
    Use this function to generate a HTTP error.

    Parameters
    ----------
    code : int, optional
        Error code, by default 404
    title : str, optional
        Error tile, by default "Error"
    description : str, optional
        Error description, by default ""
    """
    abort(code, {"title": title, "description": description})


def check_project_id(project_id: str):
    """
    Use this method to check if the give project id is valid.


    Parameters
    ----------
    project_id : str
        _description_
    """
    path = get_project_path("project_" + project_id)
    if not os.path.exists(path):
        create_http_error(title="Not found", description=f"Project {project_id} not found")


#######################################
#       Create your function below   #
#######################################


@authenticate
@space_route
@return_json
def route_get_projects() -> str:
    """
    Use this function to render all project in ```../json/``

    Returns
    -------
    str
        all projects
    """
    projects_root = get_project_path("")
    projects = []
    for _, dirs, _ in os.walk(projects_root):
        for directory in dirs:
            projects.append(
                {
                    "@type": "Project",
                    "defaultBranch": {"@id": "defaultBranch"},
                    "description": "",
                    "name": directory.replace("_", " "),
                    "@id": directory.split("_")[1],
                },
            )
    return projects


@authenticate
@space_route
@return_json
def route_get_project(project_id: str) -> str:
    """
    Use this function to get information of one project.

    Parameters
    ----------
    project_id : str
        Project Id

    Returns
    -------
    str
        Project information
    """
    check_project_id(project_id)
    return {
        "@type": "Project",
        "defaultBranch": {"@id": "defaultBranch"},
        "description": "",
        "name": f"project {project_id}",
        "@id": project_id,
    }


@authenticate
@space_route
@return_json
def route_get_elements(project_id: str) -> str:
    """
    use this function to get all elements of a project.

    Parameters
    ----------
    project_id : str
        Project id

    Returns
    -------
    str
        All elements
    """
    check_project_id(project_id)
    return load_project(project_id)


@authenticate
@space_route
@return_json
def route_get_element(project_id: str, element_id: str) -> str:
    """
    Return a specific element of a project.

    Parameters
    ----------
    project_id : str
        Project Id
    element_id : str
        Element Id

    Returns
    -------
    str
        Element information
    """
    check_project_id(project_id)
    data = load_project(project_id)
    for element in data:
        if element["@id"] == element_id:
            return element
    create_http_error(
        title="Not Found",
        description=f"Element {element_id}  not found in Project {project_id}",
    )
