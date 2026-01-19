File: docs/decisions/ADR-0006-ourbox-hardware-naming-convention.md

# ADR-0006: Adopt an OurBox Hardware Naming Convention Using Form Factor + Trim With Stable Model IDs

## Status
Accepted

## Date
2026-01-19

## Deciders
Founder (initial); future Board + Members (ratification/amendment per `docs/policies/founding/CONSTITUTION.md`)

## Context

ADR-0003 establishes an organization-wide naming strategy: a human marketing name plus a machine
identifier, with stable names across generations and revisions. ADR-0004 names the first OurBox
device “OurBox Mini” with model identifier `TOO-OBX-MINI-01`.

However, OurBox will grow into multiple physical shapes (outer mold lines) and multiple “trim”
configurations (e.g., storage-heavy vs GPU-enabled). Without a clear OurBox-family convention, we
risk drifting into inconsistent or misleading names (“Max”, “Ultra”, “Pro”, or premature “Mega”)
and we risk creating SKU naming that is not stable, not legible, and hard to support.

We need an OurBox-specific rule that:

- scales from small “near-router” devices to rack-scale systems,
- keeps marketing names stable and vendor-agnostic,
- gives support/manufacturing an unambiguous identifier system,
- supports optional configuration “trims” without exploding the marketing name surface area.

This ADR applies ONLY to the **OurBox** hardware family (personal server / personal AI appliance).
Other hardware families (e.g., automobiles, robots) will have their own family-specific naming ADRs.

## Decision

### 1) OurBox marketing names use: Family + Form Factor + optional Trim

**Marketing name format (normative):**

`OurBox <Form Factor> [<Trim>]`

- **Family** is always `OurBox` for this product line.
- **Form Factor** is the physical envelope / outer mold line.
- **Trim** is an optional configuration intent label (storage-optimized, compute-optimized, etc.).

We use **spaces** in marketing names (no hyphenation in the official product name):
- ✅ `OurBox Mini`
- ✅ `OurBox Mini Harvest`
- ✅ `OurBox Desk Forge`
- ❌ `OurBox Mini-Harvest` (allowed informally, not the official marketing name)
- ❌ `OurBox Mini Pro` / `Ultra` / `Max` (banned for OurBox; see principles below)

This preserves the two-layer strategy from ADR-0003 while making the OurBox family internally
consistent.

---

### 2) OurBox form factor vocabulary is reserved and defined

Form Factor names are **reserved tokens** for the OurBox family. They must correspond to a durable,
meaningful physical class (outer mold line), not a performance adjective.

**Approved OurBox form factors (normative):**

| Form Factor | Meaning (outer mold line) | Notes / intent |
|---|---|---|
| **Mini** | Pocketable / near-router appliance; unobtrusive, low-power | “Plug it in and forget it.” Not “mobile-first.” |
| **Desk** | Desktop-size enclosure meant to sit on/near a desk | More expansion than Mini; still home-friendly. |
| **Tower** | Larger enclosure optimized for expansion and performance | Intended for “add GPU / many drives” capability. |
| **Rack** | Rackmount chassis (1U/2U/etc.) | For structured deployments; still OurBox philosophy. |
| **Cabinet** | A complete rack/cabinet system (multi-node or blade-like) sold as a unit | A “system”, not just a chassis. |

**Rules (normative):**
- Form factor names **do not** include vendor/platform (`Raspberry Pi`, `N100`, etc.) or years.
- Form factor names are **not** used to imply pricing tiers; they indicate shape/physical class.
- A new OurBox form factor name requires an ADR update (addendum to this ADR or a superseding ADR).

---

### 3) OurBox trims are configuration-intent labels, not spec sheets

Trim names express **what the configuration is “for”**, not the complete bill of materials.

**Marketing trim rules (normative):**
- Trim is optional; if there is only one configuration, omit the trim in marketing.
- Trims must be **single-word, Title Case**, plain English nouns.
- Trims must avoid mythology and avoid status adjectives (`Pro`, `Elite`, `Max`, `Ultra`).

**Initial trim vocabulary (normative to start):**
- **Harvest** — storage-oriented configuration (drives, backup, capacity, resiliency)
- **Forge** — compute-oriented configuration (GPU/accelerator-enabled, local AI performance)

