---
title: Durability, budgets, and recovery
description: State ownership, request identity, complete observations, and safe Runtime shutdown.
---

## Native ownership

Runtime owns its native SQLite and local-file service clients. The application supplies canonical private directories, authority policy, and limits. A supplied provider credential source remains application-owned.

`open_sqlite()` can persist setup and policy before a later construction step fails. Cleanup releases owned resources; it does not roll back all durable writes. Retry with the same explicit storage binding and policy when recovering setup.

## Exact replay and uncertain commits

A request ID identifies accepted arguments and a saved result. Exact replay recovers that result. A reused ID with different arguments is a conflict. Optimistic versions prevent applying mutations against stale state.

`StorageError` can mean the caller lacks certainty about persistence. Keep the original request or mutation identity and recover its receipt/state. Generating a fresh ID can duplicate work. Unknown external effects need their own recovery; local request replay does not repeat an external action safely.

## Three kinds of budget

| Limit | Scope |
| --- | --- |
| `GoalLimits` | Accepted task/execution/decision/revision counts. |
| `ExecutionOutputLimits` | Accepted output count, output bytes, and return bytes per execution. |
| Artifact/read limits | Host-selected per-operation byte limits and complete-observation bounds. |

Revising a plan or retrying a task does not reset history. Permission, admission, and operation read limits are completeness bounds, not pagination hints: overflow refuses unsafe decisions.

## Process and call lifetime

Construct a new Runtime after a host fork. Live instances cannot be shared across forks. Open before the host's event loop, await underlying operations, and close after they finish.

Cancellation of an awaiting coroutine does not prove its file/SQL thread stopped. Concurrent close/new calls and aggregate asynchronous draining are unsupported. Management cancellation likewise is not physical process termination.

## Schema compatibility

Wrong application/schema state must not be silently repurposed. Unknown schema versions raise explicit storage errors. Historical permission policy meaning requires an exact operator-supplied `LegacyPolicyInterpretation` mapping.

Use [Open and close Runtime](../../guides/runtime-lifecycle/), [Troubleshooting](../../support/troubleshooting/), and [Errors and limits](../../reference/errors/).

## Advanced transaction retry bounds

Shared service composition can supply `TransactionRetrySettings` from `agentfabric_runtime.services.transactions`. `max_attempts` is a positive bounded integer; `max_elapsed_seconds` is a positive finite timeout. These bound starting additional transaction attempts after confirmed write conflicts. They never interrupt an accepted transaction or prove an uncertain commit failed.

This is storage-level conflict retry, separate from agent-directed before-start task Retry. `CommitUnknownError` requires receipt recovery rather than blindly repeating a business write or external action. Native `SQLiteRuntimeSettings` does not expose a transaction-retry setting; the option belongs to advanced shared-service constructors such as `ArtifactService`.
