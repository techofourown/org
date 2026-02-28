Official Artifact Build and Provenance Policy

Draft v1.0

Purpose

This policy defines the minimum conditions under which Tech of Our Own may represent an artifact as
an official TOOO artifact.

It establishes enforceable rules for:
	•	public buildability from source
	•	official release execution posture
	•	minimum provenance and traceability metadata
	•	privileged builder handling
	•	public disclosure boundaries

The policy exists to make official artifacts legible and trustworthy without turning the build
process into a hidden or privileged “magic lane.”

⸻

Scope

This policy applies to machine-built release artifacts that TOOO publishes or presents as official,
including (non-exhaustive):
	•	OCI artifacts and OCI images
	•	bootable OS images
	•	installer media
	•	firmware payloads and update bundles
	•	airgapped bundles
	•	packages, archives, and other release files produced by automated or scripted build processes

Additional continuity requirements apply to heavy artifacts.

This policy does not apply to:
	•	private experiments or draft outputs not represented as official
	•	community or third-party builds not published by TOOO as official
	•	general prose documents governed by separate licensing/governance decisions

This policy requires minimum traceability metadata today. It does not, by itself, require
cryptographic signatures, SBOMs, or provenance attestations for every official artifact. Those may
be added by repo-specific rules or later org-wide decisions.

⸻

Relationship to other policies

This policy is complementary to, and does not replace, other repo and org controls.

In particular:
	•	Protected Branch Release Automation Policy governs how automation may write tags, releases, and
release commits on protected branches.
	•	This policy governs what must be true about the artifacts themselves, the builders that produce
them, and the minimum provenance/disclosure posture before TOOO may call an artifact “official.”

⸻

Definitions

Official artifact
An artifact published through a TOOO-controlled release channel and represented by TOOO as an
official output.

Official release channel
A TOOO-controlled publication surface designated by the repository, such as:
	•	an OCI registry namespace
	•	a GitHub Release
	•	a download endpoint
	•	an equivalent public release location

Compatible artifact
An artifact built from TOOO public source using documented public build entrypoints, but not published
by TOOO as an official artifact.

Heavy artifact
An artifact whose build or publication is materially resource-intensive, long-running, large,
hardware-specific, or otherwise release-critical. Examples include bootable OS images, installer
media, firmware bundles, and airgapped bundles.

Organization-controlled build infrastructure
Build infrastructure administered by TOOO, with TOOO-controlled access policy and credential
lifecycle. This may include self-hosted runners, dedicated build hosts, organization-managed cloud
execution, or equivalent systems.

Public build entrypoint
A version-controlled, repo-contained script, workflow, or documented command path that allows a
third party to build a compatible artifact from public source.

Privileged builder
A build workflow or execution environment that has release credentials, privileged network or storage
access, or authority to publish official artifacts.

Trusted release context
A controlled source context authorized to produce official artifacts, such as a protected branch,
approved tag, or equivalent repository-defined release ref.

Provenance metadata
The minimum traceability information associated with an artifact. At minimum this includes:
	•	source repository identity
	•	source revision
	•	version/tag or release identifier (if any)
	•	build or publication timestamp
	•	artifact digest/checksum/reference

Where signatures or attestations exist, they are additive controls on top of this metadata.

⸻

The rule
	1.	Only artifacts that satisfy this policy and are published through a TOOO-controlled official release channel may be represented as official TOOO artifacts.
	2.	Official artifacts MUST be buildable from public source using documented public build entrypoints kept in version control.
	3.	Official artifacts MUST carry, or be accompanied by, minimum provenance metadata.
	4.	Official heavy-artifact release capability MUST remain operable on organization-controlled build infrastructure and MUST NOT depend exclusively on third-party hosted CI execution.
	5.	Privileged builders MUST NOT execute untrusted public pull request code with release credentials or privileged network/storage access.
	6.	Public repositories, public artifacts, and public documentation MUST NOT disclose sensitive internal infrastructure details.
	7.	Compatible third-party artifacts MAY be built from the same public source and entrypoints, but they are not official TOOO artifacts unless TOOO publishes them through an official release channel.
	8.	No artifact may be described as “signed,” “verified,” or “attested” unless that claim is true for the artifact actually published.

⸻

Required controls

Source and build controls
	•	Official build and publication logic MUST live in version-controlled repositories and follow normal
repo change control.
	•	Each repository producing official artifacts MUST document its public build entrypoint(s).
	•	Official artifacts MUST be produced only from trusted release contexts.
	•	Repositories SHOULD separate unprivileged validation builds from privileged release builds.
	•	Repositories SHOULD document:
	•	official release channel(s)
	•	artifact types produced
	•	the difference between official artifacts and compatible/custom artifacts
	•	Repositories SHOULD make clear whether an artifact is expected to be consumed by:
	•	digest
	•	checksum
	•	version tag
	•	or another stable identifier

Privileged builder controls
	•	Privileged builders MUST use least-privilege credentials.
	•	Release credentials MUST NOT be exposed to forked pull requests or other untrusted execution paths.
	•	Credentials SHOULD be short-lived where feasible and MUST NOT be written to logs or embedded in
