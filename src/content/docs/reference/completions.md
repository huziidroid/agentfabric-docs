---
title: Task completion and coordinator API
description: Executor returns, outcome inspection, retention, and explicit reconciliation passes.
---

Completion models are in `agentfabric_runtime.goals.schemas`. The structural boundary is `TaskCompletionClient` in `agentfabric_runtime.goals.interfaces`. [Completion fields](../generated/outcomes/) and [client/factory signatures](../generated/clients/) give exact types/defaults.

## `runtime.task_completions.record`

```python
await runtime.task_completions.record(
    completion,
    expires_at=return_expiry,
    credential=original_executor_credential,
)
```

This is a contextual call: `completion` is a valid `TaskCompletion` or `TaskCompletionV2` for the original task executor's actual execution/attempt. `return_expiry` is the application-selected retention deadline for a new publication. It returns `TaskCompletionReceipt`, containing execution ID, return reference, publication state, and expiry.

The call requires the original exact task executor credential. A management credential is not a substitute. Actual response shape, binding, declared source/output access, and accepted return budget are verified. New recording requires an expiry; omitted expiry only replays existing accepted publication.

V1 yielded completion requires its wait; V2 permits a checkpoint yield without waiting. Exact replay does not grant new file or stop authority. A receipt is not a technical outcome or proof that the worker stopped.

## `runtime.task_completions.inspect`

`inspect(execution_id, *, credential)` returns `TaskOutcomeSnapshot` metadata to current namespace management or the original exact executor context and resource epoch. A workload credential is insufficient. It does not require reading return artifact bytes. Availability is pending, recorded, or unavailable_legacy. A recorded snapshot includes its exact technical reference and canonical outcome.

## Coordinator factory and passes

`runtime.create_task_coordinator(*, environment, coordinator_credential, worker_id, claim_seconds, io_timeout)` returns a guarded coordinator. Supply an explicit trusted environment and a callback returning the current management credential, rather than a captured expired token. Claim duration and I/O timeout are explicit bounds.

| Method | Effect / return |
| --- | --- |
| `pending(after, limit)` | Discover existing execution IDs needing coordination; `None` starts discovery. |
| `reconcile(execution_id)` | Verify recorded return, stopped/resource evidence, and complete effects; return `TaskOutcomeSnapshot`. |

These passes start no handler or background loop and authorize no next task. Dummy environments cannot qualify physical stop/isolation guarantees. Pending reasons preserve uncertainty rather than inventing a final outcome.

## Errors and lifetime

Input/format, authority, publication conflict/integrity/availability, and storage errors retain their categories. Unsupported canonical completion/outcome formats have named errors. Backend or evidence failures can leave a pending snapshot. Caller cancellation does not prove underlying work stopped; quiesce calls before closing Runtime or borrowed adapters.

Read [Task returns and outcomes](../../runtime/outcomes/) and [Record and reconcile returns](../../guides/outcomes/).
