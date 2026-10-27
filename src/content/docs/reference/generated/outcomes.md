---
title: Task completion and outcome models
description: Source-derived fields and signatures for the unreleased SDK preview.
---

> **Unreleased source preview.** Generated declarations describe types, not a promise that every contract has an executable implementation. Read the [behavioral API reference](../../overview/) and [capability matrix](../../../runtime/capabilities/) first.

Field defaults shown as `Field(...)` include validation metadata. A `Field(...)` without `default=` or `default_factory=` is required. Inherited fields from classes in the same source module are included. Cross-field invariants are explained in the concept and behavioral reference pages.

## `agentfabric_runtime.goals.schemas`

### `TaskCompletion`

Import: `agentfabric_runtime.goals.schemas.TaskCompletion`

Frozen V1 executor envelope; application return data is separately verified.

| Field | Type | Default / validation |
| --- | --- | --- |
| `execution_id` | `Identifier` | `Required` |
| `attempt_id` | `Identifier` | `Required` |
| `response` | `TaskResponse` | `Required` |
| `format` | `Literal['task-completion-v1']` | `'task-completion-v1'` |

### `TaskCompletionV2`

Import: `agentfabric_runtime.goals.schemas.TaskCompletionV2`

Explicit V2 executor envelope supports a yielded checkpoint without waiting.

| Field | Type | Default / validation |
| --- | --- | --- |
| `execution_id` | `Identifier` | `Required` |
| `attempt_id` | `Identifier` | `Required` |
| `response` | `TaskResponse` | `Required` |
| `format` | `Literal['task-completion-v2']` | `'task-completion-v2'` |

### `TaskCompletionReceipt`

Import: `agentfabric_runtime.goals.schemas.TaskCompletionReceipt`

Publication metadata only, not an outcome or proof that a worker stopped.

| Field | Type | Default / validation |
| --- | --- | --- |
| `execution_id` | `Identifier` | `Required` |
| `return_ref` | `ContentReference` | `Required` |
| `state` | `Literal['publishing', 'published', 'deleting', 'expired', 'deleted']` | `Required` |
| `expires_at` | `UtcDatetime` | `Required` |

### `PendingExecutionOutcomeV1`

Import: `agentfabric_runtime.goals.schemas.PendingExecutionOutcomeV1`

New native acceptance marker; no technical outcome exists yet.

| Field | Type | Default / validation |
| --- | --- | --- |
| `format` | `Literal['execution-outcome-v1']` | `'execution-outcome-v1'` |
| `state` | `Literal['pending']` | `'pending'` |

### `RecordedExecutionOutcomeV1`

Import: `agentfabric_runtime.goals.schemas.RecordedExecutionOutcomeV1`

Frozen V1 response semantics and canonical metadata encoding.

| Field | Type | Default / validation |
| --- | --- | --- |
| `state` | `Literal['recorded']` | `'recorded'` |
| `origin` | `Literal['handler', 'runtime']` | `Required` |
| `status` | `Literal['succeeded', 'failed', 'yielded', 'denied', 'expired', 'cancelled', 'interrupted']` | `Required` |
| `response` | `TaskResponse \| None` | `None` |
| `return_ref` | `ContentReference \| None` | `None` |
| `cause` | `ErrorCode \| None` | `None` |
| `applying_controller_version` | `Version \| None` | `None` |
| `format` | `Literal['execution-outcome-v1']` | `'execution-outcome-v1'` |

### `RecordedExecutionOutcomeV2`

Import: `agentfabric_runtime.goals.schemas.RecordedExecutionOutcomeV2`

V2 allows a real yielded checkpoint without a requested wait.

| Field | Type | Default / validation |
| --- | --- | --- |
| `state` | `Literal['recorded']` | `'recorded'` |
| `origin` | `Literal['handler', 'runtime']` | `Required` |
| `status` | `Literal['succeeded', 'failed', 'yielded', 'denied', 'expired', 'cancelled', 'interrupted']` | `Required` |
| `response` | `TaskResponse \| None` | `None` |
| `return_ref` | `ContentReference \| None` | `None` |
| `cause` | `ErrorCode \| None` | `None` |
| `applying_controller_version` | `Version \| None` | `None` |
| `format` | `Literal['execution-outcome-v2']` | `'execution-outcome-v2'` |

### `TaskOutcomeSnapshot`

Import: `agentfabric_runtime.goals.schemas.TaskOutcomeSnapshot`

Current authorized metadata availability; no artifact is required for an outcome.

| Field | Type | Default / validation |
| --- | --- | --- |
| `execution_id` | `Identifier` | `Required` |
| `availability` | `Literal['pending', 'recorded', 'unavailable_legacy']` | `Required` |
| `reference` | `TechnicalOutcomeReference \| None` | `None` |
| `outcome` | `RecordedExecutionOutcomeV1 \| RecordedExecutionOutcomeV2 \| None` | `None` |
| `pending_reason` | `Literal['not_started', 'resource_unverified', 'storage_unavailable', 'backend_unavailable', 'read_limit'] \| None` | `None` |
