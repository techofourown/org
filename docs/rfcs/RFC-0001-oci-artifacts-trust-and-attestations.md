# RFC-0001: OCI Artifact Distribution, Trust, and Attestations (Phased Plan)
**Created:** 2026-02-26  
**Updated:** 2026-02-26

---

## What

This RFC proposes a long-term, org-wide strategy for distributing TOOO artifacts via OCI, including:

- signer identity and a user-owned trust policy model (“one lane, explicit trust”)
- signatures for TOOO releases
- SBOM + provenance attestations as OCI referrers
- compatibility metadata for hardware-installed payloads (OS images, firmware, OTA bundles)
- offline-verifiable install/update for devices

It is intentionally phased so TOOO can ship apps now (ADR-0007) without having to finish the entire
trust + pipeline system today.

---

## Why

We need three things simultaneously:

1) **Rapid iteration on apps** across multiple hardware targets without rebuilding/ reflashing OS images.
2) **A future-proof trust model** where users can cryptographically tell “TOOO built this” vs “someone else built this.”
3) **No two-lane split.** Same distribution shape for everyone; trust is explicit and user-controlled.

OCI gives us the content-addressed substrate (digests). This RFC describes how we can layer trust,
auditability, and hardware safety on top—when we’re ready.

---

## How (phased)

### Phase 0 (Now): Ship apps via OCI digests with minimal process
Goal: unblock app work with minimal pipeline cost.

**Proposed minimum:**
- Build/push images to `ghcr.io/techofourown/...`
- Record/print the resulting digest
- Deploy by digest in k8s manifests (or in whatever app orchestrator is used)

**Non-goals in Phase 0:**
- mandatory signatures
- SBOM/provenance
- hardware compatibility enforcement

This is the “fast lane” inside one lane: not different rules, just fewer adopted layers.

---

### Phase 1: TOOO release signing (identity clarity, “who built this”)
Goal: users can cryptographically verify TOOO-published releases.

**Proposal:**
- Use Sigstore-style signing (keyless preferred) or a KMS-backed key where needed.
- Publish a clear list of “TOOO signer identities” (e.g., CI workload identities).
- Tooling surfaces signer identity on install/update:
  - VERIFIED SIGNATURE: <identity>
  - or UNSIGNED

**Key rule (one lane):**
- Verification is always performed.
- Trust is a user choice:
  - trust a signer identity OR pin a digest.

---

### Phase 2: SBOM + provenance attestations as OCI referrers (auditability)
Goal: increase auditability and supply-chain visibility without changing distribution shape.

**Proposal:**
- Attach SBOM (SPDX or CycloneDX) as an OCI referrer to release digests.
- Attach provenance attestation (build workflow identity, source revision, timestamp).
- Tooling checks presence/validity for “TOOO release” trust profiles.

---

### Phase 3: Hardware-installed payloads as OCI artifacts (OS images, firmware, OTA bundles)
Goal: unify “things we flash” with the same digest+signature trust model.

**Proposal:**
- Package OS images (.img.xz), firmware payloads, and OTA bundles as OCI artifacts (not necessarily “container images”).
- Attach:
  - signature(s)
  - provenance
  - SBOM (where applicable)
  - compatibility constraints (product family, model ID, revision constraints, ABI constraints)

**Safety proposal:**
- flashers/updaters enforce compatibility fail-closed by default

---

## Trust model proposal (“one lane, explicit trust”)

### Core concept
- **Digest** answers “what bits are these?”
- **Signature** answers “who is claiming responsibility?”
- **Trust policy** answers “do I accept this signer or this exact digest on this device?”

### Proposed trust policy structure
A device maintains a local, user-owned trust policy that can include:

- Trusted signer identities (e.g., “TOOO CI identity”, “my key”, “friend key”)
- Pinned digests (trust-by-exact-bits)
- Optional policy presets (“TOOO-only”, “TOOO + pinned digests”, etc.) as convenience, not modes

### Proposed acceptance rule
Installer/updater/flasher accepts an artifact only if:
- it has a valid signature from a trusted signer identity, OR
- its digest is explicitly pinned in the trust policy.

This avoids “developer mode” while preserving total freedom.

---

## Operational artifact conventions (proposed)

### Naming
Align OCI repo naming with typed-prefix repo naming (ADR-0002/ADR-0003).

### Tagging
- Releases: `vMAJOR.MINOR.PATCH`
- Dev iteration: `dev`, `edge`, `pr-<n>` (allowed)
- Docs prefer digest pinning; tags are for humans.

### Minimum metadata (always)
OCI labels/annotations:
- source repo URL
- revision SHA
- version string
- created timestamp

### Release metadata (Phase 2+)
- SBOM referrer
- provenance referrer
- signature referrer

---

## Hardware compatibility metadata proposal (Phase 3+)

Any hardware-installed payload should declare:
- product family token (e.g., `ourbox`)
- model identifier (ADR-0004, e.g., `TOO-OBX-MBX-01`)
- revision/variant compatibility
- bootloader/firmware ABI constraints (if applicable)

Flasher/updater behavior:
- default fail-closed (refuse incompatible payloads)
- explicit override allowed, but noisy and logged

---

## Trade-offs (if known)

### Pros
- Single distribution “shape” for everything (OCI + digest + optional referrers).
- Strong future trust model without blocking app iteration today.
- Mirrors/self-hosting remain first-class.

### Cons
- Some ecosystem friction around OCI for non-container payloads (Phase 3 is work).
- Implementing good trust UX is non-trivial (but worth it).

---

## Open Questions

1) Which signing identity mechanism do we standardize on first (keyless vs KMS-backed)?
2) How do we publish/communicate “TOOO signer identities” in a way that’s stable and auditable?
3) Where should device trust policy live (file path, format, export/import)?
4) What is the minimal “trust report” UX (CLI + UI) that makes signer identity unmistakable?
5) For airgapped installs, what is the canonical offline bundle format (OCI layout tar, or “bundle directory”)?

---

## Next Steps

- Adopt ADR-0007 (already minimal) and proceed with Phase 0 for apps.
- Prototype a minimal “digest capture + deploy-by-digest” workflow in one app repo.
- Revisit Phase 1 signing once it starts paying rent (e.g., first wider release / first third-party mods / first security concerns).

---

## References
- ADR-0007: Adopt OCI artifacts as canonical distribution substrate
- ADR-0002 / ADR-0003 / ADR-0004 (naming and hardware identifiers)
- `docs/governance/VALUES.md`
