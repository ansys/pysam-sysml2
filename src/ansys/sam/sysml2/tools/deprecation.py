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
"""Deprecation helpers for metamodel changes (consistent warnings and errors)."""

from typing import NoReturn
import warnings


def warn_moved(attr: str, alternative: str) -> None:
    """Emit a DeprecationWarning that a property moved in the new metamodel."""
    warnings.warn(
        f"'{attr}' moved in the new metamodel; it now lives on '{alternative}'. "
        f"Access '{alternative}' directly; this shim will be removed in a future release.",
        DeprecationWarning,
        stacklevel=3,
    )


def raise_readonly(attr: str, alternative: str) -> NoReturn:
    """Raise a clear AttributeError telling the caller which writable attribute to use."""
    raise AttributeError(
        f"'{attr}' is read-only in the new metamodel. Use '{alternative}' to set a value "
        f"(for example, element.{alternative} = ...)."
    )
