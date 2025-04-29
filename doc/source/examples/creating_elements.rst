Creating New Elements Example
#############################

Let's create and configure a new element in an existing model.

Make sure you have access to a valid server and a project containing the `Bike` structure.

If not, you can download this model : `Bike Model </_static/code/bike.xmi>`_.

Open SAM Editor on your browser, and select the wanted organization (*MyOrga* for example).
Then, click on `New Project` > `SysMl V2` > `Import File`.
Click on `Choose File`  in the  `File to import` input, and select the `bike.xmi` file you just downloaded.
The name of the project will automatically set to `bike`.
Click on `Import` and wait for the project to be loaded.

*✅ Congratulations, you now have a bike model to work on !*

Create an AttributeUsage for the Bicycle Frame Length
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to create a new ``AttributeUsage`` element inside the ``Bike`` and assign it a value.

.. note::

    You need to change `Organization ID`, `Server Url` and `Token` with your own data, see :ref:`This section for more information<Info_Section>`.

.. code:: python

    from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager
    from ansys.sam.sysml2.tools import Factory

    # Create your connector for the Sam Server
    connector = AnsysSysML2APIConnector(
        server_url="https://127.0.0.1:8443/", # Your Sam server base URL
        organization_id="<Orga ID>", # The Organization ID
        token="<Token>", # Your Auth Token (See section below)
        use_ssl=False # IF the server has a valid SSL
    )

    model_manager = SysML2ProjectManager(connector=connector)
    project = model_manager.get_project("<Bike Project ID>")

    bike = project.get_root_package().Structure.Bike

    factory = Factory(project, connector)

    new_bicycle_frame_length = factory.create_elements(
        "AttributeUsage", name="length", owner=bike.frame
    )

    new_bicycle_frame_length.parse_and_set_value("60 [cm]")

    print(project.get_root_package().Structure.Bike.frame.length.get_value())

✅ You just created a new element and assigned a parsed value to it!
