.. _ref_contributing:

============
Contributing
============

PySam-SysML2 is a Python library dedicated to make access to SysML v2 Standard API easier. It is developed by the R&D team dedicated to Ansys SAM. For now, the only tested implementation of the SysML v2 Std API is the one proposed by SAM.

Contributing to PySam-SysML2 is welcomed and can be in the form of discussions, code, 
documentation, or issue reports.


Overall guidance on contributing to a PyAnsys library appears in the
`Contributing <https://dev.docs.pyansys.com/>`_ topic
in the *PyAnsys Developer's Guide*. Ensure that you are thoroughly familiar
with it and all style guidelines before attempting to contribute to PySam-SysML2.
 
The following contribution information is specific to PySam-SysML2.

PySam-SysML2 documentation
------------------------
Documentation for the latest stable release of PySam-SysML2 is hosted at
`PySam-SysML2 Documentation <https://pysam-sysml2.docs.pyansys.com>`_.

This version is automatically kept up to date via GitHub actions.


Posting Issues
--------------

Use the `PySam-SysML2 Issues <https://github.com/ansys/pysam-sysml2/issues>`_
page to submit questions, report bugs, and request new features. When possible, 
use one of the existing templates.


To reach the project support team, email `pyansys.core@ansys.com <pyansys.core@ansys.com>`_.

Discussions
-----------

Use the `PySam-SysML2 Discussions <https://github.com/ansys/pysam-sysml2/discussions>`_	
page to ask questions, share ideas, and connect with other users.


Contributing code
-----------------

.. Note::
   As PySam-SysML2 is associated to the SysML v2 Std API and so strongly related to SAM, Any contribution is analyzed and possibly
   integrated by the SAM development team.

Getting the source code
^^^^^^^^^^^^^^^^^^^^^^^
Run this code to clone and install the latest version of PySam-SysML2 in development mode:

.. code::

    git clone https://github.com/ansys/pyscadeone
    cd pyscadeone
    pip install pip -U
    pip install -e .

Code style
^^^^^^^^^^
PySam-SysML2 follows PEP8 standard as outlined in the `PyAnsys Development Guide
<https://dev.docs.pyansys.com>`_.


Testing
^^^^^^^

PySam-SysML2 uses `pytest`. In the main directory use:

.. code::

    pytest

Tests are in `tests` folder. Please add your own tests for non-regression.
