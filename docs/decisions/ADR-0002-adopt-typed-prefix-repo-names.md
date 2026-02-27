# ADR-0002: Adopt Typed Prefix Repository Naming Convention


## Context

Tech of Our Own will maintain many repositories over time covering fundamentally different kinds of
artifacts: organizational governance, software products, hardware designs, bootable images, websites,
facilities documentation, publications/educational media, and shared tooling.

As the repository count grows, a flat list of repos in a GitHub organization becomes harder to
navigate and easier to misinterpret. Ambiguous names increase the risk of confusion, misrouted work,
brittle automation, and support mistakes.

We want a naming scheme that is:

- **Self-classifying** at a glance (what kind of repo is this?)
- **Predictable** for new repos and teams
- **Stable** as new product lines appear
- **Not redundant**

### Key observation: the org name is already the namespace

Within GitHub, the organization name is already present in every URL:

`github.com/techofourown/<repo>`

Therefore, repeating `techofourown` inside repository names is redundant and adds noise without
adding classification value.

Example of redundancy:

- `github.com/techofourown/tool-techofourown-av` (redundant)
- `github.com/techofourown/tool-av` (clear)

This ADR updates the naming convention to treat the GitHub organization as the implicit namespace
and to keep repository names focused on *artifact type + meaningful identity*.

## Decision

Tech of Our Own will name repositories using a **typed prefix convention** so that the repository
name itself communicates the primary artifact type without requiring users to open the repo.

### 1) Repository names MUST use an approved typed prefix

Every repository name MUST begin with one of the approved prefixes in Appendix C (e.g., `sw-`,
`hw-`, `img-`, `pub-`, `tool-`).

### 2) Repository names MUST NOT include the org name as a token

Repository names MUST NOT include `techofourown` (or any org-name equivalent) as a name token.

- The GitHub org already provides the namespace.
- Adding it again does not improve clarity and reduces readability.

**Exceptions (rare):**
- GitHub-reserved repositories (e.g., `.github`) are exempt.
- Mirrors/forks where upstream naming constraints require it may be exempt, but SHOULD be documented
  in the README.

### 3) After the prefix, names use meaningful tokens

After the prefix, repository names are composed of **1 or more** hyphen-separated tokens that
describe what the repo is for.

Common patterns are defined in Appendix B.

### 4) Prefer product tokens only when they add clarity

Use a product token (e.g., `ourbox`) when it improves clarity. Do not add “scope” tokens that merely
restate the org namespace.

Examples:

- ✅ `sw-ourbox-os` (product token adds clarity)
- ✅ `img-ourbox-matchbox` (product token + device role)
- ✅ `tool-av` (org-wide tool; no product token needed)
- ✅ `pub-studio` (org-wide publications/canonical media artifacts)

### 5) Shared, cross-product repos MAY use the reserved token `common`

For repos that are intentionally shared across multiple products and/or multiple publication
projects, the reserved token `common` MAY be used to make that intent explicit:

- `lib-common-…`
- `tool-common-…`

Use `common` sparingly. If the repo is plainly org-wide by nature (e.g., general audio/video
utilities), `common` is optional.

## Rationale

Typed prefixes keep large organizations navigable and reduce operational risk:

- Humans can tell what a repo contains without opening it.
- Automation can apply policies based on repo type (CI templates, CODEOWNERS, release rules).
- Naming remains stable even as the org adds products, device families, and new artifact types.

Removing the org name from repo names keeps the scheme **legible and non-redundant**, and matches how
real-world namespaces work: the org already tells you “this is Tech of Our Own.”

A small controlled vocabulary of prefixes prevents naming drift while still allowing growth. Adding
new prefixes should be deliberate (via ADR update) rather than ad-hoc.

## Consequences

### Positive

- Repository purpose is immediately clear from the name (software vs hardware vs publications vs
  tools).
- Names are shorter and more readable because the org name is not duplicated.
- Scales cleanly as new products and publication lines appear.
- Enables predictable automation and governance by repo type.

### Negative

- Requires discipline: new repos must follow the convention instead of ad-hoc naming.
- Edge cases will appear (repos spanning multiple artifact types) and can trigger debate.
- Existing repos that include `techofourown` in their name may look “legacy” relative to the new
  rule.

### Mitigation

- Maintain this ADR as the canonical reference and include a short “Naming Cheatsheet” in the GitHub
  org README.
- Use a lightweight review checklist for new repo creation (prefix, tokens, target/variant).
- For legacy repos that include the org name, prefer **gradual, opportunistic renames** when the
  value is worth it. GitHub preserves redirects on rename; document the rename in the repo CHANGELOG
  or README.

---

