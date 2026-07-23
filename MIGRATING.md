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
- reads enum-valued properties (`direction`, `visibility`, `kind`, `portionKind`) as strings
- renames model elements
- accesses or resolves connection ends (feature chaining)
- reads or writes feature values
- relies on Python-native return values from `get_value()`
- builds or navigates diagrams through the diagram REST API

---

## Quick summary of breaking changes

| Area | Before | Now |
|---|---|---|
| Containment / owner | `element.owner` | `element.owning_membership` or `element.owning_namespace` depending on intent |
| Visibility | `element.visibility` | `SysMLTools.get_element_visibility(element)` (write via `element.owning_membership.visibility`) |
| Similar membership-owned properties | directly on element | now on `owning_membership` |
| Enum properties | `"out"` (string) | `FeatureDirectionKind.OUT` (enum member) |
| Name updates | `element.name = "..."` | `element.declared_name = "..."` |
| Libraries | no direct access | `project.get_libraries_packages()` |
| Connection ends | directly usable in all cases, then via `element.get_source()` / `element.get_target()` | `SysMLTools().resolve_feature_chaining(...)` or `SysMLTools().get_connector_ends(...)` |
| Feature values | Python-native values or tuples | value element (`.value` for literals, `SysMLTools.serialize_expression(...)` for expressions) |
| Diagrams | navigable diagram model via REST API | removed (image download only) |

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

To read the visibility of an element, use the helper:

```python
SysMLTools.get_element_visibility(au)
```

It reads the value from the element's owning membership (or its owning feature membership for features) and works for both the scripting and metamodel flavors, returning `None` when the element has no owning membership. The value is a `VisibilityKind` enum member (see [7. Enum-valued properties](#7-enum-valued-properties)). To write, set it on the owning membership directly:

```python
au.owning_membership.visibility = VisibilityKind.PUBLIC
```

The same pattern applies to other properties such as:

- `parameterDirection`
- `kind`
- similar membership-owned properties

### What to do

To read visibility, use `SysMLTools.get_element_visibility(element)`. For other membership-owned properties (or to write visibility), go through `owning_membership`.

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

## 5. Connection endpoints and feature chaining

A connection end (`source` or `target`) is an **end feature** that may reference its target through a **feature chaining**, a navigation path such as `a.b.c`. Because of inheritance and redefinition, the element a chaining resolves to is **context dependent**: the same feature can resolve to a different element depending on where it is observed.

Reading `connection.source` (or `connection._source`) therefore returns the raw end feature, not the meaningful element it represents.

Access to connection ends went through three stages: ends were originally directly usable in all cases, then were accessed through the element-level `get_source()` / `get_target()` helpers. Those helpers have now been removed, and end resolution lives in `SysMLTools`, which resolves each end within the connection's own context.

> [!NOTE]
> The `SysMLTools` feature-chaining resolver described in the **Now** step is still under review and has not been merged yet. The API may change before it lands.

### Before

```python
# ends were directly usable in all cases
source = connection.source
target = connection.target
```

### Intermediate

```python
# accessed through the element-level helpers
source = connection.get_source()
target = connection.get_target()
```

### Now

```python
from ansys.sam.sysml2.tools import SysMLTools

source = SysMLTools().resolve_feature_chaining(connection, "source")
target = SysMLTools().resolve_feature_chaining(connection, "target")

# Or resolve both ends at once:
source, target = SysMLTools().get_connector_ends(connection)
```

### What to do

Replace any element-level `get_source()` / `get_target()` calls (and the former `RepresentativeResolver`) with `SysMLTools`. It auto-detects whether you use the static or dynamic representation from the element you pass in, accounts for feature chaining, inheritance, and redefinition, and returns `None` when the end or context is missing.

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
- the returned value is the value **element** (a literal such as `LiteralInteger`, or an `OperatorExpression`)

For a literal value, read its `.value` property directly:

```python
>>> myIntFeature.get_value().value
10
>>> myStringFeature.get_value().value
'Hello'
>>> myBoolFeature.get_value().value
False
>>> myFloatFeature.get_value().value
10.56
```

