# Tech of Our Own

## Declaration of Values

### Status

Draft (Founder proposal).
This document is meant to be *amended by members* through the governance process described in `CONSTITUTION.md` and `BOARD_OPERATIONS.md`.

---

## Preamble

Tech of Our Own exists because modern technology is increasingly built to **extract**: attention, data, money, autonomy, dignity. This is not an accident. It's the predictable result of incentives, gatekeepers, and digital locks.

We believe a different future is possible--one where technology is **trustworthy because it is inspectable**, resilient because it is **user-owned and forkable**, and sustainable because it is governed for **users and members** rather than outsiders.

We don't exist to "disrupt." We exist to **restore agency**.

Our goal isn't that nobody ever abuses our work. Open systems can be abused. Our goal is that when someone tries to poison the well, the poison is **visible**, **auditable**, and **easy to route around**.

---

## What we mean by "user" and "member"

* A **user** is a person using the technology.
* A **member** is a user who participates in governance/ownership of the co-op.
* We avoid framing people primarily as "customers." If someone pays us, that's a transaction; it doesn't change their dignity or status as a person.

---

## Non-negotiables

These are the values we do not trade away for growth, headlines, enterprise deals, or "market realities."

### 1) User sovereignty over user convenience

If we must choose, we choose **sovereignty**:

* the user can run it
* the user can leave it
* the user can verify it
* the user can repair it
* the user can migrate it

Convenience is allowed. Dependence is not.

### 2) Inspectability is a right, not a feature

We value systems that are **intelligible, observable, inspectable, interpretable**--not because it's trendy, but because it's how you prevent silent harm.

Practical implications:

* Source-available isn't enough. We aim for **buildable** and **verifiable**.
* No "trust us" privacy posture. We prefer "verify us."

### 3) No lock-in, including lock-in to us

We treat lock-in as an ethical failure--even if it makes us money.

Practical implications:

* Data export is not a checkbox. It must be **easy, complete, and routine**.
* You should be able to run without our servers.
* If Tech of Our Own disappears, your stuff should keep working.

### 4) Privacy by architecture, not policy

We minimize data collection because the best breach is the data you never collected.

Practical implications:

* Default to **local-first**.
* Minimize identity requirements.
* No "must create an account" to use your own hardware.
* If we ever offer hosted services, they must remain **optional** and **exit-friendly**.

### 5) Freedom to self-host and host for each other

Hosting is not a loophole to be tolerated; it's a core mode of operation.

Practical implications:

* "Host for your household" and "host for your neighbor" are first-class use cases.
* Systems should support partitioning, multi-user isolation, and sane admin UX.

### 6) Opposition to digital locks that remove user agency

DRM and anti-circumvention culture are the enemy of user autonomy.

Practical implications:

* We do not ship "remote bricking."
* We do not make products that *require* gatekeeper approval to remain functional.

### 7) Security is a baseline obligation

Security isn't a marketing bullet; it's duty of care.

Practical implications:

* Encryption in transit and at rest (where appropriate).
* Secure defaults.
* Clear threat model docs.
* Responsible vulnerability handling.

### 8) Governance and incentives matter more than heroics

We assume all systems drift toward extraction unless actively governed against it.

Practical implications:

* Transparent governance
* documented decision-making
* explicit rules for power (including the founder)
* mechanisms that make "quiet capture" hard

### 9) Transparency, including financial transparency

We don't ask for trust while hiding the balance sheet.

Practical implications:

* We aim for annual reports and open accounting practices.
* Members should be able to answer: "Where did the money go?"

### 10) We build for humans, not engagement metrics

We reject the attention-extraction playbook.

Practical implications:

* No dark patterns.
* No addiction loops as a business strategy.

---

## Our defaults

When we design products, write policies, or make tradeoffs, these are our "default settings."

### Default: Local-first, network-optional

* Works on your hardware.
* Works offline as much as possible.
* Network access expands capability, not dependence.

### Default: Open standards and portable formats

* If your data can't move, you don't own it.
* Prefer boring, documented formats over proprietary cleverness.

### Default: Modularity and repairability

* We favor designs that can be repaired and upgraded.
* Hardware should be maintainable with common tools where feasible.

