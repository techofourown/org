# ADR-0010: Adopt a Dedicated Public-Platform Identity Service Separate from App-Local and Device-Local Identity

- **Date:** 2026-03-26
- **Related:**
  - `../governance/VALUES.md`
  - `../governance/MISSION.md`
  - `../governance/CONSTITUTION.md`
  - `./ADR-0009-separate-human-and-machine-email-using-purpose-specific-subdomains.md`
  - `../rfcs/RFC-0002-public-platform-identity-provider-options.md`

---

## Context

Tech of Our Own is beginning to accumulate multiple TOOO-operated internet
surfaces that either already require accounts or are very likely to require
them soon:

- a Discourse forum
- public-site commenting flows backed by the forum
- future course or school surfaces
- future storefront and order-history surfaces
- future donation history and receipts access
- future member or governance-adjacent web surfaces
- future account-security and profile-management flows

These are all part of the **public TOOO platform**: internet services operated
by TOOO under the `techofourown.com` domain family.

A naive approach would let the first major application become the root identity
system. In practice, that would likely mean treating Discourse as the canonical
account database and asking every later service to route identity through the
forum.

That is the wrong center of gravity.

A forum account is shaped around forum concepts:

- public handle and profile
- moderation state
- trust level / reputation
- discussion and notification preferences

Those are appropriate for community discussion. They are not the right root
model for the broader TOOO platform, where one person may want to:

- buy something without joining the forum
- take a course without adopting a public discussion persona
- donate without becoming a community participant
- maintain one private account identity while using different app-local names
  or profiles

At the same time, TOOO must keep a second boundary equally clear:

- **public-platform identity** for TOOO-operated web services
- **device-local / product-local identity** for user-owned systems such as
  OurBox

Those are not the same problem.

The eventual identity system inside an OurBox device or an OurBox-hosted
household service may need very different properties, including some
combination of:

- offline-first operation
- local-network-first operation
- household or peer-hosted administration
- optional federation rather than mandatory central accounts
- no dependency on a TOOO-operated service for normal local use

Because TOOO's values explicitly reject lock-in, surveillance, and mandatory
accounts for local use of user-owned hardware, the existence of a TOOO
public-platform account system must not become a backdoor requirement for using
OurBox or any future local-first product.

This ADR is therefore an **architecture decision**, not a product-selection
decision. It decides that the public platform needs a dedicated identity
service, but it does **not** yet decide which software TOOO will use to
implement it.

---

## Decision

Tech of Our Own will adopt a **dedicated public-platform identity service** for
TOOO-operated web properties.

Concretely:

1. **TOOO-operated internet services that require accounts will rely on a
   dedicated identity service rather than treating any single application as
   the root account system.**

2. The canonical home for this service is:

   - **`accounts.techofourown.com`**

3. Applications such as the forum, school, storefront, donation portal, and
   future member-facing web services are treated as **relying parties /
   clients** of that identity service.

4. No single product application, including Discourse, is the canonical root
   identity system for the broader TOOO platform.

5. The dedicated identity service is the source of truth for the **minimal
   common identity core**, including at minimum:

   - a stable internal subject identifier
   - verified contact methods as needed
   - authentication factors and security state
   - account lifecycle state
   - platform-level security events and audit-relevant account changes

6. Individual applications remain the source of truth for their own
   **app-local state**, including examples such as:

   - forum profile, handle, trust level, moderation state
   - course enrollment and progress
   - order history and fulfillment state
   - donation history
   - future member-community or governance-local attributes

7. Cross-application linkage must use a **stable platform subject
   identifier**, not email address as the canonical join key.

8. The dedicated public-platform identity service must be implemented using
   **standards-based federation and login protocols**. At minimum, the
   selected implementation must support:

   - OpenID Connect / OAuth 2.0 for application login

   Desirable but not strictly required on day one:

   - SAML for future compatibility where justified
   - directory / provisioning integrations where justified

9. The selected implementation must support modern, user-protective
   authentication controls, including at minimum:

   - phishing-resistant authentication options such as passkeys / WebAuthn
   - MFA support
   - sane recovery and account-security workflows
   - auditable administrative actions

10. The identity service must be deployable in an **organization-controlled**
    manner and must not require TOOO to hand root account authority to a
    third-party SaaS provider.

11. This ADR applies to the **public TOOO platform only**. It does **not**
    decide identity architecture for:

    - OurBox device-local login
    - household or community-hosted product identity
    - peer-hosted or federated identity inside TOOO products
    - offline/local service authentication on user-owned systems

12. Public-platform accounts must not become a universal requirement for all
    interactions. Account-free or guest flows may still be used where they are
    the better privacy- and adoption-aligned choice.

    Examples that may remain guest-capable where practical:

    - donations
    - purchases / checkout
    - reading public content

13. Account-related transactional mail for the public platform should align
    with ADR-0009, using the `accounts.techofourown.com` rail for
    verification, password-reset, magic-link, and security mail.

14. The question of **which identity provider** TOOO should choose is deferred
    to:

    - `../rfcs/RFC-0002-public-platform-identity-provider-options.md`
    - a later follow-up ADR that records the actual software choice

---

## Scope

This ADR applies to TOOO-operated public internet services and web properties
that need account identity under the TOOO domain family.

This includes:

- public platform login and SSO
- cross-app account identity between TOOO-operated web apps
- central account security and recovery
- platform account lifecycle and subject identifiers
- the architectural boundary between shared identity and app-local state

