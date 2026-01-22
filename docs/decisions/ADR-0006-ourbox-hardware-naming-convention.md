File: docs/decisions/ADR-0006-ourbox-hardware-naming-convention.md

# ADR-0006: Adopt an OurBox Hardware Naming Convention Using Model + Trim With Stable Model IDs

## Status
Accepted

## Date
2026-01-19

## Deciders
Founder (initial); future Board + Members (ratification/amendment per `docs/policies/founding/CONSTITUTION.md`)

## Context

ADR-0003 establishes an organization-wide naming strategy: a human marketing name plus a machine
identifier, with stable names across generations and revisions. ADR-0004 names the first OurBox
device "OurBox Matchbox" with model identifier `TOO-OBX-MBX-01`.

However, OurBox will grow into multiple models and multiple "trim" configurations (e.g., storage-heavy
vs GPU-enabled). Without a clear OurBox-family convention, we risk drifting into inconsistent or misleading
names ("Max", "Ultra", "Pro") and we risk creating SKU naming that is not stable, not legible, and hard to support.

We need an OurBox-specific rule that:

- scales from small appliances to rack-scale systems,
- keeps marketing names stable and vendor-agnostic,
- gives support/manufacturing an unambiguous identifier system,
- supports optional configuration "trims" without exploding the marketing name surface area.

This ADR applies ONLY to the **OurBox** hardware family (personal server / personal AI appliance).
Other hardware families (e.g., automobiles, robots) will have their own family-specific naming ADRs.

## Decision

### 1) OurBox marketing names use: Family + Model + optional Trim

**Marketing name format (normative):**

`OurBox <Model> [<Trim>]`

- **Family** is always `OurBox` for this product line.
- **Model** is the product model name (e.g., Matchbox, Tinderbox).
- **Trim** is an optional configuration intent label (storage-optimized, compute-optimized, etc.).

We use **spaces** in marketing names (no hyphenation in the official product name):
- ✅ `OurBox Matchbox`
- ✅ `OurBox Matchbox Harvest`
- ✅ `OurBox Tinderbox Forge`
- ❌ `OurBox Matchbox-Harvest` (allowed informally, not the official marketing name)
- ❌ `OurBox Matchbox Pro` / `Ultra` / `Max` (banned for OurBox; see principles below)

This preserves the two-layer strategy from ADR-0003 while making the OurBox family internally
consistent.

---

### 2) OurBox model vocabulary is reserved and defined

Model names are **reserved tokens** for the OurBox family. They must be memorable, evocative names
that communicate the product's nature without encoding specs or tiers.

**Approved OurBox models (normative):**

| Model | Meaning | Notes / intent |
|---|---|---|
| **Matchbox** | Small-form-factor appliance; unobtrusive, low-power | "Plug it in and forget it." Not "mobile-first." |
| **Tinderbox** | Desktop-class enclosure; high-capacity service host | More expansion than Matchbox; still home-friendly. |
| **Tower** | Larger enclosure optimized for expansion and performance | Intended for "add GPU / many drives" capability. |
| **Rack** | Rackmount chassis (1U/2U/etc.) | For structured deployments; still OurBox philosophy. |
| **Cabinet** | A complete rack/cabinet system (multi-node or blade-like) sold as a unit | A "system", not just a chassis. |

**Rules (normative):**
- Model names **do not** include vendor/platform (`Raspberry Pi`, `N100`, etc.) or years.
- Model names are **not** used to imply pricing tiers; they indicate the product class.
- A new OurBox model name requires an ADR update (addendum to this ADR or a superseding ADR).

---

### 3) OurBox trims are configuration-intent labels, not spec sheets

Trim names express **what the configuration is "for"**, not the complete bill of materials.

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

### 4) OurBox model identifiers remain stable per model + generation

Per ADR-0003, OurBox hardware uses a separate model identifier independent from marketing trim.

**Model identifier format (normative):**

`TOO-OBX-<MODEL>-<GEN>`

- `<MODEL>` is a short token derived from the model name: `MBX` (Matchbox), `TBX` (Tinderbox), etc.
- `<GEN>` is a two-digit generation number.

