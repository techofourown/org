# RFC-0002: Public-Platform Identity Provider Options for TOOO Accounts

- **Created:** 2026-03-26
- **Updated:** 2026-03-26

---

## What

This RFC explores concrete implementation options for the dedicated
public-platform identity service established by:

- `../decisions/ADR-0010-adopt-dedicated-public-platform-identity-service.md`

The problem here is specific.

TOOO needs an identity service for **TOOO-operated web properties** such as:

- forum / comment login
- future school / course login
- future storefront or order-history login
- future donation-history access
- future member-facing or governance-adjacent web login

This is the **public TOOO platform** problem.

It is **not** the same as the identity problem inside OurBox or future TOOO
local-first products. A product-local identity system may need to operate
offline, under household control, without any mandatory dependency on
TOOO-operated services. That is a different problem and should be treated as
such.

This RFC is about how TOOO should implement the public-platform account rail
at:

- `accounts.techofourown.com`

---

## Why

The public platform needs a dedicated identity layer because neither of the
obvious shortcuts is acceptable.

### Shortcut 1: Let Discourse become the account system

Rejected in ADR-0010.

That makes a community application the root identity authority for the entire
platform.

### Shortcut 2: Let every app manage its own login

Also rejected.

That creates fragmented identity, fragmented recovery, and inconsistent
security.

Identity is a security-critical surface. OWASP treats authentication and
authorization as distinct, security-sensitive concerns, and NIST explicitly
recommends phishing-resistant authentication options where practical. That
means TOOO should evaluate identity software deliberately rather than drifting
into whatever the first app makes convenient.

The choice also matters because TOOO's brand and mission are not neutral on
this topic. The selected solution should fit TOOO's commitments to:

- privacy by architecture
- no lock-in, including lock-in to us
- local-first values
- organization-controlled infrastructure
- inspectability and future exit

---

## How (Evaluation Frame)

This RFC uses the following evaluation criteria.

### 1) Control and sovereignty

The solution should support an organization-controlled deployment model and
avoid forcing TOOO to hand its root account system to a third-party SaaS
vendor.

### 2) Protocol and exit posture

The solution should support standards-based app integration.

Minimum expectation:

- OpenID Connect / OAuth 2.0 for relying-party login

Highly desirable:

- SAML support where later integrations justify it
- directory / provisioning support where useful

### 3) Security posture

The solution should support:

- passkeys / WebAuthn
- MFA
- recovery flows
- auditable admin changes
- secure session and account lifecycle management

### 4) Public-platform fit

The solution should work well for a multi-app public platform with one shared
identity core and app-local business state.

### 5) Customization and UX control

TOOO may want branded, low-friction login and recovery experiences under its
own domain family. The solution should not make that path impossible or
brittle.

### 6) Operational burden

The solution should be realistic for a small but serious organization to run.

### 7) Product-boundary discipline

The solution must fit the public platform **without** pulling OurBox or future
local-first products into a mandatory TOOO-operated account dependency.

---

## Candidate Options

### Option A: Custom-build the identity service

#### Shape

TOOO writes and maintains its own identity stack:

- signup / login
- session management
- token issuance
- MFA / passkeys
- recovery flows
- app integrations
- admin tooling
- audit surfaces

#### Pros

- exact fit to TOOO's product model
- no external product compromise forced on the architecture
- full control over UX, data model, and lifecycle semantics

#### Cons

- highest engineering and security burden by far
- TOOO becomes responsible for every mistake in:
  - account recovery
  - session handling
  - MFA
  - WebAuthn / passkeys
  - token flows
  - admin escalation paths
  - security patch cadence
- easily becomes a long tail of security and compliance work
- highly likely to delay real product work

#### Fit assessment

This should be treated as the **exception path**, not the default path.

A custom build only makes sense if TOOO discovers a hard requirement that the
open-source identity products cannot satisfy without unacceptable compromise.

#### Current read

Not recommended as the starting move.

### Option B: authentik

#### What the official docs say

authentik describes itself as an IdP and SSO platform, offers a
forever-free open-source project, and states that it supports major protocols
including OAuth2, SAML, LDAP, and SCIM. Its docs also emphasize configurable
flows and stages, while its feature material calls out FIDO2 / WebAuthn /
passkey support. Its official messaging leans heavily into self-hosting and
taking control of sensitive identity data.

#### Pros

- strong self-hosted / sovereignty story
- broad protocol surface for future integrations
- flexible flows and policy model
- passkey support exists now
- plausible fit for a multi-app public platform without forcing TOOO into a
  huge, highly composable assembly project

#### Cons

- flexibility can become complexity if not governed
- some enterprise features sit outside the open-source core
- TOOO would still need to learn the product deeply enough to operate it
  confidently

#### Fit assessment

Strong candidate.

