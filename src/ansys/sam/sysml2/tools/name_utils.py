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
"""Name utilities class for the PySAM SysML2 diagram library."""


class NameUtils:
    """Helps standardize element names."""

    @staticmethod
    def to_snake_case(string: str) -> str:
        """Convert a camelCase or PascalCase string to snake_case."""
        parts: list[str] = []
        for i, ch in enumerate(string):
            if ch.isupper() and i > 0:
                parts.append("_")
                parts.append(ch.lower())
            else:
                parts.append(ch.lower())
        out = "".join(parts)
        if out in ("class", "import", "type"):
            out += "_"
        return out

    @staticmethod
    def to_key(string: str) -> str:
        """Convert a camelCase or PascalCase string to _snake_case attribute name."""
        attr = NameUtils.to_snake_case(string)
        return f"_{attr}"

    @staticmethod
    def snake_to_camel(key: str) -> str:
        """Convert a snake_case string to camelCase."""
        parts: list[str] = []
        to_upper = False
        for ch in key:
            if ch == "_":
                to_upper = True
                continue

            if to_upper:
                parts.append(ch.upper())
                to_upper = False
            else:
                parts.append(ch.lower())
        return "".join(parts)