For an expression value (or when you want a serialized representation), use `SysMLTools.serialize_expression`:

```python
>>> from ansys.sam.sysml2.tools import SysMLTools
>>> SysMLTools.serialize_expression(myIntFeature.get_value())
'10'
>>> SysMLTools.serialize_expression(myUnitFeature.get_value())
'10 [kg]'
>>> SysMLTools.serialize_expression(myArithmeticFeature.get_value())
'5 + 5'
>>> SysMLTools.serialize_expression(myReferenceFeature.get_value())
'baseValue + baseValue'
>>> SysMLTools.serialize_expression(myBooleanExpressionFeature.get_value())
'not true'
```

### What to do

If your code previously expected `get_value()` to return Python-native values, adapt it to handle value elements instead: read `.value` for literals, and use `SysMLTools.serialize_expression()` for expressions.

If you relied on `parse_and_set_value()`, it is still available on the feature; the serialization helper is now provided by `SysMLTools`.

---

## 7. Enum-valued properties

Enumeration-typed properties now return **enum members** instead of plain strings. This applies to `direction` (`FeatureDirectionKind`), `visibility` (`VisibilityKind`), `portionKind` (`PortionKind`), and `kind` (resolved to `RequirementConstraintKind`, `StateSubactionKind`, `TransitionFeatureKind`, or `TriggerKind` depending on the owning element).

### Before

```python
>>> root.get("Parts").get("Port").direction
'out'
```

### Now

```python
>>> root.get("Parts").get("Port").direction
<FeatureDirectionKind.OUT: 'out'>
>>> root.get("Parts").get("Port").direction = FeatureDirectionKind.IN
>>> root.get("Parts").get("Port").direction
<FeatureDirectionKind.IN: 'in'>
>>> root.get("Parts").get("Port").direction.name
'IN'
```

This also affects the properties from [2. Visibility and related properties](#2-visibility-and-related-properties): `owning_membership.visibility` now returns a `VisibilityKind` member rather than a string.

### What to do

- assign enum members (for example `FeatureDirectionKind.IN`) instead of strings
- compare against enum members rather than string literals
- use `.name` (`'IN'`) or `.value` (`'in'`) when you need a string representation

---

## 8. Diagram navigation / REST API removed

Diagram functionality is specific to projects of type **SAM**.

The SAM diagram REST API used to navigate an in-memory diagram model has been removed. `SAMDiagramManager` and `SamRestApiConnector`, along with the diagram builder and diagram element/plane classes, are no longer available.

Downloading diagram images (also SAM-only) is still supported through `SamApiConnector` and `SamDiagramDownloader`.

### Before

```python
with SAMDiagramManager(connector=sam_connector) as diagram_manager:
    diagram_manager.load_diagrams(model=project)
```

### Now

```python
from ansys.sam.sysml2.diagrams.api import SamApiConnector
from ansys.sam.sysml2.diagrams.tools import SamDiagramDownloader

connector = SamApiConnector(server_url=server_url, token=token)
downloader = SamDiagramDownloader(connector=connector, project_id=project_id)

connector.get_diagrams_info(project_id)
downloader.download_diagram(diagram_id, path)
downloader.download_all_diagrams(path)
```

### What to do

Drop any code that built or navigated in-memory diagram element/plane objects through the REST API, and switch to downloading diagram images instead.

---

## Recommended checks for users testing `183-all`

If you are currently testing `183-all`, we recommend reviewing any code that:

1. uses `owner`
2. accesses visibility, kind, or parameter direction directly on elements
3. compares enum-valued properties (`direction`, `visibility`, `kind`, `portionKind`) against strings
4. assigns to `name`
5. inspects or resolves connection endpoints (directly, or via the removed `get_source()` / `get_target()`; now through `SysMLTools`)
6. expects `get_value()` to return Python-native values
7. builds or navigates diagrams through the diagram REST API

---

## Scope of this guide

This file is intended to document the main migration changes for users testing the `183-all` branch.

It is intentionally incremental and may be updated regularly as the migration progresses.

If you encounter behavior that is not documented here yet, please treat this file as the current reference for migration-related updates on this branch.