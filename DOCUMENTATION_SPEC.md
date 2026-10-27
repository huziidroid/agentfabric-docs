# Public SDK documentation specification

This project follows Diátaxis: tutorials for learning, guides for user tasks, concepts for explanation, and reference for factual lookup. This is a documentation framework, not a formal certification.

## Audience and scope

Primary audience: application developers embedding the Python Runtime SDK. Secondary audience: trusted host integrators and extension implementers. Cover every implemented public capability and schema family. Keep future facades and experimental scheduling visibly separate. Do not present simulated evidence as physical execution guarantees.

## Page requirements

- Tutorial: achievable result, prerequisites, complete runnable program, expected output, cleanup, next steps. No unexplained ellipses or assumed helpers.
- Concept: problem, definitions, concrete example, relationships/ownership, lifecycle and invariants, limits, links to guide/reference.
- Guide: task, prerequisite state and authority, concrete steps or contextual code, expected result, failures/recovery, references.
- Reference: import path, exact signature, parameter types/defaults/constraints, required authority, preconditions, return schema, state changes, replay/conflicts, errors, cancellation/concurrency notes, and related examples.

## Accuracy and coverage

- Record the source preview, package metadata, and reproducibility limits.
- Maintain source-derived schema/signature pages and a capability coverage map.
- Keep generated declarations secondary to handwritten behavior explanations.
- Document credential ownership, bounded inheritance, admission versus execution, immutable outcomes, management versus agent Resume, before-start Retry, and unknown effects explicitly.
- Do not invent a package-index installation or a working Finish/physical runner.
- Keep internal review logs and secrets outside public content.

## Quality gates

Run `pnpm check`, a production build, internal link/anchor/asset verification, and the complete runnable example against the recorded Runtime source preview. Inspect the production homepage, a document, mobile navigation, and search. A separate reviewer must check coverage and implementation accuracy before publication.

## Independent research sources

- [Diátaxis](https://diataxis.fr/)
- [Tutorials](https://diataxis.fr/tutorials/)
- [Reference](https://diataxis.fr/reference/)
- [Python documentation style guide](https://devguide.python.org/documentation/style-guide/)
- [Temporal Python SDK documentation](https://docs.temporal.io/develop/python)
- [Stripe developer resources](https://docs.stripe.com/development)
- [W3C page structure guidance](https://www.w3.org/WAI/tutorials/page-structure/)
