
# ADR-0016: Establish the Tech of Our Own Standards Publication System

- **Date:** 2026-05-11
- **Status:** Accepted
- **Related:**
  - `../governance/VALUES.md`
  - `../governance/CONSTITUTION.md`
  - `./ADR-0002-adopt-typed-prefix-repo-names.md`
  - `./ADR-0003-standardize-naming-across-artifacts.md`
  - `./ADR-0006-adopt-cc-by-4-0-public-documents-and-educational-media.md`

---

## Context

Tech of Our Own is beginning to publish documents that are not merely internal
governance records, software documentation, hardware documentation, public
education materials, or implementation notes.

They are standards.

A TOOO standard is intended to be a public, durable, citable, versioned
document that defines an interoperability, conformance, practice, or publication
boundary that independent people, tools, runtimes, devices, agents, and
organizations can implement or rely on.

The immediate pressure comes from the Portable Application Kernel standard.

PAK is expected to become the first major TOOO technical standard family. It is
also expected to grow into many parts. Before that growth happens, TOOO needs a
publication system that defines how standards themselves are identified,
numbered, structured, revised, cited, licensed, and maintained.

This decision is not about the final structure of PAK.

This decision is not about assigning a standard number to PAK.

This decision is not about adding any technical capability to PAK or any other
standard.

This decision is about creating the standards publication system itself and
assigning it the root standards identity.

TOOO already has organizational mechanisms for recording decisions. This ADR
records the organization-level decision to establish a standards publication
system. The standards publication system itself will be defined as a TOOO
standard.

---

## Decision

Tech of Our Own will establish a dedicated standards publication system.

The standards publication system is assigned the standard-family identity:

