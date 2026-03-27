# AI-Assisted Operations and Secret Exposure Policy
**Draft v1.2**

## Purpose

This policy defines how TOOO uses AI assistants in platform operations without
quietly turning them into secret custodians or widening secret blast radius
beyond deliberate human control.

This policy is written for the current reality:

- a small founder-led operations posture
- meaningful use of AI assistants
- shell-heavy and documentation-heavy workflows
- growing public-platform infrastructure
- a real offline continuity path using approved recovery media

The goal is not to ban AI assistants.

The goal is to make their role explicit, bounded, and safe enough for TOOO's
current stage.

---

## Scope

This policy applies to AI-assisted work near TOOO public-platform operations,
including:

- service setup and troubleshooting
- shell sessions on trusted maintainer machines
- editing config or deployment templates
- reviewing logs or deployment artifacts
- drafting runbooks, ADRs, RFCs, and policies
- any workflow that could expose or manipulate keys, secrets, recovery
  material, or mounted offline continuity media

This policy applies whether the assistant is:

- local
- remote
- terminal-oriented
- chat-oriented
- embedded in an editor or automation environment

---

## Definitions

### AI assistant

A software system that helps generate, transform, inspect, or act on text,
commands, code, or system state.

### Secret-bearing context

Any context where the assistant could view, infer, export, modify, or cause
use of live secret material.

### High-risk secret action

Any action that materially changes TOOO's trust posture, recovery posture, or
secret exposure surface.

Examples:

- generating or exporting key material
- changing recipient sets
- rotating core credentials
- touching recovery-key material
- changing registrar / DNS / mail-root credentials
- exporting a vault or credential store
- mass-decrypting secret files
- mounting and reading approved offline recovery media during live continuity
  work

### Mounted offline recovery session

Any session in which the approved offline recovery medium is unlocked,
inserted, mounted, or being actively refreshed or used for recovery.

---

## Policy

### 1) AI assistants are tools, not maintainers

AI assistants are not:

- maintainers
- approvers
- custodians
- continuity actors
- cryptographic principals

A human maintainer remains accountable for all privileged actions.

### 2) Default to redaction and placeholders

When asking an AI assistant for help, the default must be:

- redacted values
- placeholder secrets
- minimal excerpts
- derived descriptions rather than live secret content

Do not reveal more than the task genuinely requires.

### 3) No whole-vault exposure

Whole-vault exposure is prohibited.

This includes, at minimum:

- pasting an entire credential export into an assistant
- handing an assistant a full vault unlock plus bulk export
- exposing a full collection of recovery codes or TOTP seeds
- bulk-sharing every environment file “just for convenience”

### 4) No private keys, seed material, or recovery codes in routine assistant prompts

The following must not be pasted into routine assistant prompts or sessions
unless there is a narrowly justified, deliberate recovery or incident-response
need:

- private keys
- armored secret-key exports
- recovery codes
- TOTP seeds
- break-glass credentials
- vault master secrets

Even then, the human maintainer should prefer not to do so.

### 5) Local shell assistants must be treated as high capability when agents are unlocked

If a local shell-capable assistant is operating in a session where:

- a GPG agent is unlocked
- a credential store is open
- a shell has inherited live secret environment variables

the assistant must be treated as operating in a **high-capability** context.

In that state:

- keep the session window short
- limit the task scope
- avoid casual exploratory prompting
- close or relock access once the task is complete

### 6) Mounted offline recovery sessions are treated as high-capability by default

When approved offline recovery media is mounted:

- broad assistant sessions are prohibited
- exploratory “look around” work is prohibited
- the task must remain narrowly scoped
- no live continuity bundle should be exported to the assistant in bulk
- if documentation help is needed, first relock/eject or redact the material

### 7) High-risk secret actions require explicit human initiation and review

High-risk secret actions must not be delegated implicitly to an assistant.

They require deliberate human initiation and human review.

Examples include:

