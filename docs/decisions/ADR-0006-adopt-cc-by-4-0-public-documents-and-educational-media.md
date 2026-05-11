# ADR-0006: Adopt CC BY 4.0 for Tech of Our Own public documents, standards, and educational media

- **Date:** 2026-01-30
- **Updated:** 2026-05-11
- **Related:**
  - `../governance/VALUES.md` (Declaration of Values)
  - `../governance/CONSTITUTION.md`
  - `../ethos/Signs_and_Ancestrals.md` (example "commons" ethos doc)
  - `./ADR-0001-adopt-agplv3-core-software.md` (software licensing posture)
  - `./ADR-0005-adopt-cern-ohl-s-2-0-core-hardware-designs.md` (hardware licensing posture)

---

## Context

Tech of Our Own publishes more than software and hardware designs. We also publish “human-layer”
materials: founding documents, policies, decision records (ADRs), templates, ethos memos, guides,
public standards, and public education content such as podcasts and teaching series.

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

For standards specifically, this decision is about making the text of the standard easy to copy,
mirror, quote, translate, annotate, teach, index, and adapt with attribution. It is not a decision to
optimize TOOO standards for patent holders, proprietary enclosure, closed compatibility gates, or
corporate adoption at the expense of user sovereignty.

Finally, we already use purpose-fit licenses for our other artifact types:

- **Core software**: AGPLv3 (ADR-0001)
- **Core hardware designs**: CERN-OHL-S-2.0 (ADR-0005)

We need an equally clear, widely understood license posture for **public documents, standards, and
educational media**.

---

## Decision

Tech of Our Own will license eligible public documents, standards text, and educational media under:

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

For TOOO standards, CC BY 4.0 applies to the standards text and closely related publication material:
prose, tables, diagrams, examples, definitions, explanatory material, non-executable metadata, and
document-generation sources whose primary purpose is producing or validating the public standard,
unless a more specific license notice says otherwise.

This ADR does **not** grant patent rights, trademark rights, endorsement rights, certification
rights, compatibility-mark rights, or official-status rights.

That is intentional.

TOOO standards are published so people can build, inspect, fork, interoperate, and route around
capture. They are not published to create patent toll roads, official-mark traps, or proprietary
compatibility gates.

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
- document-generation sources whose primary purpose is producing, validating, or publishing covered
  public documents or standards, unless separately licensed

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
- reference implementations, SDKs, conformance harnesses, runtimes, or reusable tools unless
  explicitly marked otherwise
- TOOO trademarks, logos, product names, standard names, certification marks, compatibility marks, or
  official-status claims
- patents or patent claims
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

CC BY 4.0 matches our stated requirements for public documents, standards, and educational media:

- **Reuse is the point:** translations, annotations, teaching, and adaptations are explicitly allowed.
- **Attribution is required:** derivatives must point back to the source, preserving provenance.
- **Commercial use is allowed:** the license does not restrict the ecosystem to non-commercial actors.
- **Widely understood:** CC BY is a common, standard license for writing/media, reducing friction for
  reuse.

For standards, this is a document-layer decision. It makes the text of the standard part of the
commons. It does not turn TOOO standards into a patent-holder accommodation program, and it should
not be reinterpreted later as a problem to solve by making standards easier to enclose.

This decision also supports our broader values:

- **The Sign of the Voice:** publish and teach so others can see and act.
- **Inspectability and transparency:** people can inspect, cite, and carry the text forward.
- **Exit and forkability (for ideas):** communities can adapt and continue without dependence on TOOO.
- **Resistance to enclosure:** standards text can spread without turning official status, patents, or
  compatibility claims into tools of capture.

---

## Consequences

### Positive

- People and organizations can adopt TOOO’s written frameworks and educational materials without
  asking permission.
- Translations and localized versions become legally straightforward.
- A shared ethical and technical language can spread beyond TOOO products and brand boundaries.
- Attribution requirements preserve lineage and make “where this came from” legible.
- TOOO standards text can spread as part of the commons while keeping the anti-enclosure posture
  explicit.

### Negative / Tradeoffs

- Third parties can commercially reuse our CC BY materials (e.g., sell a book or course that includes
  them), as long as attribution is provided.
- Adapted versions could circulate that are lower quality or misleading, even if they correctly
  attribute the source.
- Readers may confuse an adaptation with the canonical TOOO version unless we make canonical linking
  obvious.
- Some patent holders, proprietary implementers, or closed vendors may dislike that TOOO does not
  optimize standards policy around their adoption comfort.

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

### Option F: Corporate-friendly standards adoption posture
- Rejected.
- TOOO does not publish standards to maximize adoption by patent holders, closed vendors, gatekeepers,
  or proprietary platform operators.
- TOOO welcomes implementation when it increases user sovereignty, interoperability, inspectability,
  portability, and forkability.
- TOOO rejects changes whose main purpose is to make standards easier to use as patent toll roads,
  compatibility traps, official-mark traps, or proprietary enclosure mechanisms.

---

## Implementation notes

### 1) Repository hygiene (normative)

For `org-techofourown` and any future content-first repos (podcasts, teaching series, standards)
adopting this policy:

- Include a top-level `LICENSE` file indicating **CC BY 4.0**.
- For major documents, include a short “License & Attribution” section near the top.
- Clearly mark any files or directories that are not covered by the CC BY document-layer default.

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

### 4) Future standards policy (normative direction)

Any future TOOO standards-publication policy must preserve the distinction between:

- freedom to reuse the standards text,
- permission to claim official TOOO status,
- permission to use TOOO marks,
- patent or patent-assertion posture,
- and conformance or compatibility claims.

This ADR must not be used later to argue that TOOO standards should be made more comfortable for
patent enclosure or proprietary compatibility gates.

---

## References

- CC BY 4.0 license: https://creativecommons.org/licenses/by/4.0/
- `../governance/VALUES.md`
- `../governance/CONSTITUTION.md`
- `./ADR-0001-adopt-agplv3-core-software.md`
- `./ADR-0005-adopt-cern-ohl-s-2-0-core-hardware-designs.md`
- `../ethos/Signs_and_Ancestrals.md`