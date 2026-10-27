---
title: Errors and limits
description: Failure categories, retry guidance, completeness bounds, and accepted budgets.
---

## Public error categories

Most core errors live in `agentfabric_runtime.core.errors`. Authentication and artifact errors have their own modules.

| Error | Import module | Meaning / response |
| --- | --- | --- |
| `AuthorizationError` | `core.authentication` | Current credential/context/policy/resource authority failed. Correct authority; do not infer permissions from IDs. |
| `RequestConflictError` | `core.errors` | Accepted ID reused with different arguments or stale expected state. Recover original response or refetch before a genuinely new mutation. |
| `RecordNotFoundError` | `core.errors` | Absent record or record outside trusted access binding. Do not widen access to search for it. |
| `AcceptanceExpiredError` | `core.errors` | New acceptance deadline passed. Inspect original request before replacement. |
| `StorageError` | `core.errors` | Persistence/integrity failure; optional `code` gives bounded detail. Original request identity may be required to resolve uncertainty. |
| `UnsupportedSchemaError` | `core.errors` | Database application/schema is unsupported. Do not silently reuse or downgrade state. |
| `ClaimLostError` | `core.errors` | Scheduling claim expired or was fenced. Stale controller must not continue. |
| `EnvironmentError` | `core.errors` | Dummy environment outcome unavailable or command rejected; not proof about a physical backend. |
| `ArtifactIntegrityError` | `artifacts.errors` | Byte/file identity differs from immutable publication. Stop trusting content. |
| `ArtifactUnavailableError` | `artifacts.errors` | Content pending, expired, deleted, or otherwise unavailable. Inspect/recover under original authority. |
| `UnsupportedTaskCompletionFormatError` | `goals.serialization` | Completion format cannot be interpreted. Preserve format identity. |
| `UnsupportedExecutionOutcomeFormatError` | `goals.serialization` | Outcome format cannot be interpreted. Do not relabel metadata. |

Names in the table are prefixed with `agentfabric_runtime.` when importing. Strict Pydantic validation, `ValueError`, and `NotImplementedError` are also relevant. In particular, current Finish is unimplemented.

Advanced state adapters distinguish `WriteConflictError` (confirmed uncommitted business write) and `CommitUnknownError` (commit certainty unavailable), in `agentfabric_runtime.storage.errors`, both within the storage error family. These are adapter-boundary information, not permission for the application to repeat external side effects.

## Explicit limits

| Type | Fields / scope |
| --- | --- |
| `GoalLimits` | `max_tasks`, `max_executions`, `max_decisions`, `max_revisions`; accumulated accepted-work budgets. |
| `ExecutionOutputLimits` | `max_outputs`, `max_output_bytes`, `max_return_bytes`; ordinary output versus canonical task return. |
| `ArtifactLimits` | `max_ingest_bytes`, `max_read_bytes`; per-call payload bounds. |
| `PermissionReadLimits` | `max_origin_grants`; complete origin-grant observation. |
| `AdmissionReadLimits` | `max_candidate_grants`; complete admission candidate observation. |
| `OperationReadLimits` | `max_goal_operations`; all relevant executions/roles, not just checkpoint-listed actions. |

Exact numeric bounds/defaults are in [common models](../generated/core/), [goal models](../generated/goals/), [artifact models](../generated/artifacts/), [permission models](../generated/permissions/), and [operation models](../generated/operations/).

Read-limit overflow refuses progression rather than treating partial results as complete. Plan revision/retry does not reset counters. Cancellation or timeout does not establish that SQL/file/external work failed.

See [Troubleshooting](../../support/troubleshooting/) and [Durability and recovery](../../runtime/durability/).
