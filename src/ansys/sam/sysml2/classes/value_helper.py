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

"""Value helper for Feature values (new SysML2 metamodel).

A Feature's value is the primitive carried by the most recent Literal*
element owned by the Feature (``Feature.ownedFeature``). Writing a value
creates a fresh Literal owned by the Feature in a single commit; reading
walks ``ownedFeature`` in reverse and returns the value of the first
Literal* it finds.

Operator/expression values and standard-library support are not handled
here; they land together in a future iteration.
"""

from typing import Union
from uuid import uuid4

from ansys.sam.sysml2.dto.commit.commit_class import Commit
from ansys.sam.sysml2.dto.commit.data_version import DataVersion
from ansys.sam.sysml2.exception.runtime_exception import UnsupportedValueExpression

_LITERAL_TYPES = (
    "LiteralString",
    "LiteralInteger",
    "LiteralRational",
    "LiteralBoolean",
)

# ScriptingMapper stores ``"_" + camelCase`` JSON keys; SysMLMapper exposes
# snake_case properties backed by ``"_" + snake_case``.
_SCRIPTING_FIELDS = {
    "owned_feature": "_ownedFeature",
    "value": "_value",
}
_SYSML_FIELDS = {
    "owned_feature": "owned_feature",
    "value": "value",
}


class ValueHelper:
    """Helper class for feature value resolution and update."""

    def __init__(self, fields: dict):
        """Construct a new instance with the given field-name map.

        Parameters
        ----------
        fields : dict
            Mapping from logical field name (``"owned_feature"``,
            ``"value"``) to the actual attribute name on the target
            element class.
        """
        self._fields = fields

    @staticmethod
    def get_value_for_scripting_element(element):
        """Get the value of the feature for a scripting (dynamic) element.

        Parameters
        ----------
        element : SysMLElement
            Scripting element to read the value from.

        Returns
        -------
        Any
            The primitive value, or ``None`` if no Literal is attached.
        """
        return ValueHelper(_SCRIPTING_FIELDS)._get_value(element)

    @staticmethod
    def get_value_for_sysml_element(element):
        """Get the value of the feature for a typed metamodel element.

        Parameters
        ----------
        element : Feature
            Typed metamodel element to read the value from. Must be a
            ``Feature``; otherwise an exception is raised.

        Returns
        -------
        Any
            The primitive value, or ``None`` if no Literal is attached.

        Raises
        ------
        UnsupportedValueExpression
            If ``element`` is not a ``Feature``.
        """
        from ansys.sam.sysml2.meta_model.feature import Feature

        if not isinstance(element, Feature):
            raise UnsupportedValueExpression("Can't read value of non feature element")
        return ValueHelper(_SYSML_FIELDS)._get_value(element)

    @staticmethod
    def set_or_update_value(element, value_type, new_value: Union[str, int, float, bool]):
        """Create the commit needed to set or update the value of ``element``.

        Parameters
        ----------
        element : SysMLElement or Element
            Feature whose value is updated.
        value_type : type or str
            Python type of ``new_value``, or the string ``"operator"``
            when called from ``parse_and_set_value``. Operator values
            are not supported yet (see module docstring).
        new_value : Union[str, int, float, bool]
            New primitive value to record.
        """
        instance = ValueHelper(_SYSML_FIELDS)
        if element._observer is None:
            raise UnsupportedValueExpression(
                "Element is not attached to a project; cannot set its value."
            )
        if value_type == "operator":
            raise UnsupportedValueExpression(
                "Operator/expression values are not supported yet; "
                "they will be added together with standard-library support."
            )
        if element._observer._is_transactional_mode:
            instance._add_to_stack(element, new_value)
        else:
            instance._direct_update_value(element, new_value)

    def _add_to_stack(self, element, new_value):
        """Queue the value-create commits on the observer's transaction stack.

        Parameters
        ----------
        element : SysMLElement or Element
            Feature whose value is being set.
        new_value : Any
            New primitive value to record.
        """
        literal_id = str(uuid4())
        element._observer.notify(literal_id, "@type", self._literal_type(new_value))
        element._observer.notify(literal_id, "owningNamespace", {"@id": element._id})
        element._observer.notify(literal_id, "value", new_value)

    def _direct_update_value(self, element, new_value):
        """Create a new Literal owned by ``element`` in a single commit.

        Parameters
        ----------
        element : SysMLElement or Element
            Feature whose value is being set.
        new_value : Any
            New primitive value to record.
        """
        literal_id = str(uuid4())
        commit = Commit(element._observer._project_id)
        change = DataVersion()
        change.identify(literal_id)
        change.add_change("@type", self._literal_type(new_value))
        change.add_change("owningNamespace", {"@id": element._id})
        change.add_change("value", new_value)
        commit.add_change(change)

        element._observer._connector.create_commit(
            element._observer._project_id, commit.to_json()
        )
        element._observer.reload_project()

    def _literal_type(self, new_value) -> str:
        """Return the ``@type`` of the Literal to create for ``new_value``.

        Parameters
        ----------
        new_value : Any
            Primitive value whose Python type drives the Literal class.

        Returns
        -------
        str
            One of ``"LiteralBoolean"``, ``"LiteralInteger"``,
            ``"LiteralRational"``, ``"LiteralString"``.

        Raises
        ------
        UnsupportedValueExpression
            If the Python type of ``new_value`` is not supported.
        """
        # ``bool`` must be checked before ``int`` since ``bool`` is a
        # subclass of ``int`` in Python.
        if isinstance(new_value, bool):
            return "LiteralBoolean"
        if isinstance(new_value, int):
            return "LiteralInteger"
        if isinstance(new_value, float):
            return "LiteralRational"
        if isinstance(new_value, str):
            return "LiteralString"
        raise UnsupportedValueExpression(
            f"Unsupported primitive value type: {type(new_value).__name__}"
        )

    def _get_value(self, element):
        """Return the primitive value carried by the latest owned Literal.

        Parameters
        ----------
        element : SysMLElement or Element
            Feature whose value is being read.

        Returns
        -------
        Any
            Primitive value of the most recent Literal owned by the
            feature, or ``None`` if none is present.
        """
        owned = getattr(element, self._fields["owned_feature"], []) or []
        # Reverse iteration so the latest ``set_value`` wins on a repeated write.
        for child in reversed(list(owned)):
            if type(child).__name__ in _LITERAL_TYPES:
                return getattr(child, self._fields["value"], None)
        return None
