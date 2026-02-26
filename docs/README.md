# Documentation

This directory holds all project documentation, organized by purpose and lifecycle.

## Structure

```
docs/
├── governance/    # Mission, vision, values, constitution, board operations
├── policies/      # Organizational principles, standards, and rules
├── decisions/     # Architecture Decision Records (ADRs)
├── rfcs/          # Pre-decisional exploration and proposals
├── ethos/         # Shared language and cultural principles
└── requirements/  # System/interface requirements and verification (optional)
```

## When to use what

- **Governance (`governance/`)** — mission lock and power structure (constitution, board rules).
- **Policies (`policies/`)** — ongoing rules, constraints, and standards that are enforceable.
- **ADRs (`decisions/`)** — record a decision that was made, with context, rationale, consequences, and links to any originating RFC.
- **RFCs (`rfcs/`)** — explore ideas or proposals before deciding; capture options, trade-offs, and open questions.
- **Ethos (`ethos/`)** — shared language, principles, and cultural memos.
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
