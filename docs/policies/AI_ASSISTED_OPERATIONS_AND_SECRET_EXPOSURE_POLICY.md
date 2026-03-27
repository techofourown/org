# AI-Assisted Operations and Secret Exposure Policy
**Draft v1.3**

## Purpose

This policy defines how TOOO uses AI assistants in platform operations, and how
to keep their role explicit without quietly turning them into secret custodians or
widening secret blast radius beyond deliberate human control.

This policy is written for the current reality:

- a small founder-led operations posture
- meaningful use of AI assistants
- shell-heavy and documentation-heavy workflows
- growing public-platform infrastructure
- a real offline continuity path using approved recovery media

The goal is not to ban AI assistants or to create rules that prevent the human
operator from getting help when it matters most.

The goal is to make the assistant's role explicit, bounded, and understood — while
preserving the human operator's authority to use assistants as they see fit.

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
- mass-decrypting secret files
- mounting and reading approved offline recovery media during live continuity
  work

### Mounted offline recovery session

Any session in which the approved offline recovery medium is unlocked,
inserted, mounted, or being actively refreshed or used for recovery.

---

## Guidelines

### 1) AI assistants are tools, not maintainers

AI assistants are not:

- maintainers
- approvers
- custodians
- continuity actors
- cryptographic principals

A human maintainer remains accountable for all privileged actions.

### 2) Default to redaction and placeholders

When asking an AI assistant for help, the default should be:

- redacted values
- placeholder secrets
- minimal excerpts
- derived descriptions rather than live secret content

Avoid revealing more than the task genuinely requires.

### 3) Use caution with private keys and sensitive cryptographic material

The following should generally be kept out of routine assistant prompts:

- private keys
- armored secret-key exports
- recovery codes
- TOTP seeds
- break-glass credentials

There are legitimate scenarios where the operator needs AI assistance with
cryptographic material — for example, restoring a backup, debugging a failed
key operation, or following a complex recovery procedure. In those cases, the
operator may work with this material in an assistant session.

When doing so, prefer:

- sharing only what the task requires, not the full keyring
- avoiding inclusion of key material in system prompts or persistent storage
- starting a fresh session or ending the current session once key work is
  complete

### 4) Be aware of high-capability contexts

If a local shell-capable assistant is operating in a session where:

- a GPG agent is unlocked
- a credential store is open
- a shell has inherited live secret environment variables

the operator should recognize this as a **high-capability** context.

Good practices in that state:

- keep the session focused on the task at hand
- consider relocking access once the task is complete
- be aware that the assistant has access to material beyond the immediate
  conversation

### 5) Be mindful during mounted offline recovery sessions

When approved offline recovery media is mounted, the operator should be aware
that the assistant has elevated access to sensitive material.

Good practices:

- keep the task focused where possible
- avoid bulk-exporting continuity bundles into the assistant context
- consider whether the assistant needs to interact with the mounted material
  directly, or whether the operator can relay specific items

The AI assistant should never refuse to help solely because recovery media is
mounted. If the operator needs assistance during a recovery or continuity
session — including exploratory work to diagnose a problem — the assistant
should help. The assistant may note the elevated context and ask the operator
to confirm before performing sensitive operations.

### 6) High-risk secret actions require human initiation

High-risk secret actions should not be delegated implicitly to an assistant.

They should involve deliberate human initiation and human review.

Examples include:

- generating or rotating the operator key
- generating or rotating the recovery key
- changing GPG recipient sets
- exporting encrypted backups of key material
- rotating registrar, DNS, or root mail credentials
- mass decrypting or re-encrypting secret inventories
- refreshing or using offline continuity media during real recovery work

**Key rotation always requires explicit human authorization.** An AI assistant
should never autonomously rotate, revoke, or replace cryptographic material.
The human operator always decides when and whether rotation happens. This is
the one firm rule in this policy.

### 7) Assistants may work on encrypted or non-secret representations

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

### 8) Assistants are not the only record of anything important

A chat transcript or assistant session should not be the canonical record for:

- continuity procedures
- secret inventory
- key fingerprints
- recovery instructions
- rotation history

Those records should exist in TOOO-controlled documents or protected records.

### 9) Prefer human touchpoints over silent access

When an AI assistant encounters sensitive material or is about to perform an
action that touches secrets, it should ask the human operator for confirmation
rather than proceeding silently or refusing outright.

The assistant's role is to advise and to surface decisions — not to act as a
gatekeeper or to override the operator's judgment.

### 10) Public policy, private runbooks

This public policy defines the boundary.

Detailed mounted-media runbooks and continuity mechanics belong in TOOO's
private operations documentation, not in public chat transcripts or public repo
comments.

---

## Examples of recommended and discouraged patterns

### Recommended patterns

- asking an assistant to draft a redacted Ansible secret-file structure
- asking an assistant to review an encrypted-file layout
- sharing a log excerpt to diagnose a failing service
- asking an assistant to draft or refine runbooks and governance docs
- asking an assistant to help during a recovery session when the operator
  needs guidance
- working with cryptographic material in a focused session, then starting
  fresh afterward

### Discouraged patterns

- pasting a large collection of unrelated credentials into one conversation
  without a clear operational need
- keeping a shell assistant open in a long-running session with an unlocked
  GPG agent and broad directory access for unrelated exploratory work
- treating assistant memory or transcript history as the continuity system
- allowing an assistant to autonomously rotate or revoke keys without human
  confirmation

---

## Deviations from guidance

These guidelines exist to promote good operational practice. The human
operator may deviate from them when operational need dictates.

When deviating:

- be deliberate about the scope and duration
- consider whether a fresh session is warranted afterward
- if secret material was exposed more broadly than intended, consider whether
  rotation is warranted — but rotation is always the human's decision, not
  an automatic response

---

## Human responsibility and AI behavior on deviations

During the founder-led phase, the human TOOO operator is responsible for
following these guidelines and for the consequences of deviating from them.

When an AI assistant recognizes that a session has deviated from these
guidelines, the expected behavior is:

- **inform the human** — surface the concern clearly
- **ask for confirmation** before continuing with the sensitive action
- **proceed per human direction** — the operator decides

An AI assistant should never:

- autonomously rotate, revoke, or replace cryptographic material
- unilaterally end a session or refuse to help
- take autonomous corrective action without human approval

If an autonomous or long-running agent session encounters a guideline
deviation and does not have pre-authorization for the specific action, it
should pause and wait for human input.

---

## Trigger for re-evaluation

This policy should be re-evaluated when:

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