If TOOO wants one integrated self-hosted platform with good protocol coverage
and modern auth features, authentik belongs near the top of the shortlist.

### Option C: Keycloak

#### What the official docs say

Keycloak's official site highlights identity brokering, user federation,
centralized admin management, user self-service, and fine-grained
authorization. Its docs also include WebAuthn and passkey support, including
passwordless flows.

#### Pros

- mature and widely used
- broad ecosystem and large knowledge base
- strong protocol and federation story
- identity brokering and user federation are first-class capabilities
- modern auth features are present, including passkeys / WebAuthn

#### Cons

- operationally heavier than some alternatives
- may feel more enterprise-shaped than TOOO needs on day one
- can encourage taking on more IAM surface area than the first phase actually
  requires

#### Fit assessment

Strong candidate.

If TOOO values maturity, breadth, and long-term ecosystem confidence over
simplicity, Keycloak is a very credible option.

### Option D: ZITADEL

#### What the official docs say

ZITADEL's docs highlight passkeys / MFA, OIDC / SAML / OAuth2, multi-tenancy
with branding customization and self-service, and an exhaustive audit trail.
Its self-hosting docs explicitly cover self-hosted deployment paths, including
Docker Compose.

#### Pros

- self-hosted path exists and is actively documented
- strong modern-login posture, including passkeys
- good fit for branded multi-organization or multi-tenant scenarios
- auditability is explicit in the product story

#### Cons

- the product posture feels somewhat more cloud-and-B2B-shaped than some other
  candidates
- TOOO would need to decide whether the multi-tenancy model is a benefit or
  just extra shape
- likely more infrastructure opinion than a lightweight homelab-oriented tool

#### Fit assessment

Strong candidate.

Especially worth serious evaluation if TOOO expects multi-org account
boundaries, branded subspaces, or wants auditability and tenant separation
early.

### Option E: Ory (Kratos + Hydra, potentially more)

#### What the official docs say

Ory documents a composable ecosystem with clear boundaries:

- Kratos for identity management
- Hydra for OAuth 2.0 / OpenID Connect
- Oathkeeper for identity-aware proxying
- Keto for access control

Ory explicitly says these services can work standalone or be combined. Its
docs describe Kratos as handling identity flows such as login, logout,
recovery, session management, profile management, and MFA, while Hydra is the
OIDC provider layer rather than identity management itself.

#### Pros

- very strong composability
- attractive if TOOO wants maximum control over custom UX and app architecture
- good separation between identity management and token-service concerns
- can be a strong long-term foundation for a more custom, platform-shaped auth
  stack

#### Cons

- more assembly work than integrated platforms
- higher architectural burden on TOOO
- better for teams comfortable composing multiple security services rather than
  adopting one more integrated IdP product

#### Fit assessment

Strong candidate, but for a different temperament.

If TOOO wants a more explicitly composable stack and is willing to own more
integration work, Ory deserves real attention. If TOOO wants the fastest path
to a coherent single-platform IdP, it may be more than necessary.

### Option F: Authelia

#### What the official docs say

Authelia describes itself as an open-source authentication and authorization
server and portal that provides MFA and SSO for applications via a web portal.
It also states that it is an OpenID Connect 1.0 Provider and acts as a
companion for common reverse proxies. Its docs also include WebAuthn /
passkey configuration.

#### Pros

- open source and self-host-friendly
- good fit for SSO + MFA around self-hosted apps
- strong reverse-proxy integration story
- lighter-weight operational vibe than the biggest IAM platforms

#### Cons

- product shape appears more centered on app protection / SSO portal use cases
  than on being the primary customer-account system for a multi-surface public
  platform
- may be better at "protect a fleet of apps" than at serving as TOOO's
  long-term public-platform account authority

#### Fit assessment

Possible, but likely secondary.

Authelia looks more attractive for internal or self-hosted app protection than
for TOOO's central public-platform identity tier.

### Option G: Dex

#### What the official docs say

Dex documents itself as an identity service using OpenID Connect to drive
authentication for other apps. It also says Dex acts as a portal to other
identity providers through connectors, deferring authentication to LDAP, SAML,
OIDC, GitHub, Google, Active Directory, and others.

#### Pros

- simple, focused architecture
- strong federation / connector story
- useful if TOOO primarily wants a broker layer in front of other identity
  sources

#### Cons

- product shape is narrower than a full customer-account / public-platform
  identity system
- appears stronger as a broker than as a rich system of record for
  TOOO-managed accounts
- likely better as a supporting component than as the main long-term
  public-platform accounts system

#### Fit assessment

Useful reference option, but probably not the leading candidate for TOOO's
root public-platform account system.

### Option H: Managed SaaS identity platforms (reference only)

Examples might include commercial hosted account platforms.

#### Pros

- faster time to launch
- reduced operational burden
- often polished UX and operational tooling

#### Cons