### Default: Community knowledge compounds

* Docs are part of the product.
* We build systems where users help each other without needing a priesthood of experts.

---

## How we break ties in dilemmas

This section is the "you can actually use it" part.

When two good goals conflict, we choose in this order:

1. **User sovereignty** (can run, can leave, can verify)
2. **Safety & security** (harm prevention beats novelty)
3. **Transparency & auditability**
4. **Interoperability & portability**
5. **Long-term sustainability** (avoid brittle dependence on any single org, including us)
6. **Convenience & polish**
7. **Growth & adoption** (growth is a tool; not the mission)

A few concrete dilemma resolutions:

### "We could make onboarding magical if we route everyone through our servers..."

We prefer:

* optional relays
* user-owned domains
* clear "self-host / friend-host / co-op-host" paths
* an exit button that actually works

**We do not** make "magic" that creates silent dependence.

### "We could make more money by collecting telemetry / selling insights..."

We do not do that. Full stop.

If we need money:

* we sell hardware
* we sell support
* we charge transparently for hosting
* we accept donations
* we build co-op economics
  ...but we don't finance the mission by violating the mission.

### "We could ship faster if we keep parts closed..."

We accept slower shipping over closed core dependencies that undermine inspectability.

### "A big company wants to adopt and scale our work..."

Adoption is welcome. Poisoning is inevitable.
Our job is to make poisoning **visible**, **auditable**, and **easy to route around**.

### "An enterprise deal would fund everything, but they want control..."

We reject deals that distort governance or require exclusionary lock-in.

---

## What we refuse

This is our "red line" list.

* Selling user data, or building a business model dependent on surveillance
* Mandatory accounts for local use of user-owned hardware
* Dark patterns and addiction-driven engagement mechanics
* DRM that removes a user's ability to use what they own
* "Source available" theater that cannot be rebuilt or verified
* Hidden financials in a system asking for community trust
* Governance capture by outside investors at the expense of members/users
* Lock-in as a strategy (including lock-in to Tech of Our Own)

---

## What these values imply about licensing

Licenses are not the mission, but they are one enforcement lever.

Our licensing choices must support:

* inspectability of network-deployed software
* the ability to self-host
* freedom to fork
* freedom to host for others
* prevention of "secret SaaS forks" of the core

Practically, that usually means:

* strong reciprocity for networked core components (closing the SaaS loophole)
* permissive where it increases user freedom without enabling silent capture (e.g., some client edges)

(Exact decisions belong in a separate policy/ADR, but the *value* is: **no secret hosted modifications of the core**.)

---

## What these values imply about money

We want a way to make money with our heads held high.

That means:

* Profit is acceptable as **fuel**, not as the purpose.
* "Nice things" must be compatible with being "of our own"--collective benefit, not founder extraction.
* Pay must be fair, understandable, and bounded (see `PAY_RATIO_POLICY.md`).

If we ever feel pressure to enshittify to grow, we choose to grow slower.

---

## Founder values vs co-op values

The founder's job is to propose and protect the initial mission--then to gradually transfer power into durable governance that survives the founder.

Founder value commitments:

* build in public
* document power
* reduce bus factor
* treat canonical control as stewardship, not ownership

(Details live in `FOUNDER_STEWARDSHIP.md`.)

---

## Mapping to your policy folder

This values declaration should "plug into" your existing doc set like this:

* `MISSION.md` -> what we are here to do
* `VISION.md` -> what the future looks like if we succeed
* `CONSTITUTION.md` -> how power works, member rights, amendment process
* `BOARD_OPERATIONS.md` -> procedural integrity (how decisions happen)
* `FOUNDER_STEWARDSHIP.md` -> founder power limits, succession, keys
* `PAY_RATIO_POLICY.md` -> codifies fairness + prevents internal enshittification
* **this doc** -> how we decide when everything is a tradeoff

---

## Short version

If you need a "1-minute" version for the README or the landing page:

> We build technology that users can run, understand, and leave.
> We reject lock-in, surveillance business models, and digital coercion.
> We choose transparency, portability, and community governance over growth-at-all-costs.
> We will not finance this mission by betraying it.

---