This ADR does **not** apply to:

- local identity inside OurBox or future TOOO products
- product-local admin and household accounts
- identity federation inside user-owned deployments
- licensing posture for identity software
- specific implementation details such as deployment manifests, backup methods,
  database choice, or secret-management tooling

Those belong in the implementation repo(s), ops documentation, or follow-up
ADRs.

---

## Rationale

### 1) Identity and application state are different concerns

A dedicated identity service allows TOOO to keep a small shared identity core
while leaving application-specific meaning inside each application.

That prevents the forum from becoming the accidental root model for every later
service.

### 2) The public platform needs one account system, not one account per app

A person should be able to have a single TOOO platform identity that can be
reused across multiple TOOO-operated web services without requiring separate
credentials or fragmented account recovery.

That is the right shape for a growing public platform.

### 3) Discourse should be part of the house, not the foundation of the house

Discourse is a community application. It is not the right place to anchor all
future account identity, commerce, education, and membership-adjacent
relationships.

Treating it as a relying party keeps the architecture clean.

### 4) Public-platform identity must not leak into product-local identity

TOOO's values are explicit:

- local-first
- no lock-in
- no mandatory account to use your own hardware
- hosted services remain optional and exit-friendly

If a TOOO public-platform account became the root identity for OurBox itself,
TOOO would be laying track toward the very dependency it claims to reject.

This ADR blocks that architectural drift early.

### 5) Standards and self-hostability preserve exit

The point of a dedicated identity service is not to create a new central choke
point. It is to make identity legible, portable, and controllable.

That requires:

- organization-controlled deployment
- standards-based application integration
- a future migration path that does not require rewriting every app

### 6) Security needs to be first-class from the beginning

Authentication, recovery, and account lifecycle are some of the easiest places
to create silent, catastrophic weakness.

TOOO should not stumble into that surface casually. The architecture should
assume from the start that the identity tier is a security-critical part of the
platform.

---

## Consequences

### Positive

- TOOO gets a clean architectural center for cross-app public-platform
  accounts.
- Discourse can be integrated without becoming the root identity database.
- Future school, store, and member-facing surfaces can share login without
  sharing app-local state.
- The architecture remains compatible with TOOO's local-first, anti-lock-in
  values.
- The later software-selection decision can be made against clear
  architectural requirements.

### Negative / Tradeoffs

- TOOO now has a distinct platform service category to operate and secure.
- Some implementation complexity moves forward in time instead of being
  postponed.
- There is a new conceptual boundary maintainers must respect: shared identity
  vs app-local state.
- Public-platform identity and device-local identity will need separate
  treatment, which increases architectural surface area.

### Mitigation

- Keep the shared identity core intentionally small.
- Treat application-local profiles and business data as local to each app.
- Choose standards-based integration rather than app-specific coupling.
- Keep the public-platform / device-local boundary explicit in later product
  ADRs.
- Use the upcoming RFC to compare concrete implementation options before
  committing.

---

## Options Considered

### Option A: Let Discourse become the root account system

- Rejected.
- It couples the broader TOOO platform to a community application and lets
  forum assumptions leak into non-forum services.

### Option B: Build every app with its own local login system

- Rejected.
- It creates fragmented identity, inconsistent security posture, poor UX, and
  weakens the later ability to add coherent SSO.

### Option C: Adopt a dedicated public-platform identity service and treat apps as relying parties

- Accepted.
- This creates the right architectural center while keeping apps and future
  products decoupled.

### Option D: Use the same architecture for the public platform and for OurBox device-local identity

- Rejected.
- These two domains have materially different requirements. Conflating them
  would undermine TOOO's local-first and anti-lock-in commitments.

---

## Implementation Notes

### 1) Canonical domain

The intended canonical domain is:

- `accounts.techofourown.com`

This aligns with the account/security mail rail already reserved in ADR-0009.

### 2) Central identity data should stay minimal

Good examples of central identity data:

- stable subject ID
- verified email state
- MFA / passkey enrollment state
- recovery state
- platform-level admin / disabled flags

Bad examples of central identity data:

- forum trust level
- course progress
- order totals
- donation history
- app-specific public handles when they only matter inside one app

### 3) Subject ID is the durable join key

Applications should key local account records to the dedicated identity
service's stable subject ID. Email can change; the subject identifier should
not.

### 4) Not every flow requires an account

This ADR authorizes a dedicated identity service. It does not require TOOO to
force accounts onto all public interactions.

### 5) Standards posture

The eventual implementation should be chosen with a strong bias toward:

- OpenID Connect for app login
- modern MFA and passkeys
- exportability and future migration
- organization-controlled deployment

### 6) Follow-up work

Expected follow-up work:

- RFC evaluating concrete identity-provider options
- later ADR selecting the implementation
- implementation repo and ops runbooks
- application integration ADRs where needed (forum, school, store, etc.)

---

## References

### Internal

- `../governance/VALUES.md`
- `../governance/MISSION.md`
- `../governance/CONSTITUTION.md`
- `./ADR-0009-separate-human-and-machine-email-using-purpose-specific-subdomains.md`
- `../rfcs/RFC-0002-public-platform-identity-provider-options.md`

### External

- OWASP Authentication Cheat Sheet:
  https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- NIST SP 800-63B: https://pages.nist.gov/800-63-4/sp800-63b.html
- NIST SP 800-63B Authenticator guidance:
  https://pages.nist.gov/800-63-4/sp800-63b/authenticators/
