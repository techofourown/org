# ADR-0015: Establish a Foundation, Brand, and Implementation Ecosystem Above Tech of Our Own Technology

- **Date:** 2026-04-02
- **Status:** Proposed
- **Related:**
  - `../governance/MISSION.md`
  - `../governance/VISION.md`
  - `../governance/VALUES.md`
  - `../governance/CONSTITUTION.md`

---

## Context

Tech of Our Own is the mission-locked foundation for a growing family of
non-extractive technologies.

That foundation already has clear commitments:

- non-extractive consumer technology
- local-first ownership and user control
- no subscriptions
- no hostage mechanics
- no sale of user data
- open-source core software
- governance designed to resist drift into extraction

The mission also explicitly extends beyond the first flagship product into
future product categories where people need technology that respects them.

At the same time, TOOO is no longer dealing with one undifferentiated public
audience or one fixed product expression.

Different user and application clusters will predictably need different:

- public-facing brands
- product names
- emotional registers
- industrial design choices
- hardware embodiments
- materials and bills of materials
- application suites
- implementation strategies
- community structures
- roadmap processes
- organizational forms

Some brands may stay in near-lockstep with TOOO reference implementations.

Others may:

- repackage them
- white-label them
- adapt them to different hardware
- maintain variant bills of materials
- maintain their own application surfaces
- remain hardware-agnostic
- or organize their own governance and roadmap around the technology

That variation is not necessarily mission drift.
It is often the natural consequence of building a true ecosystem rather than a
single monolithic consumer brand.

A rigid “foundation / product / brand” stack — one foundation, one product
expression, one public brand — is too narrow for the ecosystem TOOO actually
intends to support.

TOOO therefore needs a decision record that does three things at once:

1. keeps the foundation and its non-negotiables intact,
2. allows multiple public brands and multiple product embodiments above it,
3. and allows those brands to vary in both product expression and social /
   organizational structure without forcing every brand into one template.

---

## Decision

Tech of Our Own will adopt a **foundation, brand, and implementation ecosystem**
architecture.

More specifically:

### 1) Tech of Our Own remains the foundation identity

“Tech of Our Own” remains the name of the mission-locked foundation.

It remains the identity used for:

- governance documents
- constitutional and policy materials
- the GitHub organization and org control plane
- open-source core software stewardship
- organization-wide technical standards and decisions
- contributor-facing surfaces
- foundation-level trust and continuity materials

TOOO is primarily a foundation identity.

It may also act as an umbrella or endorsement layer where useful, but it is not
required to be the primary public-facing brand on every surface.

### 2) TOOO may support multiple brands above or alongside the foundation

TOOO may operate, sponsor, incubate, endorse, or interoperate with multiple
public brands built on TOOO technology.

A brand may be oriented around:

- a user cluster
- an application cluster
- a product family
- a cultural or editorial posture
- a deployment pattern
- or any combination of the above

Examples could include brands centered on artists, parents, cypherpunks,
traditional-life users, culturally elite privacy adopters, or other distinct
clusters.

### 3) A brand is not limited to relabeling a TOOO reference product

A brand may have its own:

- product names
- industrial design
- materials
- colors and finishes
- bill of materials
- hardware platform choices
- packaging
- application bundle or suite
- installation and onboarding posture
- support model
- public trust surface

A brand may track a TOOO reference implementation closely, or it may diverge in
specific layers while still building on TOOO technology.

### 4) The foundation’s strongest continuity layer is software, standards, and reference implementations

TOOO’s central connective tissue is not any one hardware bill of materials.

The foundation’s primary shared layer is:

- software
- interfaces
- standards
- reference implementations
- compatibility posture
- mission-governed technical direction

Reference implementations exist to:

- verify the software in real use
- demonstrate a coherent baseline
- accelerate adoption
- provide known-good starting points

They do **not** imply that every brand must use the same hardware, the same
materials, the same enclosure, or the same product expression.

### 5) Brands may vary in how tightly they align to TOOO implementations

Permitted patterns include, without limitation:

- a brand that stays in lockstep with a TOOO reference implementation
- a brand that changes packaging, materials, industrial design, or bill of materials
- a brand that ships a different hardware embodiment on the same core software
- a brand that is primarily an application suite and remains hardware-agnostic
- a brand that adopts only selected TOOO components
- a brand that maintains a deeper variant of the software stack, including a
  different OS distribution or other implementation-level divergence

This ADR does not require all brands to sit at the same layer of the stack.

### 6) Brands may have their own organization and governance

A brand may, where appropriate, maintain its own:

- meetings
- officers
- roadmap process
- voting process
- community procedures
- operating organization
- affiliated legal or quasi-legal structure

