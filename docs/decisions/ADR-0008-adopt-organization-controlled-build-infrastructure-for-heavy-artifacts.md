ADR-0008: Adopt Organization-Controlled Build Infrastructure for Heavy Artifacts
	•	Date: 2026-02-28
	•	Related:
	•	../governance/VALUES.md
	•	../governance/MISSION.md
	•	../governance/CONSTITUTION.md
	•	./ADR-0007-adopt-oci-artifacts-for-app-distribution.md
	•	../rfcs/RFC-0001-oci-artifacts-trust-and-attestations.md
	•	../policies/OFFICIAL_ARTIFACT_BUILD_AND_PROVENANCE_POLICY.md

⸻

Context

Tech of Our Own ships more than lightweight application code. We also produce heavy artifacts:
bootable operating system images, installer media, firmware payloads, airgapped bundles, and other
machine-built release outputs that are materially large, long-running, hardware-specific, or
otherwise resource-intensive to build and publish.

These builds differ from ordinary application CI. They often benefit from persistent caches or
mirrors, controlled toolchains, higher-capacity compute, large local storage, predictable network
egress, and carefully-scoped publication credentials. In practice, the ability to build and publish
these artifacts is part of TOOO’s real release capability, not just a convenience job.

TOOO develops in public and currently uses GitHub as a public collaboration surface and release
visibility surface. That is compatible with our values. But if official heavy-artifact production
depends entirely on third-party hosted execution, TOOO becomes vulnerable to hosted-runner quotas,
rate limits, queue delays, policy changes, network restrictions, and cost shifts outside its control.
That kind of dependency is in tension with our stated commitments to user sovereignty, inspectability,
exit, and resilience against gatekeepers.

At the same time, we do not want a secret or magical build lane. The build logic for official
artifacts should remain in public repositories as documented, repo-contained entrypoints so that
others can build compatible artifacts on their own workstations, servers, cloud accounts, or
self-hosted runners. The difference between an official TOOO artifact and a third-party build
should come from publication identity and provenance, not from hidden build steps.

⸻

Decision

We will adopt organization-controlled build infrastructure as the default release-capable
execution posture for heavy artifacts.

Concretely:
	1.	Official heavy artifacts MAY be built on organization-controlled infrastructure
using public, repo-contained build entrypoints.
	2.	Public GitHub remains the source-of-truth for collaboration and public release visibility,
but official heavy-artifact build capability MUST NOT depend exclusively on GitHub-hosted execution.
	3.	This ADR is posture-level and vendor-neutral.
It does not require a specific CI product, runner product, hosting topology, or private network
design. It requires the capability boundary: TOOO must retain a build-and-publish path for heavy
artifacts on infrastructure it controls.
	4.	Public-source buildability remains first-class.
Heavy-artifact repositories SHOULD expose documented build entrypoints that both TOOO-controlled
builders and independent builders can use, subject to environment-specific configuration.
	5.	Official status derives from TOOO-controlled publication and provenance, not from secrecy of the build process.
	6.	Third-party hosted CI MAY still be used
for validation, convenience, public observability, or auxiliary automation, but it is not the
only permissible or sufficient release path for official heavy artifacts.

⸻

Scope

This ADR applies to heavy artifacts, including at minimum:
	•	bootable OS images
	•	installer media
	•	firmware payloads and update bundles
	•	airgapped bundles
	•	other machine-built release artifacts designated by a repository as materially resource-intensive
or release-critical

This ADR does not require every lightweight application build or ordinary container image build
to use the same execution posture, although projects MAY choose to align with it.

This ADR also does not publish or require publication of internal infrastructure identifiers,
credentials, topology, secret-handling details, or capacity-planning details.

⸻

Rationale

1) Release capability should not be a rented permission

If TOOO can only produce official heavy artifacts when a third-party hosted CI platform allows it,
then TOOO does not fully control its own release capability. For release-critical artifacts, that is
too much dependence on someone else’s quotas, policies, and economics.

2) Public source and organization-controlled execution are compatible

Building on organization-controlled infrastructure does not make the system closed, provided that the
source, build logic, and entrypoints remain public and documented. This preserves openness while
reducing operational dependence.

3) Heavy artifacts have real operational needs

