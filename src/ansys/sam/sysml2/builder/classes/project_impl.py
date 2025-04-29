# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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

"""Private implementation for Project."""

from typing import List, Set

from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.classes.unresolved_field import UnresolvedField


class ProjectImpl(Project):
    """Private class for project building."""

    _id: str
    _env: dict
    _root: List[SysMLElement]
    _unresolved_fields: List[UnresolvedField]
    _libraries_ids: Set[str]
    _name: str

    def __init__(self, id: str, name: str):
        """
        Construct Method for new instance.

        Parameters
        ----------
        id : str
            project id.
        """
        super().__init__()
        self._id = id
        self._root = list()
        self._name = name
        self._unresolved_fields = list()
        self._libraries_ids = set()
        self._env = dict()

    def add_element(self, element: SysMLElement):
        """
        Add an element to the project env.

        Parameters
        ----------
        element : SysMLElement
            The element to add.
        """
        self._env[element._id] = element

    def update_unresolved_fields(self, unresolved_fields: List[UnresolvedField]):
        """
        Update all unresolved field.

        Parameters
        ----------
        unresolved_fields : List[UnresolvedField]
            All new fields
        """
        self._unresolved_fields.extend(unresolved_fields)

    def get_root(self) -> List[SysMLElement]:
        """
        Return the list of root packages.

        Returns
        -------
        List[SysMLElement]
            List of roots packages
        """
        return self._root

    def get_root_package(self) -> SysMLElement:
        """
        Return root package.

        Returns
        -------
        SysMLElement
            Root element
        """
        return [x for x in self._root if x.__class__.__name__ == "Package"][0]

    def get_name(self) -> str:
        """
        Getter for name.

        Returns
        -------
        str
            Project name
        """
        return self._name

    def find_element_by_id(self, element_id: str) -> SysMLElement:
        """
        Find element with id.

        Parameters
        ----------
        element_id : str
            Element Id

        Returns
        -------
        SysMLElement
            Founded Element
        """
        return self._env.get(element_id, None)

    def find_elements_by_name(self, elements_name: str) -> List[SysMLElement]:
        """
        Find all element with name.

        Parameters
        ----------
        elements_name : str
            Name if elements

        Returns
        -------
        List[SysMLElement]
            founded Element
        """
        return [
            el for _, el in self._env.items() if SysMLUtil.check_inherited_name(el) == elements_name
        ]

    def start_modification(self):
        """Authorize user to write on the model."""
        for _, element in self._env.items():
            element._IS_READ_ONLY = False

    def end_modification(self, reload: bool = False):
        """
        Commit all registered modification on the model.

        Parameters
        ----------
        reload : bool, optional
            Reload the model from server, by default False
        """
        for _, element in self._env.items():
            element._IS_READ_ONLY = True