- generating or rotating the operator key
- generating or rotating the recovery key
- changing GPG recipient sets
- exporting encrypted backups of key material
- rotating registrar, DNS, or root mail credentials
- mass decrypting or re-encrypting secret inventories
- refreshing or using offline continuity media during real recovery work

### 8) Logs and diagnostics must be scrubbed before sharing

Before sharing logs, configs, or screenshots with an assistant, the human
maintainer must scrub where practical:

- passwords
- tokens
- private keys
- cookies
- session identifiers
- email addresses if they are not needed
- provider account numbers if they are not needed

### 9) Assistants may work on encrypted or non-secret representations

AI assistants may safely help with:

- encrypted files as encrypted files
- templates
- redacted configs
- placeholder `.env` files
- deployment structure
- runbook drafting
- policy drafting
- command sequencing that does not require live secret disclosure

That is the preferred pattern.

### 10) Assistants are not the only record of anything important

A chat transcript or assistant session is not the canonical record for:

- continuity procedures
- secret inventory
- key fingerprints
- recovery instructions
- rotation history

Those records must exist in TOOO-controlled documents or protected records.

### 11) Convenience is not a justification for widening exposure

The fact that sharing a live secret would make a conversation easier or faster
is not by itself sufficient justification to share it.

TOOO chooses deliberate human choke points over convenience when the two
conflict.

### 12) Public policy, private runbooks

This public policy defines the boundary.

Detailed mounted-media runbooks and continuity mechanics belong in TOOO's
private operations documentation, not in public chat transcripts or public repo
comments.

---

## Examples of allowed and disallowed patterns

### Allowed patterns

- asking an assistant to draft a redacted Ansible secret-file structure
- asking an assistant to review an encrypted-file layout
- sharing a scrubbed log excerpt to diagnose a failing service
- asking an assistant to draft or refine runbooks and governance docs
- asking an assistant to help write drill documentation **after** the mounted
  offline-media session has been closed or sufficiently redacted

### Disallowed patterns

- pasting the full registrar password, GitHub recovery codes, and mail-admin
  creds into one conversation
- keeping a shell assistant open in a long-running session with an unlocked GPG
  agent and broad directory access for unrelated exploratory work
- asking an assistant to bulk export a credential store or secret repo because
  it is “faster”
- treating assistant memory or transcript history as the continuity system
- leaving an assistant session active while offline continuity media is mounted
  and then casually browsing or exporting its live contents

---

## Exceptions

Exceptions are allowed only for:

- incident response
- emergency recovery
- urgent continuity repair
- situations where the human maintainer has concluded that a narrower safe path
  does not exist

Any exception must be:

- deliberate
- narrow
- time-limited
- followed by cleanup and, where necessary, secret rotation

If a live secret was exposed more broadly than intended, rotate it.

---

## Enforcement

During the founder-led phase, the responsible TOOO operator is responsible for
compliance.

Violations require immediate remediation, which may include:

- ending the assistant session
- relocking the agent or credential store
- ejecting and relocking the approved offline recovery medium
- rotating affected secrets
- documenting the exposure and corrective action
- tightening future assistant boundaries

---

## Trigger for Re-evaluation

This policy must be re-evaluated when:

- TOOO adds another human maintainer
- TOOO adopts a self-hosted assistant environment with materially different
  trust boundaries
- TOOO formalizes a human credential-vault product and assistant access model
- TOOO's privileged operations move to a different execution posture

---

## References

- `../decisions/ADR-0012-adopt-gpg-for-early-stage-platform-ops-secret-management.md`
- `../decisions/ADR-0013-adopt-apricorn-aegis-secure-key-3nx-as-offline-platform-recovery-media.md`
- `./PLATFORM_OPS_KEY_AND_SECRET_HANDLING_POLICY.md`
- `./SOLE_MAINTAINER_CONTINUITY_AND_RECOVERY_POLICY.md`
- `./HARDWARE_ENCRYPTED_OFFLINE_RECOVERY_MEDIA_POLICY.md`
- `../governance/VALUES.md`
- `../governance/FOUNDER_STEWARDSHIP.md`
