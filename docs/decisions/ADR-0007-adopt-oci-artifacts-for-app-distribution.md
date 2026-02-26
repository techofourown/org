# ADR-0007: Adopt OCI Artifacts as the Canonical Distribution Substrate (Apps + Platform Components)

- **Date:** 2026-02-26
- **Status:** Accepted (Founder decision; intended for later Board ratification)
- **Deciders:** Founder (initial), future Board + Members (ratification/amendment)
- **Related:**
  - `ADR-0002-adopt-typed-prefix-repo-names.md`
  - `ADR-0003-standardize-naming-across-artifacts.md`
  - `docs/governance/VALUES.md` (inspectability, no lock-in, forkability)
  - (Proposed) `docs/rfcs/RFC-0001-oci-artifacts-trust-and-attestations.md`

---

## Context

Tech of Our Own needs a single, repeatable way to ship and update *applications* across multiple
hardware targets without coupling app iteration to OS image flashing.

We want a distribution substrate that:

- works across targets (x86/arm, multiple devices),
- is content-addressed (so “what I pulled” is unambiguous),
- is mirrorable/self-hostable with standard tools (no lock-in),
- supports an eventual robust trust model (signatures, SBOM, provenance),
- and does not require us to finish the “final pipeline” today in order to ship apps now.

OCI registries and OCI artifacts are widely-supported infrastructure for exactly this job.

---

## Decision

### We adopt OCI artifacts (OCI registry + manifests + digests) as the canonical distribution substrate for TOOO-shipped application artifacts and platform components.

This ADR is intentionally **minimal**. It makes one core call:

> **Apps and deployable platform components are distributed as OCI artifacts, and are identified by digests.**

Everything else (signing, SBOM, provenance, hardware compatibility metadata, flasher rules) is
specified as a proposed roadmap in RFC-0001, not locked in by this ADR.

---

## Scope (what this ADR covers now)

This ADR applies to:

- application containers deployed onto devices post-boot (e.g., k3s workloads)
- “platform components” that we deploy the same way (ingress components, small services, etc.)
- installers/CLIs that we choose to ship as OCI artifacts

This ADR does **not** require (today) that:

- OS images (.img.xz) be shipped via OCI
- firmware payloads be shipped via OCI
- signatures/SBOM/provenance be mandatory today

Those may become decisions later (see RFC-0001).

---

## Normative rules (minimum constraints to keep us on the final path)

### 1) Canonical reference is by digest
- Any *deployment* reference for an artifact MUST be expressible as a digest reference:
  - `registry/namespace/name@sha256:<digest>`
- Tags MAY exist for convenience, but digests are the ground truth.

### 2) Registry location (initial)
- Initial publishing registry for TOOO artifacts is:
  - `ghcr.io/techofourown`
- Mirroring MUST remain possible with standard OCI tooling (docker/podman/oras).

### 3) Naming alignment with repo identity
- OCI repository names SHOULD match the producing Git repository name (typed-prefix scheme).
  - Example: repo `sw-ourbox-portal` → `ghcr.io/techofourown/sw-ourbox-portal`
- If one repo produces multiple artifacts, it MAY use path segments:
  - `ghcr.io/techofourown/sw-ourbox-os/identity`

### 4) Version tags for releases; dev tags allowed for iteration
- Release tags SHOULD use SemVer: `vMAJOR.MINOR.PATCH`.
- Development tags (e.g., `dev`, `edge`, `pr-123`) MAY be used for iteration.
- Documentation and “stable install” guidance SHOULD prefer digest pinning.

### 5) Minimum metadata (keep provenance legible without heavy machinery)
TOOO-built images SHOULD include these OCI labels:
- `org.opencontainers.image.source` (repo URL)
- `org.opencontainers.image.revision` (git SHA)
- `org.opencontainers.image.version` (tag/version string)
- `org.opencontainers.image.created` (timestamp)

(We are explicitly *not* requiring SBOM/provenance referrers in this ADR.)

---

## Consequences

### Positive
- Unblocks rapid app iteration across multiple targets immediately.
- Separates “app delivery” from “OS image flashing” by default.
- Keeps us on a direct path to stronger trust later (signatures/attestations attach naturally to OCI digests).
- Users can mirror/self-host artifacts using standard tooling.

### Negative / Tradeoffs
- Digest pinning is a mindset shift (but it’s the right long-term move).
- We must be disciplined about naming and labeling to avoid “mystery artifacts.”

### Mitigation
- Keep this ADR minimal and use RFC-0001 for the “full hardened” plan.
- Provide lightweight tooling/docs that output “here is the digest you just built/pushed.”
- Adopt stronger requirements only when they start paying rent.

---

## Implementation notes (non-normative)

A minimal “today” loop that honors this ADR:

1) Build container image (locally or CI).
2) Push to `ghcr.io/techofourown/<name>:<tag>`.
3) Capture the resulting digest.
4) Deploy by digest (k8s manifest uses `image: ...@sha256:...`).

No signatures required *today* to comply with this ADR.

---

## References
- RFC-0001 (proposed): OCI artifacts trust model + signatures + attestations + future hardware payload packaging
