.. _ref_contributing:

==========
Contribute
==========

PySAM SysML2 is a Python library that makes accessing the SysML V2 standard API easier. It is developed by the R&D team dedicated to Ansys SAM. For now, the only tested implementation of the SysML V2 standard API is the one proposed by SAM.

Contributing to PySAM SysML2 is welcomed and can be in the form of discussions, code,
documentation, or issue reports.


Overall guidance on contributing to a PyAnsys library appears in the
`Contributing <https://dev.docs.pyansys.com/>`_ topic
in the *PyAnsys developer's guide*. Ensure that you are thoroughly familiar
with it and all style guidelines before attempting to contribute to PySAM SysML2.

The following contribution information is specific to PySAM SysML2.

PySAM SysML2 documentation
--------------------------
Documentation for the latest stable release of PySAM SysML2 is hosted at
`PySAM SysML2 documentation <https://sysml2.docs.pyansys.com>`_.

This version is automatically kept up to date with GitHub actions.


Posting Issues
--------------

Use the `PySAM SysML2 Issues <https://github.com/ansys/pysam-sysml2/issues>`_
page to submit questions, report bugs, and request new features. When possible,
use one of the existing templates.

.. update to https://github.com/ansys/pysam-sysml2/issues when ready

To reach the project support team, email `pyansys.core@ansys.com <pyansys.core@ansys.com>`_.

Contribute code
---------------

.. Note::
   As PySAM SysML2 is associated with the SysML V2 standard API and strongly related to SAM,
   any contribution is analyzed and possibly integrated by the SAM development team.

Source code
^^^^^^^^^^^^
Run this code to clone and install the latest version of PySAM SysML2 in development mode:

.. code::

    # Create a PySAM directory and the virtual environment
    mkdir PySAM
    cd PySAM
    python -m venv pysam-dev-env
    pysam-dev-env\Scripts\activate

    # Clone the repository and install
    git clone https://github.com/ansys/pysam-sysml2.git
    cd pysam-sysml2

    # Update pip and install the project with all dependencies including optional ones
    python -m pip install --upgrade pip
    pip install -e ".[doc,tests,checks]"


.. update to https://github.com/ansys/pysam-sysml2.git when ready

Code style
^^^^^^^^^^
PySAM SysML2 follows the PEP8 standard as outlined in the `PyAnsys development guide
<https://dev.docs.pyansys.com>`_. Code style is enforced using `Ruff <https://github.com/astral-sh/ruff>`_ for linting.


Testing
^^^^^^^

PySAM SysML2 uses `pytest <https://docs.pytest.org/en/stable/>`_.
In the main directory, run this command:

.. code::

    pytest

Tests are in the ``tests`` folder. Add your own tests for non-regression.

To run tests with coverage:

.. code::

    pytest --cov=ansys.sam.sysml2 --cov-report=html

This generates a coverage report in ``htmlcov/index.html``.

Documentation
^^^^^^^^^^^^^

Build the documentation
""""""""""""""""""""""""

PySAM SysML2 uses Sphinx for documentation generation. To build the documentation:

.. code::

    cd doc
    .\make.bat html

To generate a PDF version:

.. code::

    .\make.bat pdf

The generated HTML documentation is in the ``doc/_build/html`` directory
and can be viewed locally:

.. code::

    cd _build/html
    python -m http.server

Then open your browser to ``http://localhost:8000``.

The PDF is generated in the ``doc/_build/latex`` directory.

Run Vale
""""""""

Vale is used to enforce documentation style guidelines and ensure consistency across the documentation.
It checks for grammar, style, and terminology compliance with the Google developer and
Ansys style guides.

Before running Vale, you must download the style definitions:

.. code::

    cd doc
    vale sync

This downloads the required style guides defined in the ``.vale.ini`` file

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

Once installed, the hooks run automatically when you run the ``git commit`` command. The pre-commit configuration is defined in the ``.pre-commit-config.yaml`` file.

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

The CI/CD pipeline automatically run these checks on multiple Python versions (3.10, 3.11, 3.12, 3.13, and 3.14) when you submit your pull request.

.. note::
   While you can run tests locally on your installed Python version, the CI/CD pipeline ensures compatibility across all supported Python versions.