```text
TOOO STD 0000
````

The title of this standard family is:

```text
Tech of Our Own Standards Publication System
```

`TOOO STD 0000` is the root meta-standard for TOOO standards.

It owns the rules for how TOOO standards are:

* identified
* numbered
* structured
* published
* cited
* revised
* superseded
* withdrawn
* licensed
* distinguished from non-standard documents
* and maintained as public standards

Future TOOO standards must be created, assigned, published, and maintained
through the standards publication system defined by `TOOO STD 0000`.

This ADR does not assign any other TOOO standard-family number.

In particular, this ADR does not assign a final standard number to the Portable
Application Kernel. PAK is expected to become a TOOO standard family, but that
assignment will be recorded separately after the publication system exists.

---

## Scope

This ADR applies to:

* TOOO public standards
* TOOO standards families
* the organization-level decision to create a standards publication system
* the assignment of `TOOO STD 0000` to that system

This ADR does not decide:

* the full contents of `TOOO STD 0000`
* the final part-numbering system for TOOO standards
* the final standard number for PAK
* the final repository layout for standards repositories
* the detailed publication status model
* the detailed conformance model
* the detailed trademark or compatibility-claim policy
* any new technical feature for PAK or any other standard

Those decisions belong in `TOOO STD 0000` or in later ADRs.

---

## Rationale

### 1) Standards need a system before they multiply

A single standard can survive with ad hoc structure for a while.

A family of standards cannot.

TOOO expects to publish standards in multiple domains over time, potentially
including software, runtimes, hardware, memory systems, model-training records,
operations, workplace practices, identity, provenance, and other technical or
organizational systems.

Without a common standards publication system, each standard family would invent
its own numbering, status labels, citation style, revision rules, licensing
notices, conformance language, and publication artifacts.

That would create drift exactly where TOOO needs durability.

### 2) The publication system should itself be a standard

The rules for standards should not be scattered across informal notes,
repository READMEs, or one-off decisions.

They should be defined in a public standard.

Assigning the publication system as `TOOO STD 0000` makes it the root standard
for standards. It becomes the place future readers can look to understand how
TOOO standards are supposed to exist.

### 3) `0000` is the right root identity

The `0000` family number communicates that this is not just another technical
standard.

It is the standards-system standard.

It is the document family that defines the rails for other TOOO standards.

### 4) PAK should not define the standards system for itself

PAK is the first major pressure point, but it should not be allowed to invent
rules that only work for PAK.

TOOO needs a publication architecture that can support PAK and future standards
that may look very different from PAK.

The standards system should come first.

### 5) This keeps the ADR focused

This ADR makes one organization-level decision:

```text
Create the TOOO standards publication system and assign it TOOO STD 0000.
```

It deliberately avoids packing in separate decisions about PAK numbering,
repository names, part bands, conformance classes, patent policy, certification
marks, or future standard-family assignments.

Those can be decided later, cleanly.

---

## Consequences

### Positive

* TOOO gets a root publication system for standards before standards multiply.
* Future standards can share a common identity, numbering, revision, and
  publication architecture.
* PAK can be reorganized under a TOOO-wide system rather than inventing a
  PAK-only structure.
* The standard system itself becomes public, citable, and inspectable.
* Future readers can distinguish standards from ADRs, policies, software docs,
  hardware docs, and educational publications.

### Negative / Tradeoffs

* TOOO must write `TOOO STD 0000` before major standards expansion.
* Some work that could have gone directly into PAK must pause while the
  publication system is established.
* The standards system introduces formality earlier than a small project would
  normally need.
* Poorly scoped follow-up work could make the standards system too large too
  soon.

### Mitigation

* Keep the first edition of `TOOO STD 0000` small.
* Use PAK as the first concrete test case, but do not let PAK be the only
  design target.
* Prefer focused follow-up ADRs over packing many standards-system decisions
  into this ADR.
* Treat detailed numbering, repository layout, conformance, and publication
  artifacts as follow-up decisions or as content of `TOOO STD 0000`.

---

## Options considered

### Option A: Do nothing and let each standard family invent its own structure

Rejected.

This would create naming, numbering, publication, and conformance drift across
TOOO standards.

### Option B: Put standards-system rules only in ADRs or policies

Rejected.

ADRs are good for recording decisions. Policies are good for ongoing
organizational rules.

But standards publication rules should themselves be public, citable, and
structured as a standard.

### Option C: Let PAK define the standards-system rules inside the PAK standard

Rejected.

PAK should follow the TOOO standards publication system, not become the
publication system.

### Option D: Establish `TOOO STD 0000` as the standards publication system

Accepted.

This gives TOOO a root standard for standards and keeps future standards
families from growing ad hoc.

---

## Implementation notes

### 1) Create the first draft of `TOOO STD 0000`

The next step is to draft the first minimal version of:

```text
TOOO STD 0000 — Tech of Our Own Standards Publication System
```

That draft should define only the standards-system rules that are needed to
begin publishing TOOO standards coherently.

### 2) Keep PAK separate for now

PAK should not be renumbered or expanded inside this ADR.

A later PAK-specific decision should assign PAK its standard-family identity and
perform any needed structural reset under the rules of `TOOO STD 0000`.

### 3) Keep repository naming separate

This ADR does not itself revise the repository naming ADRs.

If creating standards repositories requires new or updated repository naming
rules, those changes should be handled by the relevant naming ADRs or follow-up
governance action.

### 4) Preserve the existing licensing posture

This ADR does not change TOOO's existing public-document licensing posture.

Standards text remains governed by the applicable TOOO licensing decisions,
including ADR-0006, unless a later explicit decision says otherwise.

---

## Future changes

The following require follow-up governance action:

* reassigning `TOOO STD 0000` away from the standards publication system
* abandoning the TOOO standards publication system
* creating TOOO standards outside the authority of `TOOO STD 0000`
* assigning a standard-family number to PAK or any other standard family
* adopting a final standards repository layout
* adopting final TOOO standard-family numbering bands
* adopting official conformance, certification, compatibility-mark, or
  standards-status rules

The following do not require superseding this ADR:

* drafting the initial parts of `TOOO STD 0000`
* refining the title or internal structure of `TOOO STD 0000`
* creating a repository to hold the standards publication system
* using PAK as the first test case for the publication system
* adding implementation details that remain consistent with the decision to
  establish `TOOO STD 0000` as the root standards publication system

---

## References

* `../governance/VALUES.md`
* `../governance/CONSTITUTION.md`
* `./ADR-0002-adopt-typed-prefix-repo-names.md`
* `./ADR-0003-standardize-naming-across-artifacts.md`
* `./ADR-0006-adopt-cc-by-4-0-public-documents-and-educational-media.md`


