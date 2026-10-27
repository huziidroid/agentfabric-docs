---
title: Decision, wait, and checkpoint models
description: Source-derived fields and signatures for the unreleased SDK preview.
---

> **Unreleased source preview.** Generated declarations describe types, not a promise that every contract has an executable implementation. Read the [behavioral API reference](../../overview/) and [capability matrix](../../../runtime/capabilities/) first.

Field defaults shown as `Field(...)` include validation metadata. A `Field(...)` without `default=` or `default_factory=` is required. Inherited fields from classes in the same source module are included. Cross-field invariants are explained in the concept and behavioral reference pages.

## `agentfabric_runtime.goals.schemas`

### `Checkpoint`

Import: `agentfabric_runtime.goals.schemas.Checkpoint`

| Field | Type | Default / validation |
| --- | --- | --- |
| `task_id` | `Identifier` | `Required` |
| `execution_id` | `Identifier` | `Required` |
| `handler_version` | `ContentDigest` | `Required` |
| `input_ref` | `ContentReference` | `Required` |
| `format` | `Identifier` | `Required` |
| `content` | `ContentReference` | `Required` |
| `operation_ids` | `Annotated[tuple[Identifier, ...], Field(max_length=1000)]` | `()` |

### `WaitSpec`

Import: `agentfabric_runtime.goals.schemas.WaitSpec`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `kind` | `Literal['permission', 'user', 'timer']` | `Required` |
| `request_ref` | `Identifier` | `Required` |
| `continuation` | `Literal['next_task', 'resume_task']` | `Required` |
| `deadline` | `UtcDatetime` | `Required` |

### `WaitResolution`

Import: `agentfabric_runtime.goals.schemas.WaitResolution`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `goal_id` | `Identifier` | `Required` |
| `goal_version` | `Version` | `Required` |
| `wait_id` | `Identifier` | `Required` |
| `request_ref` | `Identifier` | `Required` |
| `outcome` | `Literal['resolved', 'denied', 'expired']` | `Required` |
| `result_ref` | `ContentReference \| None` | `None` |

### `DecisionRequest`

Import: `agentfabric_runtime.goals.schemas.DecisionRequest`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `goal_id` | `Identifier` | `Required` |
| `goal_version` | `Version` | `Required` |
| `plan_revision` | `Version` | `Required` |
| `kind` | `RequestKind` | `Required` |
| `task_id` | `Identifier \| None` | `None` |
| `execution_id` | `Identifier \| None` | `None` |
| `outcome_ref` | `TechnicalOutcomeReference \| None` | `None` |
| `wait` | `WaitSpec \| None` | `None` |
| `resolution` | `WaitResolution \| None` | `None` |
| `expires_at` | `UtcDatetime` | `Required` |

### `CompletionCheckRequest`

Import: `agentfabric_runtime.goals.schemas.CompletionCheckRequest`

| Field | Type | Default / validation |
| --- | --- | --- |
| `goal_id` | `Identifier` | `Required` |
| `goal_version` | `Version` | `Required` |
| `plan_revision` | `Version` | `Required` |
| `input_ref` | `ContentReference` | `Required` |
| `evidence` | `Annotated[tuple[ContentReference, ...], Field(max_length=1000)]` | `Required` |
| `deadline` | `UtcDatetime` | `Required` |

### `CompletionReport`

Import: `agentfabric_runtime.goals.schemas.CompletionReport`

| Field | Type | Default / validation |
| --- | --- | --- |
| `goal_id` | `Identifier` | `Required` |
| `goal_version` | `Version` | `Required` |
| `plan_revision` | `Version` | `Required` |
| `report` | `ContentReference` | `Required` |
| `evidence` | `Annotated[tuple[ContentReference, ...], Field(max_length=1000)]` | `Required` |
| `passed` | `bool` | `Required` |
| `valid_until` | `UtcDatetime` | `Required` |

### `AgentSignal`

Import: `agentfabric_runtime.goals.schemas.AgentSignal`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `goal_id` | `Identifier` | `Required` |
| `request_id` | `Identifier` | `Required` |
| `goal_version` | `Version` | `Required` |
| `plan_revision` | `Version` | `Required` |
| `outcome_ref` | `TechnicalOutcomeReference \| None` | `None` |
| `action` | `SignalAction` | `Required` |
| `assessment` | `Literal['accepted', 'rejected'] \| None` | `None` |
| `task_id` | `Identifier \| None` | `None` |
| `replacement_tasks` | `Annotated[tuple[TaskSpec, ...] \| None, Field(max_length=1000)]` | `None` |
| `checkpoint` | `Checkpoint \| None` | `None` |
| `wait` | `WaitSpec \| None` | `None` |
| `completion` | `CompletionReport \| None` | `None` |

