.. _Read_Model_Section:

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

    >>> myIntFeature.get_value()
    10
    >>> myStringFeature.get_value()
    "Hello"
    >>> myBoolFeature.get_value()
    False
    >>> myFloatFeature.get_value()
    10.56
    >>> myUnitFeature.get_value()
    '10 [kg]'
    >>> myArithmeticFeature.get_value()
    '5 + 5'
    >>> myReferenceFeature.get_value()
    'baseValue + baseValue'
    >>> myBooleanExpressionFeature.get_value()
    'not true'

The :meth:`get_value() <SysMLElement.get_value>` function supports:

- All primitive types, such as ``LiteralInteger``, ``LiteralString``, ``LiteralBoolean``, and
  ``LiteralRational`` - returns the value directly as its native Python type.
- Expressions - returns the rendered text form of the expression, including:

  - unit expressions, such as ``<value> [<unit>]`` (for example ``'10 [kg]'``);
  - arithmetic expressions (for example ``'5 + 5'``);
  - reference expressions that name other features (for example ``'baseValue + baseValue'``);
  - unary expressions (for example ``'not true'``).

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

.. _Feature_Chaining_Section:

Resolve connection ends (feature chaining)
==========================================

A connection end (``source`` or ``target``) does not always point directly at the element you
expect. An end is an *end feature* that can reference its target through a **feature chaining**, a
path such as ``a.b.c``. Because of redefinition and inheritance, the element a chaining resolves to
is *context dependent*: the same feature can resolve to a different element depending on where it is
observed.

Reading ``connection.source`` (static) or ``connection._source`` (dynamic) directly therefore
returns the raw end feature, not the meaningful element it represents. Use
:class:`SysMLTools <ansys.sam.sysml2.tools.sysmltools.SysMLTools>`
to resolve an end within its connection context:

.. code:: python

    from ansys.sam.sysml2.tools import SysMLTools

    source = SysMLTools().resolve_feature_chaining(connection, "source")
    target = SysMLTools().resolve_feature_chaining(connection, "target")

    # Or resolve both ends at once:
    source, target = SysMLTools().get_connector_ends(connection)

``SysMLTools``:

- Resolves each end within the connection's owner as context, so feature chaining, inheritance, and
  redefinition are all accounted for.
- Auto-detects whether you use the static (:class:`Project <ansys.sam.sysml2.classes.project.Project>`)
  or dynamic (scripting) representation from the element you pass in, so the same call works for both
  approaches.
- Returns the resolved representative element, or ``None`` when the end or context is missing.

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: load-model
            :link-type: doc

            Load your model

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: write-model
            :link-type: doc

            Write data to your model