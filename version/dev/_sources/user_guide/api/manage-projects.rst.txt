.. _Manage_Projects_Section:

Manage projects
###############

The :class:`SysML2ProjectManager <ansys.sam.sysml2.builder.sysml2_project_manager.SysML2ProjectManager>`
class provides methods for managing projects on the server: listing, creating, updating, and
deleting them.

To use these methods, you need an instance of the
:class:`SysML2ProjectManager <ansys.sam.sysml2.builder.sysml2_project_manager.SysML2ProjectManager>`
(see :ref:`Use a connector <Create_C_Section>`).

List projects
=============

Retrieve all projects accessible to the connected user:

.. code:: python

    projects = project_manager.get_projects()
    for p in projects:
        print(f"{p['name']} (id: {p['@id']})")

Create a project
================

Create a new project on the server. The project is automatically built and returned as a
Python object, ready to use.

Two methods are available depending on the approach:

.. tab-set::

    .. tab-item:: Dynamic approach

        .. code:: python

            project = project_manager.create_scripting_project(
                name="My New Project",
                description="A project created via PySAM SysML2",
            )

    .. tab-item:: Static approach

        .. code:: python

            project = project_manager.create_sysml_project(
                name="My New Project",
                description="A project created via PySAM SysML2",
            )

Both methods create the project on the server and return a fully loaded project object, similar
to calling ``get_scripting_project()`` or ``get_sysml_project()`` on an existing project.

Update a project
================

Rename a project or change its description:

.. code:: python

    updated = project_manager.update_project(
        project_id="<Project ID>",
        name="My Renamed Project",
        description="Updated description",
    )

Both ``name`` and ``description`` parameters are optional. Only the provided fields are updated.

Delete a project
================

Delete a project from the server:

.. code:: python

    deleted = project_manager.delete_project(project_id="<Project ID>")

.. warning::

    Deleting a project is irreversible. All data associated with the project is permanently removed.

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: approaches
            :link-type: doc

            Dynamic vs static approaches

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: load-model
            :link-type: doc

            Load a model