- weak fit with TOOO's sovereignty posture
- externalizes the most sensitive trust surface
- can create provider dependency precisely where TOOO should be most cautious
- may complicate future exit, migration, or deep customization

#### Fit assessment

Not the preferred direction for TOOO's root identity tier unless TOOO later
decides that speed materially outweighs the sovereignty cost.

For now, this RFC treats managed SaaS as a comparison baseline rather than a
recommended family.

---

## Provisional Shortlist

This is a **non-binding** read, not a selection.

The most serious candidates for the next round appear to be:

1. **authentik**
2. **Keycloak**
3. **ZITADEL**
4. **Ory**

Why these four:

- they are closer to the right scale and shape for a real public-platform
  identity tier
- they support modern protocols and strong auth features
- they preserve a self-hosted / org-controlled path
- they are more plausible long-term roots than lighter broker-only or
  reverse-proxy-centered tools

Secondary / specialized options:

- **Authelia**: more attractive for app protection / SSO portal use cases
- **Dex**: more attractive as a federation broker
- **Custom build**: keep in reserve only if product requirements force it

---

## Trade-Offs Summary

### If TOOO optimizes for an integrated self-hosted platform

Leading fit:

- authentik
- Keycloak
- ZITADEL

### If TOOO optimizes for composability and custom UX control

Leading fit:

- Ory

### If TOOO optimizes for the smallest initial app-protection setup

Leading fit:

- Authelia

### If TOOO optimizes for federation-broker simplicity

Leading fit:

- Dex

### If TOOO optimizes for maximum product-specific fit regardless of burden

Leading fit:

- custom build

---

## Open Questions

1. Does TOOO want a more integrated IdP platform or a more composable identity
   stack?
2. How much custom login and recovery UX does TOOO expect to own in phase one?
3. Do we expect multi-organization / branded tenant boundaries early enough to
   matter now?
4. How important are identity brokering and external-provider federation in
   the first public phase?
5. Do we want service accounts / machine identities in this same system early,
   or can that wait?
6. Which public surfaces truly require accounts, and which should remain
   guest-capable?
7. What are the minimum audit and admin-operability expectations for the first
   production rollout?
8. What export / migration guarantees must the chosen implementation satisfy
   before TOOO is willing to treat it as the root public-platform account
   layer?
9. What login and recovery posture best matches TOOO's privacy values without
   creating support nightmares?
10. Where should the boundary sit between public-platform identity and future
    member / governance identity, if those later diverge?

---

## Next Steps

1. Adopt ADR-0010 if the architecture boundary is accepted.
2. Reduce the option set to a working shortlist for hands-on evaluation.
3. Define a scorecard against the evaluation criteria in this RFC.
4. Run one or more small pilots with realistic relying parties:
   - Discourse
   - a lightweight account / profile surface
5. Decide whether TOOO prefers:
   - an integrated platform
   - a composable stack
6. Write a follow-up ADR selecting the identity provider and recording why.

---

## References

### Internal

- `../governance/VALUES.md`
- `../governance/MISSION.md`
- `../governance/CONSTITUTION.md`
- `../decisions/ADR-0009-separate-human-and-machine-email-using-purpose-specific-subdomains.md`
- `../decisions/ADR-0010-adopt-dedicated-public-platform-identity-service.md`

### External

- OWASP Authentication Cheat Sheet:
  https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- NIST SP 800-63B: https://pages.nist.gov/800-63-4/sp800-63b.html
- NIST SP 800-63B Authenticator guidance:
  https://pages.nist.gov/800-63-4/sp800-63b/authenticators/

#### authentik

- Docs home: https://docs.goauthentik.io/
- Features: https://goauthentik.io/features/
- Install / configure: https://docs.goauthentik.io/install-config/

#### Keycloak

- Project home: https://www.keycloak.org/
- Server administration guide:
  https://www.keycloak.org/docs/latest/server_admin/index.html
- Securing applications:
  https://www.keycloak.org/docs/latest/securing_apps/index.html

#### ZITADEL

- Docs home: https://zitadel.com/docs
- Self-hosting with Docker Compose:
  https://zitadel.com/docs/self-hosting/deploy/compose
- Open-source / self-hosting overview: https://zitadel.com/opensource

#### Ory

- Ecosystem / project overview: https://www.ory.com/docs/ecosystem/projects
- Ory Kratos: https://www.ory.sh/kratos
- Ory Hydra: https://www.ory.sh/hydra

#### Authelia

- Project home: https://www.authelia.com/
- OpenID Connect provider docs:
  https://www.authelia.com/configuration/identity-providers/openid-connect/provider/
- WebAuthn config:
  https://www.authelia.com/configuration/second-factor/webauthn/

#### Dex

- Docs home: https://dexidp.io/docs/
- Connectors overview: https://dexidp.io/docs/connectors/
