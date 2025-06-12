.. _Creating_Example:

Creating new element example
#############################

Make sure you have access to a valid server and a project containing the ``Bike`` structure.

If not, you can download this model : `Bike Model </_static/code/bike.xmi>`_.

Open SAM Editor on your browser, and select the wanted organization (*MyOrga* for example).
Then, click **New Project** > **SysML V2** > **Import File**.
Click on **Choose File** in the **File to import** input, and select the ``bike.xmi`` file you just downloaded.
The name of the project is automatically set to ``bike``.
Click on **Import** and wait for the project to be loaded.

*Congratulations, you now have a bike model to work on !*

Create an attribute usage for the bicycle frame length
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to create a new ``AttributeUsage`` element inside the ``Bike`` and assign it a value.

.. note::

    You need to change `Organization ID`, `Server URL` and `Token` with your own data, see :ref:`This section for more information<Info_Section>`.

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
        element_type="AttributeUsage", name="length", owner=bike.frame
    )

    new_bicycle_frame_length.parse_and_set_value("60 [cm]")

    print(project.get_root_package().Structure.Bike.frame.length.get_value())

You just created a new element and assigned a parsed value to it.

.. note::

    You can also assign a value directly when creating the element, without using ``set_value`` or ``parse_and_set_value``. There are two ways:

    - Use ``value=...`` for simple values (e.g., numbers).
    - Use ``expression="..."`` for values with units or expressions.

    .. code:: python

        new_bicycle_frame_length_with_value = factory.create_element(
            element_type="AttributeUsage",
            name="lengthWithValue",
            owner=bike.frame,
            value=60
        )

        new_bicycle_frame_length_with_expression = factory.create_element(
            element_type="AttributeUsage",
            name="lengthWithExpression",
            owner=bike.frame,
            expression="60 [cm]"
        )

    This lets you set values directly at creation time, depending on your data format.