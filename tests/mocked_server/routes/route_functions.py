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

# -*- coding: utf-8 -*-
"""
 Copyright (c) 2024 ANSYS, Inc.
 Unauthorized use, distribution, or duplication is prohibited.

File <server_route.py> created on Tue Nov 26 2024
"""

from collections import Counter
from functools import wraps
from json import dumps, loads
import os
from uuid import uuid4

from flask import Response, abort, request

from .const import VALID_ORGANIZATION, VALID_TOKEN

TYPE = "@type"

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
                code=401,
                title="",
                message="",
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
                code=404,
                title="resource-not-found",
                message="Organization not found",
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
            message="Make sure the file is named : project_<id>/elements.json",
        )


def load_project_data(id: str) -> dict:
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
    path = get_project_path(os.path.join(f"project_{id}", "project.json"))
    try:
        with open(path, "r") as file:
            return loads(file.read())
    except Exception:
        create_http_error(
            code=500,
            title="JSON not found",
            message="Make sure the file is named : project_<id>/project.json",
        )


def load_project_rest_data(id: str) -> dict:
    """
    Use this function to load project rest data.

    Parameters
    ----------
    id : str
        project id

    Returns
    -------
    str
        Project data
    """
    path = get_project_path(os.path.join(f"project_{id}", "api_rest.json"))
    try:
        with open(path, "r") as file:
            return loads(file.read())
    except Exception:
        create_http_error(
            code=500,
            title="JSON not found",
            message="Make sure the file is named : project_<id>/api_rest.json",
        )


def load_project_diagrams_info(id: str, diagram_id: str = "") -> dict:
    """
    Use this function to load project rest data.

    Parameters
    ----------
    id : str
        project id
    diagram_id
        diagram_id if specified get the info for the specific diagram, all otherwise

    Returns
    -------
    str
        Project data
    """
    if diagram_id:
        path = get_project_path(
            os.path.join(f"project_{id}", f"{diagram_id}_diagram_info.json")
        )
    else:
        path = get_project_path(os.path.join(f"project_{id}", "diagrams.json"))
    try:
        with open(path, "r") as file:
            return loads(file.read())
    except Exception:
        create_http_error(
            code=500,
            title="JSON not found",
            message="Make sure the file is named : project_<id>/diagrams.json",
        )


def write_project(id: str, data: dict) -> None:
    """
    Use this function to write project data.

    Parameters
    ----------
    id : str
        Project ID
    data : dict
        Modified project data to save

    Returns
    -------
    None
    """
    path = get_project_path(os.path.join(f"project_{id}", "elements.json"))
    try:
        with open(path, "w") as file:
            file.write(dumps(data, indent=4))
            file.flush()
    except Exception as e:
        create_http_error(
            code=500,
            title="Failed to write JSON",
            message=f"Could not write to file: project_{id}/elements.json. Error: {str(e)}",
        )


def create_http_error(code: int = 404, title: str = "Error", message: str = ""):
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
    abort(code, {"title": title, "message": message})


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
        create_http_error(
            title="resource-not-found",
            message=f"Project {project_id} not found",
        )


#######################################
#       Create your function below   #
#######################################


