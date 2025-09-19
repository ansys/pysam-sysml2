Getting started
===============

This section explains how to install PySam SysML2 and set up a project, including loading and initializing it.

.. _Installation_Section:

Install PySam SysML2
--------------------

.. code:: bash

    python -m pip install ansys_sam_sysml2-<version>-py3-none-any.whl

Connect to the tool
-------------------

The following code connects to PySam SysML2 using the AnsysSysML2 API connector. To connect to another SysML2 tool, see the developer guide.

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 7
    :language: python
    :caption: Import the connector and project manager

The connector gives the project manager access to the model.

Create the connector
--------------------

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 13-18
    :language: python
    :caption: Connect to the SysML2 API server

Create the project manager and load a project
---------------------------------------------

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 20-22
    :language: python
    :caption: Create the project manager and load a project

.. note::

    For more comprehensive examples on using PySam SysML2, see :ref:`Examples <Example>`.
