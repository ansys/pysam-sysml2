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


UNHANDLED = object()
"""Sentinel returned by ``scripting_deprecated_get`` when no shim applies."""


def scripting_deprecated_get(element, name):
    """Resolve a scripting deprecation read shim, or return ``UNHANDLED``.

    ``_visibility`` moved onto the owning membership in the new metamodel.
    """
    if name == "_visibility":
        owning_membership = element.__dict__.get("_owningMembership")
        if owning_membership is None:
            return None
        warn_moved("_visibility", "_owningMembership._visibility")
        return owning_membership.__dict__.get("_visibility")
    return UNHANDLED


def scripting_deprecated_set(element, name, value) -> bool:
    """Apply a scripting deprecation write shim. Return ``True`` if handled.

    ``name``/``_name`` are read-only (raise); ``_visibility`` redirects the
    write to the owning membership.
    """
    if name in ("name", "_name"):
        raise_readonly(name, "_declaredName")
    if name == "_visibility":
        warn_moved("_visibility", "_owningMembership._visibility")
        owning_membership = element.__dict__.get("_owningMembership")
        if owning_membership is not None:
            # Bypass the membership's own ``_visibility`` redirect and persist
            # the change against the membership directly.
            if getattr(owning_membership, "_observer", None) is not None:
                owning_membership._observer.notify(owning_membership._id, "_visibility", value)
            object.__setattr__(owning_membership, "_visibility", value)
        else:
            object.__setattr__(element, "_visibility", value)
        return True
    return False
