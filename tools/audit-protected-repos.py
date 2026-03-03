#!/usr/bin/env python3
"""
Audit live GitHub branch protection settings against the policy baseline.

Reads governance/protected-repos.json and verifies that every listed
repo/branch has exactly the protection settings required by:
  - PROTECTED_REPOS_PR_NO_REVIEW_POLICY.md
  - PROTECTED_BRANCH_RELEASE_AUTOMATION_POLICY.md

Must be run with a GH_TOKEN that has administration:read access on all
target repos (supply via the policy-audit GitHub App or equivalent).

Exit 0 — all settings match the baseline.
Exit 1 — one or more settings drift from the baseline.
"""

import json
import subprocess
import sys
from pathlib import Path

CONFIG = json.loads(
    (Path(__file__).parent.parent / "governance" / "protected-repos.json").read_text()
)

errors = []
checks = 0


def gh_api(path: str) -> dict:
    out = subprocess.check_output(
        ["gh", "api", "-H", "Accept: application/vnd.github+json", path],
        text=True,
    )
    return json.loads(out)


def names(items) -> list[str]:
    result = []
    for item in items or []:
        result.append(
            item.get("slug")
            or item.get("login")
            or item.get("name")
            or str(item)
        )
    return sorted(result)


for entry in CONFIG["repos"]:
    repo = entry["repo"]
    branch = entry.get("branch", "main")
    prefix = f"{repo}:{branch}"

    try:
        protection = gh_api(f"repos/{repo}/branches/{branch}/protection")
    except subprocess.CalledProcessError as exc:
        errors.append(f"{prefix}: unable to read protection settings ({exc})")
        continue

    # --- PR required ---
    pr_reviews = protection.get("required_pull_request_reviews")
    if not pr_reviews:
        errors.append(f"{prefix}: 'Require a pull request before merging' is not enabled")
        continue
    checks += 1

    # --- enforce_admins ---
    if protection.get("enforce_admins", {}).get("enabled") is not True:
        errors.append(f"{prefix}: enforce_admins must be true (currently disabled)")
    else:
        checks += 1

    # --- required_approving_review_count ---
    actual_reviews = pr_reviews.get("required_approving_review_count")
    expected_reviews = entry["required_approving_review_count"]
    if actual_reviews != expected_reviews:
        errors.append(
            f"{prefix}: required_approving_review_count={actual_reviews}, "
            f"expected {expected_reviews}"
        )
    else:
        checks += 1

    # --- bypass apps: must match expected list exactly ---
    bypass = pr_reviews.get("bypass_pull_request_allowances", {})
    actual_apps = names(bypass.get("apps"))
    expected_apps = sorted(entry.get("allowed_bypass_apps", []))
    if actual_apps != expected_apps:
        errors.append(
            f"{prefix}: bypass apps={actual_apps}, expected {expected_apps}"
        )
    else:
        checks += 1

    # --- no human users in bypass ---
    bypass_users = names(bypass.get("users"))
    if bypass_users:
        errors.append(
            f"{prefix}: human users present in bypass allowances (prohibited): {bypass_users}"
        )
    else:
        checks += 1

    # --- no teams in bypass ---
    bypass_teams = names(bypass.get("teams"))
    if bypass_teams:
        errors.append(
            f"{prefix}: teams present in bypass allowances (prohibited): {bypass_teams}"
        )
    else:
        checks += 1

    # --- allow_force_pushes ---
    actual_force = bool(protection.get("allow_force_pushes", {}).get("enabled"))
    expected_force = entry.get("allow_force_pushes", False)
    if actual_force != expected_force:
        errors.append(
            f"{prefix}: allow_force_pushes={actual_force}, expected {expected_force}"
        )
    else:
        checks += 1

    # --- allow_deletions ---
    actual_del = bool(protection.get("allow_deletions", {}).get("enabled"))
    expected_del = entry.get("allow_deletions", False)
    if actual_del != expected_del:
        errors.append(
            f"{prefix}: allow_deletions={actual_del}, expected {expected_del}"
        )
    else:
        checks += 1


print(f"Protected repo audit: {checks} checks passed, {len(errors)} failed\n")

if errors:
    print("FAILED — branch protection drift detected:\n")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)

print("OK — all protected repos match the policy baseline.")
