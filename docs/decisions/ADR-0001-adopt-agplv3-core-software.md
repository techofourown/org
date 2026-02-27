# ADR-0001: Adopt AGPLv3 for Tech of Our Own core software

- **Date:** 2026-01-17
- **Deciders:** Founder (initial), future Board + Members (ratification/amendment)
- **Related:** `../governance/VALUES.md` (Declaration of Values)

---

## Context

Tech of Our Own is building software that is meant to be run over a network:

- Users should be able to **self-host**.
- Users should be able to **host for each other** (households, friends, communities).
- We explicitly want to avoid a world where a large company can:
  1) take the code,
  2) deploy it as a hosted service,
  3) modify it (including "poisoning" it),
  4) without disclosing those modifications to the people using the service.

This is the classic "SaaS loophole": copyleft licenses triggered only by distribution allow network
deployment with private modifications.

Our Declaration of Values sets the bar:

- **Inspectability is a right, not a feature.**
- **No lock-in, including lock-in to us.**
- **Freedom to self-host and host for each other.**
- **Privacy by architecture, not policy.**
- **Governance and incentives matter more than heroics.**
- **No secret hosted modifications of the core.**

We need a license posture that:
- permits commercial hosting and paid services (including people hosting for others),
- enables forking and long-term survivability,
- but forces disclosure of modifications when the software is used over a network.

---

## Decision

### We will license Tech of Our Own core software under **GNU Affero General Public License v3.0
(AGPLv3)**.

- SPDX identifier: **`AGPL-3.0-only`**
- We choose "-only" (not "or later") so that license changes remain a deliberate governance action
  rather than an automatic external upgrade.

### Meaning (plain English)

If you modify our core software and let users interact with it over a network, you must offer those
users the **complete corresponding source code** of the modified version.

This closes the SaaS loophole and aligns with our values:
- If someone "poisons" the system, the poison becomes **visible**, **auditable**, and **easy to
  route around**.

---

## Scope

### "Core software" (AGPLv3)

"Core" includes (at minimum):

- the primary server / portal runtime
- the reference web UI shipped with the server
- admin tooling shipped as part of the runtime
- plugins/modules that run in-process with the core runtime (same address space) and are intended
  as extensions of the core system
- any code we ship as "the system" to users as a coherent product

Default rule: if it's part of the thing that provides the user-facing service, it is core.

### Non-core components (default to AGPL unless explicitly carved out)

We may publish certain "edge" components under permissive licenses only when doing so increases user
freedom without enabling secret hosted modifications of the core.

Examples that may qualify (future, not assumed today):
- thin client SDKs
- interoperability libraries
- standalone CLI tools that are not required to run the service
- data format libraries

Important: any permissive carve-out must be explicitly declared with:
- a separate `LICENSE` file in that directory,
- an ADR (or an appendix to this ADR),
- and clear boundaries that prevent "core by another name."

---

## Why this decision fits our values

- **User sovereignty:** users can host, fork, and migrate; they are not trapped behind a vendor.
- **Inspectability:** users of hosted instances can obtain the exact source they are interacting
  with.
- **No lock-in to us:** if Tech of Our Own disappears, forks and community operators can continue
  openly.
- **Host-for-each-other is preserved:** AGPL permits charging for hosting/services; it simply
  requires source availability for modified versions.
- **Anti-enshittification:** we are not "licensing our way to goodness," but we are ensuring the core
  cannot be quietly captured behind a hosted fork.

---

## Consequences

### Positive

- Closes the SaaS loophole for core functionality.
- Encourages a healthier ecosystem where hosted operators compete on:
  - reliability, UX, support, hardware, and service quality,
  - not on secret proprietary modifications.
- Makes it harder for large providers to "embrace/extend/extinguish" invisibly.
- Aligns with the ethos of trust through verification, not trust through policy.

### Negative / Tradeoffs

- Some companies will avoid adopting core code (especially for proprietary offerings). That is an
  acceptable tradeoff: our mission is not to enhance closed systems.
- Some integration patterns become harder: anything that links to or extends the AGPL core
  in-process must be AGPL-compatible.
- License compliance introduces operational requirements for hosted operators: they must provide
  source to network users. We will reduce friction by making compliance easy (see Implementation
  Notes).

---

## Options considered

### Option A: Apache 2.0 (permissive)
- Rejected.
- Allows proprietary SaaS forks with private modifications.
- Fails our stated value: no secret hosted modifications of the core.

### Option B: GPLv3
- Rejected.
- Strong copyleft on distribution, but does not close the SaaS loophole.

### Option C: MPL 2.0 (file-level copyleft)
- Rejected for core.
- Improves remixability but still does not require source disclosure for network use.
- Could be appropriate for certain edge components in the future, but it does not meet the "SaaS
  transparency" requirement for core.

### Option D: SSPL / "source-available anti-cloud" licenses
- Rejected.
- Not universally recognized as open source and can create downstream legal ambiguity.
- Risks undermining trust and broad community legitimacy.
- Overreaches relative to our stated goal: we want hosted modifications visible, not to impose
  obligations on an operator's entire infrastructure stack.

### Option E: AGPLv3
- Accepted.
- Directly targets the SaaS loophole while remaining a widely understood free software license.

---

## Implementation notes

### 1) Make compliance effortless (especially for hosters)

Core deployments should expose:

- a visible "Source Code" link in the UI
- the running version/commit hash
- a documented "how to get the source for this instance" path

Recommended pattern:
- UI footer: `Source Code | Version | License`
- link points to a git tag/commit or a published source archive

This supports our values: inspectability as a right, not a feature.

### 2) Repository hygiene

- Add root `LICENSE` (AGPLv3 text) and `COPYING` as needed.
- Add SPDX headers in source files where appropriate:
  - `SPDX-License-Identifier: AGPL-3.0-only`
- Add `CONTRIBUTING.md` stating inbound=outbound:
  - contributions are accepted under the project's license by default
  - we do not require a CLA that enables proprietary relicensing by a central actor (unless members
    explicitly approve such a change)

### 3) Dependency policy

Because AGPL is copyleft, we must ensure third-party dependencies are license-compatible.

- Establish a lightweight review rule for new dependencies:
  - record dependency name and license
  - confirm compatibility with AGPLv3
  - reject "source-available" dependencies that create downstream restrictions contradictory to our
    values

### 4) Plugins and extensions

Because we intend a plugin ecosystem:

- In-process plugins are treated as extensions of the core program and must be under
  AGPLv3-compatible terms.
- Out-of-process integrations (over HTTP, message queues, etc.) can be any license, because they are
  separate programs interacting over a network protocol.

This is not about purity; it is about keeping the core service auditable and non-capturable.

---

## Future changes

We expect licensing to evolve as the ecosystem grows. Any of the following changes require explicit
governance action (ADR + member process):

- adding permissive-licensed edge components
- dual licensing
- adopting "or later" terms
- introducing an exception (e.g., linking exception)

---

## References

- `../governance/VALUES.md` (Declaration of Values)
- `../governance/CONSTITUTION.md`
- `../governance/BOARD_OPERATIONS.md`
- `../governance/FOUNDER_STEWARDSHIP.md`
