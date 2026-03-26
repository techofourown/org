# ADR-0011: Adopt Keycloak as the Public-Platform Identity Provider

- **Date:** 2026-03-26
- **Related:**
  - `../governance/VALUES.md`
  - `../governance/MISSION.md`
  - `../governance/CONSTITUTION.md`
  - `./ADR-0009-separate-human-and-machine-email-using-purpose-specific-subdomains.md`
  - `./ADR-0010-adopt-dedicated-public-platform-identity-service.md`
  - `../rfcs/RFC-0002-public-platform-identity-provider-options.md`

---

## Context

ADR-0010 established that Tech of Our Own needs a **dedicated
public-platform identity service** for TOOO-operated web properties, separate
from:

- app-local identity inside any one application such as Discourse
- future device-local or product-local identity inside OurBox and other
  local-first TOOO products

That architecture decision created the boundary. It did **not** choose the
software.

RFC-0002 then evaluated the concrete options for implementing the
public-platform identity service at:

- `accounts.techofourown.com`

That RFC treated several options as serious candidates, including:

- custom build
- authentik
- Keycloak
- ZITADEL
- Ory

Among those, **Keycloak** was identified as a strong candidate because of its
maturity, broad ecosystem, standards support, identity-brokering posture, user
federation capabilities, and modern authentication support.

TOOO now needs to make the implementation decision.

This choice matters because TOOO expects the public platform to grow across
multiple account-bearing surfaces, including:

- Discourse forum login
- future public-site comment flows backed by the forum
- future school / course login
- future storefront / order-history login
- future donation-history access
- future member-facing or governance-adjacent web login

The chosen identity system must therefore do more than solve forum login.

It must support a growing, self-hosted, standards-based public platform while
remaining compatible with TOOO's values:

- privacy by architecture
- no lock-in, including lock-in to us
- organization-controlled infrastructure
- clear separation between hosted platform accounts and user-owned device-local
  identity
- openness to portable and externally anchored identity without surrendering
  canonical TOOO account authority

TOOO also wants the public platform to be able to welcome users who already
anchor identity elsewhere.

That includes, over time, some combination of:

- conventional OpenID Connect / SAML providers
- self-hosted or domain-based identity
- fediverse-adjacent identity patterns
- AT Protocol / Bluesky-linked identity patterns

That does **not** mean outsourcing TOOO's account authority to a third-party
network. It means selecting an identity provider that can keep TOOO's account
model canonical while also supporting federation, brokering, and account
linking where appropriate.

TOOO must now choose the software that best fits that role.

---

## Decision

Tech of Our Own will adopt **Keycloak** as the implementation for the
dedicated public-platform identity service established by ADR-0010.

Concretely:

1. **Keycloak** is the selected identity provider for TOOO-operated public web
   properties.

2. The canonical public-platform identity domain remains:

   - **`accounts.techofourown.com`**

3. Keycloak will be deployed in an **organization-controlled, self-hosted**
   manner.

4. Keycloak becomes the canonical source of truth for the **shared public
   platform identity core**, including at minimum:

   - stable platform subject identifiers
   - authentication and MFA / passkey state
   - recovery and account-security state
   - account lifecycle state
   - platform-level administrative identity controls

5. Applications such as:

   - Discourse
   - future school / course systems
   - future storefront systems
   - future donation-related account systems
   - future member-facing web systems

   will integrate with Keycloak as **clients / relying parties**, rather than
   acting as the root account system themselves.

6. TOOO's canonical account identity remains a **TOOO-controlled internal
   subject** inside the Keycloak-backed identity layer.

7. External identities may be:

   - brokered in
   - linked
   - used for selective federation

   but they do not replace the canonical TOOO platform subject.

8. **Native TOOO sign-in remains a first-class path.** No outside identity
   network is mandatory for access to TOOO's public platform.

9. This ADR applies to the **public TOOO platform only**.

   It does **not** decide the identity architecture for:

   - OurBox device-local identity
   - household / community-hosted identity inside TOOO products
   - future product-local auth that must work offline or without dependence on
     TOOO-operated services

10. Any future use of Keycloak for **internal workforce identity**, physical
    access, or other non-public platform identity domains requires explicit
    follow-up design work and must preserve clear separation from the
    public-platform account boundary.

