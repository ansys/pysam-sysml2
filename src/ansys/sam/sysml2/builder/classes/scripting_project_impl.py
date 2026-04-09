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

"""Private implementation for a scripting project."""

from typing import List, Set

from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil
from ansys.sam.sysml2.classes.scripting_project import ScriptingProject
from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.classes.unresolved_field import UnresolvedField


class ScriptingProjectImpl(ScriptingProject):
    """Provides a private class for scripting project building."""

    _id: str
    _env: dict
    _root: List[SysMLElement]
    _unresolved_fields: List[UnresolvedField]
    _libraries_ids: Set[str]
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
        self._root = list()
        self._name = name
        self._unresolved_fields = list()
        self._libraries_ids = set()
        self._env = dict()

    def add_element(self, element: SysMLElement):
        """Add an element to the project environment."""
        self._env[element._id] = element

    def update_unresolved_fields(self, unresolved_fields: List[UnresolvedField]):
        """
        Update all unresolved fields.

        Parameters
        ----------
        unresolved_fields : List[UnresolvedField]
            List of all new fields.
        """
        self._unresolved_fields.extend(unresolved_fields)

    def get_root(self) -> List[SysMLElement]:
        """
        Get a list of root packages.

        Returns
        -------
        List[SysMLElement]
            List of root packages.
        """
        return self._root

    def get_root_package(self) -> SysMLElement:
        """Get the root package."""
        root = next(
            iter(
                [
                    x
                    for x in self._root
                    if x.__class__.__name__ == "Package" and x._name == self._name
                ]
            ),
            None,
        )
        if root is None:
            raise ValueError("The project does not contain any root package.")
        return root

    def get_name(self) -> str:
        """Get the project name."""
        return self._name

    def find_element_by_id(self, element_id: str) -> SysMLElement:
        """
        Find an element by its ID.

        Parameters
        ----------
        element_id : str
            Element ID.

        Returns
        -------
        SysMLElement
            SysMLElement retrieved.
        """
        return self._env.get(element_id, None)

    def find_elements_by_name(self, element_name: str) -> List[SysMLElement]:
        """
        Find all elements by name.

        Parameters
        ----------
        element_name : str
            Name of elements.

        Returns
        -------
        List[SysMLElement]
            List of elements retrieved.
        """
        return [
            el for _, el in self._env.items() if SysMLUtil.check_inherited_name(el) == element_name
        ]

    def start_transactional_mode(self):
        """
        Start a transactional mode for model edition.

        This method will stop direct update for the model,
        and register all changes until you commit or stop the transactional mode.

        Warning, all calculated modifications will not be applied,
        until the commit of all changes.
        """
        self.get_root_package()._observer.set_transactional_mode(True)

    def stop_transactional_mode(self):
        """
        Stop the current transaction.

        This method will close the current transaction and commit all changes to the server.
        """
        self.get_root_package()._observer.set_transactional_mode(False)
