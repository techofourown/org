# Hardware-Encrypted Offline Recovery Media Policy
**Draft v1.1**

## Purpose

This policy defines how TOOO treats its approved hardware-encrypted offline
recovery media during the current founder-led public-platform phase.

It exists so the offline recovery path is not vague.

This policy turns the medium-selection decision from `ADR-0013` into an
enforceable public boundary while leaving exact operating mechanics in
TOOO-controlled private operations documentation.

---

## Scope

This policy applies to TOOO's current approved hardware-encrypted offline
recovery medium for public-platform continuity work.

It applies to:

- continuity custody
- continuity refresh
- validation drills
- actual recovery use
- assistant-boundary handling while the medium is in use

---

## Definitions

### Continuity bundle

The set of continuity artifacts written to the approved offline recovery medium.

### Continuity refresh

A deliberate update of the continuity bundle after a material change or as part
of scheduled maintenance.

### Continuity drill

A deliberate validation that proves the offline recovery medium and continuity
bundle are still usable.

### Resting state

The desired storage posture of the approved recovery medium when it is not being
actively refreshed or used for recovery.

---

## Policy

### 1) Approved medium

The approved device class for current offline continuity custody is the medium
selected by `ADR-0013`.

No other removable medium is considered the standard continuity medium unless a
follow-up decision says otherwise.

### 2) The approved medium is not the only cryptographic boundary

The approved device protects the medium itself from casual access.

It does **not** replace file-level cryptographic protection.

Sensitive artifacts written to the device must remain protected at the file
level as appropriate.

### 3) Continuity media is not a daily working secret store

The approved medium exists for:

- offline continuity custody
- deliberate refresh of continuity artifacts
- validation drills
- actual recovery work

It must not be treated as a casual, day-to-day secret dump.

### 4) Restrictive resting-state handling is required

When not in active use, the approved continuity medium must remain:

- locked
- physically removed
- stored away from the daily workstation
- handled in a way consistent with restrictive continuity custody

The exact device configuration and resting-state details belong in private
operations documentation.

### 5) Continuity-bundle composition must be defined, but privately

TOOO must maintain a defined continuity bundle for the approved medium.

The exact file inventory, naming, and layout belong in TOOO-controlled private
operations documentation rather than in this public repo.

### 6) Validation is mandatory

The approved continuity medium must be validated:

- after initial setup
- after major continuity changes
- periodically thereafter

The exact cadence and checklists belong in private operations documentation.

### 7) Detailed runbooks are private

This public policy records **what must be true**.

The following are deliberately private:

- exact device configuration values
- exact storage arrangement
- exact bundle inventory
- exact refresh steps
- exact drill checklists
- break-glass procedures

### 8) AI assistant guidance

AI assistants may help the operator before, during, or after a mounted session,
including exploratory and diagnostic work when needed.

When the approved medium is mounted, the operator should be mindful of the
assistant's access to sensitive material. The assistant may note the elevated
context and ask for confirmation before performing sensitive operations, but
should never refuse to help solely because the medium is mounted.

Assistants are not continuity custodians.

### 9) Incident handling

If the approved continuity medium is:

- lost
- stolen
- physically damaged
- behaving suspiciously
- believed to have been handled outside policy

TOOO must treat the continuity posture as degraded and remediate through its
private continuity procedures.

---

## Exceptions

Exceptions are allowed only for:

- actual recovery events
- urgent incident response
- temporary tooling or hardware failure that blocks standard handling

Any exception must be:

- narrow
- time-limited
- recorded in a protected continuity record
- followed by corrective action restoring the intended posture

---

## Enforcement

During the founder-led phase, the responsible TOOO operator is responsible for
compliance.

If the approved continuity medium has not been refreshed and validated as
required, or if it is being used as a casual working secret store, the
continuity posture must be treated as non-compliant.

---

## Trigger for Re-evaluation

This policy must be re-evaluated when:

- TOOO changes the approved hardware-encrypted continuity medium
- a second human maintainer joins platform-ops continuity custody
- TOOO adopts a materially different offline recovery architecture
- the current founder-led handling pattern stops paying rent

---

## References

- `../decisions/ADR-0013-adopt-apricorn-aegis-secure-key-3nx-as-offline-platform-recovery-media.md`
- `../decisions/ADR-0012-adopt-gpg-for-early-stage-platform-ops-secret-management.md`
- `./SOLE_MAINTAINER_CONTINUITY_AND_RECOVERY_POLICY.md`
- `./PLATFORM_OPS_KEY_AND_SECRET_HANDLING_POLICY.md`
- `./AI_ASSISTED_OPERATIONS_AND_SECRET_EXPOSURE_POLICY.md`
