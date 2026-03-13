Accessing SysML v2 Objects: Dynamic vs Static Approaches
==========================================================

This library provides access to SysML v2 objects hosted on a SysML v2 server. In the library, a SysML v2 model is represented by a ``ProjectManager`` instance. The ``ProjectManager`` offers two distinct ways to access objects, each tailored to different development environments:

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Method
     - Approach
     - Best For
   * - ``get_scripting_project()``
     - Dynamic
     - Jupyter Notebooks, interactive environments
   * - ``get_sysml_project()``
     - Static
     - Traditional IDEs (VS Code, PyCharm)

----

Dynamic Approach
------------------

The **scripting approach** is designed for interactive environments like **Jupyter Notebooks**, where code is executed cell by cell and objects are loaded dynamically at each instruction. It corresponds to the unique approach that was proposed in the release 0.1 of PySAM.

Key Characteristics
^^^^^^^^^^^^^^^^^^^

- **Optimized for auto-completion**: After typing a ``.`` (dot), the auto-completion suggestions display the **contained objects** within the current object. This makes it easy to navigate the SysML v2 model hierarchy interactively.

- **SysML v2 properties are underscore-prefixed**: To access native SysML v2 properties (such as ``name``, ``isAbstract``, ``multiplicity``, etc.), you must prefix them with an underscore (``_``).

Example
^^^^^^^

.. code-block:: python

   # Get a dynamic/scripting project from the project manager
   project = project_manager.get_scripting_project().get_root_package()

   # Auto-completion after '.' shows contained objects
   project.MyPart.  # Shows: MyAttribute, MyPort, ...

   # To access SysML v2 properties, use the underscore prefix
   project.MyPart._name          # Returns: "MyPart"
   project.MyPart._isAbstract    # Returns: False
   project.MyPart._multiplicity  # Returns multiplicity info

----

Static Approach
---------------

The **static approach** is designed for traditional **IDE environments** like VS Code or PyCharm, where code is written first and executed later. Since objects are not loaded dynamically at coding time, the content of model elements is not known in advance.

Key Characteristics
^^^^^^^^^^^^^^^^^^^

- **Only SysML v2 properties are exposed**: Because the contained objects cannot be determined at coding time, only the well-defined SysML v2 properties are available as attributes.

- **Direct access to properties**: SysML v2 properties are accessed directly without any prefix.

- **Classic access to contained elements**: The elements contained within a model element can be accessed through the ``owned_element`` property or ``get("<name>")`` method. Adding an element in another element's ``owned_element`` list is also possible. It is also possible at the creation time with something like ``factory.create_<sysml_type>_usage(name="<element_name>", owner=<container>)``. See the :ref:`create example <Creating_Example>` for more information.

Example
^^^^^^^

.. code-block:: python

   # Get a sysml/static project from the project manager
   project = project_manager.get_sysml_project().get_root_package()

   # Auto-completion after '.' shows SysML v2 properties only
   project.element.  # Shows: name, isAbstract, owned_element, multiplicity, ...

   # Access SysML v2 properties directly
   element.name           # Returns: "MyPart"
   element.isAbstract     # Returns: False
   element.owned_element  # Returns list of owned elements

----

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
     - Contained objects
     - SysML v2 properties
   * - **SysML v2 properties**
     - Prefixed with ``_``
     - Direct access (no prefix)
   * - **Entry Point**
     - ``get_scripting_project()``
     - ``get_sysml_project()``

Choose the approach that best fits your development workflow:

- Use **dynamic** when exploring models interactively and navigating object hierarchies.
- Use **static** when writing production code in a traditional IDE with type hints and static analysis.