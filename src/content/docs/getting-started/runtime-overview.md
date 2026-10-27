---
title: Runtime at a glance
description: Understand the boundary between your application, your agent, and Runtime.
---

AgentFabric Runtime is a Python SDK for recording application-defined goals and ordered tasks, enforcing application-owned authority, and preserving progress across restarts.

## Who owns what?

| Your application and agent provide | Runtime provides |
| --- | --- |
| Requested outcomes and ordered task definitions | Durable goal and task records |
| Versioned handler references and agent behavior | Validation of accepted work and decisions |
| Identity bootstrap and permission policy | Enforcement of configured authority |
| Business judgments about task results | Outcome records and validated transitions |
| Storage locations and resource limits | Native SQLite state and local artifact storage |

Runtime does not interpret a natural-language goal or invent a plan to achieve it.

## The coordination cycle

1. Register a versioned agent binding and submit a goal.
2. Runtime validates and records the declared work.
3. Dispatch accepts an execution for the current task.
4. A trusted executor records a return; outcome coordination verifies the recorded work.
5. The agent assesses the result and submits a decision.
6. Runtime validates the decision and records the next transition.

:::caution[Execution support]
The current public dispatch path records accepted execution work; it does not run a handler. Physical execution and termination guarantees remain unfinished. This cycle explains the coordination model, not an available end-to-end runner.
:::

## Integration requirements

The SDK requires Python 3.12 or newer. Native storage uses SQLite and application-owned local directories. Your host supplies explicit limits and authority policy.

This site does not yet provide a verified package-index install command or a complete runnable agent tutorial. Use the [capability guide](../../runtime/capabilities/) to assess readiness.
