Read your model
###############

One of the goal of the lib is to be able to read and parse the model, through a Python script.

The loaded model is stored in a :ref:`Project <L_Project>`.

Getter
======

To parse the project, you can use different getter.

Dot access
----------

Using the dot access, you can access to all direct named element of your Sysml element.
Also, you can access to some useful top level function, like get_value




Sub elements
~~~~~~~~~~~~

The script attach all element contained in `ownedElement` and `_inheritedFeature`, who has a name, to the container element.

.. code:: python

    >>> myPart.subPart
    <class ParUsage>

get value
~~~~~~~~~

.. warning::

    This function is only for SysML Features Element.

This is a top level function, to help user to get the Value of the feature, without read the internal structure.

.. code:: python

    >>> myExpressionFeature.getValue()
    (10,[kg])
    >>> myIntFeature.getValue()
    10
    >>> myStringFeature.getValue()
    "Hello"
    >>> myBoolFeature.getValue()
    False
    >>> myFloatFeature.getValue()
    10.56

This function support :

- All primitive type : LiteralInteger, LiteralString, ... => Return the value directly
- Simple expression : <value> [<unit>] => Return a tuple : (<value>,<unit short name>)

Else, it will raise an exception.


Underscore access
=================

Using the `_` access, you will find all Sysml Method :

.. code::

    >>> myPart._name
    myPart
    >>> myItem._ownedElement
    [<class portUsage>,...]

.. warning::

    In this first version, only existing fields (with data) are linked, so it's possible to don't find a function, who exist in Sysml V2


.. grid:: 2

    .. grid-item-card:: :fa:`arrow-left` Previous step
        :link: load_model
        :link-type: doc

        Load you model

    .. grid-item-card:: Next step :fa:`arrow-right`
        :link: write_model
        :link-type: doc

        Write in your model