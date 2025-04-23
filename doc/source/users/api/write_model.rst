Write in your model
###################


.. warning::

    This feature is in beta version and doesn't support a lot of functions.


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


parse and set
-------------

This function is for more complex expression :

.. code::

    >>> myFeature.parse_and_set_value("10 [m]")
    >>> myFeature.get_value()
    (10,"m")
    >>> myFeature.parse_and_set_value("2 + 10 [kg]")
    >>> myFeature.get_value()
    Exception UnsupportedValueExpression raised

.. only:: html

    .. grid:: 2

        .. grid-item-card::  :fa:`arrow-left` Previous step
            :link: read_model
            :link-type: doc

            Read a model

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: information
            :link-type: doc

            How to get some information