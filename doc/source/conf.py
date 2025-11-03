"""Sphinx documentation configuration file."""

from datetime import datetime
import os
from pathlib import Path

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
cname = os.getenv("DOCUMENTATION_CNAME", "sam.docs.pyansys.com")
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."

# Select desired favicon, logo, theme, and declare the html title
html_favicon = ansys_favicon
html_short_title = html_title = "pysam-sysml2"

html_theme = "ansys_sphinx_theme"
html_theme_options = {
    "github_url": "https://github.com/ansys-internal/pysam-sysml2",
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
    "icon_links": [
        {
            "name": "Support",
            "url": "https://github.com/ansys/pysam-sysml2/discussions",
            "icon": "fa fa-comment fa-fw",
        },
    ],
    "ansys_sphinx_theme_autoapi": {
        "project": project,
    },
    "static_search": {
        "threshold": 0.5,
        "minMatchCharLength": 2,
        "ignoreLocation": True,
    },
}


# LaTeX Compatible Paths
def escape_latex_path(path):
    """Escape paths for LaTeX."""
    from pathlib import Path

    abs_path = Path(path).resolve()
    latex_path = str(abs_path).replace("\\", "/")
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
latex_elements = {
    "preamble": (generate_preamble("PySAM SysML2", watermark)),
    "printindex": "",
}

# Sphinx extensions
extensions = [
    "ansys_sphinx_theme.extension.autoapi",
    "numpydoc",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
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

# Autosectionlabel configuration to avoid duplicate label warnings
autosectionlabel_prefix_document = True

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    # "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    # "SS02",  # Summary does not start with a capital letter
    # "SS03",  # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    "SS05",  # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}

# static path
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Patterns to exclude
exclude_patterns = [
    "links.rst",
]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# Configuration for Sphinx autoapi
suppress_warnings = [
    "autoapi.python_import_resolution",
    "design.grid",
    "config.cache",
    "design.fa-build",
    "toc.not_included",  # Caused by the autoapi extension and the "_grpc" folder
]

# make rst_epilog a variable, so you can add other epilog parts to it
rst_epilog = ""
# Read link all targets from file
with Path.open("links.rst") as f:
    rst_epilog += f.read()

# Keep these while the repository is private
linkcheck_ignore = [
    "https://github.com/ansys-internal/pysam-sysml2/*",
    "https://sam.docs.pyansys.com/version/stable/*",
    "https://pypi.org/project/ansys-sam-sysml2",
    "https://www.ansys.com/*",  # to be removed -- user_agent is supposed to handle this
]

# User agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.2420.81"  # noqa: E501

# If we are on a release, we have to ignore the "release" URLs, since it is not
# available until the release is published.
if switcher_version != "dev":
    linkcheck_ignore.append(
        f"https://github.com/ansys/ansys.sam.sysml2/releases/tag/v{__version__}"
    )
