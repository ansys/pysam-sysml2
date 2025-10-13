Write in your model
###################

.. warning::

    This is a beta feature and may have some issues.

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

The :meth:`parse_and_set_value() <SysMLElement.parse_and_set_value>` function handles more complex expressions:

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
    :lines: 25
    :language: python
    :caption: Create a Factory instance

Use the :meth:`create_element() <Factory.create_element>` method to create a new model element. Provide the element type and any number of keyword arguments representing its attributes:

.. code:: python

    new_attribute_usage = factory.create_element(
        element_type="AttributeUsage",
        name="new_attribute_usage",
    )

This creates a new ``AttributeUsage`` element at the root of your project. The :meth:`create_element() <Factory.create_element>` method returns the newly created element.

.. literalinclude:: ../../_static/code/creating-elements.py
    :lines: 27-29
    :language: python
    :caption: Create a new AttributeUsage element with owner

This creates a new ``AttributeUsage`` element with the specified attributes inside the ``Bike`` frame.

.. note::

    The list of accepted attributes depends on the element type you are creating. For example, ``name``, ``owner``, ``shortName``, and others are defined by the ``metamodel``.

    You can also assign a value directly when creating the element. There are two ways:

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

Update attributes directly
--------------------------

Update element properties directly using simple assignment. This is useful for quickly changing properties like names.

.. code:: python

    >>> my_attribute = factory.create_element(element_type="Attribute", name="OriginalName")
    >>> my_attribute._name = "New Name"
    New Name

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