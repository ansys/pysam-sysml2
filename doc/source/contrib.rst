.. _ref_contributing:

============
Contributing
============

PySAM SysML2 is a Python library dedicated to make access to SysML V2 standard API easier. It is developed by the R&D team dedicated to Ansys SAM. For now, the only tested implementation of the SysML V2 standard API is the one proposed by SAM.

Contributing to PySAM SysML2 is welcomed and can be in the form of discussions, code,
documentation, or issue reports.


Overall guidance on contributing to a PyAnsys library appears in the
`Contributing <https://dev.docs.pyansys.com/>`_ topic
in the *PyAnsys Developer's Guide*. Ensure that you are thoroughly familiar
with it and all style guidelines before attempting to contribute to PySAM SysML2.

The following contribution information is specific to PySAM SysML2.

PySAM SysML2 documentation
--------------------------
Documentation for the latest stable release of PySAM SysML2 is hosted at
`PySAM SysML2 Documentation <https://probable-doodle-z27n1yp.pages.github.io>`_.

.. update to https://sam.docs.pyansys.com when ready

This version is automatically kept up to date via GitHub actions.


Posting Issues
--------------

Use the `PySAM SysML2 Issues <https://github.com/ansys-internal/pysam-sysml2/issues>`_
page to submit questions, report bugs, and request new features. When possible,
use one of the existing templates.

.. update to https://github.com/ansys/pysam-sysml2/issues when ready

To reach the project support team, email `pyansys.core@ansys.com <pyansys.core@ansys.com>`_.

Contributing code
-----------------

.. Note::
   As PySAM SysML2 is associated to the SysML V2 standard API and so strongly related to SAM, any contribution is analyzed and possibly
   integrated by the SAM development team.

Getting the source code
^^^^^^^^^^^^^^^^^^^^^^^
Run this code to clone and install the latest version of PySAM SysML2 in development mode:

.. code::

    # Create a PySAM directory and the virtual environment
    mkdir PySAM
    cd PySAM
    python -m venv pysam-dev-env
    pysam-dev-env\Scripts\activate

    # Clone the repository and install
    git clone https://github.com/ansys-internal/pysam-sysml2.git
    cd pysam-sysml2

    # Update pip and install the project with all dependencies including optional ones
    python -m pip install --upgrade pip
    pip install -e ".[doc,tests,checks]"


.. update to https://github.com/ansys/pysam-sysml2.git when ready

Code style
^^^^^^^^^^
PySAM SysML2 follows PEP8 standard as outlined in the `PyAnsys Development Guide
<https://dev.docs.pyansys.com>`_. Code style is enforced using ``ruff`` for linting.


Testing
^^^^^^^

PySAM SysML2 uses `pytest`. In the main directory use:

.. code::

    pytest

Tests are in `tests` folder. Please add your own tests for non-regression.

To run tests with coverage:

.. code::

    pytest --cov=ansys.sam.sysml2 --cov-report=html

This generates a coverage report in ``htmlcov/index.html``.

Documentation
^^^^^^^^^^^^^

Building the documentation
"""""""""""""""""""""""""""

PySAM SysML2 uses Sphinx for documentation generation. To build the documentation:

.. code::

    cd doc
    .\make.bat html

To generate a PDF version:

.. code::

    .\make.bat pdf

The generated HTML documentation is available in ``doc/_build/html`` and can be viewed locally:

.. code::

    cd _build/html
    python -m http.server

Then open your browser to ``http://localhost:8000``.

The PDF is generated in ``doc/_build/latex``.

Vale documentation linting
""""""""""""""""""""""""""

Vale is used to enforce documentation style guidelines and ensure consistency across the documentation.
It checks for grammar, style, and terminology compliance with the Google and Ansys style guides.

Before running Vale, you must download the style definitions:

.. code::

    cd doc
    vale sync

This downloads the required style guides defined in ``.vale.ini``.

To check documentation files:

.. code::

    vale .

Vale reports any style violations, spelling errors, or inconsistencies. Fix these issues before submitting documentation changes.

Pre-commit hooks
^^^^^^^^^^^^^^^^

PySAM SysML2 uses pre-commit hooks to automatically check code quality before each commit.
Pre-commit runs various checks including code formatting, linting, and style validation.

To install the pre-commit hooks:

.. code::

    pre-commit install

Once installed, the hooks run automatically on ``git commit``. The pre-commit configuration is defined in ``.pre-commit-config.yaml``.

To manually run all pre-commit hooks on all files:

.. code::

    pre-commit run --all-files

If a hook fails, fix the reported issues and commit again. Some hooks (like ``ruff``) can automatically fix issues.


Quality checks workflow
^^^^^^^^^^^^^^^^^^^^^^^

Before submitting a pull request, ensure all quality checks pass:

1. **Run tests**: ``pytest``
2. **Run tests with coverage**: ``pytest --cov=ansys.sam.sysml2 --cov-report=html``
3. **Check code style**: ``ruff check .``
4. **Format code**: ``ruff format .``
5. **Check documentation style**: ``cd doc; vale sync; vale .``
6. **Run pre-commit checks**: ``pre-commit run --all-files``

The CI/CD pipeline automatically run these checks on multiple Python versions (3.10, 3.11, 3.12, 3.13) when you submit your pull request.

.. note::
   While you can run tests locally on your installed Python version, the CI/CD pipeline ensures compatibility across all supported Python versions.