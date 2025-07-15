.. _Creating_Example:

Creating new element example
#############################

Make sure you have access to a valid server and a project containing the ``Bike`` structure.

If not, you can download this model : :download:`Bike Model <../_static/code/bike.xmi>`.

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

    You need to change `Organization ID`, `Server URL` and `Token` with your own data, see :ref:`this section for more information<Info_Section>`.

.. literalinclude:: ../_static/code/creating-elements.py
    :language: python
    :caption: Creating a new AttributeUsage element using the Factory class
    :linenos:

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