# ADR-0012: Adopt GPG for Early-Stage Platform-Ops Secret Management

- **Date:** 2026-03-26
- **Updated:** 2026-03-27
- **Related:**
  - `../governance/VALUES.md`
  - `../governance/MISSION.md`
  - `../governance/CONSTITUTION.md`
  - `../governance/FOUNDER_STEWARDSHIP.md`
  - `./ADR-0009-separate-human-and-machine-email-using-purpose-specific-subdomains.md`
  - `./ADR-0010-adopt-dedicated-public-platform-identity-service.md`
  - `./ADR-0011-adopt-keycloak-as-public-platform-identity-provider.md`
  - `./ADR-0013-adopt-apricorn-aegis-secure-key-3nx-as-offline-platform-recovery-media.md`
  - `../rfcs/RFC-0003-early-stage-key-and-secret-management-for-public-platform-ops.md`

---

## Context

Tech of Our Own is beginning to operate multiple TOOO-hosted public-platform
services under the `techofourown.com` domain family, including:

- the forum at `forum.techofourown.com`
- the public-platform identity rail at `accounts.techofourown.com`
- future course, billing, donation, storefront, and member-facing web surfaces

TOOO is also moving toward **service-specific operations repositories** for
those systems, with Ansible-oriented and repo-driven workflows expected for the
service control plane.

This work is happening during a very specific stage:

- TOOO is in an early founder-led public-platform phase
- AI assistants may be used in shell-heavy and documentation-heavy workflows
- additional human operators are expected later, but the day-to-day posture is
  still intentionally simple

That creates a practical secret-management problem now.

TOOO needs a canonical answer for:

- deploy-time credentials
- service keys
- machine-readable secret files
- future per-operator access
- continuity and recovery
- strong human control even while AI assistants may help with nearby work

A key distinction matters.

TOOO does **not** need one tool to solve every secret problem forever.

It needs a canonical answer for **repo-managed, machine-readable operational
secrets** now.

That is a different job from storing long-tail human operator-memory material
such as:

- account passwords
- recovery codes
- TOTP seeds
- provider notes
- console URLs
- screenshots and attachments

This ADR is therefore deliberately scoped.

It decides the canonical substrate for **early-stage platform-ops secrets**.

It does **not** decide the final long-term human credential-vault product for
all operator-memory material.

A second related distinction now also matters.

TOOO has separately chosen a hardware-encrypted offline recovery medium for the
current phase in `ADR-0013`. That medium improves physical separation and
continuity custody, but it is **not** the canonical cryptographic substrate for
machine-readable repo secrets. GPG remains that substrate.

This document is intentionally public-facing. Detailed continuity-bundle
composition, media configuration, drill cadence, storage arrangements, and
break-glass procedures are maintained in TOOO-controlled private operations
documentation rather than in this repository.

---

## Decision

Tech of Our Own will use **GPG** as the canonical cryptographic substrate for
**early-stage platform-ops secret management**.

More specifically:

1. **Repo-managed machine-readable secrets** for TOOO-operated public-platform
   services will be stored as **GPG-encrypted files**.

2. Access will be based on **recipient keys**, not on a single shared vault
   password.

3. TOOO will maintain at minimum:
   - one day-to-day **TOOO operator GPG key**
   - one separate **TOOO recovery key** for continuity

4. Repo-managed secret files should be encrypted to:
   - the current day-to-day TOOO operator key, and
   - the TOOO recovery key

5. **Plaintext secrets must never be committed to Git.**
   Encrypted secret material may be committed only in repos whose purpose
   includes managing the relevant live service or its deployment posture.

6. TOOO will prefer **small encrypted files aligned to real secret
   boundaries**, not one monolithic encrypted blob as the canonical source of
   service configuration.

7. This ADR applies to **system / repo secrets** only.
   It does **not** make a human credential vault the canonical source of truth
   for repo-managed platform secrets.

