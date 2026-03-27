# RFC-0003: Early-Stage Key and Secret Management for TOOO Public-Platform Operations

- **Created:** 2026-03-26
- **Updated:** 2026-03-27

---

## Status Note

This RFC remains the exploration record for the early-stage public-platform key
and secret problem.

Since its initial drafting, TOOO has now adopted:

- `ADR-0012` — GPG as the canonical substrate for repo-managed machine-readable
  platform-ops secrets
- `ADR-0013` — Apricorn Aegis Secure Key 3NX as the approved
  hardware-encrypted offline recovery medium for current continuity work

This RFC is therefore not the live decision by itself. It remains the reasoning
record behind those decisions and still frames the follow-up questions that
remain open.

This RFC is intentionally public-facing. Exact continuity-bundle composition,
device hardening values, storage arrangements, drill cadence, and break-glass
procedures belong in TOOO-controlled private operations documentation rather
than in this RFC.

---

## What

This RFC explores how Tech of Our Own should handle **keys and secrets** for
its early public-platform operations.

The immediate scope is the emerging public-platform operations layer around:

- `accounts.techofourown.com` (Keycloak)
- `forum.techofourown.com` (Discourse)
- future course, billing, donation, storefront, and member-facing surfaces
- service-specific operations repos such as:
  - `ops-platform-keycloak`
  - `ops-platform-discourse`

This work is happening during a very specific organizational stage:

- TOOO currently has an early founder-led public-platform posture
- AI assistants may be used in shell-heavy and documentation-heavy workflows
- TOOO expects more human maintainers later, but is not there yet
- the public platform is growing before a large formal platform/security team
  exists

That creates a narrow but urgent problem.

TOOO needs a key and secret strategy that:

- prevents plaintext sprawl
- works cleanly with Git and Ansible-oriented service operations
- remains usable in a CLI-first workflow
- does not depend on a closed or hosted secret-management service
- leaves room for future additional human maintainers
- preserves strong human control even when AI assistants are involved in
  day-to-day workflows

This RFC is about **TOOO-operated server and service secrets** for the public
platform.

It is **not** the same problem as:

- end-user account data inside TOOO applications
- product-local identity or local secret handling inside OurBox devices
- final enterprise-scale IAM design for a much larger TOOO

A crucial distinction runs through the whole discussion:

- **system / repo secrets**
  - machine-readable files
  - deploy-time configuration
  - service credentials
  - environment material
  - secrets consumed by tools or services
- **operator-memory secrets**
  - account passwords
  - recovery codes
  - TOTP seeds
  - provider notes
  - console URLs
  - break-glass notes
- **continuity / recovery material**
  - recovery keys
  - emergency instructions
  - service inventory
  - where the critical things live and how to restore them

Those categories overlap a little, but they are not the same job.

---

## Why

TOOO needs a clean answer here now because the wrong default will create mess
quickly.

### Failure mode 1: plaintext drift

Without a deliberate system, secrets spread into:

- shell history
- ad hoc `.env` files
- local notes
- copied snippets in chat
- forgotten directories
- workstation-only state

That is the easiest path, and the worst one.

### Failure mode 2: one giant human vault becomes the source of truth

A human-friendly vault is excellent for operator memory.

It is not a good canonical source for:

- repo-managed machine-readable files
- git-friendly diffs and review
- crisp secret boundaries
- future per-operator recipient control

### Failure mode 3: hosted secrets quietly become the architecture

TOOO may tolerate hosted platforms tactically in the short term, but it should
not center its operational crown jewels on a hosted secret product or on
GitHub-hosted CI secrets.

That would rebuild dependency precisely where TOOO should be most skeptical.

### Failure mode 4: the tooling fights the real operator workflow

The current operating style is strongly:

- terminal-oriented
- repo-oriented
- scriptable
- local-operator-heavy
- free-and-open-source-biased

If the chosen secret system constantly fights that shape, it will be bypassed.

### Failure mode 5: continuity remains hand-wavy

Before `ADR-0013`, the document set acknowledged offline continuity but did not
yet name a concrete medium or operational pattern for it.

That was survivable for exploration, but not durable enough for implementation.

### Failure mode 6: AI assistants erase human choke points by accident

The current operations posture uses AI assistants. That can be a force
multiplier, but it also creates a unique risk:

- once a machine-local GPG agent is unlocked,
- once an offline recovery device is mounted,
- or once a vault is fully open,
- a broad shell-capable assistant session can see or act on more than intended

TOOO therefore needs a system that is both usable and explicit about where the
human choke points remain.

### Why stage matters

This RFC is intentionally about **the present stage of the org**.

TOOO is not yet a large multi-team institution with a dedicated security staff,
formal key ceremonies, and a mature privileged-build platform. The right answer
for a founder-led phase is not necessarily the same as the right answer ten
years later.

TOOO therefore needs a choice that is:

