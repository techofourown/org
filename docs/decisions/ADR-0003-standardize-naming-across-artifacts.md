# ADR-0003: Standardize Naming Across Artifacts Using Typed Prefixes and Stable Identifiers

## Status

Accepted

## Context

Tech of Our Own will produce and maintain many different kinds of artifacts over decades:
organizational records (governance/policies), software products, physical devices, firmware,
bootable images, websites, and commercial items (e.g., merchandise). As the organization grows across
multiple product lines (home appliances, computers, vehicles, robots, etc.), naming drift becomes a
real operational risk: ambiguity in names causes confusion, misrouted work, brittle automation, and
support failures.

We need a naming system that is (1) instantly legible to humans browsing GitHub, (2) stable across
generations (so customer-facing names don’t churn), (3) precise for operations/support/manufacturing,
and (4) extensible without inventing “one-off” conventions per team. This ADR establishes a single,
organization-wide naming strategy that applies to “anything we name,” including repository names,
hardware products, images, software components, and supporting artifacts.

## Decision

Tech of Our Own will use a **two-layer naming strategy** across all domains: (1) a **human name** for
communication and brand, and (2) a **machine identifier** for precision and automation. Where a
domain already has an industry-standard identifier system (e.g., semantic versions, part numbers,
revisions), we will adopt and enforce it consistently.

Concretely, we will apply the following mandatory rules:

1. **Repository names are typed and self-classifying**

   * Every repository name begins with a **type prefix** that identifies what the repo primarily
     contains: `org-`, `sw-`, `hw-`, `img-`, `fw-`, `ops-`, `iac-`, `lib-`, `sdk-`, `web-`, `fac-`,
     `merch-`, `tool-`, `sec-`, `sandbox-`.
   * Repo names are lowercase, hyphen-separated, and follow
     `"<type>-<scope>-<component>[-<target>][-<variant>]"`.
   * This rule is the organization-wide standard and is consistent with ADR-0002 (repository naming).

2. **Hardware products have a stable marketing name and a separate model identifier**

   * Marketing name format: `"<Family> <Model> [<Trim>]"` (no platform/vendor names; no years).
   * Model identifier format: `"TOO-<FAM>-<MODEL>-<GEN>"` (e.g., `TOO-OBX-MBX-01`).
   * Manufacturing changes are tracked as **revisions** (`Rev A`, `Rev B`, …) without changing
     marketing name or generation unless the platform class changes.

3. **Software components use stable product naming + semantic versioning**

   * Product software repos use `sw-<product>-<component>` and ship versions using SemVer (e.g.,
     `v1.2.3`).
   * Internal modules/packages use language-idiomatic naming, but the **public project identity**
     stays stable (no renaming for internal refactors).

4. **Image artifacts are named by what they are for, not what they contain**

   * Image repos use `img-<product>-<device|role>-<target>[-<variant>]`.
   * Image release artifacts embed the same tokens plus the release version (e.g.,
     `img-ourbox-mini-rpi-v0.1.0.img.xz`).
   * Hardware platform details (e.g., “Raspberry Pi 5”) do not appear in customer-facing marketing
     names; they appear in documentation and compatibility matrices.

5. **Adding new prefixes or changing conventions requires an ADR update**

   * Teams may not invent ad-hoc naming schemes. If a new artifact type appears, we add a new prefix
     and rule through the ADR process and update the naming memo accordingly.

## Rationale

Typed prefixes make repository lists navigable and prevent ambiguity at scale (“Is this hardware or
software?” becomes obvious). Separating marketing names from model identifiers prevents
customer-facing churn while still providing operational precision for support, manufacturing, and
compliance. Avoiding years and platform/vendor names in marketing names keeps product identities
stable across internal redesigns and supplier changes.

A single cross-domain policy also makes automation and governance easier: templates, CI policies,
CODEOWNERS, and documentation tooling can apply rules by prefix and domain, while humans can reason
about names without needing tribal knowledge.

## Consequences

### Positive

* Repository purpose is immediately clear at a glance (hardware vs software vs images vs org).
* Hardware can evolve across generations (e.g., Pi 5 → Pi 6 class) without renaming the product
  line.
* Support, manufacturing, and documentation can unambiguously reference a device via a model
  identifier.
* Reduces naming drift and “one-off conventions,” enabling scalable automation.

### Negative

* Requires ongoing discipline and review for new repositories and product introductions.
* Some names may feel “more formal” than casual project names.
* Edge cases (multi-purpose repos) may require deliberate scoping to choose the correct primary
  prefix.

### Mitigation

* Maintain a small “Naming Cheatsheet” in the org repo and enforce conventions with lightweight
  review checklists.
* Use CODEOWNERS and repo templates to standardize naming and initial structure.
* For ambiguous repos, choose the prefix based on the **primary artifact** and document boundaries in
  the README; split later if ownership/release cadence diverges.