11. Account-related transactional mail should continue to align with
    ADR-0009, using the `accounts.techofourown.com` mail rail for
    verification, password-reset, magic-link, and security mail.

---

## Rationale

### 1) Keycloak is the strongest fit for TOOO's long-term platform shape

TOOO is not choosing an identity solution for a single web app.

It is choosing the institutional identity backbone for a growing public
platform. That favors:

- maturity
- breadth of standards support
- identity brokering
- stable long-term ecosystem knowledge
- a platform shape that can serve many relying parties over time

Keycloak best fits that trajectory.

### 2) Keycloak fits the dedicated-identity architecture already adopted

ADR-0010 already decided that TOOO needs:

- a dedicated public-platform identity layer
- not Discourse as the root account database
- not one local-login system per app

Keycloak is a natural implementation of that architecture because it is shaped
to be a shared identity authority for multiple applications rather than an
app-local convenience login layer.

### 3) Keycloak supports standards and federation without giving away
canonical authority

TOOO wants to welcome users who already steward identity elsewhere, including
users from open and federated ecosystems.

That means the public-platform identity system needs room for:

- standards-based federation
- identity brokering
- account linking
- future portable-identity integrations

Keycloak is well suited to that posture.

Just as importantly, it allows TOOO to keep a canonical internal account
subject rather than making the platform wholly dependent on any one external
provider or social network.

### 4) Keycloak is a better long-term fit than a custom build

A custom identity stack would maximize product-specific control, but it would
also make TOOO responsible for every difficult part of account security:

- recovery
- MFA
- passkeys
- session handling
- token issuance
- audit surfaces
- administrative escalation paths

That is too much security-critical surface area to take on as a first move
when a strong open-source option already exists.

### 5) Keycloak is a better fit for TOOO's expected scale than lighter-weight
alternatives

Other candidates in RFC-0002 were serious and credible.

But TOOO's expected direction is not "small app SSO forever." It is a growing
institution with multiple public services and potentially many future identity
consumers.

That favors a more mature, institution-scale identity platform over a lighter
or more convenience-oriented choice.

### 6) Keycloak aligns with TOOO's sovereignty and anti-lock-in values

TOOO's values reject platform dependency, silent capture, and lock-in.

Selecting a self-hosted, open-source identity provider on
organization-controlled infrastructure is consistent with that posture.

This keeps TOOO from placing its most sensitive trust surface under a managed
SaaS provider or under an app-local system that would be painful to unwind
later.

---

## Consequences

### Positive

- TOOO gets a real, dedicated public-platform identity backbone.
- Discourse can be integrated immediately without becoming the root account
  system.
- Future school, storefront, donation, and member-facing surfaces can share
  one canonical account system.
- TOOO preserves a native account system while still allowing external
  identity brokering and linking.
- The architecture remains consistent with TOOO's local-first and anti-lock-in
  commitments.
- Keycloak's maturity and ecosystem reduce the risk of TOOO painting itself
  into a corner too early.

### Negative / Tradeoffs

- Keycloak is operationally heavier than some alternatives.
- It introduces a real IAM service category that TOOO must run, secure, back
  up, and understand.
- Its platform shape is more institution-scale than TOOO immediately needs on
  day one.
- Federation and account linking still require careful product design; the
  software choice does not remove that complexity.
- A poor realm / client / attribute model could create confusion if TOOO is
  not disciplined.

### Mitigation

- Start with a narrow first rollout centered on the public platform.
- Keep the shared identity core intentionally small.
- Keep app-local state out of Keycloak.
- Integrate Discourse first, then add later relying parties incrementally.
- Use standards-based integration consistently so later migration remains
  possible if TOOO ever needs it.
- Preserve a strict boundary between public-platform identity and product-local
  identity.

---

## Options Considered

### Option A: Custom-build the identity service

- Rejected.
- Too much security-critical engineering burden for a first implementation.
- Delays real platform work while forcing TOOO to become an identity vendor.

### Option B: authentik

- Not selected.
- authentik remained a serious candidate with a strong self-hosted and modern
  auth story.
- TOOO did not choose it because Keycloak was judged the better fit for the
  expected long-term institutional scale, maturity, and identity-brokering
  posture of the public platform.

### Option C: Keycloak

