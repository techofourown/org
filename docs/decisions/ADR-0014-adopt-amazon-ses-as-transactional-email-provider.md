# ADR-0014: Adopt Amazon SES as the Transactional Email Provider for Public-Platform Machine Mail

- **Date:** 2026-03-30
- **Related:**
  - `../governance/VALUES.md`
  - `../governance/MISSION.md`
  - `../governance/CONSTITUTION.md`
  - `./ADR-0009-separate-human-and-machine-email-using-purpose-specific-subdomains.md`
  - `./ADR-0012-adopt-gpg-for-early-stage-platform-ops-secret-management.md`
  - `./ADR-0013-adopt-apricorn-aegis-secure-key-3nx-as-offline-platform-recovery-media.md`
  - `../rfcs/RFC-0004-transactional-email-provider-options-for-public-platform-machine-mail.md`

---

## Context

TOOO now has real public-platform services that need machine-generated email in
order to launch and operate normally.

The current day-one machine-mail rails are:

- `accounts.techofourown.com`
- `forum.techofourown.com`
- `updates.techofourown.com`

Those rails cover:

- account verification, password resets, and security mail
- forum notifications, digests, and reply-by-email
- direct updates / news communication with TOOO's audience

A few architectural boundaries are already settled.

From `ADR-0009`:

- human-operated apex-domain mail and machine-generated mail are separate
- apex-domain human mail is out of scope for this provider decision
- machine mail should be separated by function and reputation class
- `accounts`, `forum`, and `updates` are the correct public-platform rails

A second operational constraint now also matters:

- **forum reply-by-email is required from day one**

That means the provider choice is not merely about outbound SMTP.
It must also support a workable inbound path.

TOOO evaluated several credible options, especially:

- Amazon SES
- Mailgun
- Postmark
- split-provider patterns such as Postmark for auth and Mailgun for everything
  else

The decisive factor in this decision is **cost**.

This ADR is intentionally blunt about that:

**TOOO is choosing Amazon SES because it is much cheaper.**
It is **not** choosing SES because SES is the most elegant operator experience
or the least integration work.

TOOO is knowingly accepting additional setup friction in order to minimize
recurring provider spend.

---

## Decision

Tech of Our Own will use **Amazon SES** as the transactional email provider for
its **public-platform machine mail**.

More specifically:

1. Amazon SES is the selected provider for day-one public-platform machine-mail
   rails:

   - `accounts.techofourown.com`
   - `forum.techofourown.com`
   - `updates.techofourown.com`

2. This ADR applies to **machine-generated public-platform mail only**.

   It does **not** change the current out-of-scope posture for human-operated
   apex-domain mail at `@techofourown.com`.

3. TOOO is choosing SES **primarily because of cost**.

   This decision does **not** claim that SES is the easiest or nicest
   operational choice. It records that TOOO is willing to accept more setup
   friction in exchange for materially lower recurring provider spend.

4. TOOO will use SES for **outbound sending** on all three day-one machine-mail
   rails.

5. TOOO will also use SES for the **forum inbound mail edge** needed for
   day-one reply-by-email.

6. Because SES receiving endpoints are not POP3 or IMAP mailboxes, TOOO accepts
   that forum reply-by-email requires a **TOOO-controlled inbound integration
   path** rather than a turnkey mailbox-polling setup.

7. TOOO is **not** adopting a split-provider model for auth vs forum vs updates
   mail at this stage.
   The cost advantage of one-provider SES is the controlling factor.

8. The canonical day-one updates / newsletter rail remains:

   - `updates.techofourown.com`

   If TOOO later prefers “news” as user-facing language, that is a naming
   follow-up, not a different provider decision.

9. This ADR chooses the **email transport provider**.
   It does **not** choose the long-term newsletter, campaign, or CRM control
   plane that may sit on top of that provider later.

---

## Rationale

### 1) SES is dramatically cheaper than the serious alternatives

Amazon SES currently prices email at:

- outbound email: `$0.10 / 1,000 emails`
- inbound email: `$0.10 / 1,000 emails`

By contrast, the relevant self-serve alternatives currently start at much
higher recurring floors:

- Mailgun Basic: `$15/mo` with only `1 custom sending domain`
- Mailgun Foundation: `$35/mo` with `50,000 emails` and `1,000 custom sending domains`
- Postmark Basic: `$15/mo` with `5 custom sending domains`
- Postmark Pro: `$16.50/mo` with inbound email processing
- Postmark Platform: `$18/mo` with inbound email processing

Because TOOO wants **three sending domains from day one** and **reply-by-email
from day one**, the realistic comparison is not “SES vs one tiny-domain starter
plan.” The realistic comparison is SES against higher bundled plans that still
cost materially more.

That makes SES the obvious choice under a cost-dominant posture.

### 2) SES still satisfies the minimum functional requirements

Despite the extra friction, SES supports the key pieces TOOO actually needs:

- SMTP sending
- verified identities at domain level
- DKIM support
- inbound email receiving
- MX-based receipt handling

That means SES is not being chosen as a false economy that fails the
requirements. It is being chosen as the cheapest provider that still clears the
minimum bar.

### 3) One provider is cheaper and simpler than splitting providers

A split-provider architecture might be defensible if TOOO believed the auth rail
needed a premium provider badly enough to justify the cost.

At this stage, TOOO does not judge that trade worthwhile.

The organization is choosing to keep:

- one machine-mail transport provider
- multiple function-specific subdomains
- one internal operational model

rather than paying extra to divide provider relationships before the platform
has earned that complexity.

### 4) Reply-by-email is the main SES pain point, but TOOO accepts it