- strong enough to stop bad habits now
- simple enough to actually use
- open enough to fit TOOO's values
- staged enough to evolve later without rewriting the whole story

---

## How (Evaluation Frame)

## First principle: separate system secrets from operator memory

Before comparing tools, TOOO should explicitly separate three jobs.

### Job A: protect system / repo secret material

Examples:

- database passwords
- SMTP credentials
- application secret keys
- OIDC client secrets
- structured Ansible secret files
- deploy-time environment files

These are the secrets that most naturally belong near the service-control-plane
repos.

### Job B: protect operator-memory material

Examples:

- Hetzner login
- registrar login
- GitHub recovery codes
- TOTP seeds
- support notes
- weird provider instructions
- human-admin passwords that are retrieved, not templated

These are the secrets that most naturally belong in a human-oriented encrypted
credential store, not as repo truth.

### Job C: protect continuity / break-glass material

Examples:

- offline recovery key material
- encrypted backup of the working operator key
- continuity packet
- restore instructions
- service inventory and emergency sequence docs

This material must survive laptop loss, founder unavailability, and future
handoff.

---

## Candidate Options

### Option A: KeePassXC as the primary authoritative secret system

#### Shape

Use an encrypted vault as the main place where TOOO stores both human
credentials and service secrets.

#### Pros

- excellent for passwords, notes, TOTP, and recovery codes
- easier to understand under fatigue
- better searchable operator memory than raw crypto files
- stronger default human gating than shell-native crypto tooling

#### Cons

- poor Git / repo ergonomics
- coarse access boundary once the vault is unlocked
- weak fit for machine-readable deploy files
- sharing scales more like “shared unlock world” than per-file recipient control
- not the best canonical source for service repos

#### Fit assessment

Strong for **operator-memory secrets**.

Weak as the canonical source for **repo-managed system secrets**.

### Option B: raw GPG-encrypted files as the canonical secret substrate

#### Shape

Use GPG as the crypto layer and store secrets as encrypted files, encrypted to
one or more operator recipient keys.

Examples:

- `secrets/prod/postgres.env.gpg`
- `secrets/prod/smtp.env.gpg`
- `ansible/inventories/production/group_vars/all/secrets.yml.gpg`

#### Pros

- excellent CLI fit
- strong Git / repo fit
- natural per-recipient model
- free and open source
- portable across repos and future code-host migration
- very good fit for Ansible and file-based service operations

#### Cons

- GPG has real operational footguns
- key lifecycle needs discipline
- weak as a searchable human credential cabinet
- an unlocked local agent can widen blast radius during assistant-heavy shell
  sessions
- requires explicit continuity planning so the system does not die with one
  laptop or one person

#### Fit assessment

Strong candidate for **system / repo secrets**.

### Option C: `pass` or a similar GPG-backed CLI password-store layer

#### Shape

Use GPG as the crypto layer but add a more human-friendly CLI secret store on
top.

#### Pros

- keeps GPG as the root primitive
- more humane than raw encrypted blobs for some use cases
- still terminal-native

#### Cons

- adds another abstraction layer
- still better for secret retrieval than for structured repo-managed deploy
  files
- can blur the boundary between operator memory and system truth if used
  carelessly

#### Fit assessment

Interesting companion layer, not the core starting decision.

### Option D: SOPS or another structured-secret wrapper

#### Shape

Use a higher-level tool that encrypts values inside YAML / JSON / env-like files.

#### Pros

- better editing story for some structured files
- can improve ergonomics for YAML-heavy infrastructure

#### Cons

- adds tooling and abstraction early
- can distract from the deeper decision about the crypto substrate
- still does not solve the human operator-memory problem by itself

#### Fit assessment

Plausible later refinement, not required as the first move.

### Option E: Ansible Vault as the primary authoritative system

#### Shape

Use Ansible's vaulting system as the main secret-management answer.

#### Pros

- directly adjacent to Ansible use
- workable for playbook-heavy environments

#### Cons

- narrower than TOOO's full problem
- weaker fit as a broader operator-identity story
- often centers on shared vault passwords or vault-ID workflows rather than
  explicit per-recipient cryptographic identity

#### Fit assessment

Usable, but not the cleanest center of gravity for TOOO's broader posture.

### Option F: hosted secret managers or GitHub-hosted secrets as authority

#### Shape

Store the source of truth for secrets in hosted secret stores, CI-secret
surfaces, or other third-party managed systems.

#### Pros

- easy to start in hosted-CI-centric organizations

#### Cons

- pushes TOOO toward hosted dependency as the architectural center
- weak fit for local operator-driven deploys
- poor long-term portability
- clashes with TOOO's self-hosting and sovereignty posture

#### Fit assessment

Poor fit for TOOO's intended direction.

---

## Trade-Offs Summary

## The decisive split

The strongest pattern is:

