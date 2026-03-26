# ADR-0009: Separate Human and Machine Email Using Purpose-Specific Subdomains

- **Date:** 2026-03-26
- **Related:**
  - `../governance/VALUES.md`
  - `../governance/MISSION.md`
  - `./ADR-0003-standardize-naming-across-artifacts.md`

---

## Context

Tech of Our Own is beginning to accumulate multiple public and semi-public
internet surfaces under the same parent domain:

- human correspondence (`john@techofourown.com` and future role mailboxes)
- a Discourse forum
- blog-comment notifications and reply flows tied to the public site
- future donations and storefront receipts
- future account verification and password-reset mail
- a future online school or course-notification surface
- future announcement or campaign mail

These surfaces may live in different repositories, on different servers, and
behind different applications. Email identity, however, is domain-wide.
Deliverability problems created by one class of mail can spill into other
classes of mail if they share the same sender identity or reputation bucket.

That makes email an organization-level concern rather than a repo-local or
server-local implementation detail.

A naive approach would send everything from the apex domain
(`@techofourown.com`) through one provider or one sender identity. That looks
simple at the beginning, but it creates avoidable risk:

- high-volume community notifications can damage the deliverability of critical
  mail
- receipts and password resets can become entangled with digests and discussion
  mail
- human correspondence can share reputation with machine-generated mail
- later growth forces a disruptive reorganization under load

At the same time, splitting every individual application into its own email
vendor or its own arbitrary mail domain would be over-fragmented and
operationally noisy.

TOOO needs a mail strategy that:

- keeps the public identity under `techofourown.com`
- protects critical mail through reputation isolation
- preserves clear human-vs-machine boundaries
- scales cleanly as more products and services appear
- does not require a full re-architecture every time a new app or server is
  added

---

## Decision

Tech of Our Own will use a two-tier email strategy:

1. **Human-operated mail** and **machine-generated mail** are separate classes
   and must not share the same default sending identity.

2. **Human-operated mail** will use the apex domain:

   - `techofourown.com`

   This is the domain for real people corresponding as TOOO.

   Current provider posture:
   - TOOO retains **Zoho Mail** as the current provider for human-operated
     apex-domain mailboxes.

3. **Machine-generated mail** will use a **dedicated transactional mail
   platform** separate from the human-mail provider.

   The durable architectural rule is:
   - **one human-mail system**
   - **one transactional-mail platform**
   - **multiple authenticated machine-mail subdomains under
     `techofourown.com`**

   The exact transactional vendor is an operational implementation detail so
   long as it supports domain authentication, programmatic sending, suppression
   management, and function-level isolation.

4. Machine-generated mail will be partitioned by **mail function / reputation
   class**, not by every individual app or codebase.

5. TOOO adopts the following canonical machine-mail subdomains:

   - **`forum.techofourown.com`**
     - community notifications
     - forum digests
     - mentions and reply notifications
     - blog-comment notifications when the public site is integrated with
       Discourse
     - reply-by-email or inbound forum mail if enabled

   - **`accounts.techofourown.com`**
     - email verification
     - password resets
     - magic links
     - security alerts
     - other account and identity mail across TOOO properties

   - **`billing.techofourown.com`**
     - donation receipts
     - storefront/order receipts
     - invoices
     - payment confirmations
     - refund notifications

   - **`school.techofourown.com`**
     - course enrollment mail
     - lesson reminders
     - assignment notifications
     - school/community learning notifications

   - **`updates.techofourown.com`**
     - bulk announcements
     - campaign mail
     - non-critical broadcast updates

6. The default sharing rule is:

   - mail may be shared across multiple products **when it belongs to the same
     function**
   - mail must be split when it belongs to a meaningfully different trust,
     deliverability, or operational class

   Example:
   - forum signup verification and storefront password resets may both use
     `accounts.techofourown.com`
   - forum digests and donation receipts must **not** share a rail

7. The default prohibition is:

   - **machines do not send routine transactional or bulk mail from
     `@techofourown.com`**
   - the apex domain is reserved for human-operated correspondence by default

8. TOOO will **not** create one transactional subdomain per app by default.
   New subdomains are created when there is a real mail-function boundary, not
   merely because a new service exists.

