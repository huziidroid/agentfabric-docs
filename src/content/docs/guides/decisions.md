---
title: Apply agent decisions and operator controls
description: Validate exact decision context and keep operator intent separate from agent judgments.
---

## Prerequisites

The goal has a current `DecisionRequest`. The configured decision actor supplies the signal through a current management principal with that exact identity; management controls use their own current authorized credential. A valid registered name alone does not authenticate either caller.

## Apply a decision

1. Read `pending_decision()` under supported current authority. If it returns `None`, do not invent a request.
2. Have the agent assess exact saved evidence as required by the request.
3. Construct `AgentSignal` with a stable signal ID, matching request/goal/version/plan, matching outcome reference where applicable, and the exact action-specific payload.
4. Call `goals.signal(signal, credential=decision_credential)` and save its `DecisionReceipt`.
5. Dispatch separately if the result authorizes work. Stop and Wait do not imply another dispatch.

Supported actions are Continue, Stop, Revise, Wait, Resume, and Retry. Finish remains unimplemented. Revision may retain or reorder unchanged current pending tasks. Changed tasks need new IDs; completed/rejected/superseded IDs cannot be repurposed. Preserve accumulated history/budgets and use registered handlers.

## Pause, resume, or cancel

The following is a contextual helper for an open Runtime and management credential:

```python
async def pause_goal(runtime, goal_id, management_credential):
    current = await runtime.goals.inspect(goal_id, credential=management_credential)
    return await runtime.goals.pause(
        goal_id, current.version, credential=management_credential
    )
```

Use the same read/version discipline for `resume` or `cancel`. Operator resume restores paused intent and does not read a checkpoint or dispatch. Cancellation intent does not prove physical termination.

## Recover a conflict

Replay the exact saved signal after a lost reply. Conflicting reuse is rejected. For a new decision after state changed, read the new request and evidence; do not merely replace the version number in an old judgment.

See [Decisions](../../runtime/decisions/), [Waits](../../runtime/waits/), and [Goal reference](../../reference/goals/).
