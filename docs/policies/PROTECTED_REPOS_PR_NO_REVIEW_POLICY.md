# Protected Repositories: PR Required, Review Optional (Single-Author Phase)
**Draft v1.0**

## Purpose
This policy defines how branch protection is configured during TOOO's current
single-author operating phase. It preserves change control and auditability
without creating a fake reviewer requirement when there is only one maintainer.

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
3. Required approving reviews are set to `0` while TOOO is operated by a single
   author.
4. Required status checks may still be enforced independently.
5. Admin enforcement on protected branches may remain enabled.

## Why
Even with one maintainer, required PRs provide:
- an auditable change record with intent and rationale
- consistent CI execution before merge
- predictable release and change-management workflow
- easier future transition to multi-author collaboration

Requiring approvals from non-existent reviewers adds no safety and only blocks
necessary maintenance.

## Relationship to Automation Exception Policy
TOOO may separately allow specific automation actors (for example,
`semantic-release`) to bypass PR requirements in tightly scoped cases.

That exception is defined by a separate policy and is unaffected by this
document.

## Trigger for Re-evaluation
This policy must be re-evaluated when TOOO moves out of the single-author
phase, including when any additional write-capable maintainer becomes active on
protected repositories.

At that point, required approving reviews should be raised from `0` to a
minimum of `1`, unless superseded by an updated policy.
