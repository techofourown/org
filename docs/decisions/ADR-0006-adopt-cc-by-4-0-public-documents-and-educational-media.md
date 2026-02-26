# ADR-0006: Adopt CC BY 4.0 for Tech of Our Own public documents and educational media

- **Date:** 2026-01-30
- **Status:** Draft (Founder proposal; intended to be ratified/amended by members via `CONSTITUTION.md`)
- **Deciders:** Founder (initial), future Board + Members (ratification/amendment)
- **Related:**
  - `../governance/VALUES.md` (Declaration of Values)
  - `../governance/CONSTITUTION.md`
  - `../ethos/Signs_and_Ancestrals.md` (example "commons" ethos doc)
  - `./ADR-0001-adopt-agplv3-core-software.md` (software licensing posture)
  - `./ADR-0005-adopt-cern-ohl-s-2-0-core-hardware-designs.md` (hardware licensing posture)

---

## Context

Tech of Our Own publishes more than software and hardware designs. We also publish “human-layer”
materials: founding documents, policies, decision records (ADRs), templates, ethos memos, guides, and
(soon) public education content such as podcasts and teaching series.

These materials are meant to be **read by the world**, referenced, taught, translated, and adapted.
We want them to function as a **common language** for humane technology — while remaining anchored
to their origin.

Our goals for these public materials are:

- **Adoption and reuse are encouraged** (including translations, annotations, remixes, and teaching).
- **Commercial use is allowed** (we do not want “non-commercial only” restrictions).
- **Attribution is required** so derivatives consistently point back to Tech of Our Own and/or the
  original authors as the source.
- People must be able to share improved or localized versions **without needing permission**.

We also want to avoid confusion about what is “official TOOO text” versus an adaptation. Even when
adaptations are encouraged, we want a clear “canonical source” for readers to verify.

Finally, we already use purpose-fit licenses for our other artifact types:

- **Core software**: AGPLv3 (ADR-0001)
- **Core hardware designs**: CERN-OHL-S-2.0 (ADR-0005)

We need an equally clear, widely understood license posture for **public documents and educational
media**.

---

## Decision

Tech of Our Own will license eligible public documents and educational media under:

### **Creative Commons Attribution 4.0 International (CC BY 4.0)**

- SPDX identifier: **`CC-BY-4.0`**
- License text: https://creativecommons.org/licenses/by/4.0/

### Meaning (plain English)

People may copy, share, translate, annotate, remix, and adapt our CC BY materials — including for
commercial purposes — as long as they:

- **give attribution** to the original source, and
- **indicate if changes were made**.

This aligns with our intent: these materials are a public commons gift, but the lineage must stay
visible.

---

## Scope

### 1) What this ADR covers

This ADR covers **public-facing, human-readable materials** that we intend the world to reuse and
adapt, including (non-exhaustive):

- governance and philosophy documents
- policies and standards meant to be read and referenced publicly
- ADRs, RFC templates, and organizational documentation
- ethos materials (including the Eight Signs / Ancestrels)
- educational and community materials (workshops, teaching series, guides)
- podcast-related collateral we publish (e.g., transcripts, show notes), when explicitly marked as
  CC BY

### 2) What this ADR applies to today (this repository)

As of this decision, **the content of this repository (`org-techofourown`) is treated as CC BY 4.0**
for public reuse and adaptation.

This includes (examples, not an exhaustive list):

- root documents like `README.md`, `CHANGELOG.md`
- all `docs/` content (governance documents, policies, ADRs, templates, ethos memos, requirements docs)

### 3) What is out of scope / excluded

This ADR does not decide (and does not change) licensing for:

- **software code** governed by ADR-0001 (AGPL posture for core software in product repos)
- **hardware design sources** governed by ADR-0005 (CERN-OHL posture for core hardware design repos)
- third-party works included in the repo that are not owned by TOOO (if any); those retain their
  upstream terms

### 4) Authoritative notices (explicitly not decided here)

