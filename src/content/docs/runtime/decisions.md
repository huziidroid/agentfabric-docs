---
title: Decisions, revisions, and operator controls
description: Agent judgments, exact decision requests, optimistic versions, and management intent.
---

## Decisions use a recorded request

A `DecisionRequest` identifies the exact goal version, plan revision, request context, and relevant task outcome or wait resolution. An `AgentSignal` must echo the matching request and action-specific evidence. The agent supplies the business judgment; Runtime checks whether that transition is currently valid. The current native signal path requires a management principal whose identity equals the configured decision actor.

For example, an agent may accept a reporting task's contribution and request continuation to the next task. A stale decision about an earlier outcome cannot authorize new work.

## Implemented actions

| Signal | Effect |
| --- | --- |
| `continue` | Authorize the applicable next task after required assessment. |
| `revise` | Replace pending work while preserving completed history and budgets. |
| `stop` | Record the agent's stop decision. |
| `wait` | Record a supported input dependency. |
| `resume` | Authorize same-task continuation from a recorded checkpoint. |
| `retry` | Authorize a qualifying before-start retry. |

`finish` is defined in the schema but currently raises `NotImplementedError`. Assessment/completion handlers and reports are extension contracts, not a working Finish tutorial.

## Revisions and replay

Revision may retain or reorder unchanged tasks still in the current pending set. It cannot repurpose completed, rejected, or superseded task IDs, rewrite accepted task specifications under existing IDs, or substitute unregistered handlers. Changed tasks need new IDs. It consumes the applicable accumulated budget rather than resetting counters.

`DecisionReceipt` records the applied result. Exact signal replay recovers that result; conflicting signal-ID reuse is rejected. Read the current request before proposing a new transition.

## Management controls

`pause`, `resume`, and `cancel` require management authority and the expected goal version. They express operator intent separately from agent judgments. Operator resume restores paused intent; agent resume concerns a checkpoint. Neither automatically dispatches an execution.

Resolving a wait while paused must not silently restore running intent. Cancelling an awaiting call or recording cancellation is not proof that a physical process stopped.

Follow [Apply decisions and controls](../../guides/decisions/), then consult the [Goal API](../../reference/goals/) and [decision models](../../reference/generated/decisions/).
