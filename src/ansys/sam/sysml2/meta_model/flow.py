"""Generated flow class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .connector import Connector
from .step import Step


class Flow(Connector, Step):
    """Java class 'com.ansys.metamodel.sysml2.Flow'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._flow_end = ObservedList(self, "flow_end")
        self._interaction = ObservedList(self, "interaction")
        self._payload_feature = None
        self._payload_type = ObservedList(self, "payload_type")
        self._source_output_feature = None
        self._target_input_feature = None

    @property
    def flow_end(self) -> list["FlowEnd"]:  # noqa: F821
        """
        Get the flow end property.

        Returns
        -------
        list["FlowEnd"]
            Value of property flow end.
        """
        return self._flow_end

    @property
    def interaction(self) -> list["Interaction"]:  # noqa: F821
        """
        Get the interaction property.

        Returns
        -------
        list["Interaction"]
            Value of property interaction.
        """
        return self._interaction

    @property
    def payload_feature(self) -> "PayloadFeature":  # noqa: F821
        """
        Get the payload feature property.

        Returns
        -------
        "PayloadFeature"
            Value of property payload feature.
        """
        return self._payload_feature

    @payload_feature.setter
    def payload_feature(self, value: "PayloadFeature"):  # noqa: F821
        """
        Set the payload_feature property.

        Parameters
        ----------
        value: "PayloadFeature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "payload_feature", value)
        self._payload_feature = value

    @property
    def payload_type(self) -> list["Classifier"]:  # noqa: F821
        """
        Get the payload type property.

        Returns
        -------
        list["Classifier"]
            Value of property payload type.
        """
        return self._payload_type

    @property
    def source_output_feature(self) -> "Feature":  # noqa: F821
        """
        Get the source output feature property.

        Returns
        -------
        "Feature"
            Value of property source output feature.
        """
        return self._source_output_feature

    @source_output_feature.setter
    def source_output_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the source_output_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "source_output_feature", value)
        self._source_output_feature = value

    @property
    def target_input_feature(self) -> "Feature":  # noqa: F821
        """
        Get the target input feature property.

        Returns
        -------
        "Feature"
            Value of property target input feature.
        """
        return self._target_input_feature

    @target_input_feature.setter
    def target_input_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the target_input_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "target_input_feature", value)
        self._target_input_feature = value
