Read your model
###############

PySAM SysML2 lets you read and parse the model through a Python script.

The loaded model is stored in a :class:`Project <ansys.sam.sysml2.classes.project.Project>` object.

.. _Getter:

Read SysML2 project (Static approach)
=====================================

SysML2 properties
-----------------

All SysML2 properties are accessible using dot notation.

.. code:: python

    >>> package.owned_element
    [..,..]

The utility function ``get_value`` extracts the value from a feature element.

.. code:: python

    >>> myFeature.get_value()
    5


Model elements
--------------

To retrieve a model element by name, use the ``get`` function. It returns the element if found, or ``None`` otherwise.

.. code:: python

    >>> my_element.get("my Element")
    <sysml.PartUsage>


Read scripting project (Dynamic approach)
=========================================


Access methods
==============

To parse the project, you can use dot access or underscore access.

Dot access
----------

.. currentmodule:: ansys.sam.sysml2.classes.sysml_element

With dot access, you can access all direct named elements of your SysML element. Also, you can
access some useful top-level functions, such as :meth:`get_value() <SysMLElement.get_value>`.

Sub-elements
~~~~~~~~~~~~

The following code attaches all elements contained in ``ownedElement`` and ``_inheritedFeature``,
which have names, to the container element.

.. code:: python

    >>> myPart.subPart
    <class PartUsage>

**Limitations of dot access for sub-elements:**

- **Duplicate names**: If multiple elements have the same name, only one is accessible through dot
  access. You cannot differentiate between elements with identical names using this method.

- **Names with spaces**: You cannot access elements with spaces in their names (for example, "bike
  frame") using dot notation. Python identifiers cannot contain spaces.

Function :meth:`get_value() <SysMLElement.get_value>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :meth:`get_value() <SysMLElement.get_value>` function works only for the SysML ``Feature``
element. Use this top-level function to get the value of the feature without reading the internal
structure:

.. code:: bash

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

The :meth:`get_value() <SysMLElement.get_value>` function supports:

- All primitive types, such as LiteralInteger and LiteralString - Returns the value directly.
- Simple expressions, such as ``<value> [<unit>]`` - Returns a tuple:
  ``(<value>,<unit short name>)``.

Underscore access
=================

With underscore (``_``) access, you can find all SysML2 methods:

.. code:: python

    >>> myPart._name
    myPart
    >>> myItem._ownedElement
    [<class portUsage>,...]

.. note::

    In this first PySAM SysML2 version, only existing fields (with data) are linked, which means
    that you might not find a function that exists in SysML V2.

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