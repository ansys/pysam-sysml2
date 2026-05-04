Getting started
===============

This section explains how to install PySAM SysML2 and set up a project, including loading and
initializing it.

.. _Installation_Section:

Install PySAM SysML2
--------------------

.. code:: bash

    python -m pip install ansys-sam-sysml2

Connect to the tool
-------------------

To get started, import the connector and project manager classes from the PySAM SysML2 library.

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 29
    :language: python
    :caption: Import the connector and project manager

Create the connector
--------------------

A connector is required to access a SysML2 API server. Currently, the library provides a connector for the Ansys SysML2 server, which is compatible with most SysML2-compliant servers.
This connector:

- gives you access to the main entry points of a SysML2 server
- allows you to create project managers to access models for a specific organization and user

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 35-40
    :language: python
    :caption: Connect to the SysML2 API server

Create the project manager and load a project
---------------------------------------------

As mentioned, you can create a project manager with the connector to access projects for a specific organization and user. Once you have a project manager, you can load a project by its ID. The following example uses the Bike project, which is frequently referenced in the Examples section.

.. tab-set::

    .. tab-item:: Dynamic approach

        .. literalinclude:: ../_static/code/weight-bike.py
            :lines: 42-44
            :language: python
            :caption: Create the project manager and load a project

    .. tab-item:: Static approach

        .. literalinclude:: ../_static/code/weight-bike-static.py
            :lines: 42-44
            :language: python
            :caption: Create the project manager and load a project

As you can see, there are 2 approaches to access a model. See :ref:`Approaches dynamic and static <Approaches_Section>` for more information about the differences between these approaches and when to use each of them.

.. note::

    For more comprehensive examples on using PySAM SysML2, see :ref:`Examples <Example>`.
