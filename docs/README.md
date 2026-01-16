# Documentation

This directory holds all project documentation, organized by purpose and lifecycle.

## Structure

```
docs/
├── rfcs/          # Pre-decisional exploration and proposals
├── decisions/     # Architecture Decision Records (ADRs)
├── policies/      # Governance, standards, and principles (includes founding docs)
└── requirements/  # System/interface requirements and verification (optional)
```

## When to use what

- **RFCs (`rfcs/`)** — explore ideas or proposals before deciding; capture options, trade-offs, and open questions.
- **ADRs (`decisions/`)** — record a decision that was made, with context, rationale, consequences, and links to any originating RFC.
- **Policies (`policies/`)** — organizational principles and standards; founding documents now live in `docs/policies/founding/`.
- **Requirements (`requirements/`)** — only if you need traceability (system/ICD/verification); otherwise ignore.

## Flow

```
Problem or Idea
    ↓
RFC (exploration) → Discussion → Decision
    ↓                              ↓
Implementation               ADR (record)
```

## Conventions

- **Numbering + slugs**: `RFC-0001-descriptive-slug.md` and `ADR-0001-descriptive-slug.md` (zero-padded, short hyphenated slug).
- **Status**: RFCs use `Draft | Discussion | Accepted | Rejected | Withdrawn`; ADRs use `Proposed | Accepted | Deprecated | Superseded` (with backlinks).
- **Cross-links**: ADRs link to source RFCs/issues and any supersedes/superseded-by records; RFCs link to related ADRs when promoted.
- **Change control**: create/update RFCs and ADRs via PRs. Keep them concise; prefer follow-up ADRs to massive edits.