Examples:
- `TOO-OBX-MBX-01` (Matchbox)
- `TOO-OBX-TBX-01` (Tinderbox)
- `TOO-OBX-TOWER-01` (Tower)

**Generation rules (normative):**
- Increment `<GEN>` when the platform class meaningfully changes (architecture class change, major redesign that breaks key compatibility, etc.).
- Do **not** increment `<GEN>` for ordinary manufacturing changes; those are revisions.

**Revision rules (normative):**
- Track manufacturing changes as `Rev A`, `Rev B`, … under the same model identifier unless the change triggers a generation bump.

Support-facing default reference format:
- `OurBox Matchbox (TOO-OBX-MBX-01 Rev A)`

---

### 5) Configuration identifiers capture trims and SKU-level differences without renaming the product

Because the **model identifier** does not encode trim, we define a separate configuration identifier
for operations/manufacturing/support.

**Configuration identifier format (normative):**

`CFG-<MODEL>-<TRIM>-<NN>`

- `<MODEL>` is the model token: `MBX` (Matchbox), `TBX` (Tinderbox), etc.
- `<TRIM>` is one of: `BASE`, `HARVEST`, `FORGE` (or future approved trims).
- `<NN>` is a two-digit number for variants within the trim (region, PSU variant, bundled storage options, etc.).

Examples:
- `CFG-MBX-BASE-01` (Matchbox base configuration)
- `CFG-MBX-HARVEST-01` (Matchbox with Harvest trim)
- `CFG-TBX-BASE-01` (Tinderbox base configuration)
- `CFG-TBX-FORGE-01` (Tinderbox with Forge trim)

Recommended full, unambiguous support reference:
- `OurBox Matchbox Harvest (TOO-OBX-MBX-01 Rev A, CFG-MBX-HARVEST-01)`

**Rule (normative):** RAM size, SSD size, and similar "spec options" should generally live in the
configuration system (or BOM/part numbers), not in marketing names.

---

### 6) Repo naming for OurBox hardware follows the product family monorepo pattern

This ADR updates ADR-0002/ADR-0003 repo rules for OurBox to use a product family monorepo.

Recommended repo patterns (normative for new OurBox repos):
- Product family monorepo: `pf-ourbox` with subdirectories `hw/matchbox`, `hw/tinderbox`, etc.
- Bootable images: `img-ourbox-<model-token-lowercase>-<target>[-<variant>]`
  Examples: `img-ourbox-matchbox-rpi`, `img-ourbox-tinderbox-amd64`
- Firmware (if needed): `fw-ourbox-<model-token-lowercase>-<component>`

("Target" tokens like `rpi`, `amd64`, etc. belong in repos/images and compatibility docs—not in the marketing name.)

---

## Rationale

- **Clarity without hype:** "Matchbox / Tinderbox / Tower / Rack / Cabinet" communicate physical reality
  through evocative, memorable names without pretending we've reached "mega-scale" on day one.
- **Future-proof brand stability:** marketing names remain stable as internal compute modules and
  suppliers change.
- **Support precision:** model id + revision + configuration removes ambiguity and prevents "which
  one do you have?" failures.
- **Prevents SKU name explosion:** trims capture intent, while configuration IDs capture options.

## Consequences

### Positive
- OurBox naming becomes predictable and legible across hardware generations and models.
- Marketing names remain stable and vendor-agnostic.
- Support/manufacturing can refer to exact hardware unambiguously.
- New OurBox devices can be introduced without inventing ad-hoc tier words.

### Negative
- Requires discipline: teams may be tempted to reintroduce "tier adjectives" or encode specs into names.
- Model names are constrained to a reserved vocabulary, which may feel limiting.

### Mitigation
- Adding a new model or trim requires an ADR addendum/superseding ADR, keeping the vocabulary controlled.
- Use configuration identifiers (CFG) and BOM/part numbers for variant complexity rather than inventing new marketing names.

## References
- ADR-0003: `ADR-0003-standardize-naming-across-artifacts.md`
- ADR-0004: `ADR-0004-name-ourbox-matchbox.md`
- ADR-0002: `ADR-0002-adopt-typed-prefix-repo-names.md`
- Docs conventions: `docs/README.md`
