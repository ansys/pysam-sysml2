.. _Manage_Projects_Example:

Manage projects
###############

This example shows how to manage SysML v2 projects on a SAM server using the
:class:`SysML2ProjectManager <ansys.sam.sysml2.builder.sysml2_project_manager.SysML2ProjectManager>`
class. It explains how to perform these tasks:

- List all existing projects.
- Create a new project.
- Update a project name and description.
- Delete a project.

.. note::

    For more details on each operation, see the user guide page
    :ref:`Manage projects <Manage_Projects_Section>`.

Prerequisites
=============

Ensure that you meet these prerequisites:

- A running SAM server instance.
- A valid organization ID and token.

Python example
==============

.. literalinclude:: ../_static/code/manage-projects.py
    :language: python
    :caption: Project management: create, list, update, and delete projects
    :linenos:

.. note::

    - Replace placeholder values with your actual SAM configuration.
    - Deleting a project is irreversible. All data associated with the project is permanently
      removed.
