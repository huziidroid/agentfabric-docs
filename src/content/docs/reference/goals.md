---
title: Goal and decision API
description: Registration, submission, dispatch, observation, signals, wait resolution, and management controls.
---

Use asynchronous `runtime.goals`. Native signatures are from `agentfabric_runtime.services.goals.SQLGoalClient`, constructed by Runtime. Models are in `agentfabric_runtime.goals.schemas`; [exact methods](../generated/clients/), [goal models](../generated/goals/), and [decision models](../generated/decisions/) provide complete parameters/defaults/fields.

## Declare and dispatch

These methods require namespace management authority.

| Method | Result / effect |
| --- | --- |
| `register(binding, *, credential)` | Record immutable versioned handler/decision binding; return `AgentBinding`. |
| `submit(spec, *, credential)` | Validate accepted inputs/limits/deadline and idempotent request; return goal `Identifier`. |
| `dispatch(goal_id, version, *, credential)` | Match expected goal version and currently authorized task/input; return accepted execution `Identifier`. No handler runs. |

Inputs must be readable through declared authority, handlers must match the registered binding, task IDs are unique, and accepted limits must be supplied for native work as required by the SDK. Deadline/budgets apply to new work; exact replay is not a new launch.

## Read progress

Native read methods require current namespace management authority. A decision actor in the complete native scenarios is separately bootstrapped as a management principal; its name alone is insufficient.

| Method | Return |
| --- | --- |
| `status(goal_id, *, credential)` | `GoalStatus`. |
| `inspect(goal_id, *, credential)` | `GoalDetails`, including saved declaration and current progress. |
| `list(after, limit, *, credential)` | `GoalPage`; `after=None` starts discovery. |
| `tasks(goal_id, *, credential)` | Ordered tuple of `TaskView`. |
| `executions(goal_id, task_id, *, credential)` | Tuple of accepted execution identifiers. |
| `pending_decision(goal_id, *, credential)` | Current `DecisionRequest` or `None`. |
| `events(goal_id, after, limit, *, credential)` | Tuple of `GoalEvent`; cursor is nonnegative. |
| `decisions(goal_id, after_version, limit, *, credential)` | Chronological tuple of `GoalDecisionRecord` by applied version; no cross-page snapshot. |
| `inspect_wait(goal_id, *, credential)` | Current `WaitSpec` or `None`, under the wait service's current authorized access. |

## Signals and wait resolution

`signal(signal, *, credential)` requires a current management principal whose identity is the configured decision actor. A workload or executor credential is insufficient for this native signal path. It returns `DecisionReceipt`. Signal IDs bind exact requests and payloads. Version, plan revision, task/outcome, checkpoint, and wait evidence must match the action.

Implemented actions: Continue, Stop, Revise, Wait, Resume, Retry. Finish raises `NotImplementedError`. Revision changes pending work while preserving history and budgets. Unknown consumed effects or incomplete observations block unsafe progression.

`resolve_wait(resolution, *, credential)` requires configured trusted resolver authority and returns `GoalSnapshot`. Permission/timer facts are verified. Resolution is distinct from continuation and preserves paused intent.

## Management controls

`pause`, `resume`, and `cancel` each take `(goal_id, version, *, credential)` and return `GoalStatus`. Management authority and expected versions are required. Operator resume restores paused intent, reads no checkpoint, and launches no execution. Cancellation is not physical termination evidence.

## Errors and recovery

Malformed fields, unreadable content, expired new acceptance, stale versions/conflicting IDs, missing state, unsupported actions, and persistence faults fail explicitly. Keep original accepted IDs for replay; refetch current state before a new decision. See [Errors](../errors/) and [Declare and inspect a goal](../../guides/goals/).
