Getting started
===============

This section's scope is about user installation.


.. _Installation_Section:

Installation
-------------


.. code:: bash

    python -m pip install ansys_sam_sysml2-<version>-py3-none-any.whl


Use
---

.. note::

    You can find examples :ref:`here <Example>`.

Connect to the tool
~~~~~~~~~~~~~~~~~~~

Here, the AnsysSysML2 API Connector is used. If you want to connect to any other SysMLV2 tool, please read the developer guide.


First import the Connector and the Project manager.

.. code:: python

    from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager

The connector provides the project manager with access to the model.

Then create the connector :

.. code:: python

    conn = AnsysSysML2APIConnector(
        server_url="https://127.0.0.1:8443", # The base URL of the Standard API
        organization_id="<Orga ID>", # Organization Id where is stored the project
        token="<Token>", # Your Personal access token
        use_ssl=False, # If you need to verify HTTPS or not
    )

Then, you can create the project manager and load a project:

.. code:: python

    model_manager = SysML2ProjectManager(connector=conn)

    project = model_manager.get_project("<Project ID>") #You can find it in the URL of the Editor