build artifacts.
	•	Privileged builders MUST be attributable to a specific automation identity, release workflow, or
named release procedure.
	•	Where feasible, privileged release builders SHOULD use isolated execution environments separate
from general-purpose CI validation jobs.

Provenance and traceability controls

Every official artifact MUST be traceable to:
	•	the source repository
	•	the source revision or commit SHA
	•	the version, tag, or release identifier (if any)
	•	the build or publication timestamp
	•	the artifact digest, checksum, or equivalent stable reference

Additional expectations:
	•	For OCI artifacts, the canonical identity SHOULD be the digest, and metadata SHOULD include:
	•	org.opencontainers.image.source
	•	org.opencontainers.image.revision
	•	org.opencontainers.image.version
	•	org.opencontainers.image.created
	•	For file artifacts, a checksum file (for example SHA-256) SHOULD accompany the release.
	•	Each official release SHOULD also be traceable internally to:
	•	a build workflow run,
	•	a privileged builder identity,
	•	or an equivalent publication record.
	•	If cryptographic signatures or attestations are adopted for a repository, they SHOULD be published
and documented clearly, but the absence of signing MUST NOT be misrepresented as verified provenance.

Public disclosure controls

Public docs MAY describe the build/release posture using general terms such as:
	•	organization-controlled build infrastructure
	•	official builders
	•	trusted release workflows
	•	public distribution endpoints

Public docs, public repos, and public artifacts MUST NOT publish:
	•	internal hostnames, IP addresses, or runner registration details
	•	credential material or secret storage mechanics
	•	internal network topology
	•	exact private cache/mirror topology
	•	break-glass procedures
	•	sensitive capacity or planning details that do not help users build or verify artifacts

Public docs SHOULD explain:
	•	where official artifacts are published
	•	how users can inspect version, digest, or checksum information
	•	how third parties can build compatible artifacts from public source
	•	the distinction between official artifacts and compatible/custom artifacts

Heavy-artifact continuity controls
	•	Each repository that produces official heavy artifacts MUST maintain at least one documented
organization-controlled release path.
	•	If a repository also uses third-party hosted CI for convenience, validation, or public visibility,
failure of that external service MUST NOT eliminate TOOO’s ability to cut an official heavy-artifact release.
	•	Maintainer laptops or ad-hoc workstations MAY be used for experimentation or emergency recovery,
but they are not the primary continuity plan for official heavy-artifact production.
	•	The documented organization-controlled release path SHOULD be revalidated whenever major build or
publication changes are made.

⸻

Audit and traceability

Each repository producing official artifacts MUST maintain a minimal record (in-repo or centrally) of:
	•	artifact types produced
	•	public build entrypoint(s)
	•	official release channel(s)
	•	trusted release contexts
	•	privileged builders, workflows, or release identities
	•	provenance metadata fields surfaced to users
	•	whether signatures or attestations are currently used

Additional expectations:
	•	Each official release SHOULD be traceable to a specific publication event, workflow run, or
equivalent builder record.
	•	Privileged builder scope and publication controls SHOULD be reviewed periodically
(at least quarterly) and whenever a repository makes major build or release changes.
	•	A repository MUST be able to answer, for an official artifact:
	•	what source it came from,
	•	what exact revision produced it,
	•	where it was officially published,
	•	and what stable artifact identity users should rely on.

⸻

Exceptions

Exceptions are allowed only to remediate:
	•	release continuity failures
	•	release integrity issues
	•	security incidents affecting build or publication systems

Any exception must:
	•	be approved by repository administrators and the org platform/security owner
	•	be time-limited
	•	be documented with:
	•	reason
	•	scope
	•	impacted artifacts
	•	corrective actions

Exceptions MUST NOT allow TOOO to represent an artifact as official if its source revision or stable
artifact identity cannot be established.

If an exception involves suspicious credential exposure or disclosure of sensitive internal details,
credential rotation and artifact review are mandatory.

⸻

Enforcement
	•	Repository maintainers are responsible for:
	•	documenting public build entrypoints
	•	documenting official release channels
	•	surfacing required provenance metadata
	•	clearly distinguishing official artifacts from compatible/custom artifacts
	•	Platform/Security is responsible for:
	•	privileged builder credential lifecycle
	•	access policy for organization-controlled build infrastructure
	•	incident response related to build and publication systems

Violations require immediate remediation, which may include:
	•	stopping or withdrawing official publication
	•	correcting missing or inaccurate provenance metadata
	•	revoking or rotating credentials
	•	removing sensitive internal details from public surfaces
	•	reclassifying an artifact as non-official if provenance cannot be established
	•	temporarily disabling release publication until controls are restored

⸻

References
	•	../decisions/ADR-0008-adopt-organization-controlled-build-infrastructure-for-heavy-artifacts.md
	•	../decisions/ADR-0007-adopt-oci-artifacts-for-app-distribution.md
	•	../rfcs/RFC-0001-oci-artifacts-trust-and-attestations.md
	•	./PROTECTED_BRANCH_RELEASE_AUTOMATION_POLICY.md
	•	../governance/VALUES.md
