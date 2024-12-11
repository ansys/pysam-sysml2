Developer installation
======================

#. Start by cloning this repository:

   .. code:: bash

      git clone https://github.com/ansys-internal/pysam-sysml2



#. Make sure you have the latest required build system and doc, testing, and CI tools:

   .. code:: bash

      python -m pip install -U pip flit tox
      python -m pip install -r requirements.txt


#. Finally, verify your development installation by running:

    .. code:: bash

        tox


How to test
-----------

This project takes advantage of `tox`_. This tool allows to automate common
development tasks (similar to Makefile) but it is oriented towards Python
development.

Using tox
^^^^^^^^^

As Makefile has rules, `tox`_ has environments. In fact, the tool creates its
own virtual environment so anything being tested is isolated from the project in
order to guarantee project's integrity. The following environments commands are provided:

- **tox -e style**: checks for coding style quality.
- **tox -e py**: checks for unit tests.
- **tox -e py-coverage**: checks for unit testing and code coverage.
- **tox -e doc**: checks for documentation building process.


A note on pre-commit
^^^^^^^^^^^^^^^^^^^^

The style checks take advantage of `pre-commit`_. Developers are not forced but
encouraged to install this tool via:

.. code:: bash

    python -m pip install pre-commit && pre-commit install


Documentation
-------------

For building documentation, you can use tox :


.. code:: bash

    tox -e doc

Then, open a terminal in *_build/html* and type

.. code:: bash

    py -m http.server

Finally, open your browser and go to `localhost:8000 <http://localhost:8000>`_ for your documentation.


.. LINKS AND REFERENCES
.. _black: https://github.com/psf/black
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _isort: https://github.com/PyCQA/isort
.. _pip: https://pypi.org/project/pip/
.. _pre-commit: https://pre-commit.com/
.. _PyAnsys Developer's guide: https://dev.docs.pyansys.com/
.. _pytest: https://docs.pytest.org/en/stable/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _tox: https://tox.wiki/