We may add trims later, but each addition must:
- be defined (what it means),
- be stable over time,
- and avoid becoming a proxy for every minor spec difference (RAM/SSD size should not create new trim names).

---

### 4) OurBox model identifiers remain stable per form factor + generation

Per ADR-0003, OurBox hardware uses a separate model identifier independent from marketing trim.

**Model identifier format (normative):**

`TOO-OBX-<FORM>-<GEN>`

Examples:
- `TOO-OBX-MINI-01`
- `TOO-OBX-DESK-01`
- `TOO-OBX-TOWER-01`

**Generation rules (normative):**
- Increment `<GEN>` when the platform class meaningfully changes (architecture class change, major redesign that breaks key compatibility, etc.).
- Do **not** increment `<GEN>` for ordinary manufacturing changes; those are revisions.

**Revision rules (normative):**
- Track manufacturing changes as `Rev A`, `Rev B`, … under the same model identifier unless the change triggers a generation bump.

Support-facing default reference format:
- `OurBox Mini (TOO-OBX-MINI-01 Rev A)`

---

### 5) Configuration identifiers capture trims and SKU-level differences without renaming the product

Because the **model identifier** does not encode trim, we define a separate configuration identifier
for operations/manufacturing/support.

**Configuration identifier format (normative):**

`CFG-<TRIM>-<NN>`

- `<TRIM>` is one of: `BASE`, `HARVEST`, `FORGE` (or future approved trims).
- `<NN>` is a two-digit number for variants within the trim (region, PSU variant, bundled storage options, etc.).

Examples:
- `CFG-BASE-01`
- `CFG-HARVEST-01`
- `CFG-FORGE-01`

Recommended full, unambiguous support reference:
- `OurBox Mini Harvest (TOO-OBX-MINI-01 Rev A, CFG-HARVEST-01)`

**Rule (normative):** RAM size, SSD size, and similar “spec options” should generally live in the
configuration system (or BOM/part numbers), not in marketing names.

---

### 6) Repo naming for OurBox hardware follows the typed-prefix scheme

This ADR does not change ADR-0002/ADR-0003 repo rules; it makes OurBox usage explicit.

Recommended repo patterns (normative for new OurBox repos):
- Hardware design: `hw-ourbox-<form-factor-lowercase>`  
  Examples: `hw-ourbox-mini`, `hw-ourbox-desk`
- Bootable images: `img-ourbox-<form-factor-lowercase>-<target>[-<variant>]`  
  Examples: `img-ourbox-mini-rpi`, `img-ourbox-desk-amd64`
- Firmware (if needed): `fw-ourbox-<form-factor-lowercase>-<component>`

(“Target” tokens like `rpi`, `amd64`, etc. belong in repos/images and compatibility docs—not in the marketing name.)

---

## Rationale

- **Clarity without hype:** “Mini / Desk / Tower / Rack / Cabinet” communicate physical reality and
  create a clean spectrum without pretending we’ve reached “mega-scale” on day one.
- **Future-proof brand stability:** marketing names remain stable as internal compute modules and
  suppliers change.
- **Support precision:** model id + revision + configuration removes ambiguity and prevents “which
  one do you have?” failures.
- **Prevents SKU name explosion:** trims capture intent, while configuration IDs capture options.

## Consequences

### Positive
- OurBox naming becomes predictable and legible across hardware generations and shapes.
- Marketing names remain stable and vendor-agnostic.
- Support/manufacturing can refer to exact hardware unambiguously.
- New OurBox devices can be introduced without inventing ad-hoc tier words.

### Negative
- Requires discipline: teams may be tempted to reintroduce “tier adjectives” or encode specs into names.
- Form factor names are constrained to a reserved vocabulary, which may feel limiting.

### Mitigation
- Adding a new form factor or trim requires an ADR addendum/superseding ADR, keeping the vocabulary controlled.
- Use configuration identifiers (CFG) and BOM/part numbers for variant complexity rather than inventing new marketing names.

## References
- ADR-0003: `ADR-0003-standardize-naming-across-artifacts.md`
- ADR-0004: `ADR-0004-name-ourbox-mini.md`
- ADR-0002: `ADR-0002-adopt-typed-prefix-repo-names.md`
- Docs conventions: `docs/README.md`
