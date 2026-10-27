---
title: Declare and inspect a goal
description: Register a versioned binding, accept ordered tasks, and inspect dispatch records.
---

## Prerequisites

An open Runtime, readable published input, explicit budgets/deadline, and management authority. The [complete goal tutorial](../../tutorials/declare-goal/) supplies a runnable native example.

## Declare and accept

1. Construct immutable `HandlerReference` values that pin version/deployment/configuration digests and environment identity.
2. Construct `AgentBinding` with registered handlers, a decision actor in the namespace, and `decision_mode="signals"`.
3. Register the binding with `goals.register()`.
4. Construct `TaskSpec` entries with unique task IDs, exact registered handler, input, expected output, and checkpoint format when used.
5. Construct `GoalSpec` with stable submission request ID, root input, ordered tasks, goal budgets, accepted output budgets, and deadline. Submit with `goals.submit()`.

The response is a durable goal ID. Submission does not launch a handler.

## Inspect and dispatch

Read `goals.inspect(goal_id, credential=...)` to obtain current version and accepted details. Call `goals.dispatch(goal_id, details.version, credential=...)` only for currently authorized work. It returns an accepted execution ID; current dispatch performs no physical handler execution.

Use `tasks()` and `executions()` to distinguish logical tasks from attempts. Use `task_completions.inspect()` to observe actual technical outcome availability; a queued invocation has no invented success.

## Page history

Start `list(after=None, limit=...)` and follow `next_cursor`. Use nonnegative cursors for events and applied-version cursors for decisions. Respect page limits; cross-page reads are not a snapshot of frozen state.

On a stale version, refetch and evaluate current state. For an uncertain accepted request, recover the original identity instead of submitting new work blindly.

See [Goals and executions](../../runtime/lifecycle/) and [Goal API](../../reference/goals/).
