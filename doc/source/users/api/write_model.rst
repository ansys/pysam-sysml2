Write in your model
###################


.. warning::

    This feature is in beta version and could have some issues.


Update feature value
====================

There is two functions to update the value of a feature:

- set_value()
- parse_and_set_value()

set value
---------

This function is for all primitive type :

.. code::

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

The model is updated after all set, to keep it the most accurate as possible.


Create new elements
===================

You can create new elements in your model using the ``Factory`` class.

.. tip::

    A complete example is available :ref:`here <PM_Section>`.

.. code::

    factory = Factory(project, connector)

Then, use the ``create_element()`` method to create a new model element.
You must provide the type of the element, as well as any number of keyword arguments representing its attributes:

.. code::

    new_attribute_usage = factory.create_element(
        "AttributeUsage",
        name="new_attribute_usage",
    )

This will create a new ``AttributeUsage`` element at the root of your project.
The ``create_element()`` method returns the newly created element.

.. code::

    bike = project.get_root_package().Structure.Bike

    new_attribute_usage = factory.create_element(
        "AttributeUsage",
        name="new_attribute_usage",
        owner=bike,
        shortName="attrUsage01"
    )

This will create a new ``AttributeUsage`` element with the given attributes inside the ``Bike``.

.. note::

    The list of accepted attributes depends on the type of element you are creating.
    For example ``name``, ``owner``, ``shortName``, and others defined by the metamodel.

.. only:: html

    .. grid:: 2

        .. grid-item-card::  :fa:`arrow-left` Previous step
            :link: read_model
            :link-type: doc

            Read a model

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: diagram_model
            :link-type: doc

            How to get use diagrams