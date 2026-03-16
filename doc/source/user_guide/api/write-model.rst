.. _Write_Model_Section:

Write data to your model
########################

.. note:: To avoid performance issues, don't forget to use `Transaction mode`_. See the bottom of this page for details.


Update a feature value
======================

You have two functions for updating the value of a feature:

.. currentmodule:: ansys.sam.sysml2.classes.sysml_element

- :meth:`set_value() <SysMLElement.set_value>`
- :meth:`parse_and_set_value() <SysMLElement.parse_and_set_value>`

Function :meth:`set_value() <SysMLElement.set_value>`
------------------------------------------------------

The :meth:`set_value() <SysMLElement.set_value>` function supports all primitive types:

.. code:: python

    >>> myFeature.set_value(True)
    >>> myFeature.get_value()
    True
    >>> myFeature.set_value(10)
    >>> myFeature.get_value()
    10
    >>> myFeature.set_value("Hello")
    >>> myFeature.get_value()
    Hello
    >>> myFeature.set_value(10.5)
    >>> myFeature.get_value()
    10.5

The model updates after you set all values to ensure accuracy.

Function :meth:`parse_and_set_value() <SysMLElement.parse_and_set_value>`
--------------------------------------------------------------------------

The :meth:`parse_and_set_value() <SysMLElement.parse_and_set_value>` function handles more complex
expressions:

.. code:: python

    >>> myFeature.parse_and_set_value("10 [m]")
    >>> myFeature.get_value()
    (10, "m")
    >>> myFeature.parse_and_set_value("2 + 10 [kg]")
    >>> myFeature.get_value()
    Exception UnsupportedValueExpression raised

Create new elements
===================

.. currentmodule:: ansys.sam.sysml2.tools.factory

Use the :class:`Factory` class to create new elements in your model.

.. tip::

    For a comprehensive example, see :ref:`Create a new element <Creating_Example>`.

.. literalinclude:: ../../_static/code/creating-elements.py
    :lines: 46
    :language: python
    :caption: Create a Factory instance

Use the :meth:`create_<element_type>()` method to create a new model element.
Provide the element type and any number of keyword arguments representing its attributes:

.. code:: python

    new_attribute_usage = factory.create_attribute_usage(
        name="new_attribute_usage",
    )

This creates a new ``AttributeUsage`` element at the root of your project. The
:meth:`create_<element_type>()` method returns the newly created element.

.. literalinclude:: ../../_static/code/creating-elements.py
    :lines: 48-50
    :language: python
    :caption: Create a new AttributeUsage element with owner

This creates a new ``AttributeUsage`` element with the specified attributes inside the ``Bike``
frame.

.. note::

    The list of accepted attributes depends on the element type you are creating. For example,
    ``name``, ``owner``, ``shortName``, and others are defined by the ``metamodel``.

    You can also assign a value directly when creating the element. There are two ways:

    - ``value=...`` for simple values (such as numbers).
    - ``expression="..."`` for values with units or expressions.

    .. tab-set::

        .. tab-item:: Dynamic approach

            .. code:: python

                new_bicycle_frame_length_with_value = factory.create_attribute_usage(
                    name="lengthWithValue",
                    owner=bike.frame,
                    value=60
                )

                new_bicycle_frame_length_with_expression = factory.create_attribute_usage(
                    name="lengthWithExpression",
                    owner=bike.frame,
                    expression="60 [cm]"
                )

        .. tab-item:: Static approach

            .. code:: python

                new_bicycle_frame_length_with_value = factory.create_attribute_usage(
                    name="lengthWithValue",
                    owner=bike.get("frame"),
                    value=60
                )

                new_bicycle_frame_length_with_expression = factory.create_attribute_usage(
                    name="lengthWithExpression",
                    owner=bike.get("frame"),
                    expression="60 [cm]"
                )

    This lets you set values directly at creation time, depending on your data format.

Update attributes directly
--------------------------

Update element properties directly using simple assignment. This is useful for quickly changing
properties like names.


.. tab-set::

    .. tab-item:: Dynamic approach

        .. code:: python

            >>> my_attribute = factory.create_attribute_usage(name="OriginalName")
            >>> my_attribute._name = "New Name"
            New Name

    .. tab-item:: Static approach

        .. code:: python

            >>> my_attribute = factory.create_attribute_usage(name="OriginalName")
            >>> my_attribute.name = "New Name"
            New Name

Moving Elements
---------------

Use ``append()`` - on the owned element property - to move an element to a different container.
The element is automatically removed from its current container.

.. tab-set::

    .. tab-item:: Dynamic approach

        .. code:: python

            new_container._owned_element.append(element_to_move)

    .. tab-item:: Static approach

        .. code:: python

            new_container.owned_element.append(element_to_move)

Removing Elements
-----------------

| If you use the ``remove()`` method of the owned element property, the element is deleted from the model.
| Please use this with caution: if a diagram displays this removed element, the diagram will display errors.

Transaction mode
----------------
When you perform write operations, the model is updated after each operation to ensure accuracy. However, if you want to perform multiple write operations without intermediate updates, you can use the transaction mode. In transaction mode, the model updates only after you complete all your operations. This can improve performance when making multiple changes to the model, but be aware that the model will not reflect any changes until you exit the transaction mode.


.. tab-set::

    .. tab-item:: Dynamic approach

        .. code:: python

            my_bike_project.start_transactional_mode()

            bike.frontWheel.rim.weight.parse_and_set_value("0.5 [kg]")
            bike.rearWheel.rim.weight.parse_and_set_value("0.8 [kg]")

            my_bike_project.stop_transactional_mode()

    .. tab-item:: Static approach

        .. code:: python

            my_bike_project.start_transactional_mode()

            bike.get("frontWheel").get("rim").get("weight").parse_and_set_value("0.5 [kg]")
            bike.get("rearWheel").get("rim").get("weight").parse_and_set_value("0.8 [kg]")

            my_bike_project.stop_transactional_mode()

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: read-model
            :link-type: doc

            Read your model

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: diagram-model
            :link-type: doc

            Work with diagrams