Some brands may be tightly run inside TOOO.
Others may be more autonomous.
Others may simply be compatible implementations or aligned surfaces.

This architecture intentionally allows a spectrum rather than one required
organizational model.

### 7) Alignment levels must be made explicit

A brand or implementation should clearly state its relationship to TOOO.

That relationship may be described in terms such as:

- **official** — operated directly under TOOO governance
- **aligned** — separately organized but explicitly adopting selected TOOO
  commitments, standards, or reference layers
- **compatible** — interoperable with TOOO technology but not governed as a TOOO
  brand

This ADR does not freeze the exact vocabulary, but it does require that the
relationship not be left ambiguous.

### 8) Official and aligned brands inherit the foundation’s non-negotiables for TOOO-governed core components

No official or foundation-aligned brand may contradict the foundation’s
constitutional never-rules for the TOOO-governed core it ships or presents as
foundation-derived.

At minimum, that includes:

- no subscriptions for core consumer functionality
- no hostage mechanics
- no sale of user data
- no behavioral advertising
- no hidden telemetry
- no lock-in as a strategy
- local-first / user-owned direction of travel
- open-source core posture where already committed
- mission-locked continuity against extraction

This does not require every brand to be operationally identical.
It does require honesty about what is core, what is inherited, and what is
brand-specific.

### 9) Human-facing names and implementation identifiers remain separate concerns

Public brand names, product names, repository names, package identifiers,
hardware model identifiers, and other machine-facing identifiers do not need to
collapse into one naming layer.

A brand may change its public language without forcing immediate changes to:

- repository names
- software package identifiers
- hardware model identifiers
- product-family tokens
- internal reference names

Likewise, a change in hardware embodiment does not by itself require a change in
foundation identity.

### 10) Each recognized brand should have a written charter

Each official or aligned brand should maintain a short written charter that
records, at minimum:

- the brand name
- intended audience or cluster
- relationship to TOOO
- what products or implementations it maintains
- what parts of the stack it controls
- what it inherits from the foundation
- what organizational model it uses
- whether it is official, aligned, or compatible
- any compatibility or divergence statement needed for clarity

Not every brand charter must be an organization-level ADR.

### 11) This architecture allows both “foundation” and “umbrella” behavior where appropriate

TOOO is best understood primarily as a foundation.

But this ADR does **not** require a hard rule that TOOO can never function as an
umbrella, umbrella-endorsed ecosystem, or public trust layer where doing so is
clear and useful.

The point is not to force one topology forever.

The point is to prevent accidental rigidity while preserving mission lock.

---

## Scope

This ADR applies to:

- organization-wide brand architecture
- the relationship between TOOO and downstream brands
- the relationship between TOOO and multiple product embodiments
- the relationship between public brands and reference implementations
- the relationship between brand-level organization and foundation-level mission

This ADR does **not** by itself decide:

- the exact names of current or future brands
- the exact name of any given product
- exact domain allocations
- exact bills of materials
- exact industrial design choices
- exact operating system choices
- exact compatibility marks or certification criteria
- exact legal structures for every downstream brand
- exact repo layouts for every downstream effort

Those may be handled by brand charters, product-family repos, brand-specific
repos, or follow-up ADRs/RFCs as needed.

---

## Rationale

### 1) One public name cannot do every job

The foundation, the commons, the product families, and the user-cluster-facing
brands do different jobs.

Forcing one name to do all of them creates confusion and weakens the system.

### 2) The mission already implies future variety

The mission extends beyond the first flagship into future product categories.

The constitution also leaves membership mechanics intentionally flexible and
allows expansion into new product categories and services.

A more plural architecture is therefore consistent with the existing governing
documents.

### 3) Software continuity matters more than one fixed hardware embodiment

TOOO’s deepest shared layer is its software, standards, interfaces, and
reference implementations.

A rigid assumption that every downstream brand is merely relabeling one
foundation hardware product would misdescribe the actual architecture.

### 4) Ecosystems need room for both lockstep and divergence

Some brands will maximize trust by staying close to TOOO reference
implementations.

Others will create value by adapting embodiments, materials, hardware, app
suites, or governance for a particular audience.

A useful foundation must support both.

### 5) Organizational plurality is normal

Real-world ecosystems often contain subsidiaries, affiliates, aligned projects,
white-labeled implementations, and more independent but still compatible
surfaces.

TOOO should not pre-emptively forbid that range if the mission can remain intact.

### 6) Clarity beats implicit assumptions

The real risk is not plurality itself.

The risk is ambiguity about:

- what is official
- what is aligned
- what is merely compatible
- what is inherited from the foundation
- what is a local brand decision
- and what divergences affect trust, compatibility, or support expectations

