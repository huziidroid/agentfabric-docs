---
title: SDK API reference
description: Public native services, calling conventions, implementation status, and source-derived declarations.
---

The reference describes the unreleased SDK preview. Start with the [source baseline](../../support/compatibility/) and [capability matrix](../../runtime/capabilities/).

## Native service map

Import `Runtime` and `SQLiteRuntimeSettings` from `agentfabric_runtime.runtime`. Use `Runtime.open_sqlite()` rather than constructing internal repositories yourself.

| Surface | Calling convention | Reference |
| --- | --- | --- |
| `Runtime.open_sqlite`, `close` | Synchronous host lifecycle | [Construction](../runtime/) |
| `runtime.identities` | Synchronous trusted host administration | [Identity](../identity/) |
| `runtime.artifacts` | Asynchronous | [Artifacts](../artifacts/) |
| `runtime.permissions` | Synchronous protected service | [Permissions](../permissions/) |
| `runtime.authority` | Synchronous protected service | [Admission](../authority/) |
| `runtime.connections` | Synchronous protected service | [Connections](../connections/) |
| `runtime.provider_credentials` | Optional synchronous trusted resolver | [Provider credentials](../connections/) |
| `runtime.goals` | Asynchronous | [Goals](../goals/) |
| `runtime.task_completions` | Asynchronous | [Task completion](../completions/) |
| `runtime.create_task_coordinator(...)` | Synchronous factory; asynchronous explicit passes | [Coordinator](../completions/) |

No `operations`, `executions`, `workspace`, or `scheduler` attribute is supplied by this Runtime. Their protocols are [extension contracts](../../runtime/extensions/).

## Reference conventions

Behavioral pages below explain authority, state changes, replay, errors, and lifetime. Source-derived pages provide exact signatures, parameter annotations/defaults, field types, and `Field(...)` validation metadata. Read them together: a declaration can include future contract values that current code rejects.

An `async def` must be awaited. Synchronous authority/identity methods may perform I/O and should be hosted accordingly. `SecretStr` values are trusted credential material; never infer authority from a request-body `Identity` value.

## Failure and concurrency contract

Protected entries verify credentials and current state. Exact request/mutation replay recovers accepted results; conflicting reuse raises a conflict. Version parameters identify expected saved state. Fresh authorization may still reject a replay, so a saved receipt is not perpetual authority.

For error meanings and response guidance, use [Errors and limits](../errors/). Caller cancellation is not evidence that underlying SQL/file work stopped. Quiesce actual operations before closing owned services.

## Exact declarations

- [Common values and identity models](../generated/core/)
- [Native client methods and Runtime settings](../generated/clients/)
- [Artifact models and interface](../generated/artifacts/)
- [Permission/admission schemas](../generated/permissions/)
- [Goal/task models](../generated/goals/)
- [Decision/wait/checkpoint models](../generated/decisions/)
- [Task completion/outcome models](../generated/outcomes/)
- [Operation contracts](../generated/operations/)
- [Environment/execution contracts](../generated/environment/)
- [Experimental scheduling declarations](../generated/scheduling/)
