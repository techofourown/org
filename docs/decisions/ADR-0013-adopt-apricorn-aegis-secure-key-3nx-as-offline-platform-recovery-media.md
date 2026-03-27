# ADR-0013: Adopt Apricorn Aegis Secure Key 3NX as Offline Platform Recovery Media

- **Date:** 2026-03-27
- **Updated:** 2026-03-27
- **Related:**
  - `../governance/VALUES.md`
  - `../governance/FOUNDER_STEWARDSHIP.md`
  - `./ADR-0012-adopt-gpg-for-early-stage-platform-ops-secret-management.md`
  - `../rfcs/RFC-0003-early-stage-key-and-secret-management-for-public-platform-ops.md`
  - `../policies/SOLE_MAINTAINER_CONTINUITY_AND_RECOVERY_POLICY.md`
  - `../policies/HARDWARE_ENCRYPTED_OFFLINE_RECOVERY_MEDIA_POLICY.md`

---

## Context

TOOO now has an explicit early-stage decision for repo-managed machine-readable
platform-ops secrets: `ADR-0012` establishes **GPG** as the canonical
cryptographic substrate for that material.

That decision still left one important operational question partly implied:

**what physical medium will TOOO actually use for offline continuity and
recovery custody during the current founder-led phase?**

The current phase has very specific constraints:

- public-platform services now matter enough that recovery can no longer remain
  vague or laptop-bound
- continuity must survive workstation loss, operator fatigue, and ordinary
  operational drift
- the continuity posture must be strong enough to separate recovery material
  from day-to-day convenience
- the solution must remain compatible with TOOO's values while still being
  practical to operate

TOOO needs an offline medium that is:

- physically removable and easy to store away from the daily workstation
- independent of a hosted provider
- independent of a specific OS-level encrypted-volume stack
- usable on ordinary machines during recovery
- hardware-encrypted before the host can read the contents
- simple enough to use deliberately under stress
- a good fit for restrictive, continuity-oriented handling

The Apricorn Aegis Secure Key 3NX is a hardware-encrypted removable USB device
with a built-in keypad and host-independent unlock flow. It supports:

- keypad-entry unlock before insertion
- admin-controlled access behavior
- automatic lock behavior
- brute-force resistance
- offline use without a companion SaaS or remote control plane

At the same time, this device is not open hardware, not open firmware, and not
the kind of user-facing core technology TOOO would ever want to make central to
its public product promise.

This is therefore a bounded operational decision, not a new philosophical
center of gravity.

This document is intentionally public-facing. Detailed device configuration,
continuity-bundle composition, storage arrangements, drill cadence, and
break-glass procedures are maintained in TOOO-controlled private operations
documentation rather than in this repository.

---

## Decision

TOOO will use the **Apricorn Aegis Secure Key 3NX** as the approved
**hardware-encrypted offline recovery medium** for current public-platform
continuity work.

More specifically:

1. The Apricorn Aegis Secure Key 3NX is the designated offline removable medium
   for TOOO's current platform-continuity bundle.

2. The Apricorn medium is a **custody and transport layer**, not the sole
   cryptographic boundary.
   Sensitive material written to the device must still remain protected at the
   file level as appropriate.

3. The Apricorn medium is **not** a daily working secret store.
   It exists for:
   - offline continuity custody
   - deliberate refresh of continuity artifacts
   - periodic validation
   - actual recovery work

4. TOOO will maintain multiple protected continuity copies during this phase.
   The exact copy strategy and storage arrangement are defined privately rather
   than in this public ADR.

5. Detailed operational handling for the approved medium, including:
   - device configuration
   - continuity-bundle composition
   - storage arrangement
   - drill cadence
   - refresh workflow
   - break-glass handling

   is governed by private TOOO operations documentation, not by public
   governance text alone.

---

## Rationale

### 1) This gives the recovery path a real physical home

The earlier document set said TOOO needed offline continuity material.

