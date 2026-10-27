---
title: Goals, tasks, and executions
description: Ordered accepted plans, immutable handler bindings, inspection, and durable progress.
---

## The three units of work

A goal is a durable requested outcome with limits and decisions. A task is one logical contribution to that goal. An execution is one invocation performing some or all of a task. A retry or checkpoint continuation creates another execution for the same task.

A reporting goal might contain read, analyze, and format tasks. The accepted order belongs to the plan. Runtime does not infer this order from the natural-language description.

## Accepted declarations

`AgentBinding` pins a version, registered handler references, decision actor, and mode. `TaskSpec` pins an exact registered handler, input reference, expected output, and optional checkpoint format. `GoalSpec` combines the binding, root input, ordered tasks, deadline, goal budgets, and accepted output limits.

Handler references pin digests and environment identity; they are not callable import paths. Signal mode is the implemented direct decision path. Handler-mode and completion-check declarations do not establish executable assessment support.

## Register, submit, dispatch

Registration establishes a versioned binding. Submission records a goal idempotently. Dispatch checks current state and requirements before accepting execution work. These are separate operations. Dispatch currently records accepted work and does not physically run a handler.

Task completion records and outcome reconciliation supply technical evidence. The agent then assesses contribution and requests a validated transition. Revisions preserve history and accumulated budgets.

## Inspecting progress

Use `status()` for the goal status and `inspect()` for detailed saved specification, current authorization/execution, and history counts. `tasks()` returns ordered task views; `executions()` identifies task attempts. `list()` pages goals, `events()` pages events, and `decisions()` pages applied decisions chronologically by goal version. Pagination does not promise a cross-page snapshot.

## Status values

| Goal values | Interpretation |
| --- | --- |
| `ready`, `running` | Work is ready or has an active recorded execution. |
| `awaiting_agent`, `waiting_input` | Progress depends on an agent decision or input wait. |
| `paused`, `blocked` | Operator intent or verified conditions prevent progression. |
| `completed`, `failed`, `cancelled`, `expired` | Terminal-state vocabulary. Existence of a value does not imply every path to it is implemented; Finish remains unavailable. |

Task status values are `pending`, `running`, `awaiting_agent`, `accepted`, `rejected`, `superseded`, and `cancelled`. An accepted contribution is a different record from an execution return.

See [Declare and inspect a goal](../../guides/goals/), [Decisions and revisions](../decisions/), and the [Goal API](../../reference/goals/).