### `DecisionReceipt`

Import: `agentfabric_runtime.goals.schemas.DecisionReceipt`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `goal_id` | `Identifier` | `Required` |
| `request_id` | `Identifier` | `Required` |
| `binding_digest` | `ContentDigest` | `Required` |
| `applied_version` | `Version` | `Required` |
| `action` | `SignalAction` | `Required` |

### `GoalDecisionRecord`

Import: `agentfabric_runtime.goals.schemas.GoalDecisionRecord`

The actual applied agent signal and its immutable acknowledgement.

| Field | Type | Default / validation |
| --- | --- | --- |
| `signal` | `AgentSignal` | `Required` |
| `receipt` | `DecisionReceipt` | `Required` |

### `DecisionState`

Import: `agentfabric_runtime.goals.schemas.DecisionState`

Trusted-store facts for pure guards, not caller-supplied authority/evidence.

| Field | Type | Default / validation |
| --- | --- | --- |
| `goal_id` | `Identifier` | `Required` |
| `goal_version` | `Version` | `Required` |
| `plan_revision` | `Version` | `Required` |
| `status` | `GoalStatus` | `Required` |
| `request_id` | `Identifier` | `Required` |
| `decision_actor` | `Identity` | `Required` |
| `mode` | `Literal['handler', 'signals']` | `Required` |
| `deadline` | `UtcDatetime` | `Required` |
| `limits` | `GoalLimits` | `Required` |
| `task_count` | `int` | `Field(ge=0)` |
| `execution_count` | `int` | `Field(ge=0)` |
| `decision_count` | `int` | `Field(ge=0)` |
| `revision_count` | `int` | `Field(ge=0)` |
| `pending_tasks` | `Annotated[tuple[TaskSpec, ...], Field(max_length=1000)]` | `Required` |
| `recorded_task_ids` | `tuple[Identifier, ...]` | `Required` |
| `task_outcome` | `Literal['succeeded', 'failed', 'interrupted', 'yielded', 'denied', 'expired', 'cancelled'] \| None` | `None` |
| `current_task` | `TaskSpec \| None` | `None` |
| `current_execution_id` | `Identifier \| None` | `None` |
| `current_attempt_id` | `Identifier \| None` | `None` |
| `current_outcome_ref` | `TechnicalOutcomeReference \| None` | `None` |
| `checkpoint` | `Checkpoint \| None` | `None` |
| `declared_wait` | `WaitSpec \| None` | `None` |
| `current_wait` | `WaitSpec \| None` | `None` |
| `wait_next_task_id` | `Identifier \| None` | `None` |
| `wait_resolution` | `WaitResolution \| None` | `None` |
| `handler_bindings` | `Annotated[tuple[HandlerReference, ...], Field(min_length=1, max_length=32)]` | `Required` |
| `unresolved_operations` | `int` | `Field(ge=0)` |
| `termination_verified` | `bool` | `Required` |
| `assessment_intent_recorded` | `bool` | `Required` |
| `assessment_intent_digest` | `ContentDigest \| None` | `None` |
| `assessment_termination_verified` | `bool` | `Required` |
| `completion_report` | `CompletionReport \| None` | `None` |
| `evidence_verified` | `bool` | `Required` |
| `retry_safe` | `bool` | `Required` |

### `SignalEffect`

Import: `agentfabric_runtime.goals.schemas.SignalEffect`

Pure expected transition; Stage 2 must commit it with version/receipt/obligations.

| Field | Type | Default / validation |
| --- | --- | --- |
| `status` | `GoalStatus` | `Required` |
| `dispatch_task_id` | `Identifier \| None` | `None` |
| `wait_next_task_id` | `Identifier \| None` | `None` |
| `request_kind` | `RequestKind \| None` | `None` |

### `TaskResponse`

Import: `agentfabric_runtime.goals.schemas.TaskResponse`

Application return envelope; Runtime verifies and records facts separately.

| Field | Type | Default / validation |
| --- | --- | --- |
| `status` | `Literal['succeeded', 'failed', 'yielded']` | `Required` |
| `result` | `ContentReference \| None` | `None` |
| `error_code` | `ErrorCode \| None` | `None` |
| `checkpoint` | `Checkpoint \| None` | `None` |
| `wait` | `WaitSpec \| None` | `None` |
