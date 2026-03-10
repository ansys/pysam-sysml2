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

import pytest

from ansys.sam.sysml2.builder.mapper.scripting_mapper import ScriptingMapper
from ansys.sam.sysml2.classes.sysml_element import SysMLElement


class TestScriptingMapper:

    @pytest.fixture
    def scripting_mapper(self):
        return ScriptingMapper()

    def test_check_valid_sysml_element(self, scripting_mapper: ScriptingMapper):
        data = {
            "@id": "element_id",
            "@type": "PartUsage",
            "qualifiedName": "pp::p",
        }
        element = scripting_mapper.map("pp", data, None).get_element()
        assert isinstance(element, SysMLElement)
        assert element._id == "element_id"
        assert element.__class__.__name__ == "PartUsage"

    def test_invalid_sysml_element(self, scripting_mapper: ScriptingMapper):
        data = {
            "@id": "element_id",
        }
        with pytest.raises(Exception):
            scripting_mapper.map("pp", data, None)

    def test_create_element_string_field(self, scripting_mapper: ScriptingMapper):
        data = {
            "@id": "element_id",
            "@type": "PartUsage",
            "name": "Element",
            "qualifiedName": "pp::p",
        }
        element = scripting_mapper.map("pp", data, None).get_element()
        assert isinstance(element, SysMLElement)
        assert element._id == "element_id"
        assert element.__class__.__name__ == "PartUsage"
        assert element._name == "Element"

    def test_create_element_list_field(self, scripting_mapper: ScriptingMapper):
        data_1 = {
            "@id": "element_id",
            "@type": "PartUsage",
            "subElements": [{"@id": "sub_element_id"}],
            "qualifiedName": "pp::p",
        }

        element = scripting_mapper.map("pp", data_1, None).get_element()
        assert isinstance(element, SysMLElement)
        assert element._id == "element_id"
        assert element.__class__.__name__ == "PartUsage"
        assert len(element._subElements) == 1

    def test_create_element_list_text(self, scripting_mapper: ScriptingMapper):
        data_1 = {
            "@id": "element_id",
            "@type": "PartUsage",
            "text": ["Content"],
            "qualifiedName": "pp::p",
        }

        element = scripting_mapper.map("pp", data_1, None).get_element()
        assert isinstance(element, SysMLElement)
        assert element._id == "element_id"
        assert element.__class__.__name__ == "PartUsage"
        assert len(element._text) == 1

    def test_create_element_reference_field(self, scripting_mapper: ScriptingMapper):
        data = {
            "@id": "element_id",
            "@type": "PartUsage",
            "owner": {"@id": "part_id"},
            "qualifiedName": "pp::p",
        }
        owner = {
            "@id": "part_id",
            "@type": "Part",
            "name": "Part",
            "qualifiedName": "pp::p",
        }

        mapped_element = scripting_mapper.map("pp", data, None)
        mapped_owner = scripting_mapper.map("pp", owner, None)
        element = mapped_element.get_element()
        owner = mapped_owner.get_element()
        unresolved_fields = (
            mapped_element.get_unresolved_fields()
            + mapped_owner.get_unresolved_fields()
        )
        env = {"element_id": element, "part_id": owner}
        for unresolved_field in unresolved_fields:
            element_id = unresolved_field.get_id()
            el = env.get(element_id, None)
            if element is not None:
                unresolved_field.resolve(el)
        assert isinstance(element, SysMLElement)
        assert element._id == "element_id"
        assert element.__class__.__name__ == "PartUsage"
        assert element._owner is owner