## Appendix A: Global Naming Rules (Normative)

1. **Lowercase only** (`a–z`, `0–9`) except GitHub-reserved repositories (e.g., `.github`).
2. **Hyphen-separated tokens**; no spaces, underscores, or periods.
3. **Typed prefix required** (Appendix C).
4. **No org-name tokens** inside repo names (e.g., do not include `techofourown`).
5. **No redundant type words** inside the name (the prefix already conveys type).
6. Keep names **descriptive but concise**; avoid encoding metadata better expressed as tags,
   releases, or docs.
7. If a repo genuinely spans multiple artifact types, choose the prefix based on the **primary
   artifact**, document boundaries in the README, and split later if needed.

---

## Appendix B: Name Shapes by Repository Type (Normative)

> Notation: tokens in `<>` are placeholders; `[]` are optional.

1) **General (most repos)**  
   `"<type>-<name>"`  
   Where `<name>` is one or more hyphen-separated tokens.

   Examples: `tool-av`, `org-control-plane`, `sec-disclosure`

2) **Product repos (recommended when product context matters)**  
   `"<type>-<product>-<component>"`

   Examples: `sw-ourbox-os`, `hw-ourbox-matchbox`

3) **Explicitly shared repos (optional)**  
   `"<type>-common-<component>"`

   Examples: `tool-common-av`, `lib-common-crypto`

4) **Images**
   ` "img-<product>-<device|role>[-<target>][-<variant>]"`

   Examples: `img-ourbox-matchbox`, `img-ourbox-tinderbox`, `img-ourbox-mini-rpi5-debug`

5) **Firmware**  
   ` "fw-<product>-<device|role>-<target>[-<variant>]"`

   Examples: `fw-ourbox-matchbox-rpi`, `fw-ourbox-ec-amd64`

6) **Libraries / SDKs (optional language token)**  
   `"<lib|sdk>-<name>[-<lang>]"`  
   or product-scoped: `"<lib|sdk>-<product>-<name>[-<lang>]"`

   Examples: `lib-ourbox-formats-ts`, `sdk-ourbox-js`

---

## Appendix C: Approved Type Prefixes (Normative)

The following prefixes are approved for repository names:

- `org-` — Organization/institution repositories (governance, policies, procedures)
- `fac-` — Facilities/buildings/sites documentation
- `sw-` — Software product repositories
- `hw-` — Hardware design repositories
- `pf-` — Product family repositories (cross-cutting family specs, surveys, decisions, naming, BOMs)
- `img-` — Bootable image recipes and image build systems
- `fw-` — Firmware repositories
- `ops-` — Operations/deployment configuration repositories (e.g., GitOps)
- `iac-` — Infrastructure-as-code repositories
- `pub-` — Publications and educational media (transcripts, show notes, books, manuals, curricula)
- `lib-` — Internal shared libraries intended for imports by our code
- `sdk-` — SDKs intended for external/partner use or explicitly supported developer surfaces
- `web-` — Websites (org or product)
- `merch-` — Merchandise and brand physical goods assets
- `tool-` — Tooling (build/test/automation/media pipelines) not itself a product runtime
- `sec-` — Security/trust artifacts (threat models, disclosure tooling, posture docs)
- `sandbox-` — Experiments/prototypes not intended to be confused with supported products

Adding new prefixes requires an ADR update (or a superseding ADR) to prevent drift.

---

## Appendix D: Token Conventions (Normative)

1) **Product tokens** (examples)
- `ourbox`
- `ourphone`
- `ourauto`
- `ourbot`

Use a product token when it adds clarity. Do not use the org name as a token.

2) **`common` token**
- `common` is reserved for intentionally shared repos across multiple products/projects.

3) **Target tokens** (examples)
- Hardware/platform: `rpi`, `rpi4`, `rpi5`
- Architecture: `arm64`, `amd64`
- Cloud: `aws`, `gcp`, `azure`

4) **Variant tokens** (examples)
- `minimal`, `debug`, `hardened`, `lts`, `dev`

---

## Appendix E: Canonical Examples (Informative)

Preferred examples (new scheme):

- `org-control-plane`
- `sw-ourbox-os`
- `pf-ourbox`
- `hw-ourbox-matchbox`
- `img-ourbox-matchbox`
- `img-ourbox-woodbox`
- `web-site`
- `pub-studio`
- `tool-av`
- `tool-common-av`
- `sec-disclosure`
- `sandbox-lab-notes`

Legacy examples (allowed but discouraged going forward):

- `org-techofourown`
- `web-techofourown`

Legacy repos MAY be renamed over time when beneficial; GitHub redirects make renames low-risk, but
documentation and references should be updated deliberately.
