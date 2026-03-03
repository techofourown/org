# Protected Repositories: PR Required, Review Gate with Admin Override (Single-Author Phase)
**Draft v1.1**

## Purpose
This policy defines how branch protection is configured during TOOO's current
single-author operating phase. It creates a deliberate review gate on every PR
while preserving the sole maintainer's ability to consciously override that gate
when acting as the authoritative decision-maker.

## Scope
This policy applies to repositories that are already designated as protected.

This policy does **not** define:
- which repositories must be protected
- who may administer protection settings

Those decisions remain out of scope for this document.

## Policy
For protected repositories:

1. Pull requests to protected branches are required.
2. Direct pushes to protected branches are disallowed.
3. Required approving reviews are set to `1`.
4. Admin enforcement (`enforce_admins`) must be **disabled**, so that a repository
   administrator can override the review requirement when acting as sole maintainer.
5. Required status checks may still be enforced independently.

## Why
Required PRs provide an auditable change record, consistent CI execution, and a
predictable workflow. Setting required reviews to `1` adds a deliberate friction
point — the maintainer must consciously act to merge, rather than merging silently.

With `enforce_admins` disabled, the sole maintainer is never locked out: they can
use the "Merge without waiting for requirements" override when appropriate. This is
a conscious action, not a silent bypass, and it preserves the audit trail in the
PR record.

This model is preferred over `0` required reviews because it makes the merge a
deliberate, visible decision rather than a frictionless default. When a second
maintainer joins, the override becomes genuinely meaningful — the maintainer is
choosing to override an external review, not merely acknowledging their own PR.

## Relationship to Automation Exception Policy
TOOO may separately allow specific automation actors (for example,
`semantic-release`) to bypass PR requirements in tightly scoped cases.

That exception is defined by a separate policy and is unaffected by this
document.

## Trigger for Re-evaluation
This policy must be re-evaluated when TOOO moves out of the single-author
phase, including when any additional write-capable maintainer becomes active on
protected repositories.

At that point, `enforce_admins` should be re-evaluated — disabling it grants
bypass to all administrators, which is appropriate for a sole maintainer but
may be too broad once the team grows.
