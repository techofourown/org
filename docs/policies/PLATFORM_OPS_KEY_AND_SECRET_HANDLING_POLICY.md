# Platform Ops Key and Secret Handling Policy
**Draft v1.2**

## Purpose

This policy defines the enforceable rules for how TOOO handles keys and secrets
for public-platform operations during the current early stage.

It exists to prevent:

- plaintext sprawl
- accidental dependence on one laptop or one memory
- secret handling that fights the repo-driven workflow
- casual widening of blast radius during AI-assisted operations
- continuity material existing only as an idea instead of in deliberate,
  protected custody

This policy is written for the current founder-led public-platform phase:
a small operations surface, possible use of AI assistants, and a growing set of
public-platform services.

---

## Scope

This policy applies to TOOO-operated public-platform operations, including at
minimum:

- `accounts.techofourown.com`
- `forum.techofourown.com`
- future public-platform services operated under the `techofourown.com` family
- service operations repos such as:
  - `ops-platform-keycloak-private`
  - `ops-platform-discourse-private`

This policy applies to three classes of sensitive material:

1. **System / repo secrets**
2. **Operator-memory secrets**
3. **Continuity / break-glass material**

This policy does **not** decide:

- end-user application secret handling
- product-local secret handling inside OurBox or other local-first products
- the long-term final product choice for a human credential vault

---

## Definitions

### System / repo secret

Machine-readable secret material used by services, deploy tooling, or
configuration workflows.

Examples:

- database passwords
- SMTP credentials
- service secret keys
- OIDC client secrets
- deploy-time environment files
- Ansible secret values

### Operator-memory secret

Human-retrieved secret material or sensitive admin context.

Examples:

- hosting account logins
- registrar passwords
- recovery codes
- TOTP seeds
- console URLs
- provider notes

### Continuity / break-glass material

Sensitive material needed to restore, recover, or hand off control.

Examples:

- recovery-key material
- encrypted backup of the working key
- continuity packet
- restore instructions

### Trusted maintainer machine

A machine explicitly designated for TOOO platform operations and protected by
normal host-security controls.

### Approved offline recovery medium

The hardware-encrypted removable medium approved for current continuity custody
by `ADR-0013`.

### AI assistant

A software assistant used to help with planning, shell execution, authoring, or
analysis. AI assistants are tools, not accountable maintainers.

---

## Policy

### 1) Classification before storage

Every new sensitive item must be classified before it is stored.

The required classes are:

- system / repo secret
- operator-memory secret
- continuity / break-glass material

Do not allow a secret to “just land somewhere” without an explicit class.

### 2) Canonical substrate for system / repo secrets

System / repo secrets must use the canonical substrate established by
`ADR-0012`:

- **GPG-encrypted files**

These files must be encrypted to:

- the active TOOO operator key, and
- the TOOO recovery key

### 3) Plaintext in Git is prohibited

Plaintext secrets must not be committed to Git.

This prohibition includes, at minimum:

- config files
- `.env` files
- example files that contain live secrets
- inventory files
- markdown notes
- issue text
- PR descriptions
- commit messages

### 4) Repo storage is limited to repos whose purpose warrants it

Encrypted secret files may be committed only in repositories whose purpose
includes managing the relevant service or deployment posture.

Do not use unrelated repos as general secret dumping grounds.

### 5) Small boundaries are required

Secret material must be split along real boundaries where practical.

Prefer:

- one file per service
- one file per credential set
- one file per environment boundary

Avoid giant encrypted catch-all files unless there is a clear operational reason
not to.

### 6) Operator-memory secrets stay out of Git

Operator-memory secrets must not be stored in Git, even when encrypted, unless a
later explicit decision defines an exception.

Until TOOO formally standardizes a human-oriented credential-vault product,
operator-memory secrets must be stored only in an **encrypted local credential
store** under TOOO-controlled operator custody.

Minimum requirements for that store are:

- encrypted at rest
- protected by a strong unlock factor
- backed up according to the continuity policy
- not automatically exported into chat, issue trackers, or shell history

### 7) Continuity material must exist in protected offline custody

Continuity / break-glass material must not be stored only on the daily
workstation.

At minimum, TOOO's continuity posture must include:

