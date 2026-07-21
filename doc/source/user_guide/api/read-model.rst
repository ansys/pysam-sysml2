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

The utility function ``get_value`` returns the value element of a feature. Read the literal value
through ``value``, or render any value element as text with ``SysMLTools.serialize_expression``.

.. code:: python

    >>> myFeature.get_value()
    <LiteralInteger>
    >>> myFeature.get_value().value
    5
    >>> SysMLTools.serialize_expression(myFeature.get_value())
    '5'


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
element. It returns the feature's value element (a literal such as ``LiteralInteger`` or an
expression such as ``OperatorExpression``) without reading the internal structure:

.. code:: python

    >>> myIntFeature.get_value()
    <LiteralInteger>
    >>> myArithmeticFeature.get_value()
    <OperatorExpression>

Read the literal value directly through ``_value``:

.. code:: python

    >>> myIntFeature.get_value()._value
    10
    >>> myStringFeature.get_value()._value
    'Hello'
    >>> myBoolFeature.get_value()._value
    False
    >>> myFloatFeature.get_value()._value
    10.56

Render any value element (literal or expression) as text with
``SysMLTools.serialize_expression``:

.. code:: python

    >>> from ansys.sam.sysml2.tools import SysMLTools
    >>> SysMLTools.serialize_expression(myIntFeature.get_value())
    '10'
    >>> SysMLTools.serialize_expression(myUnitFeature.get_value())
    '10 [kg]'
    >>> SysMLTools.serialize_expression(myArithmeticFeature.get_value())
    '5 + 5'
    >>> SysMLTools.serialize_expression(myReferenceFeature.get_value())
    'baseValue + baseValue'
    >>> SysMLTools.serialize_expression(myBooleanExpressionFeature.get_value())
    'not true'

``SysMLTools.serialize_expression`` supports:

- All primitive literals, such as ``LiteralInteger``, ``LiteralString``, ``LiteralBoolean``, and
  ``LiteralRational``, which render as text (for example ``'10'``).
- Expressions, which render in their text form, including:

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