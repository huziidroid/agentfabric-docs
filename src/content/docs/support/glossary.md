---
title: Glossary
description: Quick definitions linked to the full SDK concept explanations.
---

| Term | Meaning |
| --- | --- |
| [Namespace](../../runtime/concepts/) | Application/owner isolation subject. |
| [Principal](../../runtime/identities/) | Current verified identity, authentication role, expiry, and applicable exact context. |
| [Execution role](../../runtime/identities/) | Task, assessment, or check purpose within access context. |
| [Grant](../../runtime/permissions/) | Scoped authority bounded by recipient, context, lineage, and expiry. |
| [Binding](../../runtime/permissions/) | Trusted eligible roots and context for an actor at a policy version. |
| [Connection](../../runtime/connections/) | Exact provider/account/origin and protected credential metadata. |
| [Admission](../../runtime/admission/) | Current authorization of one immutable operation intent. |
| [Consumption](../../runtime/admission/) | Single-use action ordering; replay does not authorize another external effect. |
| [Artifact](../../runtime/artifacts/) | Bounded managed content with identity, digest, state, and retention. |
| [Goal](../../runtime/lifecycle/) | Durable requested outcome, ordered tasks, limits, and decisions. |
| [Task](../../runtime/lifecycle/) | One logical contribution across execution attempts. |
| [Execution](../../runtime/lifecycle/) | One invocation for part or all of a task. |
| [Agent signal](../../runtime/decisions/) | Explicit intent tied to an exact recorded decision request. |
| [Wait](../../runtime/waits/) | Recorded dependency with verified resolution and explicit continuation. |
| [Checkpoint](../../runtime/checkpoints/) | Pinned same-task continuation state and source binding. |
| [Retry](../../runtime/retry/) | Implemented before-start reattempt of exact accepted input. |
| [Technical outcome](../../runtime/outcomes/) | Immutable canonical recorded metadata, separate from contribution judgment. |
| [Claim / resource lease](../../runtime/extensions/) | Experimental scheduling control lifetime versus allocation lifetime; hard expiry remains separate. |
