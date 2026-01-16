# ADR-0002: Adopt Typed Prefix Repository Naming Convention

## Status

Proposed

## Context

Tech of Our Own will maintain many repositories over time covering fundamentally different kinds of
artifacts: organizational governance (bylaws, policies), software products, bootable system images,
hardware designs, websites, facilities documentation, and merchandise assets. These artifacts will
have different owners, review requirements, release cadences, and security postures, and the set
will expand as we introduce additional products and device families.

As the repository count grows, a flat list of repos in a GitHub organization becomes harder to
navigate and easier to misinterpret. Ambiguous names (e.g., a product name that could be software or
hardware) increase the risk of confusion, misrouting changes, and mistakes in automation. We need a
naming scheme that is human-readable at a glance, predictable for future repos, and stable as new
product lines appear.

## Decision

We will name every repository using a **typed prefix convention** so that the repository name itself
communicates the primary artifact type (e.g., software vs hardware vs image) without requiring users
to open the repo.

Repository names will be lowercase and hyphen-separated and will follow one of the approved patterns
defined below. The first token (the prefix) must be selected from the approved prefix list. After
the prefix, the name will include a **scope slug** (organization-wide or product-specific) and a
**component slug** (the specific repo purpose within that scope). Certain repo types (notably images
and firmware) may add optional **target** and **variant** tokens when necessary for clarity.

## Rationale

A typed prefix convention is a proven, scalable approach for large GitHub organizations because it
makes the repo list self-classifying. It reduces ambiguity (“is this hardware or software?”),
improves discoverability, and enables consistent automation (e.g., policies, CODEOWNERS checks, CI
templates) based on a repo’s prefix. It also accommodates multiple products and multiple artifact
types without requiring a separate “specifications” repository or forcing every repo into a single
rigid structure.

Using a small, controlled vocabulary of prefixes prevents naming drift while still allowing growth.
Keeping names short, consistent, and parseable improves onboarding and reduces operational errors
over time.

## Consequences

### Positive

* Repository purpose is immediately clear from the name (hardware vs software vs image vs org, etc.).
* Scales cleanly as we add new products and device families without renaming existing repos.
* Enables predictable automation and governance (policy enforcement, templates, CODEOWNERS rules) by
  repo type.
* Reduces confusion and accidental changes in the wrong repository.

### Negative

* Requires discipline: new repos must follow the convention instead of ad-hoc naming.
* Some repo names may feel longer than informal names (e.g., `sw-ourbox-os` instead of `ourbox`).
* Edge cases will appear (repos that seem to span types) and can trigger debate.

### Mitigation

* Maintain this ADR as the canonical reference and add a short “Naming Cheatsheet” to the GitHub org
  README.
* Use a lightweight review checklist for new repo creation (prefix, scope, component, optional
  target/variant).
* If a repo genuinely spans multiple types, choose the prefix based on the repo’s **primary
  artifact** and document the boundary in the repo README; split later if ownership or change-control
  demands it.
* If a new artifact type emerges, add a new prefix via an ADR update (or a superseding ADR) rather
  than inventing one-off names.

---

## Appendix A: Global Naming Rules (Normative)

1. **Lowercase only** (`a–z`, `0–9`).
2. **Hyphen-separated tokens**; no spaces, underscores, or periods.
3. **No redundant type words** inside the name (the prefix already conveys type).
4. Prefer short conventional tokens over prose.
5. Keep names descriptive but concise; avoid encoding metadata better expressed in
   tags/releases/docs.

---

## Appendix B: Name Shapes by Repository Type (Normative)

1. **General (most repos)**  
   `"<type>-<scope>-<component>"`

2. **Images**  
   `"<type>-<scope>-<component>-<target>[-<variant>]"`

3. **Hardware**  
   `"<type>-<scope>-<device>[-rev-<rev>]"` (revision token optional)

4. **Libraries / SDKs**  
   `"<type>-<scope>-<name>-<lang>"`

---

## Appendix C: Approved Type Prefixes (Normative)

The following prefixes are approved for repository names:

* `org-` — Organization/institution repositories (governance, policies, procedures)
* `fac-` — Facilities/buildings/sites documentation
* `sw-` — Software product repositories
* `hw-` — Hardware design repositories
* `img-` — Bootable image recipes and image build systems
* `fw-` — Firmware repositories
* `ops-` — Operations/deployment configuration repositories (e.g., GitOps)
* `iac-` — Infrastructure-as-code repositories
* `lib-` — Internal shared libraries intended for imports by our code
* `sdk-` — SDKs intended for external/partner use or explicitly supported developer surfaces
* `web-` — Websites (org or product)
* `merch-` — Merchandise and brand physical goods assets
* `tool-` — Tooling (build/test/automation) not itself a product runtime
* `sec-` — Security/trust artifacts (threat models, disclosure tooling, posture docs)
* `sandbox-` — Experiments/prototypes not intended to be confused with supported products

---

## Appendix D: Scope and Token Conventions (Normative)

1. **Scope slugs**

   * `techofourown` — Organization-wide canonical scope
   * Product scopes (examples): `ourbox`, `ourphone`, `ourauto`, `ourbot`
   * `common` — Reserved for intentionally cross-product shared repos

2. **Optional target tokens** (examples)

   * Hardware/platform: `rpi`, `rpi4`, `rpi5`
   * Architecture: `arm64`, `amd64`
   * Cloud: `aws`, `gcp`, `azure`

3. **Optional variant tokens** (examples)

   * `lowram`, `highram`, `minimal`, `debug`, `hardened`, `lts`

---

## Appendix E: Canonical Examples (Informative)

* `org-techofourown`
* `fac-techofourown-hq`
* `sw-ourbox-os`
* `img-ourbox-mini-rpi`
* `hw-ourbox-mini`
* `hw-ourbox-mega`
* `web-techofourown`
* `merch-techofourown`
