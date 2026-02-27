# Protected Branch Release Automation Policy

**Draft v1.0**

## Purpose

This policy defines how TOOO performs automated releases (using **semantic-release**) without weakening the security posture of **protected, pull-request-only branches**. It creates a narrow, auditable exception that allows release automation to publish tags/releases and (optionally) commit generated release artifacts, while keeping “humans must use PRs” as the default rule.

## Scope

This policy applies to any TOOO repository where:

* one or more branches are configured as **protected** and **pull-request-only**, and
* **semantic-release** is used to publish releases from those branches.

Out of scope for this policy:

* when and why a branch becomes protected
* which branches are selected as release branches (that decision is repo-specific)

## Definitions

**Protected PR-only branch**  
A branch with rules that require changes to be made through pull requests (e.g., “Require a pull request before merging” and/or equivalent rulesets).

**Release workflow**  
A GitHub Actions workflow that runs semantic-release to:

* determine the next version from conventional commits,
* create/push a tag, and
* create/update a GitHub Release, and optionally
* commit generated release artifacts back to the release branch (e.g., `CHANGELOG.md`).

**Release App**  
A dedicated GitHub App used solely to perform release writes that would otherwise be blocked by PR-only protection.

**Release token**  
A short-lived installation token minted at workflow runtime from the Release App and used for:

* authenticated git pushes (branch and tags)
* GitHub API calls made by semantic-release

**Release write**  
Any direct write to a protected PR-only branch or its tags performed by automation, including:

* pushing a release commit to the branch
* pushing tags
* creating/updating a GitHub Release

**Allowed release artifacts**  
The explicit list of files that release automation is permitted to modify and commit (repo-defined; commonly `CHANGELOG.md` and version files).

## The rule

1. **Humans do not push directly** to protected PR-only branches. All human changes must land via pull request.
2. **The only permitted direct pushes** to a protected PR-only branch are **Release writes** performed by the Release workflow using the **Release App token**.
3. The default **`GITHUB_TOKEN` must not be used** to perform Release writes to protected PR-only branches.
4. The exception for release automation must be **minimal and scoped**:

   * scoped to the specific release branch(es) for that repo
   * scoped to the smallest bypass necessary (PR-only requirement bypass only)
   * attributable to a single automation identity (the Release App)

## Required controls

### Release App controls

* **Dedicated automation identity**
  Release writes must use a GitHub App created for release automation. Personal access tokens tied to human accounts are not permitted for protected-branch release bypass.

* **Least privilege**
  The Release App must have the minimum repository permissions required:

  * Minimum required: **Contents: Read & write**
  * Optional, only if needed by the chosen semantic-release plugins: **Issues**, **Pull requests**, etc.
  * No unnecessary permissions (especially admin-level permissions).

* **Install scope**
  The Release App must be installed only on repositories that use it.

* **Bypass scope**
  The Release App may be granted bypass only for the PR-only requirement and only for the specific release branch(es) where releases are published. Broad or organization-wide bypass is not allowed.

* **Credential handling and lifecycle**

  * The App private key must be stored as a GitHub Actions secret and must never be committed to git.
  * Tokens must be minted at runtime and are short-lived.
  * No token material may be written to build artifacts or logs.
  * Keys/tokens must be rotated immediately on suspected exposure and on a regular cadence (at least annually).

### Workflow controls

* **Trusted execution context**
  Any workflow that performs Release writes must run from the protected release branch context (e.g., `on: push` to the release branch). Release writes must not depend on untrusted code paths for execution.

* **Token usage requirements**

  * The checkout step must use the Release token so git operations use the Release App identity.
  * semantic-release must use the Release token for GitHub API calls.
  * Workflow permissions for `GITHUB_TOKEN` should remain minimal where feasible (read-only), since the Release App token is used for Release writes.

* **No user-controlled push behavior**
  Release workflows must not accept user-provided inputs that influence:

  * which remote is pushed to
  * which branch is pushed
  * which files are committed
  * arbitrary shell commands that run before push

* **Concurrency**
  Release workflows must be serialized per release branch to prevent race conditions (double-tagging, conflicting release commits).

### Change surface controls

* **Allowed release artifacts only**

  * Release commits may only include files on the repo’s **Allowed release artifacts** list.
  * Release commits must not include functional code changes.

* **Release commit clarity**

  * Release commit messages must clearly identify that they are automated release commits (e.g., `chore(release): X.Y.Z`).
  * Release commits must not be used to smuggle unrelated changes.

* **Tag discipline**

  * Tags must follow semantic versioning (e.g., `vX.Y.Z`).
  * Published tags are treated as immutable. Deleting or moving a published tag is prohibited except under the exception process.

## Audit and traceability

* Every release must be traceable to:

  * a specific workflow run
  * a specific git tag and/or GitHub Release
  * the Release App identity that performed the write

* Each repository using protected-branch release automation must maintain a minimal record (in-repo or centrally) of:

  * the release branch(es)
  * the Release workflow path/name
  * the Release App name/identifier
  * the Allowed release artifacts list

* Permissions and bypass scope must be reviewed periodically (at least quarterly) to confirm:

  * the Release App remains least-privilege
  * bypass scope is not broader than necessary
  * release commits stay within Allowed release artifacts

## Exceptions

Exceptions are allowed only to remediate release integrity or security issues (e.g., incorrect tag, failed release commit, compromised credentials) and must:

* be approved by repository administrators and the org security owner
* be documented with reason, impact, and corrective actions
* include credential rotation if the exception involves suspicious activity or secret exposure

## Enforcement

* Repository administrators are responsible for:

  * keeping protected branches PR-only for humans
  * ensuring only the Release App has the minimal bypass required

* Platform/Security is responsible for:

  * Release App credential lifecycle (storage, rotation, revocation)
  * permission reviews and incident response related to release automation

* Violations require immediate remediation:

  * revert unauthorized changes
  * revoke/rotate credentials if applicable
  * reduce permissions/bypass scope to compliant levels
  * disable release automation until controls are restored
