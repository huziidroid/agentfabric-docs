---
title: Record and reconcile task returns
description: Use original executor authority and explicit coordination to obtain technical outcomes.
---

## Prerequisites

A trusted executor has an actual return for an accepted task invocation, the original exact executor credential, an explicit return retention deadline, and an environment capable of supplying the required evidence. The public native dispatch path does not supply a physical handler, so this guide is for host/backend integration.

## Record the actual return

Construct `TaskCompletion` or `TaskCompletionV2` with exact execution ID, attempt ID, and verified `TaskResponse`. Success needs a result reference; failure needs an error code; yield needs the exact checkpoint and format-appropriate wait behavior.

Await `runtime.task_completions.record(completion, expires_at=return_expiry, credential=original_executor_credential)`. Retain the original accepted envelope and expiry for recovery. The resulting receipt concerns publication, not physical stop or contribution to the goal.

## Coordinate explicitly

1. Create a coordinator with `runtime.create_task_coordinator()` and explicit environment, current management-credential callback, worker ID, claim duration, and I/O timeout.
2. Discover existing work using `pending(after=None, limit=...)`.
3. Await `reconcile(execution_id)` for the relevant execution.
4. Inspect `TaskOutcomeSnapshot` and its availability/pending reason. Reconciliation verifies and finalizes existing work; it launches no handler and authorizes no next task.
5. Only use recorded exact technical evidence to request agent judgment.

## Preserve format and uncertainty

V1 and V2 completion/outcome formats have different yield rules. Unknown formats are explicit errors. Pending/backend/storage/read-limit conditions are not successes, and a recorded runtime-origin denial is different from a handler failure.

Keep the coordinator's credential callback current. Finish underlying work before closing Runtime/environment/source components. Dummy outcomes cannot qualify physical termination.

See [Outcome concepts](../../runtime/outcomes/) and [Completion/coordinator reference](../../reference/completions/).
