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

"""Derived List for SysMl List."""

from typing import Any

from ansys.sam.sysml2.classes.sysml_element import SysMLElement


def mount_observer_and_access(function):
    """
    Check write access and notify observer.

    Parameters
    ----------
    function : callable
        Function to watch
    """

    def wrapper(self, *args):
        if not self._owner._IS_READ_ONLY:
            val = function(self, *args)
            if self._owner._observer is not None:
                self._owner._observer.list_notify(self._owner._id, self._name, self)
            return val

    return wrapper


class DerivedList(list):
    """Derived list class."""

    _content: list
    _name: str
    _owner: SysMLElement

    def __init__(self, owner: SysMLElement, name: str, *args):
        """
        Construct method for new instance.

        Parameters
        ----------
        owner : SysMLElement
            Owner of this list.
        """
        if len(args) > 0:
            super().extend(args)
        self._owner = owner
        self._name = name

    @mount_observer_and_access
    def append(self, object: Any):
        """
        Override method append.

        Parameters
        ----------
        object : any
            /

        """
        return super().append(object)

    @mount_observer_and_access
    def extend(self, iterable):
        """
        Override method extend.

        Parameters
        ----------
        iterable : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        return super().extend(iterable)

    @mount_observer_and_access
    def insert(self, index, object):
        """
        Override method insert.

        Parameters
        ----------
        index : _type_
            _description_
        object : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        return super().insert(index, object)

    @mount_observer_and_access
    def remove(self, value):
        """
        Override method remove.

        Parameters
        ----------
        value : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        return super().remove(value)

    @mount_observer_and_access
    def pop(self, index=-1):
        """
        Override method pop.

        Parameters
        ----------
        index : int, optional
            _description_, by default -1

        Returns
        -------
        _type_
            _description_
        """
        return super().pop(index)

    @mount_observer_and_access
    def reverse(self):
        """
        Override method reverse.

        Returns
        -------
        _type_
            _description_
        """
        return super().reverse()

    @mount_observer_and_access
    def __iadd__(self, value):
        """
        Override method __iadd__.

        Parameters
        ----------
        value : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        return super().__iadd__(value)

    @mount_observer_and_access
    def __imul__(self, value):
        """
        Override method __imul__.

        Parameters
        ----------
        value : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        return super().__imul__(value)

    @mount_observer_and_access
    def __setitem__(self, key, value):
        """
        Override method __setitem__.

        Parameters
        ----------
        key : _type_
            _description_
        value : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        return super().__setitem__(key, value)

    @mount_observer_and_access
    def __delitem__(self, key):
        """
        Override method __delitem__.

        Parameters
        ----------
        key : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        return super().__delattr__(key)
