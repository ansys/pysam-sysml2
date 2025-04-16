.. _Create_C_Section:

Use a connector
##################


A connector is the interface between the library and the SysML V2 Server.
It uses the Standard API to load and publish information in a model.


Connectors
==========

For now, you only have a connector for Ansys SAM tool.


Usage
-----

.. note::

    To find all required data (Ids, token,..)  see :ref:`Here <Info_Section>`


You can find classes specification :ref:`Here <C_I_Section>`

.. code:: python

    conn = AnsysSysML2APIConnector(
        server_url="https://127.0.0.1:8443", # The base URL of the Standard API
        organization_id="<Orga ID>", # Organization Id where is stored the project
        token="<Token>", # Your Personal access token
        use_ssl=False, # If you need to verify HTTPS or not
    )



.. grid:: 2

    .. grid-item-card::
        :link: create_conn
        :link-type: doc

    .. grid-item-card:: Next step :fa:`arrow-right`
        :link: load_model
        :link-type: doc

        Load a model