- **GPG is strongest for system / repo secrets**
- **a human credential store is strongest for operator memory**
- **a physically separate offline recovery medium is strongest for continuity
  custody**

This is why the real decision is not “which tool does everything.”

It is:

- what is the canonical system for machine-readable operational secrets at this
  stage?
- what remains deliberately outside Git?
- what physical medium gives continuity material a real home?

## Why GPG looked strongest

GPG aligns with the current TOOO shape:

- repo-first
- Ansible-friendly
- local trusted operator workflows
- free and open source preference
- desire for future per-operator cryptographic identity
- desire to avoid hosted dependency becoming the secret architecture

## Why a human credential store still matters later

GPG does not magically become a good place for:

- TOTP seeds
- URLs
- recovery codes
- screenshots
- weird provider notes
- searching under stress

A later human-oriented credential store will probably still pay rent.

The point is simply that it should not be allowed to silently become the
canonical source of truth for repo-managed machine-readable service secrets.

## Why the approved offline medium pays rent now

A named offline continuity medium solves a different but critical problem:

- physically separate custody
- removable offline storage
- restrictive continuity handling
- less dependence on the daily workstation
- a real place for the continuity bundle to live

That is why `ADR-0013` complements `ADR-0012` instead of competing with it.

## AI-assistant trade-off

GPG is very good for automation and shell-native work.

That is both a strength and a risk.

If the responsible operator unlocks a GPG agent, mounts the offline recovery
media, or imports recovery material and then hands a broad shell session to an
assistant, local decryption power can expand beyond deliberate intent.

A human-oriented vault or an unmounted recovery medium has more friction there,
which can sometimes be protective.

This RFC therefore does **not** treat ergonomics alone as the whole question.
The real goal is:

- strong repo posture
- strong human choke points
- explicit continuity
- no illusion that “single maintainer + assistant” is the same as a staffed
  ops team

---

## Provisional Read

The strongest early-stage posture appeared to be — and has now become — the
following:

1. **Use GPG as the canonical substrate for repo-managed machine-readable
   platform-ops secrets**
2. **Keep operator-memory material out of Git**
3. **Choose a named hardware-encrypted offline medium for continuity custody**
4. **Delay the product-level decision on the human credential vault**
5. **Require explicit continuity / recovery material from the start**
6. **Treat AI assistants as powerful tools, not secret custodians**

That remains the cleanest fit for TOOO's current stage.

---

## Open Questions

1. Should TOOO create a fully separate TOOO operations key hierarchy from the
   founder's other personal crypto use on day one?
2. Should hardware tokens be a day-one requirement, a recommendation, or a
   later hardening step?
3. What exact file layout should `ops-platform-keycloak` and
   `ops-platform-discourse` use for encrypted secret material?
4. What minimal encrypted credential-store requirements should apply before
   TOOO formally standardizes a human-oriented vault product?
5. What local workflow rules are needed around:
   - temporary plaintext files
   - shell history
   - editor swap files
   - unlocked GPG agents during assistant sessions?
6. At what point should TOOO formalize multi-human recipient management and
   join/leave key ceremonies?
7. How much of the public-platform ops posture should eventually be moved from
   founder-only continuity into a true TOOO-controlled shared-custody model?

---

## Next Steps

The immediate next steps from this RFC have now effectively become:

1. implement the GPG file layout in the relevant service ops repos
2. initialize the approved offline continuity medium according to policy
3. generate:
   - one day-to-day TOOO operator GPG key
   - one TOOO recovery key
4. define the initial secret layout for:
   - `ops-platform-keycloak`
   - `ops-platform-discourse`
5. establish the first continuity bundle and run the first validation drill
6. revisit the need for a formal human-oriented credential-vault decision later,
   once the operator-memory problem and team size justify it

The exact continuity-bundle shape, media hardening profile, drill routine, and
break-glass path belong in private TOOO operations documentation rather than in
this public RFC.

---

## References

### Internal

- `../governance/VALUES.md`
- `../governance/MISSION.md`
- `../governance/CONSTITUTION.md`
- `../governance/FOUNDER_STEWARDSHIP.md`
- `../decisions/ADR-0009-separate-human-and-machine-email-using-purpose-specific-subdomains.md`
- `../decisions/ADR-0010-adopt-dedicated-public-platform-identity-service.md`
- `../decisions/ADR-0011-adopt-keycloak-as-public-platform-identity-provider.md`
- `../decisions/ADR-0012-adopt-gpg-for-early-stage-platform-ops-secret-management.md`
- `../decisions/ADR-0013-adopt-apricorn-aegis-secure-key-3nx-as-offline-platform-recovery-media.md`

### External

- GnuPG: https://www.gnupg.org/
- KeePassXC: https://keepassxc.org/
- `pass`: https://www.passwordstore.org/
- Mozilla SOPS: https://getsops.io/
- Ansible Vault:
  https://docs.ansible.com/ansible/latest/vault_guide/index.html
