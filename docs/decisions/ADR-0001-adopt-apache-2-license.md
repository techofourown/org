# ADR-0001: Adopt Apache License 2.0 for the Core Codebase

## Status

Accepted

## Context

Tech of Our Own is building a local-first, self-hostable personal server and “home screen portal” experience intended to be run by individuals, families, and communities on hardware they control. The project’s success depends on broad adoption, remixing, and distribution — including by hobbyists, integrators, small businesses, and community groups — without imposing obligations that would discourage use or complicate downstream deployments.

A key design constraint is that we **do not want to force openness on downstream users**. Specifically, we want downstream users and forkers to be able to: (a) use the software commercially, (b) sell devices or services built on it, and (c) keep modifications private if they choose. We also want the upstream project (Tech of Our Own) to retain full freedom to commercialize its own work, while avoiding licenses that create downstream compliance burden or “viral” effects that conflict with our goals.

Finally, because this project is adjacent to hardware, security, and potentially AI infrastructure, we must consider the risks and expectations around patents and commercial adoption. Many companies and institutions require a clear patent grant in the license to reduce adoption risk.

## Decision

We will license the core Tech of Our Own codebase under the **Apache License 2.0**.

All contributions to the core repository will be accepted under Apache 2.0 terms. We will include the Apache 2.0 `LICENSE` file in the repository and maintain required attribution/notice practices for third-party dependencies consistent with their respective licenses.

## Rationale

Apache 2.0 is a permissive license that aligns tightly with our stated priorities:

* **Maximum downstream freedom**: Downstream users may use, modify, sell, and distribute the software, including as part of commercial products, without being required to publish modifications.
* **No “forced openness”**: Apache 2.0 does not impose copyleft requirements that would compel forkers or hosted providers to disclose source changes.
* **Strong commercial compatibility**: Apache 2.0 is widely accepted in industry and reduces friction for commercial use and distribution.
* **Explicit patent grant**: Apache 2.0 includes an express patent license and patent termination provisions that are commonly expected for infrastructure and platform software. This is a meaningful advantage versus simpler permissive licenses where patent terms are not explicit.
* **Clear operational obligations**: Apache’s requirements (license text, notices, attribution) are straightforward to comply with and do not introduce the “network use” obligations associated with AGPL.

### Alternatives considered

* **AGPLv3 / GPLv3 (copyleft)**: Rejected because copyleft is designed to compel publication of changes (AGPL especially for network use), which conflicts with our goal of allowing private modifications and frictionless downstream appropriation.
* **MIT / BSD-2 / BSD-3 (permissive)**: Technically compatible with our goals and very simple, but provides less explicit patent protection than Apache 2.0. Given our hardware/security/AI adjacency and the desire to support institutional and commercial adoption, Apache 2.0 is the stronger default.
* **Dual licensing / source-available**: Rejected for v1 because it complicates the project’s trust story and governance, increases contributor/legal complexity, and conflicts with the intent to make appropriation straightforward and broadly permitted.

## Consequences

### Positive

* Reduces adoption friction for individuals, companies, community hosts, and integrators.
* Allows downstream forks and commercial offerings (including closed/private modifications), consistent with our “user freedom” ethos.
* Provides a clear patent license grant that improves confidence for commercial adopters and contributors.
* Simplifies compliance compared with copyleft licenses, especially for hosted and appliance-style deployments.

### Negative

* Competitors may legally fork the code, keep changes private, and sell competing products without contributing back.
* Apache 2.0 does not prevent “open core” behavior by third parties or the creation of hosted offerings that diverge from our ethics.
* We must actively manage attribution/NOTICE obligations across dependencies, especially when shipping appliance images.

### Mitigation

* **Differentiate on trust, brand, and governance**: Maintain strong trademarks and clear branding guidelines so users can distinguish official Tech of Our Own releases from forks, without restricting code freedom.
* **Make exit and interoperability first-class**: Ensure migration/export and interoperability are product defaults, so exploitative forks cannot easily trap users (even if they exist).
* **Adopt licensing hygiene in CI**: Maintain a simple dependency license inventory and a compliance checklist for releases to correctly include required notices and attributions.
* **Build a community contribution flywheel**: Invest in documentation, packaging, and a welcoming contributor process so contributing upstream is the easiest path for most good-faith adopters, even though it is not required.