- Accepted.
- Best fit for TOOO's public-platform identity architecture, expected scale,
  federation posture, and self-hosted sovereignty requirements.

### Option D: ZITADEL

- Not selected.
- ZITADEL remained a serious candidate.
- It was not selected because TOOO preferred Keycloak's maturity and more
  obviously self-hosted institution-scale posture for the first
  implementation.

### Option E: Ory

- Not selected.
- Ory remained attractive as a more composable stack.
- TOOO did not choose it because it would require more assembly and
  architectural burden than needed for the first production identity layer.

### Option F: Managed SaaS identity

- Rejected.
- Weak fit with TOOO's sovereignty and anti-lock-in posture for the canonical
  account system.

### Option G: Let Discourse remain the root account system

- Rejected.
- Already rejected in architecture by ADR-0010.
- A forum is part of the platform, not the root identity authority for the
  platform.

---

## Implementation Notes

### 1) Canonical public identity host

The public-platform identity service should live at:

- `accounts.techofourown.com`

### 2) Start with a dedicated public-platform realm / boundary

The initial rollout should use a dedicated public-platform account boundary.

Do not treat the first Keycloak deployment as a dumping ground for every future
identity concern.

At minimum, public-platform accounts must remain clearly separated from:

- future internal workforce identity
- future physical-access / office identity
- future product-local identity
- future OurBox device-local identity

### 3) Stable subject identifiers are the durable join key

Applications should key local records to Keycloak's stable subject identifier.

Do **not** use email address as the canonical join key across applications.

### 4) Discourse should be the first relying party

The immediate practical rollout should make **Discourse** a client of
Keycloak via standards-based login.

That gives TOOO a real first consumer of the platform identity service without
letting the forum become the platform identity root.

### 5) Keep app-local data out of Keycloak

Keycloak is for shared identity and security state, not for app-local business
state.

Examples that should remain outside Keycloak:

- forum trust levels
- moderation history
- course progress
- order history
- donation history
- app-local public profile state that only matters inside one app

### 6) Federation should roll out in stages

Day one does not need to solve every external identity case.

A sensible staged approach is:

1. native TOOO sign-in
2. generic OpenID Connect federation where justified
3. account linking and brokering for selected external identity sources
4. later verified-link and / or login experiments for fediverse-adjacent and
   AT Protocol-adjacent identity flows where they make sense

### 7) Recovery independence matters

TOOO must preserve the ability for a user to recover access to their TOOO
platform account without making the entire account permanently hostage to an
outside identity source.

### 8) Mail alignment

Verification, password reset, security alert, and similar account mail should
align with ADR-0009 and use the account / security rail for
`accounts.techofourown.com`.

### 9) Public platform only

This ADR selects Keycloak for the public TOOO platform.

It does **not** authorize making TOOO public-platform accounts mandatory for:

- OurBox local use
- device-local admin
- household-hosted product access
- offline / local product functionality

That prohibition remains part of TOOO's broader values and architecture.

---

## Future Changes

The following do **not** require superseding this ADR so long as the software
choice and architecture boundary remain intact:

- moving Keycloak between TOOO-controlled hosts
- changing internal deployment topology
- changing database or backup implementation details
- adding new relying parties
- staging external identity integrations over time

The following **do** require follow-up governance action:

- replacing Keycloak as the selected public-platform identity provider
- collapsing public-platform identity back into app-local identity
- making TOOO public-platform accounts a mandatory dependency for local-first
  TOOO products
- merging public-platform identity and product-local identity into one
  undifferentiated system
- surrendering the canonical TOOO account system to a managed third-party SaaS
  provider

---

## References

### Internal

- `../governance/VALUES.md`
- `../governance/MISSION.md`
- `../governance/CONSTITUTION.md`
- `./ADR-0009-separate-human-and-machine-email-using-purpose-specific-subdomains.md`
- `./ADR-0010-adopt-dedicated-public-platform-identity-service.md`
- `../rfcs/RFC-0002-public-platform-identity-provider-options.md`

### External

- Keycloak project home: https://www.keycloak.org/
- Keycloak server administration guide:
  https://www.keycloak.org/docs/latest/server_admin/index.html
- Keycloak securing applications guide:
  https://www.keycloak.org/docs/latest/securing_apps/index.html
