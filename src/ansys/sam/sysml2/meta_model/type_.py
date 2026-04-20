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

"""Generated type class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .namespace import Namespace


class Type(Namespace):
    """Java class 'com.ansys.medini.metamodel.sysml.Type'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._multiplicity = None
        self._set_multiplicity = False
        self._is_abstract = False
        self._is_sufficient = False
        self._directed_feature = ObservedList(self, "directed_feature")
        self._all_feature = ObservedList(self, "all_feature")
        self._set_is_abstract = False
        self._owned_feature = ObservedList(self, "owned_feature")
        self._owned_end_feature = ObservedList(self, "owned_end_feature")
        self._feature = ObservedList(self, "feature")
        self._owned_feature_membership = ObservedList(self, "owned_feature_membership")
        self._owned_inherited_feature = ObservedList(self, "owned_inherited_feature")
        self._owned_specialization = ObservedList(self, "owned_specialization")

    @property
    def multiplicity(self) -> "Multiplicity":  # noqa: F821
        """
        Get the multiplicity property.

        Returns
        -------
        "Multiplicity"
            Value of property multiplicity.
        """
        return self._multiplicity

    @multiplicity.setter
    def multiplicity(self, value: "Multiplicity"):  # noqa: F821
        """
        Set the multiplicity property.

        Parameters
        ----------
        value: "Multiplicity"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "multiplicity", value)
        self._multiplicity = value

    @property
    def set_multiplicity(self) -> bool:  # noqa: F821
        """
        Get the set multiplicity property.

        Returns
        -------
        bool
            Value of property set multiplicity.
        """
        return self._set_multiplicity

    @property
    def is_abstract(self) -> bool:  # noqa: F821
        """
        Get the is abstract property.

        Returns
        -------
        bool
            Value of property is abstract.
        """
        return self._is_abstract

    @is_abstract.setter
    def is_abstract(self, value: bool):  # noqa: F821
        """
        Set the is_abstract property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_abstract", value)
        self._is_abstract = value

    @property
    def is_sufficient(self) -> bool:  # noqa: F821
        """
        Get the is sufficient property.

        Returns
        -------
        bool
            Value of property is sufficient.
        """
        return self._is_sufficient

    @is_sufficient.setter
    def is_sufficient(self, value: bool):  # noqa: F821
        """
        Set the is_sufficient property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_sufficient", value)
        self._is_sufficient = value

    @property
    def directed_feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the directed feature property.

        Returns
        -------
        list["Feature"]
            Value of property directed feature.
        """
        return self._directed_feature

    @property
    def all_feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the all feature property.

        Returns
        -------
        list["Feature"]
            Value of property all feature.
        """
        return self._all_feature

    @property
    def set_is_abstract(self) -> bool:  # noqa: F821
        """
        Get the set is abstract property.

        Returns
        -------
        bool
            Value of property set is abstract.
        """
        return self._set_is_abstract

    @property
    def owned_feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the owned feature property.

        Returns
        -------
        list["Feature"]
            Value of property owned feature.
        """
        return self._owned_feature

    @property
    def owned_end_feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the owned end feature property.

        Returns
        -------
        list["Feature"]
            Value of property owned end feature.
        """
        return self._owned_end_feature

    @property
    def feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the feature property.

        Returns
        -------
        list["Feature"]
            Value of property feature.
        """
        return self._feature

    @property
    def owned_feature_membership(self) -> list["FeatureMembership"]:  # noqa: F821
        """
        Get the owned feature membership property.

        Returns
        -------
        list["FeatureMembership"]
            Value of property owned feature membership.
        """
        return self._owned_feature_membership

    @property
    def owned_inherited_feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the owned inherited feature property.

        Returns
        -------
        list["Feature"]
            Value of property owned inherited feature.
        """
        return self._owned_inherited_feature

    @property
    def owned_specialization(self) -> list["Specialization"]:  # noqa: F821
        """
        Get the owned specialization property.

        Returns
        -------
        list["Specialization"]
            Value of property owned specialization.
        """
        return self._owned_specialization
