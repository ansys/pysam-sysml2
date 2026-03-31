# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Private implementation for a project."""

from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.classes.unresolved_field import UnresolvedField
from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.meta_model.package import Package


class ProjectImpl(Project):
    """Provides a private class for project building."""

    _id: str
    _env: dict
    _root: list[Element]
    _unresolved_fields: list[UnresolvedField]
    _libraries_ids: set[str]
    _name: str

    def __init__(self, project_id: str, name: str):
        """
        Construct a new instance.

        Parameters
        ----------
        project_id : str
            Project ID.
        name : str
            Project name.
        """
        super().__init__()
        self._id = project_id
        self._root = []
        self._name = name
        self._unresolved_fields = []
        self._libraries_ids = set()
        self._env = {}

    def add_element(self, element: Element):
        """Add an element to the project environment."""
        self._env[element.id] = element

    def update_unresolved_fields(self, unresolved_fields: list[UnresolvedField]):
        """
        Update all unresolved fields.

        Parameters
        ----------
        unresolved_fields : List[UnresolvedField]
            List of all new fields.
        """
        self._unresolved_fields.extend(unresolved_fields)

    def get_root(self) -> list[Package]:
        """
        Get a list of root packages.

        Returns
        -------
        List[Package]
            List of root packages.
        """
        return self._root

    def get_root_package(self) -> Package:
        """Get the root package."""
        matches = [x for x in self._root if isinstance(x, Package) and x.name == self._name]
        if not matches:
            raise ValueError(f"No root Package named '{self._name}' found in project")
        return matches[0]

    def get_name(self) -> str:
        """Get the project name."""
        return self._name

    def find_element_by_id(self, element_id: str) -> Element | None:
        """
        Find an element by its ID.

        Parameters
        ----------
        element_id : str
            Element ID.

        Returns
        -------
        Element
            Element retrieved.
        """
        return self._env.get(element_id)

    def find_elements_by_name(self, element_name: str) -> list[Element]:
        """
        Find all elements by name.

        Parameters
        ----------
        element_name : str
            Name of elements.

        Returns
        -------
        List[Element]
            List of elements retrieved.
        """
        return [
            el for el in self._env.values() if SysMLUtil.check_inherited_name(el) == element_name
        ]

    def start_transactional_mode(self) -> None:
        """
        Start a transactional mode for model edition.

        This method will stop direct update for the model,
        and register all changes until you commit or stop the transactional mode.

        Warning, all calculated modifications will not be applied,
        until the commit of all changes.
        """
        self.get_root_package()._observer.set_transactional_mode(True)

    def stop_transactional_mode(self) -> None:
        """
        Stop the current transaction.

        This method will close the current transaction and commit all changes to the server.
        """
        self.get_root_package()._observer.set_transactional_mode(False)
