# Sole Maintainer Continuity and Recovery Policy
**Draft v1.2**

## Purpose

This policy defines the minimum continuity and recovery posture for TOOO's
current founder-led public-platform phase.

It exists to prevent the following organizational failures:

- the platform dies with one laptop
- the platform dies with one memory
- the platform dies because recovery material was never written down
- the platform dies because the offline path was only aspirational
- continuity depends on AI assistants instead of durable human-governed records

The goal is not to pretend TOOO already has a staffed operations team.

The goal is to make the current stage survivable, legible, and recoverable.

---

## Scope

This policy applies to continuity and recovery material for TOOO's
public-platform operations layer, including at minimum:

- Keycloak at `accounts.techofourown.com`
- Discourse at `forum.techofourown.com`
- associated ops repos
- associated keys, backups, and service inventory

This policy applies while TOOO has one primary human maintainer with possible
use of AI assistants.

---

## Policy

### 1) No single-machine dependency

The public-platform operations posture must not depend on one workstation as the
only place where recovery is possible.

At minimum, TOOO must maintain:

- one primary trusted maintainer machine, and
- one additional restore path that has been deliberately prepared and tested

That second path may be:

- a second trusted machine, or
- a tested machine-rebuild workflow using preserved encrypted material

### 2) No single-copy dependency

Critical recovery material must exist in more than one durable location.

At minimum, TOOO must maintain:

- one working copy, and
- one additional protected continuity copy outside the daily workstation

The exact copy strategy for this phase is maintained in TOOO-controlled private
operations documentation rather than in this public policy.

### 3) Required continuity artifacts

The following artifacts are mandatory in some protected form:

1. **TOOO recovery key**
2. **Encrypted backup of the day-to-day operator key or subkeys**
3. **Key fingerprint inventory**
4. **Continuity packet**
5. **Restore instructions**
6. **Protected offline continuity custody**

### 4) Continuity packet is required

TOOO must maintain a continuity packet that is recoverable without relying on
memory alone.

At minimum, the continuity packet must identify:

- active public-platform services
- canonical domains
- relevant operations repos
- where system / repo secrets live conceptually
- where operator-memory secrets live conceptually
- backup locations conceptually
- key fingerprints
- restore order of operations
- emergency notes that explain the minimum path back to operability

The continuity packet itself must be encrypted at rest.

### 5) Approved offline recovery medium is required

The current approved offline recovery medium is the device class selected by
`ADR-0013`.

That medium must be handled according to both:

- public posture-level policy, and
- private TOOO operations documentation that carries the exact mechanics

### 6) Recovery material must be separated from day-to-day convenience

The TOOO recovery key and related break-glass material must not be treated as a
daily-use convenience asset.

They must be:

- stored offline or otherwise removed from routine daily use
- protected against casual local exposure
- retrieved only for deliberate recovery, continuity work, or key-management
  maintenance

### 7) Changes must update continuity artifacts promptly

Whenever TOOO adds or materially changes a critical service, the continuity
packet and key inventory must be updated promptly.

This includes:

- new critical repos
- new critical domains
- new root credentials
- new recovery dependencies
- key rotation
- change of canonical host or provider

Material changes must also trigger a continuity refresh and targeted validation.

### 8) Restore drills are mandatory

TOOO must perform continuity validation:

- once after initial setup
- after major key or secret-architecture changes
- periodically during active platform operation

At some regular interval, TOOO must also perform a deeper recovery exercise that
goes further than a quick mount-and-check.

The exact cadence and drill shape belong in private operations documentation
rather than in this public policy.

### 9) A drill must prove more than “the media still exists”

A continuity drill is only valid if it proves that the continuity artifacts are
still usable through the intended recovery path.

At minimum, a valid drill must confirm that TOOO can still:

- access the protected continuity copy
- locate the expected continuity artifacts
- read the continuity packet through the intended path
- treat recovery-key and operator-key backup material as intelligible and usable
  in principle
- return the continuity media to protected storage afterward

### 10) Recovery access dependencies must be recoverable too

If continuity depends on an additional unlock factor, recovery record, or other
access prerequisite, that prerequisite must itself be preserved in a protected
recovery path and not assumed to exist only in one memory or one machine.

### 11) AI assistants are not continuity custodians

AI assistants may help draft or refine recovery documents.

They are not continuity custodians.

Continuity exists only when the protected records, keys, and restore paths are
actually stored and recoverable under human-governed control.

No broad assistant session should remain active while approved recovery media is
mounted for live continuity work.

### 12) Public posture, private mechanics

This public policy records what must be true.

The exact details for:

- continuity-bundle composition
- device configuration
- storage arrangement
- drill cadence
- refresh workflow
- break-glass handling

belong in TOOO-controlled private operations documentation rather than in this
repository.

### 13) A future second human maintainer changes the model

The moment TOOO adds another human maintainer with real platform access, the
continuity model must expand beyond founder-only recovery thinking.

This policy must then be reviewed for:

- recipient expansion
- custody changes
- shared recovery expectations
- join / leave procedures

---

## Minimum interpretation guidance

This policy is intentionally minimum-bound, not maximalist.

It does **not** require TOOO to already have:

- a board-run key ceremony
- a dedicated security team
- a staffed NOC
- an enterprise HSM stack

It **does** require TOOO to stop pretending that “I know roughly where things
are” is a continuity plan.

It also requires TOOO to stop treating “one encrypted USB stick somewhere” as a
complete continuity answer.

---

## Exceptions

Exceptions are allowed only for:

- incident response
- urgent recovery work
- temporary tooling failure that blocks compliant backup handling

Any exception must be:

- time-limited
- recorded in a protected continuity note
- followed by corrective action that restores the required continuity posture

---

## Enforcement

During the founder-led phase, the responsible TOOO operator is responsible for
compliance.

If required continuity artifacts do not exist, or if the continuity posture has
not been refreshed and validated after material change, the platform must be
treated as under-documented and under-protected until remedied.

---

## Trigger for Re-evaluation

This policy must be re-evaluated when:

- a second human maintainer joins the platform-ops workflow
- TOOO adopts a formal human credential-vault product with shared custody
- TOOO adopts a materially different secret and recovery architecture
- TOOO adds sufficiently many public-platform services that the current packet
  shape becomes inadequate

---

## References

- `../decisions/ADR-0012-adopt-gpg-for-early-stage-platform-ops-secret-management.md`
- `../decisions/ADR-0013-adopt-apricorn-aegis-secure-key-3nx-as-offline-platform-recovery-media.md`
- `./PLATFORM_OPS_KEY_AND_SECRET_HANDLING_POLICY.md`
- `./HARDWARE_ENCRYPTED_OFFLINE_RECOVERY_MEDIA_POLICY.md`
- `./AI_ASSISTED_OPERATIONS_AND_SECRET_EXPOSURE_POLICY.md`
- `../governance/FOUNDER_STEWARDSHIP.md`
- `../governance/VALUES.md`
