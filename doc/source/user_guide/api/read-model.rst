Read your model
###############

One of the goal of the lib is to be able to read and parse the model through a Python script.

The loaded model is stored in a :ref:`Project <L_Project>`.

.. _Getter:

Access methods
==============

To parse the project, you can use different access methods.

Dot access
----------

Using the dot access, you can access all direct named element of your SysML element.
Also, you can access to some useful top level function, like `get_value` for example.

Sub elements
~~~~~~~~~~~~

The script attaches all elements contained in ``ownedElement`` and ``_inheritedFeature``, who has a name, to the container element.

.. code:: python

    >>> myPart.subPart
    <class ParUsage>

.. warning::

    **Limitations of dot access for sub-elements:**

    - **Duplicate names**: If multiple elements have the same name, only one is accessible through dot access. You cannot differentiate between elements with identical names using this method.

    - **Names with spaces**: Elements with spaces in their names (for example, "bike frame") cannot be accessed using dot notation. Python identifiers cannot contain spaces.

Function ``get_value``
~~~~~~~~~~~~~~~~~~~~~~

.. warning::

    This function is only for SysML Features Element.

This is a top level function to help user to get the Value of the feature without having to read the internal structure.

.. code:: python

    >>> myExpressionFeature.get_value()
    (10, 'kg')
    >>> myIntFeature.get_value()
    10
    >>> myStringFeature.get_value()
    "Hello"
    >>> myBoolFeature.get_value()
    False
    >>> myFloatFeature.get_value()
    10.56

This function supports:

- All primitive types: LiteralInteger, LiteralString, etc. - Returns the value directly
- Simple expressions: <value> [<unit>] - Returns a tuple: (<value>,<unit short name>)

Otherwise, it raises an exception.

Underscore access
=================

Using the ``_`` access, you can find all SysML methods:

.. code:: python

    >>> myPart._name
    myPart
    >>> myItem._ownedElement
    [<class portUsage>,...]

.. warning::

    In this first version, only existing fields (with data) are linked, so it's possible to don't find a function, which exist in SysML V2

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: load-model
            :link-type: doc

            Load your model

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: write-model
            :link-type: doc

            Write in your model