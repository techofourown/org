# Protected Repositories: PR Required, Admin Enforced, No Required Review (Single-Author Phase)
**Draft v1.2**

## Purpose
This policy defines how branch protection is configured during TOOO's current
single-author operating phase. It enforces a mandatory PR workflow for all human
changes, preserves a full audit trail, and keeps the sole maintainer unblocked —
without using bypass mechanisms that defeat the PR requirement itself.

## Scope
This policy applies to repositories that are already designated as protected.

This policy does **not** define:
- which repositories must be protected
- who may administer protection settings

Those decisions remain out of scope for this document.

## Policy
For protected repositories under GitHub classic branch protection:

1. Pull requests to protected branches are required for all human changes.
2. Direct human pushes to protected branches are disallowed.
3. Admin enforcement (`enforce_admins`) must be **enabled**. Admins are subject to
   the same PR requirement as all other contributors.
4. Required approving reviews are set to `0`. The sole maintainer may merge their
   own PR without a second reviewer.
5. Required status checks may still be enforced independently.
6. `bypass_pull_request_allowances` is reserved exclusively for approved automation
   actors (see `PROTECTED_BRANCH_RELEASE_AUTOMATION_POLICY.md`). Human maintainers
   must not be added to this list.

## Why enforce_admins must be enabled

Disabling `enforce_admins` does not produce a "review-only bypass." It produces a
**full branch-protection bypass**, including the PR requirement. An empirical test
confirmed that with `enforce_admins=false`, a repository administrator can push
commits directly to a protected branch with no PR, no review, and no CI run. GitHub
acknowledges this explicitly in the remote output:

> Bypassed rule violations for refs/heads/main: Changes must be made through a pull request.

This is unsafe and defeats the audit model this policy exists to enforce.
`enforce_admins=false` is therefore **prohibited** for human workflows on protected
repositories.

## Why required reviews are set to 0

With `enforce_admins` enabled, setting `required_approving_review_count` to 1 would
lock the sole maintainer out of merging entirely, since there is no second person to
provide a review. Requiring an approval from a non-existent reviewer adds no safety
and blocks necessary maintenance.

The friction in this model comes from the mandatory PR itself: every change requires
an explicit PR, CI execution, and a deliberate merge action. That is sufficient for
the single-author phase.

## What this achieves

- Every human change lands via a PR, creating an auditable record with intent and CI results.
- No human maintainer (including admins) can silently push directly to a protected branch.
- The sole maintainer can merge their own PR once status checks pass, without being
  blocked on an unavailable reviewer.
- The release automation bot retains its narrow, scoped bypass for direct release
  commits as defined separately.

## Relationship to Automation Exception Policy
TOOO may allow specific automation actors (for example, `semantic-release`) to bypass
PR requirements in tightly scoped cases. That exception is defined in
`PROTECTED_BRANCH_RELEASE_AUTOMATION_POLICY.md` and is unaffected by this document.

## Future refinement: GitHub Rulesets
GitHub Rulesets may support more granular bypass control, potentially allowing a model
where a human maintainer can bypass the *review requirement* specifically while the
*PR requirement* still applies to them. If TOOO adopts Rulesets, this policy should be
updated after validating that:
1. Human direct push to `main` is blocked.
2. Human PR merge without approval is allowed.
3. Human PR merge before status checks pass is blocked.
4. Release bot direct release write still works.

Until that is validated in a test repository, the classic branch protection model
described above is the required configuration.

## Trigger for Re-evaluation
This policy must be re-evaluated when:
- TOOO moves out of the single-author phase (raise `required_approving_review_count`
  from 0 to at least 1 when a second active maintainer joins).
- TOOO adopts GitHub Rulesets and validates the more granular bypass model described
  above.
