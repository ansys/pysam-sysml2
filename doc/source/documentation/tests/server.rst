Mocked Server
#############

Because the library need to load a model from a server,
we decide to create a mocked server, who simulate the SysMLv2 standard API implemented on Ansys SAM tool.

.. warning::

    The goal is not to tests the API but how the library call it and use his return


Actual path are :

+------------------------------------------------------------------+-----------------------------------------+------------+
| **endpoint**                                                     | **Params**                              | **Return** |
+------------------------------------------------------------------+-----------------------------------------+------------+
| /projects                                                        | organization_id                         | JSON       |
+------------------------------------------------------------------+-----------------------------------------+------------+
| /projects/<project_id>                                           | organization_id, project_id             | JSON       |
+------------------------------------------------------------------+-----------------------------------------+------------+
| /projects/<project_id>/commits/<head>/elements                   | organization_id, project_id             | JSON       |
+------------------------------------------------------------------+-----------------------------------------+------------+
| /projects/<project_id>/commits/<head>/elements/<elements_id>     | organization_id, project_id, elements_id| JSON       |
+------------------------------------------------------------------+-----------------------------------------+------------+

Manage Projects
===============

Since this server simulates a model server, you need some projects for your tests.

The server dynamically fetches projects from the folder:

``tests/mocked_server/json/``

Project Structure
-----------------

A project structure is simple: you need to create a directory named `project_<id>`.
This directory must contain one required file: `elements.json`, which holds all the elements.

The structure of the *json* folder is as follows:

.. code-block:: text

    📂 json
        ├── 📂 project_1
        │    ├── 📃 elements.json
        │    └── 🖼️ model.png
        ├── 📂 project_2
        │    └── 📃 elements.json
        ...

You can optionally add a screenshot of the model (`model.png`) to assist with testing.

To generate the `elements.json` file, you should use the SAM implementation of the SysMLv2 standard API and call the `/elements` endpoint to retrieve a valid JSON.


Adding Your Own Endpoint
=========================

To add your own endpoint, you first need to create a **return function**.
This function will be executed when the endpoint is called on the server.

To illustrate this section, let's take an example:

➡️ Add a new endpoint: `/hello/<name>` which returns a JSON with a personalized greeting message.

Step 1: Define Your Return Function
-----------------------------------

Navigate to the file:

``tests/mocked_server/routes/routes_function.py``

After the section containing the *tool functions*, you will find all the existing return functions.
You can define your own function in this section.

For this example, the `hello` function will be:

.. code-block:: python

    @return_json
    def hello(name):
        return {
            "message": f"Hello {name} !!"
        }

The line `@return_json` uses a decorator function (see `Tool Functions Overview`).

The `hello` function takes one parameter: `name`, which is the parameter provided by the user in the URL.
The function simply returns a dictionary with a key `"message"` and a value `"Hello <name>!"`.

Step 2: Add Your Endpoint to the Server
---------------------------------------

Once your function is ready, navigate to the file:

``tests/mocked_server/routes/__init__.py``

In this file, there is a list named `routes_list` that stores all declared endpoints.

Now, decide the accepted HTTP method for your endpoint. The server provides four objects corresponding to the main HTTP methods:

- **GET**: Use `ServerGetRouteMapping`.
- **POST**: Use `ServerPostRouteMapping`.
- **DELETE**: Use `ServerDeleteRouteMapping`.
- **PUT**: Use `ServerPutRouteMapping`.

For our example, we need the `GET` method.
Let's define the endpoint:

.. code-block:: python

    routes_list = [
        ...,
        ServerGetRouteMapping(
            route="/hello/<name>",
            controller_function=hello,
        )
    ]

And that's all! By using `<>`, you define a URL parameter. This object links the endpoint to your function.

.. caution::
   Do not use the same function name for two different endpoints, even if they use different HTTP methods.
   Remember: **1 function = 1 endpoint**.

Tool Functions Overview
========================

Here are some of the existing tool functions you can use:

- **space_route**
  This function is a `decorator <https://docs.python.org/3/glossary.html#term-decorator>`_
  that checks if the provided organization ID in the URL is valid.

- **return_json**
  This function is a `decorator <https://docs.python.org/3/glossary.html#term-decorator>`_
  that converts the returned object (e.g., dictionaries or lists) into a JSON string format.

- **check_project_id**
  This function checks if the provided ID corresponds to an existing project folder.

- **get_project_path**
  This function resolves the relative path of a project.

- **load_project**
  This function loads all the data (elements) of the requested project.

- **create_http_error**
  This function creates an HTTP error (e.g., 404, 400, 500, ...) with a specified title and description.