This ADR turns that from an implication into an actual named medium and custody
practice.

### 2) Host-independent keypad unlock is a good fit for the current phase

The Aegis Secure Key 3NX unlocks before the host reads the device, which is
operationally cleaner than relying on a particular host-side encrypted-volume
stack during recovery.

That matters when recovery must work on more than one machine.

### 3) Restrictive, continuity-oriented handling is the right posture

Continuity media should not behave like a working scratch drive.

A device that supports deliberate unlock-and-use behavior is a better fit for
continuity custody than a casual general-purpose removable drive.

### 4) This is a bounded tactical use of proprietary hardware, not a mission pivot

TOOO's public values remain centered on free and open source core technology,
inspectability, and anti-lock-in.

This device does **not** become:

- a user-facing TOOO platform dependency
- the source of truth for repo-managed secrets
- the cryptographic basis for TOOO's core software or hardware products

It is a tactical continuity accessory for the org's current operational stage.

### 5) The right public/private split is posture public, mechanics private

The fact that TOOO uses an approved offline recovery medium can be public.

The exact hardening profile, bundle inventory, validation routine, and
break-glass sequence do not need to be public to make the governance record
honest or useful.

---

## Consequences

### Positive

- TOOO now has a named, concrete offline continuity medium.
- Recovery material can be physically separated from the daily workstation.
- The chosen medium works without a hosted control plane.
- The continuity story becomes more legible and governable.
- Public governance stays honest while private operational detail stays private.

### Negative / Tradeoffs

- The Apricorn device is proprietary hardware / firmware.
- The device has its own operational quirks and maintenance needs.
- The medium still requires layered file-level cryptographic protection.
- Public docs can describe the choice, but they should not become a public
  recovery runbook.

### Mitigation

- keep GPG as the canonical cryptographic substrate
- use the device only as a continuity custody layer
- maintain more than one protected continuity copy
- keep exact configuration and procedures in private operational docs
- keep assistant sessions away from mounted continuity media during live work

---

## Implementation Notes

### 1) Continuity layering remains mandatory

The Apricorn medium improves custody and physical separation, but it does not
replace file-level cryptographic protection of the artifacts placed on it.

### 2) Public docs describe the decision, not the runbook

Public governance documents may record:

- that TOOO uses approved hardware-encrypted offline recovery media
- why that choice was made
- what architectural role the medium plays

They should not become the place where TOOO publishes:

- exact device hardening values
- exact continuity-bundle inventory
- exact storage arrangements
- exact drill checklists
- break-glass instructions

### 3) Private operations documentation carries the exact mechanics

The detailed operating model for this medium belongs in TOOO-controlled private
operations documentation.

---

## Future Changes

The following do **not** require superseding this ADR so long as the chosen
device class remains the Apricorn Aegis Secure Key 3NX:

- changing file names inside the continuity bundle
- tightening private drill cadence or refresh routines
- refining the exact copy strategy in private operational docs
- adding additional protected continuity copies

The following **do** require follow-up governance action:

- replacing the Apricorn medium as TOOO's approved offline continuity device
- deciding to rely on device-only secrecy instead of layered file-level
  cryptographic protection
- turning continuity media into a daily working secret store
- making the public repo the canonical place for break-glass procedures

---

## References

- `../governance/VALUES.md`
- `../governance/FOUNDER_STEWARDSHIP.md`
- `./ADR-0012-adopt-gpg-for-early-stage-platform-ops-secret-management.md`
- `../rfcs/RFC-0003-early-stage-key-and-secret-management-for-public-platform-ops.md`
- `../policies/SOLE_MAINTAINER_CONTINUITY_AND_RECOVERY_POLICY.md`
- `../policies/HARDWARE_ENCRYPTED_OFFLINE_RECOVERY_MEDIA_POLICY.md`
- Apricorn Aegis Secure Key 3NX User's Manual