@authenticate
@space_route
@return_json
def route_get_projects() -> list:
    """
    Use this function to render all project in ```../json/``

    Returns
    -------
    list
        all projects
    """
    projects_root = get_project_path("")
    projects = []
    for _, dirs, _ in os.walk(projects_root):
        for directory in dirs:
            projects.append(
                {
                    TYPE: "Project",
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
    return load_project_data(project_id)


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
    element = _find_element_by_id(project_id, element_id)
    if element is None:
        create_http_error(
            title="resource-not-found",
            message=f"Element {element_id}  not found in Project {project_id}",
        )
    return element


def _find_element_by_id(project_id, element_id):
    data = load_project(project_id)
    for element in data:
        if element["@id"] == element_id:
            return element


@authenticate
@space_route
@return_json
def route_get_roots_elements(project_id: str) -> list:
    """
    Return all roots elements (With no owner field).

    Parameters
    ----------
    project_id : str
        Project Id

    Returns
    -------
    list
        All roots Elements
    """
    check_project_id(project_id)
    data = load_project(project_id)
    roots_elements = []
    for element in data:
        if "owner" not in element:
            roots_elements.append(element)
    return roots_elements


@authenticate
@space_route
@return_json
def route_query(project_id: str) -> str:
    """
    Apply query to the project

    Parameters
    ----------
    project_id : str
        Project Id

    Returns
    -------
    str
        Query result
    """
    check_project_id(project_id)
    data = load_project(project_id)
    query = request.data
    try:
        query = loads(query)
    except Exception:
        create_http_error(code=500)

    return _handle_constraint(query["where"], data)


@authenticate
@space_route
@return_json
def route_create_project() -> dict:
    """
    route_create_project creates a project

    Returns
    -------
    dict
        _description_
    """
    project_info = loads(request.data)
    if "name" in project_info and "description" in project_info:
        projects_root = get_project_path("")
        for _, dirs, _ in os.walk(projects_root):
            for directory in dirs:
                project_id = directory.split("_")[1] if "_" in directory else None
                if project_id is not None:
                    existing = load_project_data(project_id)
                    if existing and existing.get("name") == project_info["name"]:
                        create_http_error(
                            code=409,
                            title="impossible-operation",
                            message="A project with this name already exists in this space.",
                        )
        return {
            TYPE: "Project",
            "defaultBranch": {"@id": "defaultBranch"},
            "description": project_info["description"],
            "name": project_info["name"],
            "@id": str(uuid4()),
        }
    create_http_error(code=405)


@authenticate
@space_route
@return_json
def route_delete_project(project_id: str) -> dict:
    """
    Delete the project with the given ID.

    Parameters
    ----------
    project_id : str
        Project Id

    Returns
    -------
    dict
        Confirmation with @type and @id
    """
    check_project_id(project_id)
    return {TYPE: "Project", "@id": project_id}


@authenticate
@space_route
@return_json
def route_update_project(project_id: str) -> dict:
    """
    Update the project with the given ID.

    Parameters
    ----------
    project_id : str
        Project Id

    Returns
    -------
    dict
        Updated project record
    """
    check_project_id(project_id)
    project_data = load_project_data(project_id)
    update_info = loads(request.data)
    if "name" in update_info:
        project_data["name"] = update_info["name"]
    if "description" in update_info:
        project_data["description"] = update_info["description"]
    return project_data


@authenticate
@space_route
@return_json
def route_create_commit(project_id: str) -> dict:
    """
    route_create_commit _summary_

    Parameters
    ----------
    project_id : str
        _description_

    Returns
    -------
    str
        _description_
    """
    check_project_id(project_id)
    project_data = load_project(project_id)
    commit_request_body = loads(request.data)

    _check_commit_validity(commit_request_body)
    change = commit_request_body.get("change")[0]

    payload = change.get("payload", None)
    identity = change.get("identity", None)

    element_changed = None
    if identity is not None:
        try:
            element_changed = [
                element
                for element in project_data
                if element.get("@id") == identity.get("@id")
            ][0]
        except IndexError:
            pass
    else:
        element_changed = _create_new_element(project_id, project_data, payload)

    if payload is None and identity is not None:
        __delete_element(element_changed, project_id)
    else:
        updated_element = __update_element(payload, element_changed)

        _save_updated_element(project_id, updated_element)

    return {"message": "Commit Successful"}


def __delete_element(element, project_id):
    project_data = load_project(project_id)
    index = project_data.index(
        [x for x in project_data if x["@id"] == element["@id"]][0]
    )
    project_data.pop(index)
    write_project(project_id, project_data)


def _save_updated_element(project_id, updated_element):
    project_data = load_project(project_id)
    index = project_data.index(
        [x for x in project_data if x["@id"] == updated_element["@id"]][0]
    )
    project_data.pop(index) and project_data.insert(index, updated_element)
    write_project(project_id, project_data)


def _create_new_element(project_id, project_data, payload):
    if payload.get(TYPE, None) is None:
        create_http_error(code=400, message="No Type for New Element")
    random_id = _generate_unique_id(project_data)
    owner_ref = payload.get("owner", None)
    try:
        owner_id = owner_ref.get("@id", None)
    except Exception:
        create_http_error(code=400, message="No Valid Owner Specified")
    owner = _find_owner(project_data, owner_id)
    owner_name = owner.get("qualifiedName")

    if payload.get("@type") == "FeatureValue":
        if "value" in payload:
            value_id = _generate_unique_id(project_data)
            payload["value"] = {"@id": value_id}

        payload.update(
            {
                "@id": random_id,
                "identifier": random_id,
                "qualifiedName": "",
            }
        )
    else:
        payload.update(
            {
                "@id": random_id,
                "identifier": random_id,
                "qualifiedName": f"{owner_name}::{payload['name']}",
            }
        )

    if "ownedElement" not in owner:
        owner["ownedElement"] = []
    owner["ownedElement"].append({"@id": random_id})

    project_data.append(payload)
    write_project(project_id, project_data)
    return _find_element_by_id(project_id, random_id)


def _find_owner(project_data, owner_id):
    try:
        return [
            el
            for el in project_data
            if el.get("@id") is not None and el.get("@id") == owner_id
        ][0]
    except IndexError:
        create_http_error(code=400, message="Invalid Owner Id")


def _generate_unique_id(project_data: list) -> str:
    """
    generate_unique_id Generate a UUID that doesn't exist in the current project data

    Parameters
    ----------
    project_data : list
        A list of dictionaries representing elements of the project

    Returns
    -------
    str
        A unique UUID string not present in any element's '@id' field
    """
    existing_ids = {element.get("@id") for element in project_data}

    while True:
        random_id = str(uuid4())
        if random_id not in existing_ids:
            return random_id


def _check_commit_validity(commit):
    change = None
    if "change" in commit:
        change = commit.get("change")
        if len(change) == 0:
            create_http_error(code=400, message="Change can't be empty")

    change = commit.get("change")[0]

    if "payload" in change and len(change.get("payload")) == 0:
        create_http_error(code=400, message="Invalid change data")

    if change.get(TYPE, None) != "DataVersion":
        create_http_error(code=400, message="No DataVersion found in commit")


def __update_element(payload, element_changed):
    for key, value in payload.items():
        if key not in element_changed:
            create_http_error(code=400, message=f"Element: Invalid {key}")
        else:
            if not isinstance(value, type(element_changed[key])):
                create_http_error(code=400, message=f"Element: Invalid Type for {key}")
            else:
                element_changed[key] = value
    return element_changed


@authenticate
@return_json
def route_get_rest_json(project_id: str) -> str:
    """
    use this function to get all rest api json.

    Parameters
    ----------
    project_id : str
        Project id

    Returns
    -------
    str
        REST API JSON
    """
    check_project_id(project_id)
    return load_project_rest_data(project_id)


@authenticate
@return_json
def route_get_diagrams_info(project_id: str):
    """Get list of diagrams for a project."""
    check_project_id(project_id)
    return load_project_diagrams_info(project_id)


@authenticate
@return_json
def route_get_single_diagram_info(project_id: str, diagram_id: str):
    """Get information for a single diagram."""
    check_project_id(project_id)
    return load_project_diagrams_info(project_id, diagram_id)


@authenticate
def route_get_diagram_image(project_id: str, diagram_id: str, file_format: str) -> str:
    """
    use this function to get diagram images.

    Parameters
    ----------
    project_id : str
        Project id

    Returns
    -------
    str
        REST API JSON
    """
    check_project_id(project_id)
    if diagram_id == "all":
        return all_diagram_as_zip(project_id, file_format)
    else:
        return get_diagram_by_id(project_id, diagram_id, file_format)


def get_diagram_by_id(project_id, diagram_id, file_format):
    accepted_file_format = ["all", "jpeg", "png", "svg"]

    if file_format in accepted_file_format:
        data = {
            "success": 200,
            "project_id": project_id,
            "diagram_id": diagram_id,
            "file_format": file_format,
        }
        if file_format == "svg":
            file_format = "svg+xml"
        return Response(
            dumps(data).encode("utf-8"),
            mimetype=f"image/{file_format}",
            headers={
                "Content-Disposition": f'attachment; filename="diagrams.{file_format}"'
            },
        )
    else:
        abort(404, description="File format not supported")


def all_diagram_as_zip(project_id, file_format):
    path = get_project_path(
        os.path.join(f"project_{project_id}", "number_of_diagrams.txt")
    )
    with open(path) as f:
        nb = int(f.read())

    accepted_file_format = ["all", "jpeg", "png", "svg"]

    if file_format in accepted_file_format:
        data = {
            "success": 200,
            "project_id": project_id,
            "number_diagrams": nb,
            "file_format": file_format,
        }
        return Response(
            dumps(data).encode("utf-8"),
            mimetype="application/zip",
            headers={"Content-Disposition": 'attachment; filename="diagrams.zip"'},
        )
    else:
        abort(404, description="File format not supported")


def _handle_constraint(constraint: dict, data: list) -> list:
    """
    handle_constraint _summary_

    Parameters
    ----------
    constraint : _type_
        _description_
    data : _type_
        _description_
    """
    match constraint[TYPE]:
        case "PrimitiveConstraint":
            return _handle_search(constraint, data)
        case "CompositeConstraint":
            res = list()
            for c in constraint["constraint"]:
                res.extend(_handle_constraint(c, data))
            return _apply_join(constraint, res)
        case _:
            return None


def _apply_join(constraint: dict, result: list) -> list:
    """
    _apply_join Sort result depending of the join operator.

    Parameters
    ----------
    constraint : dict
        The compositeConstraint
    result : list
        the result list

    Returns
    -------
    list
        the final list
    """
    if constraint["operator"] == "and":
        id_counter = Counter(element["@id"] for element in result)

        required_count = len(constraint["constraint"])
        seen_ids = set()
        final_res = []

        for element in result:
            if (
                id_counter[element["@id"]] == required_count
                and element["@id"] not in seen_ids
            ):
                final_res.append(element)
                seen_ids.add(element["@id"])

        return final_res
    return result


def _handle_search(constraint: dict, data: list) -> list:
    """
    _handle_search make the constraint search in the given data

    Parameters
    ----------
    constraint : dict
        Primitive constraint
    data : list
        data

    Returns
    -------
    list
        result
    """
    prop = constraint["property"]
    operator = constraint["operator"]
    value = constraint["value"]
    inverse = True if constraint["inverse"] == "true" else False
    operator_map = {
        "=": lambda x, y: x == y,
        ">": lambda x, y: x > y,
        "<": lambda x, y: x < y,
        ">=": lambda x, y: x >= y,
        "<=": lambda x, y: x <= y,
    }

    op_func = operator_map.get(operator)
    if not op_func and operator != "instanceOf":
        raise ValueError(f"Unsupported operator: {operator}")

    def check(e):
        if prop not in e:
            e_type = e[TYPE]
            create_http_error(
                500,
                title="SysML Error",
                message=f"Invalid fields {prop} for element {e_type}",
            )

        left = e[prop] if operator != "instanceOf" else e[TYPE]
        comparison = op_func(left, value) if op_func else left == value
        return not comparison if inverse else comparison

    return [x for x in data if check(x)]