9. Not every reserved subdomain must be provisioned on day one.
   Initial implementation may start with the current human-mail setup plus the
   community rail, while reserving the full naming plan for later expansion.

---

## Scope

This ADR applies to TOOO-controlled email under `techofourown.com`, including:

- human-operated correspondence
- community/forum mail
- auth/security mail
- receipts and money-related mail
- learning/school mail
- bulk update mail
- future TOOO-owned internet properties that send mail under the TOOO domain

This ADR does **not** decide:

- the exact transactional email vendor
- helpdesk/ticketing software
- forum software details beyond the email boundary
- exact inbox routing for every future mailbox
- internal secret-handling or credential storage procedures

Those are operational implementation details and may be documented in repo-local
ops docs or private infrastructure repos.

---

## Rationale

### 1) Human mail and machine mail should not share reputation

Human correspondence and machine-generated notifications behave differently.
They generate different volumes, complaint patterns, reply expectations, and
deliverability risks.

If community digests or bulk updates damage sender reputation, that must not
make password resets or human correspondence harder to deliver.

### 2) Critical machine mail deserves stronger isolation

Account/security mail and money mail are materially more important than
community chatter or announcements.

A password-reset message, a donation receipt, and a forum digest are not the
same kind of email. Treating them as one undifferentiated sender class is
operationally sloppy and creates avoidable risk.

### 3) Function-based partitioning is better than app-based partitioning

The right boundary is not "one subdomain per service forever."
The right boundary is "one rail per trust/reputation class."

This avoids two bad extremes:

- **under-partitioning**: everything sent from one identity
- **over-partitioning**: every app gets its own separate mail system

Function-based partitioning gives TOOO enough separation to protect
deliverability without inventing unnecessary operational sprawl.

### 4) One parent domain preserves trust and coherence

TOOO wants people to see mail coming from the TOOO domain family, not from a
pile of unrelated vendor domains.

Using authenticated subdomains under `techofourown.com` preserves:

- brand continuity
- user recognition
- future flexibility across multiple websites, servers, and products

### 5) The domain boundary should outlive any one server or repo

TOOO already has separate repos and will have separate servers.
That is normal. The email strategy should survive movement between apps, hosts,
and architectures without forcing a new naming scheme each time.

This ADR therefore belongs in the org repo, where domain-wide identity
decisions live.

### 6) The structure should be strong early, not patched later

Early architecture is the right time to set naming, boundaries, and reputation
strategy. Once real mail volume exists, cleanup is harder and riskier.

This is a low-user, high-leverage moment to establish the durable pattern.

---

## Consequences

### Positive

- Human correspondence is protected from machine-mail reputation issues.
- Critical mail classes like auth and receipts get cleaner deliverability
  boundaries.
- TOOO gets a stable, reusable mail architecture across multiple sites and
  services.
- Future products can plug into existing rails instead of improvising their
  own.
- The public email story stays coherent under one parent domain.

### Negative / Tradeoffs

- DNS and mail authentication become more complex than a single-domain setup.
- There is more conceptual overhead than "send everything from one address."
- Some future teams may want a new mail subdomain prematurely, creating naming
  pressure.
- Moving from an improvised app-local habit to an org-wide mail strategy
  requires discipline.

### Mitigation

- Reserve the naming system early.
- Provision only the rails that are actually needed now.
- Keep the functional rule simple: split by reputation class, not by app vanity.
- Document the canonical rails centrally so repos and services do not invent
  their own local conventions.

---

## Options considered

### Option A: Use the apex domain and one provider for everything

Examples:
- `noreply@techofourown.com`
- `support@techofourown.com`
- `john@techofourown.com`
- forum digests, receipts, and password resets all mixed together

**Rejected.**

This is easy at the beginning and messy later.
It blends human mail with machine mail, weakens deliverability isolation, and
creates a large blast radius when any one mail class misbehaves.

### Option B: Give every product or app its own provider and domain strategy

Examples:
- one vendor for the forum
- another vendor for the store
- another vendor for the school
- per-app subdomains or vendor domains everywhere

**Rejected.**

