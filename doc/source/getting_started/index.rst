Getting started
===============

This section's scope is about user installation.

For developer, see :ref:`dev_guide`


Installation
-------------


.. code:: bash

    python -m pip install ansys-sam-sysml2


Usage
-----

Create a connector
~~~~~~~~~~~~~~~~~~

Start a Python INterpreter and import PySam Package:

.. code:: python

    from ansys.sam.sysml2 import ConnectorFactory

Next, create the connector for your tool. Here for SAM SysML2 API.

.. code:: python

    conn = ConnectorFactory.create_ansys_sysml_connector(
            server_url="https://sam-testing.ansys.com:9050",
            organization_id="<organization_id>",
            token="<token>,
            is_secure=False
            )

Load a model
~~~~~~~~~~~~

For the moment, to load a model, use this command

.. code:: python

    conn.get_project_data(project_id=<id>)