Bootable images, installer artifacts, firmware bundles, and large airgap outputs are simply not the
same as lightweight unit-test or linter jobs. They often need more stable compute, better caches,
fewer time limits, and more deliberate release handling.

4) Trust should come from provenance, not mystique

We want one lane, not a hidden “official magic” lane. Anyone should be able to run the same public
build entrypoints. Official TOOO status comes from TOOO-controlled publication identity and
provenance, not from private build logic.

5) This keeps future migration easy

By making the decision about control of capability, rather than about one specific vendor or
runner product, TOOO keeps freedom to move between execution environments without rewriting the
public story every time.

⸻

Consequences

Positive
	•	Greater release resilience for heavy artifacts in the face of quotas, rate limits, and hosted CI policy changes.
	•	More operational control over timing, caches, storage, and publication handling for critical artifacts.
	•	Clearer public posture: public source, public build entrypoints, organization-controlled official release capability.
	•	Better contributor freedom: others can build compatible artifacts using the same public code and entrypoints.
	•	Lower platform lock-in risk for TOOO itself.

Negative / Tradeoffs
	•	TOOO takes on more operational burden for release-capable infrastructure.
	•	Public and official build paths can drift if they are not kept aligned.
	•	More care is required in documentation so public docs explain the posture without leaking sensitive
operational details.

Mitigation
	•	Keep authoritative build entrypoints in version-controlled public repositories.
	•	Pair this ADR with an enforceable provenance/disclosure policy.
	•	Periodically validate that public build entrypoints remain usable outside the privileged release path.
	•	Document capabilities, interfaces, and guarantees publicly while keeping operational security
details out of public repositories.

⸻

Options considered

Option A: Rely exclusively on third-party hosted CI for official heavy-artifact builds
	•	Rejected.
	•	Too much release capability would depend on someone else’s quotas, policy choices, and operating conditions.

Option B: Use organization-controlled build infrastructure with public source and public build entrypoints
	•	Accepted.
	•	Preserves public-source openness while keeping critical release capability under TOOO control.

Option C: Use maintainer laptops/workstations as the primary official release path
	•	Rejected.
	•	Too fragile, too person-dependent, and too hard to treat as a durable organizational release capability.

Option D: Keep official build logic private or undisclosed
	•	Rejected.
	•	Conflicts with TOOO’s stated commitments to inspectability, public buildability, and forkability.

⸻

Implementation notes

1) Public docs describe posture, not machines

Public documentation should describe:
	•	the build/release posture
	•	public build entrypoints
	•	official publication surfaces
	•	artifact identity and trust surfaces
	•	supported custom-build paths

Public documentation should not publish:
	•	internal hostnames or IP addresses
	•	runner registration details
	•	credential material
	•	secret storage mechanics
	•	internal network topology
	•	exact private cache/mirror topology
	•	break-glass procedures
	•	sensitive capacity details that do not help users build or verify artifacts

2) Repo-owned entrypoints remain authoritative

Heavy-artifact repositories should keep their primary build entrypoints in the repository itself
(scripts, documented commands, or repo-owned workflows), rather than moving the real logic into
undocumented external systems.

3) Companion policy governs official provenance/disclosure requirements

This ADR establishes the posture. The companion policy defines what must be true before TOOO may
represent an artifact as official.

4) Infrastructure implementation may evolve without a new ADR

Moving from one organization-controlled execution environment to another does not require superseding
this ADR, so long as the posture remains the same:
	•	public source remains public,
	•	build entrypoints remain documented,
	•	and official heavy-artifact build capability remains under TOOO control.

⸻

Future changes

Any of the following would require explicit follow-up governance action:
	•	making official heavy-artifact release capability depend exclusively on third-party hosted execution
	•	adopting closed or undisclosed build logic for official artifacts
	•	materially changing the meaning of “official artifact” away from provenance-based identity

⸻

References
	•	../governance/VALUES.md
	•	../governance/MISSION.md
	•	../governance/CONSTITUTION.md
	•	./ADR-0007-adopt-oci-artifacts-for-app-distribution.md
	•	../rfcs/RFC-0001-oci-artifacts-trust-and-attestations.md
	•	../policies/OFFICIAL_ARTIFACT_BUILD_AND_PROVENANCE_POLICY.md

⸻
