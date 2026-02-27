# ADR-0004: Standardize Hardware Product Identification as Model → Trim → SKU (TOO-prefixed Part Numbers)


## Date
2026-01-29

## Context

Tech of Our Own will ship physical products across multiple product families for decades. Over time, the same product “name” must remain stable for users and support, while manufacturing realities change:

- suppliers change,
- parts go obsolete,
- storage/RAM options vary,
- enclosures/colors/region bundles differ,
- software loads evolve.

If we don’t formalize a hierarchy, we end up with naming drift (marketing names that encode specs, ad-hoc “Pro/Ultra” tiers, or ambiguous configuration IDs) that breaks support, procurement, automation, and long-term documentation.

We need one organization-wide schema that:
- stays legible to humans,
- remains stable over time,
- scales across many product families,
- cleanly separates *product class* from *intent* from *exact BOM*.

This ADR defines the schema. Individual product families instantiate it in their own repos.

## Decision

Tech of Our Own will identify hardware products using a three-tier hierarchy:

**Model → Trim → SKU**

### 1) Model (size/form factor contract)

A **Model** represents the stable *physical class* of a product within a product family.

For hardware, “model” is anchored in a **size/form-factor contract**, commonly expressed as a mounting/bolt pattern or chassis class (examples: Raspberry Pi-class mounting, Mini-ITX, Micro-ATX, ATX, rack unit sizes).

**Model identifiers are stable** and do not encode trim.

**Model ID format (normative):**
`TOO-<FAM>-<MODEL>-<GEN>`

- `<FAM>` = product family token (e.g., `OBX`)
- `<MODEL>` = model token (e.g., `MBX`, `TBX`)
- `<GEN>` = two-digit generation

Manufacturing-level changes within the same model+generation are tracked as **revisions** (`Rev A`, `Rev B`, …) without changing the model identifier unless the platform class meaningfully changes.

### 2) Trim (intent/positioning label)

A **Trim** is a stable, human-legible label for the *intent* of a configuration.

- Trim names express what the configuration is “for,” not a full spec sheet.
- Trim names are stable over time and should not churn due to incidental part substitutions.

Trim may appear in marketing language (family-dependent), but trim is not a separate part number by itself.

### 3) SKU (exact BOM + software load)

A **SKU** is the atomic sellable/buildable unit: an exact BOM plus the intended software load (when applicable).

SKU identifiers are treated as **manufacturer part numbers** and must be globally unambiguous.

**SKU / Part Number format (normative):**
`TOO-<FAM>-<MODEL>-<TRIM>-<SEQ>`

- `<TRIM>` is the trim token (uppercase)
- `<SEQ>` is a three-digit sequence number (`001`, `002`, …) that uniquely identifies a specific BOM/software build within a model+trim

**Critical rule (normative):** SKU/part numbers MUST begin with `TOO-`.  
Do not use identifiers that begin with `SKU-` or `CFG-`.

## Operational Rules (Normative)

1) **Create a new Model** when the physical/platform class changes enough to invalidate core assumptions
   (mounting pattern, enclosure class, major compatibility break, etc.).

2) **Create a new Trim** when the *intent* changes in a way users/support should recognize as a distinct configuration category
   (e.g., storage-oriented vs compute-accelerated).

3) **Create a new SKU** for any change that alters the actual build in a way that matters to:
   - BOM line-items (part swap, capacity change, vendor change),
   - region bundle (PSU, cable set),
   - enclosure material/color,
   - factory programming/software load differences.

Examples of SKU-level differences (explicitly SKU, not trim):
- red vs blue enclosure
- 1 TB vs 2 TB storage
- vendor swap for an equivalent component where traceability matters

## Consequences

### Positive
- Support can identify exactly what was built/shipped without renaming the product.
- Product families can evolve BOMs safely while keeping stable model and trim semantics.
- Automation (procurement, QA matrices, documentation) becomes reliable.

### Negative
- Requires discipline: teams must bump SKU sequences for real build deltas instead of “quiet swaps.”

### Mitigation
- Product family repos must maintain a clear SKU list (BOM records) and enforce the prefix/format in documentation and tooling.

## References
- ADR-0003: Standardize Naming Across Artifacts Using Typed Prefixes and Stable Identifiers
