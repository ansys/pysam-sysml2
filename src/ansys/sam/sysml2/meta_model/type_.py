"""Generated type class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .namespace import Namespace


class Type(Namespace):
    """Java class 'com.ansys.metamodel.sysml2.Type'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._differencing_type = ObservedList(self, "differencing_type")
        self._directed_feature = ObservedList(self, "directed_feature")
        self._end_feature = ObservedList(self, "end_feature")
        self._feature = ObservedList(self, "feature")
        self._feature_membership = ObservedList(self, "feature_membership")
        self._inherited_feature = ObservedList(self, "inherited_feature")
        self._inherited_membership = ObservedList(self, "inherited_membership")
        self._input = ObservedList(self, "input")
        self._intersecting_type = ObservedList(self, "intersecting_type")
        self._multiplicity = None
        self._output = ObservedList(self, "output")
        self._owned_conjugator = None
        self._owned_differencing = ObservedList(self, "owned_differencing")
        self._owned_disjoining = ObservedList(self, "owned_disjoining")
        self._owned_end_feature = ObservedList(self, "owned_end_feature")
        self._owned_feature = ObservedList(self, "owned_feature")
        self._owned_feature_membership = ObservedList(self, "owned_feature_membership")
        self._owned_intersecting = ObservedList(self, "owned_intersecting")
        self._owned_specialization = ObservedList(self, "owned_specialization")
        self._owned_unioning = ObservedList(self, "owned_unioning")
        self._unioning_type = ObservedList(self, "unioning_type")
        self._compatible_with = False
        self._is_abstract = False
        self._is_conjugated = False
        self._is_sufficient = False
        self._set_is_abstract = False
        self._set_is_sufficient = False

    @property
    def differencing_type(self) -> list["Type"]:  # noqa: F821
        """
        Get the differencing type property.

        Returns
        -------
        list["Type"]
            Value of property differencing type.
        """
        return self._differencing_type

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
    def end_feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the end feature property.

        Returns
        -------
        list["Feature"]
            Value of property end feature.
        """
        return self._end_feature

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
    def feature_membership(self) -> list["FeatureMembership"]:  # noqa: F821
        """
        Get the feature membership property.

        Returns
        -------
        list["FeatureMembership"]
            Value of property feature membership.
        """
        return self._feature_membership

    @property
    def inherited_feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the inherited feature property.

        Returns
        -------
        list["Feature"]
            Value of property inherited feature.
        """
        return self._inherited_feature

    @property
    def inherited_membership(self) -> list["Membership"]:  # noqa: F821
        """
        Get the inherited membership property.

        Returns
        -------
        list["Membership"]
            Value of property inherited membership.
        """
        return self._inherited_membership

    @property
    def input(self) -> list["Feature"]:  # noqa: F821
        """
        Get the input property.

        Returns
        -------
        list["Feature"]
            Value of property input.
        """
        return self._input

    @property
    def intersecting_type(self) -> list["Type"]:  # noqa: F821
        """
        Get the intersecting type property.

        Returns
        -------
        list["Type"]
            Value of property intersecting type.
        """
        return self._intersecting_type

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
    def output(self) -> list["Feature"]:  # noqa: F821
        """
        Get the output property.

        Returns
        -------
        list["Feature"]
            Value of property output.
        """
        return self._output

    @property
    def owned_conjugator(self) -> "Conjugation":  # noqa: F821
        """
        Get the owned conjugator property.

        Returns
        -------
        "Conjugation"
            Value of property owned conjugator.
        """
        return self._owned_conjugator

    @owned_conjugator.setter
    def owned_conjugator(self, value: "Conjugation"):  # noqa: F821
        """
        Set the owned_conjugator property.

        Parameters
        ----------
        value: "Conjugation"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_conjugator", value)
        self._owned_conjugator = value

    @property
    def owned_differencing(self) -> list["Differencing"]:  # noqa: F821
        """
        Get the owned differencing property.

        Returns
        -------
        list["Differencing"]
            Value of property owned differencing.
        """
        return self._owned_differencing

    @property
    def owned_disjoining(self) -> list["Disjoining"]:  # noqa: F821
        """
        Get the owned disjoining property.

        Returns
        -------
        list["Disjoining"]
            Value of property owned disjoining.
        """
        return self._owned_disjoining

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
    def owned_intersecting(self) -> list["Intersecting"]:  # noqa: F821
        """
        Get the owned intersecting property.

        Returns
        -------
        list["Intersecting"]
            Value of property owned intersecting.
        """
        return self._owned_intersecting

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

    @property
    def owned_unioning(self) -> list["Unioning"]:  # noqa: F821
        """
        Get the owned unioning property.

        Returns
        -------
        list["Unioning"]
            Value of property owned unioning.
        """
        return self._owned_unioning

    @property
    def unioning_type(self) -> list["Type"]:  # noqa: F821
        """
        Get the unioning type property.

        Returns
        -------
        list["Type"]
            Value of property unioning type.
        """
        return self._unioning_type

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
    def is_conjugated(self) -> bool:  # noqa: F821
        """
        Get the is conjugated property.

        Returns
        -------
        bool
            Value of property is conjugated.
        """
        return self._is_conjugated

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
    def set_is_sufficient(self) -> bool:  # noqa: F821
        """
        Get the set is sufficient property.

        Returns
        -------
        bool
            Value of property set is sufficient.
        """
        return self._set_is_sufficient