8. Until a later follow-up decision standardizes a human-oriented credential
   vault, **operator-memory secrets** must remain:
   - outside Git,
   - encrypted at rest,
   - under TOOO-controlled operator custody,
   - and separate from the canonical repo-secret substrate

9. The offline recovery media selected in `ADR-0013` is a **continuity and
   custody layer**, not the authoritative repo-secret substrate.
   Content placed on that medium must still remain protected at the file level
   as appropriate.

10. **AI assistants are not cryptographic principals.**
    They do not receive independent standing as recipients, custodians, or
    approvers.

11. Decryption for production use will occur only on:
    - trusted operator machines, or
    - future TOOO-controlled execution contexts explicitly approved for that
      purpose

    It will **not** depend on GitHub-hosted CI as the normal decryption path
    for production platform secrets.

12. When TOOO gains additional human maintainers, each human maintainer must
    receive their **own key**, and recipient sets must be expanded and
    re-encrypted accordingly. Shared-human-password-only identity is not the
    target model.

13. This ADR does **not** decide:
    - end-user secret handling inside TOOO applications
    - product-local secret handling inside OurBox or other local-first TOOO
      products
    - the final product choice for a human-oriented credential store
    - a blanket org-wide signing policy for all repos
    - a final enterprise-scale HSM or hardware-token posture

---

## Rationale

### 1) GPG fits the actual current workflow

TOOO's present operating style is:

- terminal-heavy
- repo-heavy
- scriptable
- self-hosting-oriented
- skeptical of hosted dependency
- likely to use Ansible and file-based service operations

GPG fits that shape directly.

### 2) GPG gives TOOO a future per-operator identity model

This is the deepest architectural advantage.

With recipient-based encryption:

- another human operator can be added later without redesigning everything
- one operator can be removed by changing the recipient set
- TOOO avoids centering service repos on a single shared vault password

That matters even during an early founder-led phase, because TOOO should not
design itself into a one-person corner.

### 3) GPG is a better fit for repo-managed system secrets than a vault-first model

TOOO is about to operate service repos such as:

- `ops-platform-keycloak-private`
- `ops-platform-discourse-private`

Those repos need a secret system that works well with:

- Git
- machine-readable files
- small secret boundaries
- repeatable deploy workflows
- future additional recipients

A file-based encrypted workflow fits that shape better than a monolithic human
vault.

### 4) This preserves open, portable, non-hosted control

TOOO's values reject lock-in and silent dependence.

A hosted secret-manager-first architecture, or a GitHub-secrets-first
architecture, would move too much privileged control into infrastructure TOOO
does not own.

GPG is free, open source, portable, and not tied to a hosted vendor.

### 5) The offline recovery medium solves a different layer of the problem

The offline recovery medium selected in `ADR-0013` solves:

- physical separation from the daily workstation
- offline custody
- deliberate recovery handling
- low-friction removable-media encryption for continuity artifacts

It does **not** replace:

- per-recipient cryptographic identity
- repo-managed encrypted files
- GPG key hierarchy and rotation discipline

Keeping those roles separate makes the system easier to reason about.

### 6) The decision leaves room for a later human-oriented credential store

KeePassXC or another encrypted credential store may still become useful later
for:

- TOTP
- recovery codes
- provider notes
- URLs
- screenshots and attachments
- operator memory under fatigue

That is real.

But it is not a good reason to make a human vault the canonical source of
repo-managed machine-readable deploy secrets today.

### 7) The AI-assistant reality argues for explicit human choke points

Because AI assistants may help in shell-heavy workflows, TOOO needs explicit
boundaries around:

- unlocked GPG agents
- mounted continuity media
- secret export
- recovery material
- ambient broad access during local assistant sessions

A GPG-based system can work well here, but only if those boundaries are made
explicit in policy. This ADR chooses the substrate; companion policies provide
the day-to-day guardrails.

---

## Consequences

### Positive

- TOOO gets a secret substrate that fits repo-driven operations.
- Future per-human cryptographic access becomes natural.
- TOOO avoids making a hosted secret service the center of its privileged
  operations.
