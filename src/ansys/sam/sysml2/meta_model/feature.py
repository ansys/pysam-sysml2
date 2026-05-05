"""Generated feature class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .type_ import Type


class Feature(Type):
    """Java class 'com.ansys.metamodel.sysml2.Feature'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._chaining_feature = ObservedList(self, "chaining_feature")
        self._cross_feature = None
        self._direction = None
        self._endfeaturemembership = None
        self._feature_target = None
        self._featuring_type = False
        self._owned_cross_subsetting = None
        self._owned_feature_chaining = ObservedList(self, "owned_feature_chaining")
        self._owned_feature_inverting = ObservedList(self, "owned_feature_inverting")
        self._owned_redefinition = ObservedList(self, "owned_redefinition")
        self._owned_reference_subsetting = None
        self._owned_subsetting = ObservedList(self, "owned_subsetting")
        self._owned_type_featuring = ObservedList(self, "owned_type_featuring")
        self._owned_typing = ObservedList(self, "owned_typing")
        self._owning_feature_membership = None
        self._owning_type = None
        self._type_ = ObservedList(self, "type_")
        self._valuation = None
        self._cartesian_product = False
        self._compatible_with = False
        self._featured_within = False
        self._is_composite = False
        self._is_constant = False
        self._is_derived = False
        self._is_end = False
        self._is_ordered = False
        self._is_portion = False
        self._is_unique = False
        self._is_variable = False
        self._owned_cross_feature = False
        self._set_direction = False

    @property
    def chaining_feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the chaining feature property.

        Returns
        -------
        list["Feature"]
            Value of property chaining feature.
        """
        return self._chaining_feature

    @property
    def cross_feature(self) -> "Feature":  # noqa: F821
        """
        Get the cross feature property.

        Returns
        -------
        "Feature"
            Value of property cross feature.
        """
        return self._cross_feature

    @cross_feature.setter
    def cross_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the cross_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "cross_feature", value)
        self._cross_feature = value

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
    def endfeaturemembership(self) -> "EndFeatureMembership":  # noqa: F821
        """
        Get the endfeaturemembership property.

        Returns
        -------
        "EndFeatureMembership"
            Value of property endfeaturemembership.
        """
        return self._endfeaturemembership

    @endfeaturemembership.setter
    def endfeaturemembership(self, value: "EndFeatureMembership"):  # noqa: F821
        """
        Set the endfeaturemembership property.

        Parameters
        ----------
        value: "EndFeatureMembership"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "endfeaturemembership", value)
        self._endfeaturemembership = value

    @property
    def feature_target(self) -> "Feature":  # noqa: F821
        """
        Get the feature target property.

        Returns
        -------
        "Feature"
            Value of property feature target.
        """
        return self._feature_target

    @feature_target.setter
    def feature_target(self, value: "Feature"):  # noqa: F821
        """
        Set the feature_target property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "feature_target", value)
        self._feature_target = value

    @property
    def featuring_type(self) -> bool:  # noqa: F821
        """
        Get the featuring type property.

        Returns
        -------
        bool
            Value of property featuring type.
        """
        return self._featuring_type

    @property
    def owned_cross_subsetting(self) -> "CrossSubsetting":  # noqa: F821
        """
        Get the owned cross subsetting property.

        Returns
        -------
        "CrossSubsetting"
            Value of property owned cross subsetting.
        """
        return self._owned_cross_subsetting

    @owned_cross_subsetting.setter
    def owned_cross_subsetting(self, value: "CrossSubsetting"):  # noqa: F821
        """
        Set the owned_cross_subsetting property.

        Parameters
        ----------
        value: "CrossSubsetting"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_cross_subsetting", value)
        self._owned_cross_subsetting = value

    @property
    def owned_feature_chaining(self) -> list["FeatureChaining"]:  # noqa: F821
        """
        Get the owned feature chaining property.

        Returns
        -------
        list["FeatureChaining"]
            Value of property owned feature chaining.
        """
        return self._owned_feature_chaining

    @property
    def owned_feature_inverting(self) -> list["FeatureInverting"]:  # noqa: F821
        """
        Get the owned feature inverting property.

        Returns
        -------
        list["FeatureInverting"]
            Value of property owned feature inverting.
        """
        return self._owned_feature_inverting

    @property
    def owned_redefinition(self) -> list["Redefinition"]:  # noqa: F821
        """
        Get the owned redefinition property.

        Returns
        -------
        list["Redefinition"]
            Value of property owned redefinition.
        """
        return self._owned_redefinition

    @property
    def owned_reference_subsetting(self) -> "ReferenceSubsetting":  # noqa: F821
        """
        Get the owned reference subsetting property.

        Returns
        -------
        "ReferenceSubsetting"
            Value of property owned reference subsetting.
        """
        return self._owned_reference_subsetting

    @owned_reference_subsetting.setter
    def owned_reference_subsetting(self, value: "ReferenceSubsetting"):  # noqa: F821
        """
        Set the owned_reference_subsetting property.

        Parameters
        ----------
        value: "ReferenceSubsetting"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_reference_subsetting", value)
        self._owned_reference_subsetting = value

    @property
    def owned_subsetting(self) -> list["Subsetting"]:  # noqa: F821
        """
        Get the owned subsetting property.

        Returns
        -------
        list["Subsetting"]
            Value of property owned subsetting.
        """
        return self._owned_subsetting

    @property
    def owned_type_featuring(self) -> list["TypeFeaturing"]:  # noqa: F821
        """
        Get the owned type featuring property.

        Returns
        -------
        list["TypeFeaturing"]
            Value of property owned type featuring.
        """
        return self._owned_type_featuring

    @property
    def owned_typing(self) -> list["FeatureTyping"]:  # noqa: F821
        """
        Get the owned typing property.

        Returns
        -------
        list["FeatureTyping"]
            Value of property owned typing.
        """
        return self._owned_typing

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
    def owning_type(self) -> "Type":  # noqa: F821
        """
        Get the owning type property.

        Returns
        -------
        "Type"
            Value of property owning type.
        """
        return self._owning_type

    @owning_type.setter
    def owning_type(self, value: "Type"):  # noqa: F821
        """
        Set the owning_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_type", value)
        self._owning_type = value

    @property
    def type_(self) -> list["Type"]:  # noqa: F821
        """
        Get the type property.

        Returns
        -------
        list["Type"]
            Value of property type.
        """
        return self._type_

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
    def cartesian_product(self) -> bool:  # noqa: F821
        """
        Get the cartesian product property.

        Returns
        -------
        bool
            Value of property cartesian product.
        """
        return self._cartesian_product

    @property
    def compatible_with(self) -> bool:  # noqa: F821
        """
        Get the compatible with property.

        Returns
        -------
        bool
            Value of property compatible with.
        """
        return self._compatible_with

    @property
    def featured_within(self) -> bool:  # noqa: F821
        """
        Get the featured within property.

        Returns
        -------
        bool
            Value of property featured within.
        """
        return self._featured_within

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
    def is_constant(self) -> bool:  # noqa: F821
        """
        Get the is constant property.

        Returns
        -------
        bool
            Value of property is constant.
        """
        return self._is_constant

    @is_constant.setter
    def is_constant(self, value: bool):  # noqa: F821
        """
        Set the is_constant property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_constant", value)
        self._is_constant = value

    @property
    def is_derived(self) -> bool:  # noqa: F821
        """
        Get the is derived property.

        Returns
        -------
        bool
            Value of property is derived.
        """
        return self._is_derived

    @is_derived.setter
    def is_derived(self, value: bool):  # noqa: F821
        """
        Set the is_derived property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_derived", value)
        self._is_derived = value

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
    def is_ordered(self) -> bool:  # noqa: F821
        """
        Get the is ordered property.

        Returns
        -------
        bool
            Value of property is ordered.
        """
        return self._is_ordered

    @is_ordered.setter
    def is_ordered(self, value: bool):  # noqa: F821
        """
        Set the is_ordered property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_ordered", value)
        self._is_ordered = value

    @property
    def is_portion(self) -> bool:  # noqa: F821
        """
        Get the is portion property.

        Returns
        -------
        bool
            Value of property is portion.
        """
        return self._is_portion

    @is_portion.setter
    def is_portion(self, value: bool):  # noqa: F821
        """
        Set the is_portion property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_portion", value)
        self._is_portion = value

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
    def is_variable(self) -> bool:  # noqa: F821
        """
        Get the is variable property.

        Returns
        -------
        bool
            Value of property is variable.
        """
        return self._is_variable

    @is_variable.setter
    def is_variable(self, value: bool):  # noqa: F821
        """
        Set the is_variable property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_variable", value)
        self._is_variable = value

    @property
    def owned_cross_feature(self) -> bool:  # noqa: F821
        """
        Get the owned cross feature property.

        Returns
        -------
        bool
            Value of property owned cross feature.
        """
        return self._owned_cross_feature

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