AWS explicitly documents that SES receiving endpoints are not POP3 or IMAP mail
servers.

Discourse's self-hosted documentation shows two broad reply-by-email patterns:

- POP3 polling
- direct-delivery mail receiver

That means SES does not provide a turnkey mailbox for Discourse to poll.
TOOO must instead implement a TOOO-controlled bridge from SES receiving into
Discourse's supported incoming-mail path.

That is real extra work.

TOOO is still accepting that work because the price advantage is large enough to
matter right now.

### 5) This keeps future control-plane choices open

TOOO may later self-host newsletter or campaign logic.

Choosing SES as the transport layer does not force TOOO into a specific
newsletter application. It simply establishes the cheapest acceptable delivery
substrate underneath whatever future control plane TOOO adopts.

---

## Consequences

### Positive

- TOOO gets the lowest recurring provider spend among the serious options.
- One provider can cover `accounts`, `forum`, and `updates` from day one.
- SMTP compatibility for Keycloak and Discourse remains straightforward.
- Day-one reply-by-email remains possible.
- Future newsletter or campaign logic can still be layered on top later.

### Negative / Tradeoffs

- SES is more AWS-shaped and less turnkey than the nicer alternatives.
- TOOO must request production access before real launch because new SES
  accounts begin in the sandbox.
- SMTP credentials are region-specific.
- SES receiving is not a POP3/IMAP mailbox product.
- Day-one reply-by-email requires a TOOO-controlled inbound bridge.
- Operator burden is higher than it would be on Postmark or Mailgun.

### Mitigation

- pick one SES Region that supports both sending and receiving
- request production access early
- verify identities and DKIM for the day-one rails deliberately
- document the inbound reply-by-email bridge clearly in the ops repos
- keep provider scope narrow: transport now, control-plane decisions later

---

## Options Considered

### Option A: Amazon SES for everything

**Accepted.**

Chosen primarily because it is much cheaper than the alternatives while still
meeting the minimum functional requirements.

### Option B: Mailgun for everything

**Not selected.**

Mailgun remained a credible option, but it did not win under a cost-dominant
posture. TOOO would pay materially more for a more productized provider
experience.

### Option C: Postmark for everything

**Not selected.**

Postmark remained a credible option, especially for cleaner low-volume setup,
but it still costs materially more than SES and requires an inbound-capable tier
for day-one reply-by-email.

### Option D: Split provider (for example, Postmark for auth and Mailgun for the rest)

**Not selected.**

TOOO did not find the additional provider overhead and higher recurring floor
worth paying for at this stage.

---

## Implementation Notes

### 1) Day-one rail set

The day-one SES identities should cover:

- `accounts.techofourown.com`
- `forum.techofourown.com`
- `updates.techofourown.com`

### 2) SES sandbox exit is required

AWS states that new SES accounts begin in the sandbox, where:

- mail can only be sent to verified identities
- sending is limited to `200` messages per 24 hours

Production access must therefore be requested before real launch.

### 3) SMTP posture

Keycloak and Discourse can both use SES through the SMTP interface.

AWS also documents that SES SMTP credentials are **unique per AWS Region**.
TOOO should therefore choose a day-one SES Region deliberately and generate
credentials for that Region only.

### 4) Domain identity / DKIM posture

AWS supports domain identities and DKIM signing, including Easy DKIM.

TOOO should verify the day-one machine-mail rails and publish the required DNS
records accordingly.

### 5) Reply-by-email posture

AWS documents that SES can receive email through MX records and receipt rules,
but also explicitly notes that SES receiving endpoints are not POP3 or IMAP
servers.

Therefore TOOO should not plan on using SES itself as a POP3 mailbox.

A valid TOOO implementation path is:

1. publish the MX record for `forum.techofourown.com` to the chosen SES
   receiving endpoint
2. receive replies through SES
3. route incoming messages into a TOOO-controlled handler
4. deliver them into Discourse's supported incoming-mail path

Discourse's self-hosted documentation already acknowledges direct-delivery
incoming mail as a supported family of approach.

### 6) Newsletter / updates control plane remains separate

This ADR chooses SES as the delivery provider for `updates.techofourown.com`.

It does **not** decide whether TOOO will later use Mautic, Listmonk, or another
control-plane application for digest and broadcast logic.

---

## Future Changes

The following do **not** require superseding this ADR so long as SES remains the
transactional transport provider:

- selecting the exact SES Region
- changing the exact inbound bridge implementation for forum reply-by-email
- adding a later TOOO-controlled newsletter / campaign control plane above SES
- changing the local-part naming under the chosen subdomains

The following **do** require follow-up governance action:

- replacing SES as the transactional provider
- adopting a split-provider machine-mail architecture as the new default
- collapsing machine-generated mail back into apex-domain human mail
- materially redefining the canonical machine-mail rails established by
  `ADR-0009`

---

## References

### Internal

- `../governance/VALUES.md`
- `../governance/MISSION.md`
- `../governance/CONSTITUTION.md`
- `./ADR-0009-separate-human-and-machine-email-using-purpose-specific-subdomains.md`
- `../rfcs/RFC-0004-transactional-email-provider-options-for-public-platform-machine-mail.md`

### External

- Amazon SES pricing:
  https://aws.amazon.com/ses/pricing/
- Amazon SES receiving:
  https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html
- Amazon SES MX for receiving:
  https://docs.aws.amazon.com/ses/latest/dg/receiving-email-mx-record.html
- Amazon SES identities:
  https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html
- Amazon SES DKIM:
  https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim.html
- Amazon SES production access / sandbox:
  https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html
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
