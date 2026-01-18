# ADR-0005: Adopt CERN-OHL-S-2.0 for Tech of Our Own core hardware designs

- **Date:** 2026-01-17
- **Status:** Proposed (Founder proposal; intended to be ratified/amended by members via `CONSTITUTION.md`)
- **Deciders:** Founder (initial), future Board + Members (ratification/amendment)
- **Related:**
  - `../policies/founding/VALUES.md` (Declaration of Values)
  - `../policies/founding/CONSTITUTION.md`
  - `./ADR-0001-adopt-agplv3-core-software.md` (software licensing posture)

---

## Context

Tech of Our Own builds physical devices people can actually own, run, repair, and keep alive without
gatekeeper permission. Our hardware must be consistent with our non-negotiables:

- **User sovereignty over convenience** (can run it, leave it, repair it)
- **Inspectability is a right** (auditable, intelligible systems)
- **No lock-in, including lock-in to us**
- **Right to repair and long-life design**
- **Governance and incentives matter** (prevent quiet capture)

For hardware, “open” is not primarily a vibe — it’s a concrete set of promises:

1) people can obtain the *preferred form* of the design (not just PDFs or photos),  
2) people can manufacture, repair, and modify it, and  
3) if someone ships a modified device, the modifications should not be able to remain secret forever.

We want to enable:

- **Self-repair** and independent service shops
- **Community manufacturing** and “host for your neighbor” equivalents in hardware (build for your household / community)
- **Forks that can survive us** if TOOO disappears
- **Commercial production** (we can sell devices; others can also build/sell) without requiring permission

We also want to be explicit about what “open hardware” does *not* require:

- Publishing supplier pricing, contract terms, factory identities, or negotiated procurement details.
  Those may remain confidential. What matters is that a third party can reproduce the device from
  published design sources and documentation.

Finally: hardware has different legal surface area than software (design files, patents, trademarks,
trade secrets). This ADR chooses the **license for our hardware design artifacts**. It does not, by
itself, decide trademark policy, patent strategy, or procurement disclosure.

---

## Decision

### We will license Tech of Our Own “core hardware” design sources under **CERN-OHL-S-2.0** (Strongly Reciprocal)

- SPDX identifier: **`CERN-OHL-S-2.0`**
- We choose the **Strongly Reciprocal** variant to prevent “quiet capture” via shipping modified
  devices while withholding design changes.

### Meaning (plain English)

- Anyone may use our hardware design sources to make, modify, and sell devices.
- If you **modify the design** and **distribute** the design or **ship products** based on it, you
  must make the **corresponding modified design sources** available under the same license.

This aligns with our values:

- If someone “poisons” the design, the poison becomes **visible**, **auditable**, and **easy to route around**.
- Users are not dependent on us for repairs, continuity, or manufacturing.

### Trademark and branding are not granted

This decision is about design freedom and transparency, not brand impersonation.

- The hardware license does **not** grant rights to TOOO trademarks, logos, or product names.
- We will maintain a separate trademark policy so forks can exist without confusing users about
  what is “official TOOO hardware.”

---

## Scope

### Covered (“core hardware” design sources)

By default, all artifacts in hardware design repositories (`hw-*`) that define the device are covered,
including:

- Schematics and PCB design sources (preferred EDA formats, e.g., KiCad project sources)
- Board layout sources
- Mechanical CAD sources for enclosures, mounts, brackets, and device mechanicals
- Bills of materials (BOM) as design documentation
- Assembly drawings and manufacturing drawings
- Test fixtures and test procedure documents that are required to validate the hardware design
- Any “reference design” files we publish as the canonical device

Default rule: if it is part of what someone needs to reproduce, repair, and modify the device design,
it is covered.

### Not covered / out of scope (unless explicitly included)

- **Software/firmware** shipped on the device (covered by separate software licensing ADRs/policies)
- **Procurement details** (supplier contracts, pricing, factory identities, private vendor terms)
- **Trademarks and brand assets** (handled by trademark policy)
- **Third-party components** and their upstream licenses (we document them; we do not relicense them)

### Carve-outs (permissive edges)

Some artifacts may be intentionally permissive (e.g., connector pinouts, interface specs, file format
schemas) when doing so increases interoperability without enabling secret capture.

However, any permissive carve-out must be explicit via:
- a directory-level `LICENSE` file (or file headers),
- and a follow-up ADR describing boundaries and rationale.

---

## Rationale

### Why CERN-OHL-S-2.0

We want “open hardware” that is robust against enclosure:

- **Strong reciprocity** is the hardware analog of “close the loophole.” If someone manufactures and
  ships a modified version, they can’t keep the improvements (or regressions) proprietary indefinitely.
- **Auditability**: makes it materially easier for the community to compare versions and understand
  what changed.
- **Forkability and survivability**: if TOOO disappears, others can manufacture and maintain devices
  without legal ambiguity.

