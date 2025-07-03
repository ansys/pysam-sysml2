"""Sphinx documentation configuration file."""

from datetime import datetime

from ansys_sphinx_theme import (
    ansys_favicon,
    ansys_logo_white,
    ansys_logo_white_cropped,
    get_version_match,
    pyansys_logo_black,
    watermark,
)
from ansys_sphinx_theme.latex import generate_preamble

from ansys.sam.sysml2 import __version__

# Project information
project = "ansys-sam-sysml2"
release = version = __version__
switcher_version = get_version_match(__version__)
cname = "https://sam.docs.pyansys.com"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."

# Select desired favicon, logo, theme, and declare the html title
html_favicon = ansys_favicon
html_short_title = html_title = "pysam-sysml2"

html_theme = "ansys_sphinx_theme"
html_theme_options = {
    "github_url": "https://github.com/ansys/pysam-sysml2",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": switcher_version,
    },
    "check_switcher": False,
    "logo": "pyansys",
}


# LaTeX Compatible Paths
def escape_latex_path(path):
    """Escape paths for LaTeX."""
    import os

    abs_path = os.path.abspath(path)
    latex_path = abs_path.replace("\\", "/")
    latex_path = latex_path.replace(" ", "\\ ")
    return latex_path


watermark = escape_latex_path(watermark)
ansys_logo_white = escape_latex_path(ansys_logo_white)
ansys_logo_white_cropped = escape_latex_path(ansys_logo_white_cropped)
pyansys_logo_black = escape_latex_path(pyansys_logo_black)

# Latex PDF generation parameters
latex_additional_files = [
    watermark,
    ansys_logo_white,
    ansys_logo_white_cropped,
    pyansys_logo_black,
]
latex_elements = {"preamble": (generate_preamble("PySam", watermark))}

# Sphinx extensions
extensions = [
    "numpydoc",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    # kept here as an example
    # "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    # "numpy": ("https://numpy.org/devdocs", None),
    # "matplotlib": ("https://matplotlib.org/stable", None),
    # "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    # "pyvista": ("https://docs.pyvista.org/", None),
    # "grpc": ("https://grpc.github.io/grpc/python/", None),
}

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    "SS02",  # Summary does not start with a capital letter
    "SS03",  # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    "SS05",  # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}

# static path
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# Keep these while the repository is private
linkcheck_ignore = [
    "https://github.com/ansys-internal/pysam-sysml2/*",
    "https://sam.docs.pyansys.com/version/stable/*",
    "https://pypi.org/project/ansys-sam-sysml2",
]

# If we are on a release, we have to ignore the "release" URLs, since it is not
# available until the release is published.
if switcher_version != "dev":
    linkcheck_ignore.append(
        f"https://github.com/ansys/ansys.sam.sysml2/releases/tag/v{__version__}"
    )