This creates too much fragmentation, too many credentials, and too little
coherence. It is unnecessary for TOOO's scale and makes the parent-domain story
harder to understand.

### Option C: Use one machine-mail rail for all machine mail

Example:
- all machine mail sent from `mail.techofourown.com` or equivalent

**Rejected.**

This is cleaner than apex-only mail, but it still mixes critical auth/receipt
mail with community and announcement mail. It reduces blast-radius control too
much.

### Option D: Separate human mail from machine mail and partition machine mail by function

**Accepted.**

This gives TOOO a strong early architecture with limited complexity:
- one human rail
- one transactional platform
- multiple function-specific subdomains

---

## Implementation notes

### 1) Human-operated addresses

Examples of human-operated apex-domain addresses:

- `john@techofourown.com`
- `hello@techofourown.com`
- `press@techofourown.com`
- `support@techofourown.com`

These addresses are for people.

### 2) Machine-generated address patterns

Examples of machine-generated addresses:

- `notifications@forum.techofourown.com`
- `replies@forum.techofourown.com`
- `noreply@accounts.techofourown.com`
- `security@accounts.techofourown.com`
- `receipts@billing.techofourown.com`
- `orders@billing.techofourown.com`
- `donations@billing.techofourown.com`
- `notifications@school.techofourown.com`
- `announcements@updates.techofourown.com`

The exact local-part naming may vary, but the subdomain-purpose mapping is the
important part.

### 3) Authentication and reputation

Each machine-mail subdomain should be authenticated separately using
provider-supported domain authentication controls, including:

- SPF or provider-equivalent sender authorization
- DKIM signing
- DMARC policy where appropriate
- provider-specific return-path / bounce-domain alignment where supported

The goal is separate, legible reputation and policy boundaries per mail rail.

### 4) Provider features

The chosen transactional provider should support, at minimum:

- multiple authenticated sending domains or equivalent subdomain support
- API or SMTP sending for application integration
- suppression / bounce management
- per-stream or per-rail operational visibility
- inbound or reply handling where needed for community/forum flows

### 5) Community rail and Discourse

`forum.techofourown.com` is the canonical rail for the Discourse/community
layer, including future blog-comment notification flows that use the forum as
the discussion backend.

If reply-by-email or inbound community mail is enabled, it belongs on the
community rail, not on the auth or billing rail.

### 6) Financial mail may split later

`billing.techofourown.com` is the correct initial shared rail for:

- store receipts
- donations
- invoices
- payment confirmations

If TOOO later reaches enough volume or compliance complexity to justify further
separation, `billing` may be split via follow-up decision into more specific
rails such as `orders` and `donations`.

### 7) Bulk announcement mail stays isolated

`updates.techofourown.com` is reserved for bulk or campaign-style mail and must
not be used for account security or financial notifications.

Required, user-protective mail and opt-in broadcast mail should not share the
same reputation bucket.

### 8) Initial rollout

Immediate rollout should do the following:

1. keep apex-domain human mail on Zoho Mail
2. provision `forum.techofourown.com` on the transactional platform for
   Discourse
3. reserve the names `accounts`, `billing`, `school`, and `updates`
4. bring `accounts` and `billing` online when those systems are actually
   introduced

### 9) Public vs private documentation

Public repositories may describe the mail structure and the purpose of each
subdomain.

Public repos must not disclose:

- credentials
- secret material
- inbound-routing secrets
- provider tokens
- internal aliasing or forwarding details that do not help users

Operational details belong in private infrastructure documentation.

---

## Future changes

The following do **not** require superseding this ADR so long as the
architectural split remains intact:

- migrating human-operated mail from Zoho Mail to another human-mail provider
- changing the transactional-mail vendor
- adding or removing implementation-specific local parts
- changing server/application topology behind the mail rails

The following **do** require follow-up governance action:

- collapsing routine machine mail back onto the apex domain
- abandoning function-based rail separation
- materially redefining the meaning of the canonical subdomains
- creating an org-wide policy that contradicts the human-vs-machine split

---

## References

- `../governance/VALUES.md`
- `../governance/MISSION.md`
- `./ADR-0003-standardize-naming-across-artifacts.md`