### Why not permissive-only for core hardware

Permissive hardware licensing can be great for standards and adoption, but for our *core product
designs* it creates an easy path to:

- silent modification,
- proprietary forks shipped as physical products,
- loss of community visibility into changes that matter for safety, privacy, or user autonomy.

That fails our “poison must be visible” goal.

### Why this does not conflict with being a sustainable business

CERN-OHL-S-2.0 does not prevent commercialization. It redirects competition toward:

- quality of manufacturing
- support and warranty
- availability and supply
- usability and documentation
- trustworthy provenance and security posture

…instead of competing via secret design changes.

---

## Consequences

### Positive

- **Right to repair becomes real:** independent repair and community support are enabled by default.
- **Harder to quietly capture:** modified devices imply published design deltas.
- **More trustworthy ecosystem:** users can verify what they are buying/running.
- **Long-term continuity:** community manufacturing remains possible even if TOOO is gone.

### Negative / Tradeoffs

- Some manufacturers or would-be partners will avoid using our hardware designs because they want
  proprietary modifications.
- Compliance adds work for downstream builders who ship modified products (they must publish design
  sources).
- License enforcement for hardware can be socially and operationally harder than for software.

### Mitigation

- Make compliance **easy**:
  - provide clear release tags, source archives, and “how to comply” documentation
  - keep design repos clean and reproducible (preferred formats, stable BOMs, documented build steps)
- Maintain a **strong trademark policy** so “official” vs “fork” is clear without blocking forks.
- Publish a lightweight “Hardware Release Checklist” so our own releases are consistently open and
  reproducible (see Implementation Notes).

---

## Options considered

### Option A: CERN-OHL-P-2.0 (Permissive)
- Rejected for core hardware.
- Allows shipping modified products without publishing design changes.
- Fails the “poison must be visible” requirement for the core device.

### Option B: CERN-OHL-W-2.0 (Weakly Reciprocal)
- Not chosen as the default for core.
- Potentially useful for subcomponents intended to be embedded broadly (modules/cards), but the core
  product should not be silently modified and redistributed.

### Option C: Solderpad / Apache-style permissive hardware licenses
- Rejected for core for the same reason as permissive: enables proprietary shipped forks without
  disclosure.

### Option D: Creative Commons licenses for hardware designs
- Rejected as the default for core because they are not purpose-built for hardware source/reciprocity
  mechanics and can create ambiguity in hardware contexts.

### Option E: Proprietary or “source-available” terms
- Rejected.
- Contradicts our mission posture and undermines community trust and fork survivability.

---

## Implementation notes

### 1) Repo hygiene (normative)

For each `hw-*` repository:

- Include a top-level `LICENSE` file containing the **CERN-OHL-S-2.0** text.
- Add SPDX headers where practical in source files:
  - `SPDX-License-Identifier: CERN-OHL-S-2.0`
- Add a short `NOTICE` or `COPYING` file if needed to clarify attribution and scope.

### 2) Release artifacts: what we publish (normative)

For every hardware release (e.g., `TOO-OBX-MINI-01 Rev A`), publish at minimum:

- Preferred-source design files (EDA + CAD originals)
- Manufacturing outputs (Gerbers, drill files, pick-and-place, assembly drawings)
- BOM with manufacturer part numbers (acceptable to list multiple sources / alternates)
- Bring-up / validation procedure sufficient for a competent third party
- A clear revision identifier and tag in git

We do **not** publish supplier pricing, factory identities, or purchasing terms unless we choose to.

### 3) “Source link” for physical products (recommended)

Where practical, include on-device / packaging / docs:

- a short URL to the exact design release (tag/commit)
- model identifier + revision (e.g., `TOO-OBX-MINI-01 Rev A`)
- license notice

This supports “inspectability is a right” in the physical world.

### 4) OSHWA certification (recommended)

Where feasible and beneficial, pursue Open Source Hardware certification for shipping hardware
products, using our published design sources and this license posture.

### 5) Trademarks (follow-up required)

Create a `docs/policies/` trademark policy (or `TRADEMARKS.md` at repo root) stating:

- what counts as “official” TOOO hardware
- what fork builders may say (“compatible with…”, “based on…”) without using marks confusingly
- rules for logo/name usage

This is essential to keep forks welcome while protecting users from impersonation.

---

## Future changes

Any of the following require explicit governance action (ADR + member process as defined in the Constitution):

- switching to a different hardware license
- adding blanket permissive carve-outs for core hardware
- introducing additional restrictions beyond the chosen open hardware license terms
- adopting a new policy that materially changes what we publish for hardware releases

---

## References

- `../policies/founding/VALUES.md`
- `../policies/founding/CONSTITUTION.md`
- `./ADR-0001-adopt-agplv3-core-software.md`
- (Future) Trademark policy document
- (Future) Hardware Release Checklist / documentation standard
