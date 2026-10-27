---
title: Task returns and technical outcomes
description: Recorded handler responses, verification, canonical metadata, and explicit reconciliation.
---

## Return versus verified outcome

`TaskResponse` describes a handler result: success requires a result reference, failure requires a bounded error code, and yield requires an exact checkpoint with the applicable wait rules.

The trusted executor submits `TaskCompletion` or `TaskCompletionV2` through `task_completions.record()`, using the original task executor credential and retention expiry for a new record. Its receipt records acceptance; it does not prove termination or contribution to the goal.

## Technical metadata

A technical outcome is immutable canonical metadata with a format and digest. It distinguishes handler and runtime origins, and can reference the handler-return artifact separately. `TechnicalOutcomeReference` identifies this SQL-owned metadata.

Canonical encoding rejects duplicate/unknown fields and nonfinite values, and applies the accepted return-byte budget. Readers must preserve supported format identity instead of silently accepting arbitrary JSON.

## Outcome availability

`task_completions.inspect()` returns `TaskOutcomeSnapshot` to namespace management or the original exact executor context and resource epoch.

| Availability | Meaning |
| --- | --- |
| `pending` | Verified recorded outcome is not available yet. |
| `recorded` | An immutable technical outcome is available. |
| `unavailable_legacy` | Older state cannot provide the required outcome evidence. |

Pending reasons include `not_started`, `resource_unverified`, `storage_unavailable`, `backend_unavailable`, and `read_limit`. Treat these as reasons to inspect/reconcile, not evidence of success or safe replacement.

## Explicit coordination

`create_task_coordinator()` requires an explicit environment, current management-credential callback, worker ID, claim duration, and I/O timeout. `pending()` discovers existing work; `reconcile()` verifies and finalizes it.

The coordinator starts no handler, supplies no business judgment, and authorizes no next task. It does not start a background loop. Dummy/test backends do not qualify physical termination.

Read [Record and reconcile task returns](../../guides/outcomes/) and the [Completion and coordinator API](../../reference/completions/).