- The chosen system is free and open source.
- The chosen system layers cleanly with the approved hardware-encrypted offline
  recovery medium.
- The decision leaves clean room for a later human credential-vault layer
  without confusing the system-secret story.

### Negative / Tradeoffs

- GPG has real operational sharp edges.
- Key backup and restore discipline become mandatory.
- GPG is poor as a searchable human credential cabinet.
- An unlocked local agent can widen blast radius if the operator is sloppy,
  especially during assistant-heavy shell sessions.
- A founder-led phase still requires explicit continuity work so the setup does
  not die with one laptop or one person.

### Mitigation

- use dedicated TOOO operator and recovery keys
- keep a documented fingerprint inventory and continuity packet
- use approved offline recovery media for separated continuity custody
- prefer small logical secret files over one giant encrypted blob
- keep operator-memory material separate and encrypted
- adopt explicit policies for continuity and AI-assisted secret handling
- re-evaluate the posture when a second human maintainer joins

---

## Implementation Notes

### 1) Minimum starting key set

TOOO should begin with at least:

- one day-to-day TOOO operator GPG key
- one TOOO recovery key

### 2) Secret file shape

Prefer one encrypted file per real boundary, for example:

- database credentials
- SMTP credentials
- service app secrets
- OIDC client secrets
- one environment file per service

Avoid giant encrypted “everything” files where possible.

### 3) Repo policy

No repo may commit plaintext secrets.

A repo may commit encrypted secret material only when:

- the repo's job includes managing the live service, and
- doing so improves repeatability, continuity, and operator clarity

### 4) Continuity layering

Continuity records and key backups may be copied onto approved offline recovery
media, but those artifacts must remain cryptographically protected at the file
level as appropriate.

The offline medium is a continuity and custody layer, not the sole source of
truth for secrecy.

### 5) CI policy

GitHub-hosted CI may validate:

- file presence
- non-secret structure
- linting and syntax

GitHub-hosted CI should not be the normal decryption path for production
platform secrets.

### 6) Human credential-store posture remains a follow-up decision

This ADR intentionally leaves open which product TOOO will use for
operator-memory material.

The only requirement right now is that operator-memory material remain:

- outside Git
- encrypted at rest
- under TOOO-controlled custody
- clearly separate from the canonical repo-secret substrate

### 7) Private operational detail lives elsewhere

Exact continuity-bundle composition, device configuration, drill cadence,
storage arrangements, and break-glass procedures belong in TOOO-controlled
private operations documentation rather than in this public governance repo.

---

## Future Changes

The following do **not** require superseding this ADR so long as GPG remains the
canonical repo-secret substrate:

- adding helper scripts or wrapper commands around GPG
- adding a human-oriented credential store alongside GPG
- tightening backup or hardware-token policy
- moving decryption from local operator machines to TOOO-controlled execution
  infrastructure
- changing the exact continuity-bundle layout in private operational docs

The following **do** require follow-up governance action:

- replacing GPG as the canonical substrate for repo-managed platform secrets
- making a hosted or closed secret service the authoritative center of TOOO
  platform operations
- collapsing back to shared-human-password-only identity for repo-managed
  service secrets
- silently expanding this ADR until it pretends to settle all future TOOO key
  and secret questions without further review

---

## References

- `../governance/VALUES.md`
- `../governance/MISSION.md`
- `../governance/CONSTITUTION.md`
- `../governance/FOUNDER_STEWARDSHIP.md`
- `./ADR-0009-separate-human-and-machine-email-using-purpose-specific-subdomains.md`
- `./ADR-0010-adopt-dedicated-public-platform-identity-service.md`
- `./ADR-0011-adopt-keycloak-as-public-platform-identity-provider.md`
- `./ADR-0013-adopt-apricorn-aegis-secure-key-3nx-as-offline-platform-recovery-media.md`
- `../rfcs/RFC-0003-early-stage-key-and-secret-management-for-public-platform-ops.md`