Some future public communications may need to remain **verbatim and authoritative** (for safety,
security, or legal precision), such as:

- recalls
- service bulletins
- security advisories
- time-sensitive “official notices”

This ADR does **not** select a license posture for those materials. If/when TOOO begins publishing
that category, we will adopt a separate, explicit policy for “authoritative notices” (including how
translations are handled) via follow-up governance action.

---

## Rationale

CC BY 4.0 matches our stated requirements for public documents and educational media:

- **Reuse is the point:** translations, annotations, teaching, and adaptations are explicitly allowed.
- **Attribution is required:** derivatives must point back to the source, preserving provenance.
- **Commercial use is allowed:** the license does not restrict the ecosystem to non-commercial actors.
- **Widely understood:** CC BY is a common, standard license for writing/media, reducing friction for
  adopters.

This decision also supports our broader values:

- **The Sign of the Voice:** publish and teach so others can see and act.
- **Inspectability and transparency:** people can inspect, cite, and carry the text forward.
- **Exit and forkability (for ideas):** communities can adapt and continue without dependence on TOOO.

---

## Consequences

### Positive

- People and organizations can adopt TOOO’s written frameworks and educational materials without
  asking permission.
- Translations and localized versions become legally straightforward.
- A shared ethical language can spread beyond TOOO products and brand boundaries.
- Attribution requirements preserve lineage and make “where this came from” legible.

### Negative / Tradeoffs

- Third parties can commercially reuse our CC BY materials (e.g., sell a book or course that includes
  them), as long as attribution is provided.
- Adapted versions could circulate that are lower quality or misleading, even if they correctly
  attribute the source.
- Readers may confuse an adaptation with the canonical TOOO version unless we make canonical linking
  obvious.

---

## Options considered

### Option A: All rights reserved (default copyright)
- Rejected.
- Conflicts with our explicit goal of broad reuse, translation, and community adoption.

### Option B: CC0 (public domain dedication)
- Not chosen.
- CC0 maximizes reuse, but does not require attribution. We want the lineage to reliably point back
  to Tech of Our Own / original authors.

### Option C: CC BY-SA 4.0 (Attribution + ShareAlike)
- Not chosen (for now).
- ShareAlike can be valuable, but it adds an additional requirement that may reduce adoption by some
  organizations and complicate mixing with other materials. Our primary requirement is attribution,
  not ShareAlike reciprocity.

### Option D: CC BY-ND 4.0 (NoDerivatives)
- Rejected.
- NoDerivatives would block the very behaviors we want (translation, annotation, adaptation).

### Option E: CC BY-NC 4.0 (NonCommercial)
- Rejected.
- NonCommercial conflicts with our stated goal to allow commercial reuse while requiring attribution.

---

## Implementation notes

### 1) Repository hygiene (normative)

For `org-techofourown` and any future content-first repos (podcasts, teaching series) adopting this
policy:

- Include a top-level `LICENSE` file indicating **CC BY 4.0**.
- For major documents, include a short “License & Attribution” section near the top.

### 2) Preferred attribution (recommended standard)

We will provide a simple, copy-paste attribution format in each major document, e.g.:

- Title
- Author/Org (Tech of Our Own and/or credited authors)
- Canonical source URL
- License (CC BY 4.0 link)
- Change notice (for adaptations)

### 3) “No endorsement” note (recommended standard)

Where appropriate, documents should include:

> “Reuse does not imply endorsement by Tech of Our Own.”

This helps prevent confusion when third parties remix or reframe content.

---

## References

- CC BY 4.0 license: https://creativecommons.org/licenses/by/4.0/
- `../governance/VALUES.md`
- `../governance/CONSTITUTION.md`
- `./ADR-0001-adopt-agplv3-core-software.md`
- `./ADR-0005-adopt-cern-ohl-s-2-0-core-hardware-designs.md`
- `../ethos/Signs_and_Ancestrals.md`
