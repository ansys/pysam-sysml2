.. _Approaches_Section:

Dynamic versus static approaches
################################

This library provides access to SysML2 objects hosted on a SysML2 server. In the library, a SysML2 model is represented by a :class:`SysML2ProjectManager <ansys.sam.sysml2.builder.sysml2_project_manager.SysML2ProjectManager>` instance. The :class:`SysML2ProjectManager <ansys.sam.sysml2.builder.sysml2_project_manager.SysML2ProjectManager>` offers two distinct ways to access objects, each tailored to different development environments:

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Method
     - Approach
     - Best For
   * - :meth:`get_scripting_project() <SysML2ProjectManager.get_scripting_project>`
     - Dynamic
     - Jupyter Notebooks, interactive environments
   * - :meth:`get_sysml_project() <SysML2ProjectManager.get_sysml_project>`
     - Static
     - Traditional IDEs (VS Code, PyCharm)

.. note::

   Both approaches now sit on the **same generated metamodel**. They return the
   same generated classes and share the same data; only the *notation* differs.
   In the dynamic approach, each element is composed at runtime as
   ``(DynamicEObject, GeneratedClass)``: the ``DynamicEObject`` mixin adds dot
   navigation to children and the ``_camelCase`` accessors, while the underlying
   snake_case properties (``owned_element``, ``declared_name``, ...) are provided
   by the generated class through the MRO. As a result, ``isinstance(el,
   PartUsage)`` works natively in both approaches.

Dynamic approach
================

The **scripting approach** is designed for interactive environments like **Jupyter Notebooks**, where code is executed cell by cell and objects are loaded dynamically at each instruction. It corresponds to the unique approach that was proposed in the release 0.1 of PySAM.

Dynamic key characteristics
---------------------------

- **Optimized for auto-completion**: After typing a ``.`` (dot), the auto-completion suggestions display the **contained objects** within the current object, together with the ``_camelCase`` SysML2 accessors. The snake_case data properties are hidden from completion to keep the dynamic notation front and center. This makes it easy to navigate the SysML2 model hierarchy interactively.

- **SysML2 properties are underscore-prefixed**: To access native SysML2 properties (such as ``name``, ``isAbstract``, ``multiplicity``, etc.), you must prefix them with an underscore (``_``). The equivalent generated snake_case properties still work at runtime.

- **No-name elements stay dot-navigable**: Elements without a name receive a dot-safe fallback name ``ClassName_<id>`` (dashes replaced by underscores), so they remain reachable through dot notation, for example ``root.ConnectionUsage_4C27A76D_EB0D_4391_806F_C6103E0F41AB``.

Dynamic example
---------------

.. code-block:: python

   # Get a dynamic/scripting project from the project manager
   project = project_manager.get_scripting_project().get_root_package()

   # Auto-completion after '.' shows contained objects
   project.MyPart.  # Shows: MyAttribute, MyPort, ...

   # To access SysML2 properties, use the underscore prefix
   project.MyPart._name          # Returns: "MyPart"
   project.MyPart._isAbstract    # Returns: False
   project.MyPart._multiplicity  # Returns multiplicity info

Static approach
===============

The **static approach** is designed for traditional **IDE environments** like VS Code or PyCharm, where code is written first and executed later. Since objects are not loaded dynamically at coding time, the content of model elements is not known in advance.

Static key characteristics
--------------------------

- **Only SysML2 properties are exposed**: Because the contained objects cannot be determined at coding time, only the well-defined SysML2 properties are available as attributes.

- **Direct access to properties**: SysML2 properties are accessed directly without any prefix.

- **Classic access to contained elements**: The elements contained within a model element can be accessed through the ``owned_element`` property or ``get("<name>")`` method. Adding an element in another element's ``owned_element`` list is also possible. It is also possible at the creation time with something like ``factory.create_<sysml_type>_usage(declared_name="<element_name>", owner=<container>)``. Note that ``name`` is derived and read-only: use ``declared_name`` to name an element. Static no-name elements use the ``ClassName::<id>`` fallback, resolvable with ``get("ClassName::<id>")``. See the :ref:`create example <Creating_Example>` for more information.

Static example
--------------

.. code-block:: python

   # Get a sysml/static project from the project manager
   project = project_manager.get_sysml_project().get_root_package()

   # Auto-completion after '.' shows SysML2 properties only
   project.element.  # Shows: name, isAbstract, owned_element, multiplicity, ...

   # Access SysML2 properties directly
   element.name           # Returns: "MyPart"
   element.isAbstract     # Returns: False
   element.owned_element  # Returns list of owned elements

Summary
-------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Aspect
     - Dynamic Approach
     - Static Approach
   * - **Target Environment**
     - Jupyter Notebooks
     - VS Code, PyCharm
   * - **Object Loading**
     - Dynamic (at runtime)
     - Static (at execution)
   * - **Auto-completion shows**
     - Contained objects + ``_camelCase`` accessors
     - SysML2 properties
   * - **SysML2 properties**
     - Prefixed with ``_``
     - Direct access (no prefix)
   * - **Entry Point**
     - :meth:`get_scripting_project() <SysML2ProjectManager.get_scripting_project>`
     - :meth:`get_sysml_project() <SysML2ProjectManager.get_sysml_project>`

Choose the approach that best fits your development workflow:

- Use **dynamic** when exploring models interactively and navigating object hierarchies.
- Use **static** when writing production code in a traditional IDE with type hints and static analysis.

You can find other examples of read/write instructions in :ref:`Read your Model <Read_Model_Section>` and :ref:`Write data to your Model <Write_Model_Section>`.

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: create-conn
            :link-type: doc

            Use a connector

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: manage-projects
            :link-type: doc

            Manage projects