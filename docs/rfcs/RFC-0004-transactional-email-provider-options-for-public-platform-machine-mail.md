# RFC-0004: Transactional Email Provider Options for TOOO Public-Platform Machine Mail

- **Created:** 2026-03-30
- **Updated:** 2026-03-30

---

## Status Note

This RFC remains the exploration record for TOOO's transactional email provider
selection for the public platform.

Since this RFC's initial analysis, TOOO has now adopted:

- `ADR-0014` — Amazon SES as the transactional email provider for public-platform
  machine mail

This RFC is therefore not the live decision by itself. It remains the reasoning
record behind that decision and frames the implementation trade-offs that remain
open.

---

## What

This RFC explores how Tech of Our Own should provide **transactional and
machine-generated email** for its public platform.

The immediate public-platform scope is:

- `accounts.techofourown.com`
- `forum.techofourown.com`
- `news.techofourown.com`

This RFC assumes those three rails are needed from day one.

This RFC also assumes **reply-by-email for the forum is required from day one**.

This RFC is about **machine-generated public-platform mail only**.

It is **not** about human-operated apex-domain mailboxes at `@techofourown.com`.
That human mail posture remains out of scope here.

A useful distinction matters:

- **human-operated apex-domain mail**
  - real people corresponding as TOOO
  - currently out of scope for this provider choice

- **public-platform machine mail**
  - account verification
  - password resets
  - security alerts
  - forum notifications and digests
  - broadcast updates / news

- **newsletter / campaign control plane**
  - the software TOOO may later self-host for list management, blog digests,
    or announcement workflows
  - related to, but not identical with, the email transport provider choice

This RFC is about choosing the **transport provider** for machine mail.

---

## Why

TOOO now has real public-platform services to bring online, and those services
need outbound mail before they can operate normally.

### Immediate launch pressure

At minimum:

- Keycloak needs outbound email for verification, password resets, and security
  workflows.
- Discourse needs outbound email for forum notifications and digests.
- Discourse reply-by-email requires an inbound mail path.
- TOOO wants a news / newsletter rail from day one for direct communication
  with its audience.

### Existing architecture already constrains the shape

`ADR-0009` already established that:

- apex-domain human mail stays separate from machine mail
- machine mail should use purpose-specific subdomains
- reputation should be split by function, not by every app
- `forum`, `accounts`, and `news` are the right machine-mail rails

That narrows the provider problem.

### Cost is not a side issue

TOOO is early-stage, self-hosting-minded, and infrastructure-conscious.
Recurring provider spend matters.

Because the public platform already includes multiple servers and several new
operational systems, TOOO has reason to heavily weight:

- low recurring cost
- ability to start small
- acceptable support for both outbound and inbound machine mail

### Reply-by-email changes the provider question

If TOOO only needed outbound transactional mail, more providers would fit
cleanly.

But **day-one reply-by-email** means the provider must either:

- provide inbound mail functionality directly, or
- pair cleanly with a TOOO-controlled inbound path

That makes inbound capability a real part of the decision, not a future detail.

### Newsletter logic and delivery are different layers

TOOO may later self-host newsletter or campaign logic.

That does **not** remove the need for a delivery provider. It means the chosen
transport should be good enough to sit underneath a TOOO-controlled control
plane later.

---

## How (Evaluation Frame)

This RFC compares options using the following criteria.

### 1) Architectural fit

The provider should fit the `ADR-0009` structure:

- apex human mail out of scope
- machine mail separated by function
- one transport provider can serve multiple TOOO machine-mail rails

### 2) Day-one domain count

The provider should be evaluated against **three day-one rails**:

- `accounts.techofourown.com`
- `forum.techofourown.com`
- `news.techofourown.com`

### 3) Day-one reply-by-email

The provider must be evaluated not just for outbound sending, but for whether
TOOO can reasonably support forum reply-by-email from day one.

### 4) SMTP compatibility

The provider must work with current software choices:

- Keycloak
- Discourse

That makes SMTP compatibility a minimum expectation.

### 5) Cost discipline

Cost is a decisive criterion in this RFC, not merely one factor among many.

### 6) Future control-plane flexibility

The provider should not block a later TOOO-controlled newsletter or campaign
system.

---

## Candidate Options

### Option A: Amazon SES for all machine-mail rails

#### Shape

Use Amazon SES for:

- `accounts.techofourown.com`
- `forum.techofourown.com`
- `news.techofourown.com`

Use SES sending for outbound mail and SES receiving for the forum reply-by-email
path.

#### What the official docs say

Amazon SES supports:

- outbound email through SMTP or the SES API
- domain and email identities
- DKIM support including Easy DKIM
- inbound email receiving using MX records and SES receipt rules
- region-specific SMTP credentials
- pay-as-you-go pricing

SES pricing currently lists:

- outbound email: `$0.10 / 1,000 emails`
- inbound email: `$0.10 / 1,000 emails`
- inbound chunks: `$0.09 / 1,000 incoming chunks`

AWS also states that new SES accounts start in the sandbox, where you can only
send to verified identities and are limited to `200` messages per 24 hours
until production access is granted.

#### Pros

- dramatically lower recurring provider cost than the other leading options
- one provider can cover all three day-one rails
- SMTP works with Keycloak and Discourse
- SES can receive email as well as send it
- compatible with a future TOOO-controlled newsletter or campaign control plane

#### Cons

- more operator friction than turnkey email vendors
- AWS account and SES-region setup become part of the email story
- sandbox exit is required before real launch
- SMTP credentials are region-specific
- SES receiving endpoints are **not** POP3 or IMAP inboxes
- reply-by-email therefore needs a TOOO-controlled inbound integration path,
  rather than a simple hosted mailbox

#### Fit assessment

Strongest option if cost dominates and TOOO is willing to accept more setup and
integration work.

---

### Option B: Mailgun for all machine-mail rails

#### Shape

Use Mailgun for:

- `accounts.techofourown.com`
- `forum.techofourown.com`
- `news.techofourown.com`

Use Mailgun's outbound delivery and inbound routing for reply-by-email.

#### What the official docs say

Mailgun exposes both SMTP and HTTP APIs.

Current self-serve pricing states:

- **Basic** — `$15/mo`, `10,000 emails`, `1 custom sending domain`, `5 inbound routes`
- **Foundation** — `$35/mo`, `50,000 emails`, `1,000 custom sending domains`,
  full inbound routing
- **Scale** — `$90/mo`, `100,000 emails`

#### Pros

- outbound + inbound story is more productized than SES
- SMTP works with Keycloak and Discourse
- domain count is generous once you move above Basic
- plausible single-provider story for all machine rails

#### Cons

- not close to SES on cost
- Basic does not fit TOOO's three-domain day-one shape because it includes only
  one custom sending domain
- realistic TOOO day-one use therefore starts closer to Foundation than Basic

#### Fit assessment

Plausible one-provider choice if TOOO wants a more integrated provider
experience and is willing to spend materially more than SES.

---

### Option C: Postmark for all machine-mail rails

#### Shape

Use Postmark for:

- `accounts.techofourown.com`
- `forum.techofourown.com`
- `news.techofourown.com`

Use Postmark outbound sending and its inbound capability where needed.

#### What the official docs say

Postmark supports SMTP and its own API.

Current self-serve pricing states:

- **Basic** — `$15/mo`, `10,000 emails`, `5 custom sending domains`
- **Pro** — `$16.50/mo`, `10,000 emails`, `10 custom sending domains`,
  **inbound email processing**
- **Platform** — `$18/mo`, `10,000 emails`, unlimited custom sending domains,
  **inbound email processing**

That means Postmark's cheapest day-one fit for TOOO's requirements is not just
“five domains,” but also “inbound email processing,” which starts at **Pro**.

#### Pros

- cleaner low-volume domain story than Mailgun
- SMTP works with Keycloak and Discourse
- inbound capability exists on tiers that fit the TOOO domain count
- one-provider path is plausible

#### Cons

- still far more expensive than SES on a pure transport basis
- once inbound is required, the relevant floor is Pro/Platform rather than
  Basic
- TOOO would be paying a premium for provider polish rather than for the lowest
  possible machine-mail transport spend

#### Fit assessment

Strong low-volume non-AWS option if TOOO wants a more polished provider
experience and is willing to pay more than SES for it.

---

### Option D: Split provider — Postmark for auth, Mailgun for forum + news

#### Shape

Use:

- Postmark for `accounts.techofourown.com`
- Mailgun for `forum.techofourown.com`
- Mailgun for `news.techofourown.com`

#### Pros

- preserves a dedicated auth-mail provider
- gives the forum/update side a provider with inbound-focused features

#### Cons

- highest operational sprawl of the serious options
- higher recurring floor than a single-provider choice
- requires duplicate provider setup, secret handling, billing, and DNS vendor
  coordination
- does not fit TOOO's current “choose the cheaper acceptable system” posture

#### Fit assessment

Defensible only if TOOO decides that auth-mail isolation is worth paying for at
provider level. This RFC does not find that compelling enough under a
cost-dominant posture.

---

## Cost Snapshot (current self-serve public pricing)

These figures are enough to explain why cost pushes hard toward SES.

### Amazon SES

- outbound: `$0.10 / 1,000 emails`
- inbound: `$0.10 / 1,000 emails`
- inbound chunks: `$0.09 / 1,000 chunks`

That means `50,000` outbound emails are approximately `$5` before attachment or
other optional charges.

### Mailgun

- Basic: `$15/mo`, `10,000 emails`, `1 custom sending domain`
- Foundation: `$35/mo`, `50,000 emails`, `1,000 custom sending domains`

