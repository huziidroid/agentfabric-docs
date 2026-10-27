---
title: Current capabilities
description: Coverage of implemented SDK concepts and the explicit boundaries of extension and execution support.
---

This matrix describes the **unreleased source preview inspected October 27, 2026**. Read the [source baseline](../../support/compatibility/) before integrating. “Implemented” describes available SDK behavior, not a production qualification or a published package guarantee.

## Implemented native SDK

| Capability | Concepts | Task guide / reference |
| --- | --- | --- |
| Native construction, ownership, strict values, limits, shutdown | [Values](../concepts/), [durability](../durability/) | [Lifecycle guide](../../guides/runtime-lifecycle/), [construction reference](../../reference/runtime/) |
| Identity bootstrap, issuance, rotation, revocation, verification | [Identity](../identities/) | [Credential guide](../../guides/credentials/), [identity reference](../../reference/identity/) |
| Policy, grants, restrictions, delegation, eligibility bindings, requests/decisions | [Permissions](../permissions/) | [Access guide](../../guides/permissions/), [permission reference](../../reference/permissions/) |
| Connection metadata and optional provider credential resolution | [Connections](../connections/) | [Connection guide](../../guides/connections/), [connection reference](../../reference/connections/) |
| Exact admission, renewal, single-use consumption, complete effect observations | [Admission](../admission/) | [Admission guide](../../guides/admission/), [authority reference](../../reference/authority/) |
| All six ordinary artifact operations, retention, provenance, integrity | [Artifacts](../artifacts/) | [Runnable tutorial](../../tutorials/native-runtime/), [artifact reference](../../reference/artifacts/) |
| Registered bindings, goals, ordered tasks, dispatch acceptance, history/pagination | [Lifecycle](../lifecycle/) | [Goal tutorial](../../tutorials/declare-goal/), [goal reference](../../reference/goals/) |
| Continue, Stop, Revise, Wait, Resume, Retry; management controls | [Decisions](../decisions/) | [Decision guide](../../guides/decisions/), [goal reference](../../reference/goals/) |
| Permission/user/timer waits and verified resolution | [Waits](../waits/) | [Wait guide](../../guides/waits/), [exact models](../../reference/generated/decisions/) |
| Checkpoints, V2 no-wait yield, exact same-task continuation | [Checkpoints](../checkpoints/) | [Recovery guide](../../guides/recovery/), [completion reference](../../reference/completions/) |
| Qualifying before-start Retry | [Retry](../retry/) | [Recovery guide](../../guides/recovery/) |
| Task return publication, V1/V2 technical outcomes, explicit reconciliation | [Outcomes](../outcomes/) | [Outcome guide](../../guides/outcomes/), [completion reference](../../reference/completions/) |
| Advanced borrowed artifact adapter composition and bounded transaction-conflict retry | [Extensions](../extensions/) | [Artifact API](../../reference/artifacts/), [source declarations](../../reference/generated/artifacts/) |

## Contracts and development candidates

| Surface | Current boundary |
| --- | --- |
| `OperationClient` | Protocol only. Internal observations exist; public execution/results and original-action recovery remain unfinished. |
| `ExecutionClient`, `WorkspaceClient` | Future facade contracts; no matching Runtime attributes or complete physical runner. |
| Task/assessment/completion handler protocols | Describe behavior contracts; executable handler resolution and assessment/completion pipeline remain unfinished. |
| `finish` | Schema value exists; current signal handling raises `NotImplementedError`. |
| Environment profiles, recipes, readiness | Configuration/verification contracts do not establish a qualified physical backend. |
| Shared scheduling V2 service and migration | Experimental, unapproved source candidate; not supported native construction. |
| Dummy scheduling/environment | Simulation only; no physical isolation or termination qualification. |
| Launched-work Retry | Additional reset and external-effect recovery support remains unfinished. |

## Interpreting evidence

Dispatch records accepted execution work and runs no handler. Outcome tests use trusted test backends. Local tests, dummy environments, and simulations do not qualify physical production guarantees.

The two native tutorials are executable against the inspected source preview. More advanced task-return, admission, wait, and recovery guides describe the required trusted integration state; they do not supply a physical backend.

AgentCLI and Fabric are separate product responsibilities. This site's implementation coverage is the Runtime SDK.
