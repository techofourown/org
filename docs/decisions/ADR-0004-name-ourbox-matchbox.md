# ADR-0004: Name the First OurBox Hardware Device "OurBox Matchbox" With Model Identifier TOO-OBX-MBX-01

## Status

Accepted

## Context

Tech of Our Own is launching its first physical device: a pocketable/home-friendly server appliance
built around Raspberry Pi-class hardware, designed to run OurBox OS and provide a canonical “scan a
QR code, self-host securely” experience. We need a product name that is stable, brandable, and
extensible to future generations and variants without being tied to a specific underlying compute
module (e.g., Raspberry Pi 5 vs Raspberry Pi 6) or forcing annual renames.

This name will be the anchor for documentation, packaging, device labeling, support workflows, and
future product family expansion (e.g., larger Tinderbox model). The decision must align with
the organization-wide naming strategy (ADR-0002): stable marketing names plus precise model
identifiers.

## Decision

The first Tech of Our Own OurBox physical device will be named **OurBox Matchbox** as its customer-facing
marketing name.

Its official model identifier will be **TOO-OBX-MBX-01** (Tech of Our Own / OurBox family / Matchbox
model / Generation 01). Manufacturing-level changes will be tracked as board/device revisions
(`Rev A`, `Rev B`, …) under the same generation unless a platform-class redesign requires a
generation increment.

## Rationale

"OurBox Matchbox" is short, memorable, and evokes the small form factor through a recognizable
metaphor. It avoids vendor/platform coupling (“Raspberry Pi”) and avoids year-based
naming, allowing the product identity to remain stable as internal hardware evolves. The model
identifier provides the precision required for support, compliance, manufacturing traceability, and
compatibility documentation while keeping marketing language clean.

This naming choice also aligns with the repository naming convention already adopted (typed
prefixes): the hardware design repo and related build artifacts can follow directly from the product
and model naming without ambiguity.

## Consequences

### Positive

* Stable product name that can remain constant across multiple internal hardware generations.
* Clear family structure that naturally supports future model expansions.
* Unambiguous model identifier for labeling, support, and documentation ("Which Matchbox do you have?").
* Avoids platform/vendor dependency in branding, reducing future rebranding risk.

### Negative

* The word “OS” is not present in the hardware name; users must learn that “OurBox Matchbox runs OurBox
  OS.”
* Without the model identifier, “OurBox Matchbox” alone does not distinguish generations/configurations.
* Some customers may need context to understand "Matchbox" refers to the small form factor.

### Mitigation

* Always pair the marketing name with the model identifier in support-facing contexts (docs, labels,
  invoices): “OurBox Matchbox (TOO-OBX-MBX-01)”.
* Publish a clear compatibility and configuration table in product documentation to distinguish
  generations and optional configurations.
* Use consistent messaging in marketing copy: “OurBox Matchbox is the home appliance for running OurBox
  OS.”
