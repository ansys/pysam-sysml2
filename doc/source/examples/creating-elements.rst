.. _Creating_Example:

Create a new element
####################

Make sure that you have access to a valid server and a project containing the ``Bike`` structure.
If you do not have a project containing the ``Bike`` structure, perform the following steps:

#. Download the model: :download:`Bike Model <../_static/code/bike.xmi>`.

#. Open the SAM editor in your browser and select the desired organization (for example, *MyOrga*).

#. Select **New Project** > **SysML V2** > **Import File**.

#. Select **Choose File** for the **File to import** option.

#. Select the ``bike.xmi`` file that you just downloaded. The project name is automatically set to
   ``bike``.

#. Click **Import** and wait for the project to load.

Create an attribute usage element for the bicycle frame length
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: ansys.sam.sysml2.tools.factory

The following code shows how to create a new ``AttributeUsage`` element inside the ``Bike``
structure and assign it a value.

.. note::

    You need to replace the organization ID, server URL, and token with your own data. For more
    information, see :ref:`Find information<Info_Section>`.

.. literalinclude:: ../_static/code/creating-elements.py
    :language: python
    :caption: Create a new AttributeUsage element using the :class:`Factory` class
    :linenos:

You just created a new element and assigned a parsed value to it.

.. currentmodule:: ansys.sam.sysml2.classes.sysml_element

.. note::

    You can also assign a value directly when creating the element, without using the 
    :meth:`set_value() <SysMLElement.set_value>` or
    :meth:`parse_and_set_value() <SysMLElement.parse_and_set_value>`
    method. There are two ways:

    - ``value=...`` for simple values (such as numbers).
    - ``expression="..."`` for values with units or expressions.

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