This ADR prefers explicit disclosure over rigid uniformity.

---

## Consequences

### Positive

- TOOO can support a genuine house of brands without forcing every surface into
  one public identity.
- Brands can serve distinct user and application clusters more honestly.
- Brands can vary not only in language and aesthetics, but in product
  embodiments and organizational form.
- TOOO can keep reference implementations without turning them into a monopoly
  over all downstream embodiments.
- Software-first continuity is preserved even when hardware expressions vary.
- The foundation can remain stable while the public ecosystem experiments.

### Negative / Tradeoffs

- The ecosystem becomes more complex.
- Public audiences may need help understanding the relationship between TOOO,
  a brand, and a specific product embodiment.
- Divergence between brands can create compatibility and support confusion.
- Separate governance or roadmap structures can create coordination overhead.
- Some brands may overstate their alignment unless explicit disclosure is
  required.

### Mitigation

- Keep this ADR as the org-level structural reference.
- Require a short charter for each official or aligned brand.
- Require explicit statements of relationship and compatibility.
- Keep foundation non-negotiables legible on trust-critical surfaces.
- Document when a product is:
  - a reference implementation,
  - a lockstep variant,
  - a divergent embodiment,
  - or a hardware-agnostic software surface.
- Prefer follow-up ADRs only when a change affects shared architecture or
  shared non-negotiables.

---

## Implementation Notes

### 1) TOOO foundation surfaces remain in the org control plane

The following remain under the TOOO foundation identity unless separately
decided otherwise:

- governance documents
- constitutional materials
- policy docs
- org-wide ADRs and RFCs
- the GitHub org and control plane
- core open-source stewardship
- foundation-level trust materials

### 2) Brand-specific materials usually live outside the org governance repo

Brand-specific materials such as:

- brand books
- launch sites
- product marketing pages
- visual systems
- invitation systems
- editorial materials
- brand-level governance notes
- roadmap materials

should usually live in brand- or product-specific repositories rather than in
the public org governance repo.

### 3) Reference implementations remain important, but not mandatory for all brands

TOOO may continue to publish and maintain reference implementations for hardware,
software, or integrated product families.

Those references are important for:

- verification
- known-good baselines
- testing
- demonstration
- interoperability
- acceleration of downstream work

They are not the only allowed embodiment of TOOO technology.

### 4) Brand-specific organizations may exist

A brand may maintain its own operating structure, governance process, roadmap
body, or affiliated organization where that helps the brand serve its audience.

This ADR allows that possibility without requiring it.

### 5) Divergence should be documented where it matters

If a brand materially diverges from a TOOO reference implementation or core
compatibility posture, it should say so plainly.

Examples of divergence that may warrant explicit documentation include:

- different hardware platform
- different bill of materials
- different OS distribution or system stack
- hardware-agnostic application-only posture
- different support or upgrade expectations
- different governance or roadmap ownership

### 6) Not every new brand requires a new org-level ADR

A new brand may often be established with a brand charter alone.

A follow-up ADR is warranted only when the change affects:

- shared foundation architecture
- shared compatibility marks
- org-wide naming rules
- foundation non-negotiables
- or a shared technical standard

---

## Future Changes

The following do **not** require superseding this ADR so long as the ecosystem
model remains intact:

- launching a new brand for a new user or application cluster
- retiring a brand
- renaming a product
- introducing a new hardware embodiment
- introducing a different bill of materials or materials strategy
- creating a hardware-agnostic brand
- creating an application-suite-only brand
- creating a brand-specific roadmap process or governance model
- creating a separate org or affiliated structure for a brand
- keeping a brand in lockstep with TOOO reference implementations
- creating a more divergent implementation with explicit documentation

The following **do** require follow-up governance action:

- changing the foundation’s constitutional non-negotiables
- allowing an official or aligned brand to contradict the foundation’s
  non-extractive commitments
- changing the relationship between the foundation and core open-source
  stewardship in a way that weakens mission lock
- replacing or renaming the TOOO foundation identity itself
- changing organization-wide naming rules or shared compatibility rules in ways
  that affect multiple brands
- any sale, merger, or control transfer that would weaken the foundation’s
  continuity or allow extraction through ecosystem-layer structures

---

## References

### Internal

- `../governance/MISSION.md`
- `../governance/VISION.md`
- `../governance/VALUES.md`
- `../governance/CONSTITUTION.md`

### Notes

This ADR is intentionally structural.

It establishes that TOOO is not limited to a single brand, a single product
expression, or a single organizational model above the foundation.

It does not force a rigid “foundation / product / brand” stack.
It records a more flexible reality:

- one mission-locked foundation
- many brands
- many product embodiments
- many possible implementation layers
- one shared obligation not to drift into extraction