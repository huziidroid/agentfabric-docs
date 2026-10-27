---
title: Goal and task models
description: Source-derived fields and signatures for the unreleased SDK preview.
---

> **Unreleased source preview.** Generated declarations describe types, not a promise that every contract has an executable implementation. Read the [behavioral API reference](../../overview/) and [capability matrix](../../../runtime/capabilities/) first.

Field defaults shown as `Field(...)` include validation metadata. A `Field(...)` without `default=` or `default_factory=` is required. Inherited fields from classes in the same source module are included. Cross-field invariants are explained in the concept and behavioral reference pages.

## `agentfabric_runtime.goals.schemas`

### `AgentBinding`

Import: `agentfabric_runtime.goals.schemas.AgentBinding`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `version` | `ContentDigest` | `Required` |
| `task_handlers` | `Annotated[tuple[HandlerReference, ...], Field(min_length=1, max_length=32)]` | `Required` |
| `decision_actor` | `Identity` | `Required` |
| `decision_mode` | `Literal['handler', 'signals']` | `Required` |
| `assessment_handler` | `HandlerReference \| None` | `None` |
| `check_handler` | `HandlerReference \| None` | `None` |

### `TaskSpec`

Import: `agentfabric_runtime.goals.schemas.TaskSpec`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `handler` | `HandlerReference` | `Required` |
| `input_ref` | `ContentReference` | `Required` |
| `expected_output` | `str` | `Field(min_length=1, max_length=2048)` |
| `checkpoint_format` | `Identifier \| None` | `None` |

### `GoalLimits`

Import: `agentfabric_runtime.goals.schemas.GoalLimits`

Application-selected accepted budgets, bounded by persisted counter format.

| Field | Type | Default / validation |
| --- | --- | --- |
| `max_tasks` | `int` | `Field(ge=1, le=(1 << 63) - 1)` |
| `max_executions` | `int` | `Field(ge=1, le=(1 << 63) - 1)` |
| `max_decisions` | `int` | `Field(ge=1, le=(1 << 63) - 1)` |
| `max_revisions` | `int` | `Field(ge=1, le=(1 << 63) - 1)` |

### `GoalSpec`

Import: `agentfabric_runtime.goals.schemas.GoalSpec`

| Field | Type | Default / validation |
| --- | --- | --- |
| `request_id` | `Identifier` | `Required` |
| `namespace` | `Namespace` | `Required` |
| `agent` | `AgentBinding` | `Required` |
| `description` | `str` | `Field(min_length=1, max_length=4096)` |
| `input_ref` | `ContentReference` | `Required` |
| `tasks` | `Annotated[tuple[TaskSpec, ...], Field(max_length=1000)]` | `Required` |
| `limits` | `GoalLimits` | `Required` |
| `output_limits` | `ExecutionOutputLimits \| None` | `Field(default=None, exclude_if=lambda value: value is None)` |
| `deadline` | `UtcDatetime` | `Required` |

### `PausedGoalState`

Import: `agentfabric_runtime.goals.schemas.PausedGoalState`

| Field | Type | Default / validation |
| --- | --- | --- |
| `format` | `Literal['goal-pause-v1']` | `'goal-pause-v1'` |
| `goal_version` | `Version` | `Required` |
| `status` | `Literal['ready', 'running', 'awaiting_agent', 'blocked', 'waiting_input']` | `Required` |
| `authorized_task_id` | `Identifier \| None` | `None` |

### `TaskView`

Import: `agentfabric_runtime.goals.schemas.TaskView`

| Field | Type | Default / validation |
| --- | --- | --- |
| `spec` | `TaskSpec` | `Required` |
| `status` | `TaskStatus` | `Required` |
| `outcome_ref` | `TechnicalOutcomeReference \| None` | `None` |

### `GoalSnapshot`

Import: `agentfabric_runtime.goals.schemas.GoalSnapshot`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `namespace` | `Namespace` | `Required` |
| `version` | `Version` | `Required` |
| `plan_revision` | `Version` | `Required` |
| `status` | `GoalStatus` | `Required` |
| `deadline` | `UtcDatetime` | `Required` |

### `GoalDetails`

Import: `agentfabric_runtime.goals.schemas.GoalDetails`

Saved declaration and current progress for authorized inspection.

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `namespace` | `Namespace` | `Required` |
| `version` | `Version` | `Required` |
| `plan_revision` | `Version` | `Required` |
| `status` | `GoalStatus` | `Required` |
| `deadline` | `UtcDatetime` | `Required` |
| `spec` | `GoalSpec` | `Required` |
| `authorized_task_id` | `Identifier \| None` | `None` |
| `current_execution_id` | `Identifier \| None` | `None` |
| `untracked_execution_count` | `int` | `Field(default=0, ge=0)` |

### `GoalPage`

Import: `agentfabric_runtime.goals.schemas.GoalPage`

| Field | Type | Default / validation |
| --- | --- | --- |
| `items` | `Annotated[tuple[GoalSnapshot, ...], Field(max_length=1000)]` | `Required` |
| `next_cursor` | `Identifier \| None` | `None` |

### `GoalEvent`

Import: `agentfabric_runtime.goals.schemas.GoalEvent`

| Field | Type | Default / validation |
| --- | --- | --- |
| `sequence` | `Version` | `Required` |
| `goal_id` | `Identifier` | `Required` |
| `goal_version` | `Version` | `Required` |
| `kind` | `Identifier` | `Required` |
| `content_ref` | `ContentReference \| None` | `None` |

## `agentfabric_runtime.goals.invocations`

### `TaskContinuation`

Import: `agentfabric_runtime.goals.invocations.TaskContinuation`

| Field | Type | Default / validation |
| --- | --- | --- |
| `format` | `Literal['task-continuation-v1']` | `'task-continuation-v1'` |
| `source_outcome` | `TechnicalOutcomeReference` | `Required` |
| `checkpoint` | `Checkpoint` | `Required` |
| `wait` | `WaitSpec \| None` | `None` |
| `resolution` | `WaitResolution \| None` | `None` |

### `TaskInvocation`

Import: `agentfabric_runtime.goals.invocations.TaskInvocation`

| Field | Type | Default / validation |
| --- | --- | --- |
| `goal_id` | `Identifier` | `Required` |
| `agent_version` | `ContentDigest` | `Required` |
| `task` | `TaskSpec` | `Required` |
| `continuation` | `TaskContinuation \| None` | `Field(default=None, exclude_if=lambda value: value is None)` |