- protected offline continuity custody separate from the daily workstation, and
- recoverable records sufficient to restore operational control

The exact copy strategy, bundle composition, storage arrangement, and drill
routine belong in private TOOO operations documentation rather than in this
public policy.

### 8) Approved offline recovery media is not a plaintext exception

The existence of approved offline recovery media does **not** create an
exception that allows plaintext secrets to be copied casually onto removable
media.

Artifacts written to the approved medium must remain protected at the file level
as appropriate.

### 9) Trusted execution contexts only

Decryption and live-secret handling may occur only on:

- trusted maintainer machines, or
- explicitly approved future TOOO-controlled execution contexts

GitHub-hosted CI is not the normal live decryption path for production platform
secrets.

### 10) Secret material must not be sprayed into routine text surfaces

The following are prohibited places for live secrets:

- chat transcripts
- pull-request discussion
- issue comments
- pasted debugging logs
- screenshots shared casually
- shell history where avoidable

### 11) Rotation is mandatory on suspected exposure

Any secret must be rotated when exposure is suspected.

Triggers include:

- accidental plaintext commit
- assistant or automation session received more secret access than intended
- copied secret into an uncontrolled text surface
- lost or compromised trusted maintainer machine
- suspected compromise or suspicious handling of recovery media
- suspected theft or leakage of key material

### 12) Key inventory is required

TOOO must maintain a minimal key inventory covering:

- operator-key fingerprint
- recovery-key fingerprint
- creation / rotation dates
- what each key is for

The inventory may be kept in the continuity packet or an equivalent protected
record, but it must exist and be recoverable.

### 13) AI assistant role in secret workflows

AI assistants may help near secret workflows, including during recovery and
incident-response scenarios where the operator needs assistance.

They are not secret custodians, cryptographic recipients, or approval actors.
Key rotation or revocation always requires explicit human authorization.

Guidelines for AI assistant behavior near secrets are defined in:

- `AI_ASSISTED_OPERATIONS_AND_SECRET_EXPOSURE_POLICY.md`

### 14) Public posture, private mechanics

This public policy records **requirements and boundaries**.

The following belong in TOOO-controlled private operations documentation, not in
this repository:

- exact continuity-bundle contents
- exact device hardening values
- exact storage arrangements
- exact drill checklists and cadence
- break-glass procedures

---

## Exceptions

Exceptions are allowed only to remediate:

- incident response
- recovery failure
- urgent continuity risk
- a demonstrable tooling failure that blocks safe handling

Any exception must be:

- deliberately chosen by the responsible TOOO operator
- time-limited
- documented in a protected continuity record
- followed by corrective action

An exception must not normalize plaintext-in-Git or hosted-secrets-as-authority
as a standing operating model.

---

## Enforcement

During the current phase, the responsible TOOO operator is responsible for
compliance.

Violations require immediate remediation, which may include:

- secret rotation
- Git history cleanup where appropriate
- re-encryption to a corrected recipient set
- machine rebuild or key replacement
- recovery-media refresh or replacement
- tightening assistant or automation boundaries

---

## Trigger for Re-evaluation

This policy must be re-evaluated when any of the following become true:

- a second human maintainer receives routine platform-ops access
- TOOO standardizes a human-oriented credential-vault product
- TOOO adopts a TOOO-controlled privileged deploy environment that changes the
  decryption model materially
- TOOO's public-platform service surface expands enough that the current
  boundaries no longer pay their way

---

## References

- `../decisions/ADR-0012-adopt-gpg-for-early-stage-platform-ops-secret-management.md`
- `../decisions/ADR-0013-adopt-apricorn-aegis-secure-key-3nx-as-offline-platform-recovery-media.md`
- `../rfcs/RFC-0003-early-stage-key-and-secret-management-for-public-platform-ops.md`
- `./SOLE_MAINTAINER_CONTINUITY_AND_RECOVERY_POLICY.md`
- `./HARDWARE_ENCRYPTED_OFFLINE_RECOVERY_MEDIA_POLICY.md`
- `./AI_ASSISTED_OPERATIONS_AND_SECRET_EXPOSURE_POLICY.md`
- `../governance/VALUES.md`
- `../governance/FOUNDER_STEWARDSHIP.md`
