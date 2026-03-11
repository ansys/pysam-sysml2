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

"""Generated feature class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .type_ import Type


class Feature(Type):
    """Java class 'com.ansys.medini.metamodel.sysml.Feature'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._inherited = False
        self._type_ = ObservedList(self, "type_")
        self._default_value = None
        self._inherited_type = ObservedList(self, "inherited_type")
        self._inheriting_type = None
        self._is_composite = False
        self._is_end = False
        self._declaration = None
        self._owned_subsetting = ObservedList(self, "owned_subsetting")
        self._direction = None
        self._chaining_feature = ObservedList(self, "chaining_feature")
        self._valuation = None
        self._owned_typing = ObservedList(self, "owned_typing")
        self._set_is_composite = False
        self._set_direction = False
        self._is_ordered = None
        self._is_unique = False
        self._set_is_ordered = False
        self._set_is_unique = False
        self._set_default_value = False
        self._set_valuation = False
        self._referenced_feature = ObservedList(self, "referenced_feature")
        self._feature_value_expression = None
        self._owned_reference_subsetting = ObservedList(self, "owned_reference_subsetting")
        self._owned_redefinition = ObservedList(self, "owned_redefinition")
        self._owned_type_featuring = ObservedList(self, "owned_type_featuring")
        self._owning_feature_membership = None
        self._subsetted_feature = ObservedList(self, "subsetted_feature")
        self._redefined_feature = ObservedList(self, "redefined_feature")
        self._set_feature_value_expression = False
        self._all_redefinitions = ObservedList(self, "all_redefinitions")

    @property
    def inherited(self) -> bool:  # noqa: F821
        """
        Get the inherited property.

        Returns
        -------
        bool
            Value of property inherited.
        """
        return self._inherited

    @property
    def type_(self) -> List["Type"]:  # noqa: F821
        """
        Get the ``type_`` property.

        Returns
        -------
        List["Type"]
            Value of property ``type_``.
        """
        return self._type_

    @property
    def default_value(self) -> "Expression":  # noqa: F821
        """
        Get the default value property.

        Returns
        -------
        "Expression"
            Value of property default value.
        """
        return self._default_value

    @default_value.setter
    def default_value(self, value: "Expression"):  # noqa: F821
        """
        Set the default_value property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "default_value", value)
        self._default_value = value

    @property
    def inherited_type(self) -> List["Type"]:  # noqa: F821
        """
        Get the inherited type property.

        Returns
        -------
        List["Type"]
            Value of property inherited type.
        """
        return self._inherited_type

    @property
    def inheriting_type(self) -> "Type":  # noqa: F821
        """
        Get the inheriting type property.

        Returns
        -------
        "Type"
            Value of property inheriting type.
        """
        return self._inheriting_type

    @inheriting_type.setter
    def inheriting_type(self, value: "Type"):  # noqa: F821
        """
        Set the inheriting_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "inheriting_type", value)
        self._inheriting_type = value

    @property
    def is_composite(self) -> bool:  # noqa: F821
        """
        Get the is composite property.

        Returns
        -------
        bool
            Value of property is composite.
        """
        return self._is_composite

    @is_composite.setter
    def is_composite(self, value: bool):  # noqa: F821
        """
        Set the is_composite property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_composite", value)
        self._is_composite = value

    @property
    def is_end(self) -> bool:  # noqa: F821
        """
        Get the is end property.

        Returns
        -------
        bool
            Value of property is end.
        """
        return self._is_end

    @is_end.setter
    def is_end(self, value: bool):  # noqa: F821
        """
        Set the is_end property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_end", value)
        self._is_end = value

    @property
    def declaration(self) -> "Feature":  # noqa: F821
        """
        Get the declaration property.

        Returns
        -------
        "Feature"
            Value of property declaration.
        """
        return self._declaration

    @property
    def owned_subsetting(self) -> List["Subsetting"]:  # noqa: F821
        """
        Get the owned subsetting property.

        Returns
        -------
        List["Subsetting"]
            Value of property owned subsetting.
        """
        return self._owned_subsetting

    @property
    def direction(self) -> "FeatureDirectionKind":  # noqa: F821
        """
        Get the direction property.

        Returns
        -------
        "FeatureDirectionKind"
            Value of property direction.
        """
        return self._direction

    @direction.setter
    def direction(self, value: "FeatureDirectionKind"):  # noqa: F821
        """
        Set the direction property.

        Parameters
        ----------
        value: "FeatureDirectionKind"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "direction", value)
        self._direction = value

    @property
    def chaining_feature(self) -> List["Feature"]:  # noqa: F821
        """
        Get the chaining feature property.

        Returns
        -------
        List["Feature"]
            Value of property chaining feature.
        """
        return self._chaining_feature

    @property
    def valuation(self) -> "FeatureValue":  # noqa: F821
        """
        Get the valuation property.

        Returns
        -------
        "FeatureValue"
            Value of property valuation.
        """
        return self._valuation

    @valuation.setter
    def valuation(self, value: "FeatureValue"):  # noqa: F821
        """
        Set the valuation property.

        Parameters
        ----------
        value: "FeatureValue"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "valuation", value)
        self._valuation = value

    @property
    def owned_typing(self) -> List["FeatureTyping"]:  # noqa: F821
        """
        Get the owned typing property.

        Returns
        -------
        List["FeatureTyping"]
            Value of property owned typing.
        """
        return self._owned_typing

    @property
    def set_is_composite(self) -> bool:  # noqa: F821
        """
        Get the set is composite property.

        Returns
        -------
        bool
            Value of property set is composite.
        """
        return self._set_is_composite

    @property
    def set_direction(self) -> bool:  # noqa: F821
        """
        Get the set direction property.

        Returns
        -------
        bool
            Value of property set direction.
        """
        return self._set_direction

    @property
    def is_ordered(self) -> None:  # noqa: F821
        """
        Get the is ordered property.

        Returns
        -------
        None
            Value of property is ordered.
        """
        return self._is_ordered

    @is_ordered.setter
    def is_ordered(self, value: None):  # noqa: F821
        """
        Set the is_ordered property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_ordered", value)
        self._is_ordered = value

    @property
    def is_unique(self) -> bool:  # noqa: F821
        """
        Get the is unique property.

        Returns
        -------
        bool
            Value of property is unique.
        """
        return self._is_unique

    @is_unique.setter
    def is_unique(self, value: bool):  # noqa: F821
        """
        Set the is_unique property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_unique", value)
        self._is_unique = value

    @property
    def set_is_ordered(self) -> bool:  # noqa: F821
        """
        Get the set is ordered property.

        Returns
        -------
        bool
            Value of property set is ordered.
        """
        return self._set_is_ordered

    @property
    def set_is_unique(self) -> bool:  # noqa: F821
        """
        Get the set is unique property.

        Returns
        -------
        bool
            Value of property set is unique.
        """
        return self._set_is_unique

    @property
    def set_default_value(self) -> bool:  # noqa: F821
        """
        Get the set default value property.

        Returns
        -------
        bool
            Value of property set default value.
        """
        return self._set_default_value

    @property
    def set_valuation(self) -> bool:  # noqa: F821
        """
        Get the set valuation property.

        Returns
        -------
        bool
            Value of property set valuation.
        """
        return self._set_valuation

    @property
    def referenced_feature(self) -> List["Feature"]:  # noqa: F821
        """
        Get the referenced feature property.

        Returns
        -------
        List["Feature"]
            Value of property referenced feature.
        """
        return self._referenced_feature

    @property
    def feature_value_expression(self) -> "Expression":  # noqa: F821
        """
        Get the feature value expression property.

        Returns
        -------
        "Expression"
            Value of property feature value expression.
        """
        return self._feature_value_expression

    @feature_value_expression.setter
    def feature_value_expression(self, value: "Expression"):  # noqa: F821
        """
        Set the feature_value_expression property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "feature_value_expression", value)
        self._feature_value_expression = value

    @property
    def owned_reference_subsetting(self) -> List["ReferenceSubsetting"]:  # noqa: F821
        """
        Get the owned reference subsetting property.

        Returns
        -------
        List["ReferenceSubsetting"]
            Value of property owned reference subsetting.
        """
        return self._owned_reference_subsetting

    @property
    def owned_redefinition(self) -> List["Redefinition"]:  # noqa: F821
        """
        Get the owned redefinition property.

        Returns
        -------
        List["Redefinition"]
            Value of property owned redefinition.
        """
        return self._owned_redefinition

    @property
    def owned_type_featuring(self) -> List["TypeFeaturing"]:  # noqa: F821
        """
        Get the owned type featuring property.

        Returns
        -------
        List["TypeFeaturing"]
            Value of property owned type featuring.
        """
        return self._owned_type_featuring

    @property
    def owning_feature_membership(self) -> "FeatureMembership":  # noqa: F821
        """
        Get the owning feature membership property.

        Returns
        -------
        "FeatureMembership"
            Value of property owning feature membership.
        """
        return self._owning_feature_membership

    @owning_feature_membership.setter
    def owning_feature_membership(self, value: "FeatureMembership"):  # noqa: F821
        """
        Set the owning_feature_membership property.

        Parameters
        ----------
        value: "FeatureMembership"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_feature_membership", value)
        self._owning_feature_membership = value

    @property
    def subsetted_feature(self) -> List["Feature"]:  # noqa: F821
        """
        Get the subsetted feature property.

        Returns
        -------
        List["Feature"]
            Value of property subsetted feature.
        """
        return self._subsetted_feature

    @property
    def redefined_feature(self) -> List["Feature"]:  # noqa: F821
        """
        Get the redefined feature property.

        Returns
        -------
        List["Feature"]
            Value of property redefined feature.
        """
        return self._redefined_feature

    @property
    def set_feature_value_expression(self) -> bool:  # noqa: F821
        """
        Get the set feature value expression property.

        Returns
        -------
        bool
            Value of property set feature value expression.
        """
        return self._set_feature_value_expression

    @property
    def all_redefinitions(self) -> List["Feature"]:  # noqa: F821
        """
        Get the all redefinitions property.

        Returns
        -------
        List["Feature"]
            Value of property all redefinitions.
        """
        return self._all_redefinitions