Because TOOO wants three sending domains from day one, Mailgun Basic is not the
real shape of the decision.

### Postmark

- Basic: `$15/mo`, `10,000 emails`, `5 custom sending domains`
- Pro: `$16.50/mo`, `10,000 emails`, `10 custom sending domains`, inbound email
  processing
- Platform: `$18/mo`, `10,000 emails`, unlimited custom sending domains,
  inbound email processing

Because TOOO wants reply-by-email from day one, the relevant Postmark floor is
Pro or Platform, not merely Basic.

---

## Trade-Offs Summary

## The decisive split

The strongest trade-off in this RFC is:

- **SES is the cheapest by a wide margin**
- **Mailgun and Postmark are easier to like operationally**
- **Reply-by-email means SES requires more TOOO-owned integration work**

That is the heart of the decision.

## Why SES rises anyway under a cost-first posture

SES satisfies the minimum required shape:

- SMTP sending
- multi-domain identities
- DKIM support
- inbound email receiving
- compatibility with a future TOOO-controlled control plane

It simply does so with more AWS-shaped friction.

If TOOO is choosing primarily for **cost**, SES rises to the top.

## Why the others remain credible

Mailgun and Postmark remain real options because they reduce operator friction
and package more of the mail story into a more obvious product.

But they do so at a materially higher recurring floor.

## Reply-by-email is the main SES penalty

AWS explicitly states that SES receiving endpoints are not POP3 or IMAP inboxes.

So SES cannot be treated as “a mailbox provider that Discourse polls.”

Instead, one reasonable TOOO path is:

- SES receives forum replies
- SES receipt rules route the message into TOOO-controlled handling
- TOOO delivers the message into Discourse's supported incoming-email path

Discourse's self-hosted docs show two general families of reply-by-email setup:

- POP3 polling
- direct-delivery mail receiver

That means SES is viable, but not turnkey.

---

## Provisional Read

The strongest cost-dominant posture appeared to be — and has now become — the
following:

1. Use **Amazon SES** as the transport provider for TOOO machine mail
2. Keep human apex-domain mail out of scope and unchanged
3. Bring `accounts`, `forum`, and `news` online from day one
4. Accept that SES reply-by-email requires a TOOO-controlled inbound path
5. Keep the future newsletter or campaign control plane separate from the
   provider choice

That remains the cleanest fit for TOOO's current stage **if cost is the
deciding factor**.

---

## Open Questions

1. Which SES Region should be TOOO's day-one home for sending and receiving?
2. What exact inbound bridge should connect SES receiving to Discourse's
   supported reply-by-email path?
3. ~~Should TOOO use `updates.techofourown.com` or later rename the public-facing
   newsletter brand to `news.techofourown.com`?~~
   **Resolved:** TOOO adopted `news.techofourown.com` as the canonical
   newsletter / announcement rail.
4. How much of the future newsletter/control-plane logic should be self-hosted,
   and when?
5. At what scale, if any, would TOOO revisit the cost-vs-convenience trade and
   reconsider Postmark or Mailgun?

---

## References

### Internal

- `../decisions/ADR-0009-separate-human-and-machine-email-using-purpose-specific-subdomains.md`
- `../decisions/ADR-0014-adopt-amazon-ses-as-transactional-email-provider.md`
- `../decisions/ADR-0012-adopt-gpg-for-early-stage-platform-ops-secret-management.md`
- `../decisions/ADR-0013-adopt-apricorn-aegis-secure-key-3nx-as-offline-platform-recovery-media.md`

### External

- Amazon SES pricing:
  https://aws.amazon.com/ses/pricing/
- Amazon SES SMTP interface:
  https://docs.aws.amazon.com/ses/latest/dg/send-email-smtp.html
- Amazon SES receiving:
  https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html
- Amazon SES MX for receiving:
  https://docs.aws.amazon.com/ses/latest/dg/receiving-email-mx-record.html
- Amazon SES production access / sandbox:
  https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html
- Amazon SES identities:
  https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html
- Amazon SES DKIM:
  https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim.html
- Amazon SES SMTP credentials:
  https://docs.aws.amazon.com/ses/latest/dg/smtp-credentials.html
- Amazon SES regions and endpoints:
  https://docs.aws.amazon.com/general/latest/gr/ses.html
- Mailgun pricing:
  https://www.mailgun.com/pricing/
- Postmark pricing:
  https://postmarkapp.com/pricing
- Discourse self-hosted reply-by-email (POP3):
  https://meta.discourse.org/t/set-up-reply-by-email-with-pop3-polling/14003
- Discourse self-hosted reply-by-email (mail receiver):
  https://meta.discourse.org/t/configure-direct-delivery-incoming-email-for-self-hosted-sites-with-mail-receiver/49487
