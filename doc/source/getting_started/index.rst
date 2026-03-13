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

The following code connects to PySAM SysML2 using the
:class:`AnsysSysML2APIConnector <ansys.sam.sysml2.api.ansys_sysml2_api_connector.AnsysSysML2APIConnector>`.

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 29
    :language: python
    :caption: Import the connector and project manager

The connector gives the project manager access to the model.

Create the connector
--------------------

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 35-40
    :language: python
    :caption: Connect to the SysML2 API server

Create the project manager and load a project
---------------------------------------------


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



.. note::

    For more comprehensive examples on using PySAM SysML2, see :ref:`Examples <Example>`.
