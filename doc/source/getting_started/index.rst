Getting started
===============

This section's scope is about user installation.


.. _Installation_Section:

Installation
-------------


.. code:: bash

    python -m pip install ansys_sam_sysml2-<version>-py3-none-any.whl


Usage
-----

You can find more examples :ref:`here <Example>`

Connect to the tool
~~~~~~~~~~~~~~~~~~~

Here, we will use the AnsysSysML2 API Connector. If you want to connect to any other SysMLV2 tool, please read developer guide.


First import the connector and the Project manager.

.. code:: python

    from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager

The connector will provide to the project manager, the access to the model.

Then create the connector :

.. code:: python

    conn = AnsysSysML2APIConnector(
        server_url="https://127.0.0.1:8443", # The base URL of the Standard API
        organization_id='8a06828c8e0a4d4a018e0a52513f0001', # Organization Id where is stored the project
        token=token, # You Personal access token
        use_ssl=False, # If you need to verify HTTPS or not
    )

Then, you can create the project manager and load a project:

.. code:: python

    model_manager = SysML2ProjectManager(connector=conn)

    project = model_manager.get_project("ac00103a-8e4d-426d-bd5f-e1e6d360970c")
