# Migration Guide for the `183-all` Branch

This guide summarizes the most important changes in the `183-all` branch of PySAM SysML2.

PySAM is being updated to better align with the SysML v2 specification. As part of that work, some APIs and behaviors have changed. If you are testing `183-all`, please review this page and update your code accordingly.

> [!IMPORTANT]
> The `183-all` branch is still under active development.
> This guide reflects the current state of the migration and will be updated as the branch evolves.

---

## Who is impacted?

You are likely impacted if your code does any of the following:

- navigates ownership or containment relationships
- reads or writes visibility, kind, or parameter direction directly on elements
- renames model elements
- accesses connection endpoints
- reads or writes feature values
- relies on Python-native return values from `get_value()`

---

## Quick summary of breaking changes

| Area | Before | Now |
|---|---|---|
| Containment / owner | `element.owner` | `element.owning_membership` or `element.owning_namespace` depending on intent |
| Visibility | `element.visibility` | `element.owning_membership.visibility` |
| Similar membership-owned properties | directly on element | now on `owning_membership` |
| Name updates | `element.name = "..."` | `element.declared_name = "..."` |
| Libraries | no direct access | `project.get_libraries_packages()` |
| Connection endpoints | directly usable in all cases | may require resolving `FeatureChaining` |
| Feature values | Python-native values or tuples | raw SysML v2 expression objects |

---

## 1. Containers and memberships

PySAM now exposes intermediate membership elements explicitly.

For example, if a `PartUsage` (`PU`) “contains” an `AttributeUsage` (`AU`), the actual structure is:

- `PU` contains a `FeatureMembership` (`FMS`)
- `FMS` contains `AU`

This means that `AU` now has:

- a **real structural container**: the membership
- a **semantic container**: the enclosing namespace

### Before

```python
au.owner
```

### Now

```python
au.owning_membership   # real structural container
au.owning_namespace    # semantic container, close to the former au.owner
```

### What to do

If your code previously used `owner`, decide which meaning you actually need:

- use `owning_membership` for the actual structural parent
- use `owning_namespace` for the semantic/logical container

---

## 2. Visibility and related properties

Previously, visibility was exposed directly on the element.

Now, visibility is stored on the **relationship / membership** that owns the element.

### Before

```python
au.visibility
```

### Now

```python
au.owning_membership.visibility
```

The same pattern applies to other properties such as:

- `parameterDirection`
- `kind`
- similar membership-owned properties

### What to do

If your code reads or writes these properties directly on the element, update it to go through `owning_membership`.

---

## 3. Name handling

The `name` property is now a **derived property**.

The actual writable property is `declared_name`.

### Before

```python
au.name
au.name = "attributeUsage2"
```

### Now

```python
au.declared_name
au.declared_name = "attributeUsage2"
```

### What to do

- keep using `name` when you want the effective/derived name
- use `declared_name` when you want to rename the element

---

## 4. Access to library packages

Access to library packages is now available.

### Before

No direct access was available.

### Now

```python
project.get_libraries_packages()
```

### What to do

If you need to inspect or reuse library content, use this new API.

---

## 5. Connection endpoints and `FeatureChaining`

Connection endpoints are available through:

- `get_source()`
- `get_target()`

In some cases—especially when inherited elements are involved—the source or target may be represented as a `FeatureChaining`.

A `FeatureChaining` is a chain of features that represents the navigation path to the actual referenced element.

### Example

```python
source = RepresentativeResolver().resolve_feature_chaining(connectionUsage, "source")
target = RepresentativeResolver().resolve_feature_chaining(connectionUsage, "target")
```

### What to do

If your code assumes that `get_source()` or `get_target()` always returns a directly usable element, update it to handle `FeatureChaining` when needed.

---

## 6. Feature values

Feature value handling has changed significantly.

### Before

- `get_value()` returned:
  - a primitive value such as `int` or `str`, or
  - a 2-item tuple when a unit was involved, or
  - nothing
- `set_value()` directly set the value
- `parse_and_set_value()` parsed an expression and created the corresponding SysML v2 expression

### Now

- `get_value()` and `set_value()` map directly to `feature.featureValue.valuation`
- `get_value()` does **not** perform any conversion
- the returned value is the raw SysML v2 expression object

If you want a serialized representation, use:

```python
SysML2_Tools.serialize_expression(feature.get_value())
```

The parsing helper is still available, but now through `SysML2_Tools`.

### Example

```python
serialized = SysML2_Tools.serialize_expression(feature.get_value())
```

### What to do

If your code previously expected `get_value()` to return Python-native values, you will need to adapt it to handle SysML v2 expression objects instead.

If you relied on `parse_and_set_value()`, use the equivalent helper from `SysML2_Tools`.

---

## Recommended checks for users testing `183-all`

If you are currently testing `183-all`, we recommend reviewing any code that:

1. uses `owner`
2. accesses visibility, kind, or parameter direction directly on elements
3. assigns to `name`
4. inspects connection endpoints
5. expects `get_value()` to return Python-native values

---

## Scope of this guide

This file is intended to document the main migration changes for users testing the `183-all` branch.

It is intentionally incremental and may be updated regularly as the migration progresses.

If you encounter behavior that is not documented here yet, please treat this file as the current reference for migration-related updates on this branch.