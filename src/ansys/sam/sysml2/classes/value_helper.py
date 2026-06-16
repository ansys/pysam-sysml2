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

"""Value helper class for Feature's value."""

from typing import Union
from uuid import uuid4

from ansys.sam.sysml2.dto.commit.commit_class import Commit
from ansys.sam.sysml2.dto.commit.data_version import DataVersion
from ansys.sam.sysml2.exception.runtime_exception import UnsupportedValueExpression


class ValueHelper:
    """Helper class for feature value resolve."""

    def __init__(self, prefix: str):
        """Construct new instance with its prefix specified."""
        self.prefix = prefix

    @staticmethod
    def is_value_capable(element) -> bool:
        """Return ``True`` if the element can carry a feature value (a Feature or descendant)."""
        from ansys.sam.sysml2.meta_model.feature import Feature

        if isinstance(element, Feature):
            return True
        from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil

        try:
            mm_class = SysMLUtil.get_sysml_constructor(type(element).__name__)
        except ImportError:
            return False
        return issubclass(mm_class, Feature)

    @staticmethod
    def get_value_for_scripting_element(element):
        """Get the value of the feature."""
        instance = ValueHelper("_")
        return instance._get_value(element)

    @staticmethod
    def get_value_for_sysml_element(element):
        """Get the value of the feature."""
        # Local import avoids circular import with meta_model.feature.
        from ansys.sam.sysml2.meta_model.feature import Feature

        instance = ValueHelper("")
        if isinstance(element, Feature):
            return instance._get_value(element)
        else:
            raise UnsupportedValueExpression("Can't read value of non feature element")

    @staticmethod
    def set_or_update_value(element, value_type: type, new_value: Union[str | int | float | bool]):
        """
        Create the commit to set or update the value of type ``value_type``.

        Parameters
        ----------
        element : SysMLElement or Element
            Element whose feature value is updated.
        value_type : type
            Value type of the new value.
        new_value : Union[str | int | float | bool]
            New value to update to.
        """
        from ansys.sam.sysml2.classes.sysml_element import SysMLElement

        prefix = "_" if isinstance(element, SysMLElement) else ""
        instance = ValueHelper(prefix)
        literal = instance._find_existing_literal(element)
        if element._observer._is_transactional_mode:
            instance._add_to_stack(element, value_type, new_value, literal)
        else:
            instance._direct_update_value(element, value_type, new_value, literal)

    def _find_existing_literal(self, element):
        """Return the literal currently held by the feature's valuation, or ``None``."""
        valuation = getattr(element, self.prefix + "valuation", None)
        if valuation is None:
            return None
        return getattr(valuation, self.prefix + "value", None)

    def _literal_type_name(self, value_type):
        """Map a Python value type to its SysML literal ``@type`` name (``None`` for operators)."""
        literal_types = {
            bool: "LiteralBoolean",
            int: "LiteralInteger",
            float: "LiteralRational",
            str: "LiteralString",
        }
        return literal_types.get(value_type)

    def _add_to_stack(self, element, value_type, new_value, literal=None):
        """
        Stack the value update for the current transaction.

        In transactional mode the existing literal (when present) is always dropped
        and a new ``FeatureValue`` is recreated, so the change applies regardless of
        any literal type switch.

        Parameters
        ----------
        element : [SysMLElement|Element]
            Feature of the container.
        value_type : str
            Value type of the new value.
        new_value : Any
            New value to update to.
        literal : [SysMLElement|Element], optional
            Existing literal held by the feature, if any.
        """
        if literal is not None:
            element._observer.delete_element(literal._id)
        value_id = "value:" + str(uuid4())
        element._observer.notify(value_id, "@type", "FeatureValue")
        if value_type != "operator":
            element._observer.notify(value_id, "value", self._adapt_value(new_value))
        else:
            element._observer.notify(value_id, "value", new_value)
        element._observer.notify(value_id, "isInitial", False)
        element._observer.notify(value_id, "isDefault", True)
        element._observer.notify(value_id, "owner", element)

    def _direct_update_value(self, element, value_type, new_value, literal=None):
        """
        Update directly the value of the feature.

        When no literal exists a ``FeatureValue`` is created. When a literal of the
        same type already exists it is updated in place through its identity. When
        the literal type changes the old literal is dropped before a new
        ``FeatureValue`` is created.

        Parameters
        ----------
        element : [SysMLElement|Element]
            Feature of the container.
        value_type : str
            Value type of the new value.
        new_value : Any
            New value to update to.
        literal : [SysMLElement|Element], optional
            Existing literal held by the feature, if any.
        """
        target_type = self._literal_type_name(value_type)
        if literal is not None and target_type is not None:
            if type(literal).__name__ == target_type:
                self._commit_literal_update(element, literal, target_type, new_value)
            else:
                self._commit_literal_drop(element, literal)
                self._commit_feature_value(element, value_type, new_value)
        else:
            self._commit_feature_value(element, value_type, new_value)
        element._observer.reload_project()

    def _commit_feature_value(self, element, value_type, new_value):
        """Create a ``FeatureValue`` owned by ``element`` carrying the new value."""
        project_id = element._observer._project_id
        commit = Commit(project_id)
        change = DataVersion()
        change.add_change("@type", "FeatureValue")
        if value_type != "operator":
            change.add_change("value", self._adapt_value(new_value))
        else:
            change.add_change("value", new_value)
        change.add_change("isInitial", False)
        change.add_change("isDefault", True)
        change.add_change("owner", element)
        commit.add_change(change)
        element._observer._connector.create_commit(project_id, commit.to_json())

    def _commit_literal_update(self, element, literal, literal_type, new_value):
        """Update the existing literal in place through its identity (same type only)."""
        project_id = element._observer._project_id
        commit = Commit(project_id)
        change = DataVersion()
        change.add_change("@type", literal_type)
        change.add_change("value", new_value)
        change.identify(literal._id)
        commit.add_change(change)
        element._observer._connector.create_commit(project_id, commit.to_json())

    def _commit_literal_drop(self, element, literal):
        """Drop the existing literal so a new typed literal can be recreated."""
        project_id = element._observer._project_id
        commit = Commit(project_id)
        change = DataVersion()
        change.identify(literal._id)
        commit.add_change(change)
        element._observer._connector.create_commit(project_id, commit.to_json())

    def _adapt_value(self, new_value: Union[str | int | float | bool]):
        """Convert the value to JSON format."""
        if isinstance(new_value, bool):
            return "true" if new_value else "false"
        if isinstance(new_value, str):
            return f'"{new_value}"'
        else:
            return str(new_value)

    def _get_value(self, element):
        """Get the value of the feature via the valuation chain."""
        valuation = getattr(element, self.prefix + "valuation", None)
        if valuation is None:
            return None
        value = getattr(valuation, self.prefix + "value", None)
        if value is None:
            return None
        if hasattr(value, self.prefix + "value"):
            return getattr(value, self.prefix + "value")
        else:
            return self._parse_expression(value)

    def _parse_expression(self, value):
        """Parse an operator expression and return (value, unit_name) tuple."""
        if getattr(value, self.prefix + "operator", None) != "[":
            raise UnsupportedValueExpression("Expression not supported!")

        if hasattr(value, "_ownedMember"):
            owned_member = getattr(value, "_ownedMember", [])
        else:
            owned_member = getattr(value, "owned_member", [])

        elements = [
            x
            for x in owned_member
            if hasattr(x, self.prefix + "valuation")
            and hasattr(getattr(x, self.prefix + "valuation"), self.prefix + "value")
        ]

        if not elements:
            raise UnsupportedValueExpression("No values found in expression")

        try:
            literal = getattr(
                getattr(elements[0], self.prefix + "valuation"),
                self.prefix + "value",
            )
            result_value = getattr(literal, self.prefix + "value")
            referents = [
                getattr(
                    getattr(getattr(x, self.prefix + "valuation"), self.prefix + "value"),
                    self.prefix + "referent",
                )
                for x in elements
                if hasattr(
                    getattr(getattr(x, self.prefix + "valuation"), self.prefix + "value"),
                    self.prefix + "referent",
                )
            ]
        except AttributeError:
            raise UnsupportedValueExpression("No values found in expression")

        return (result_value, self._extract_unit_name(referents))

    def _extract_unit_name(self, referents):
        """Extract the unit name from referents, if any, otherwise return None."""
        if not referents:
            return None

        unit = referents[0]
        if hasattr(unit, self.prefix + "short_name"):
            return getattr(unit, self.prefix + "short_name")
        elif hasattr(unit, self.prefix + "shortName"):
            return getattr(unit, self.prefix + "shortName")
        elif hasattr(unit, self.prefix + "name"):
            return getattr(unit, self.prefix + "name")
        return None
