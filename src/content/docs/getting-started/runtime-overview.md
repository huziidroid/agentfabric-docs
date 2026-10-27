---
title: AgentFabric Runtime
description: Keep track of an AI worker's work, progress, results, and access.
---

**Keep track of the work, every step of the way.**

AgentFabric Runtime is the part of AgentFabric that keeps a record of an AI worker's work. It tracks planned steps, records results, checks access, and manages pauses for input or approval.

Your application defines the work. Your AI worker supplies the behavior and judges the results. Runtime provides the structure for tracking those steps and checking whether the next step is allowed.

## What Runtime helps you keep track of

| What you need to know | What Runtime records or checks |
| --- | --- |
| What are we trying to achieve? | The requested outcome and its planned steps. |
| What has happened so far? | Accepted work, recorded results, and decisions. |
| What are we waiting for? | Requests for user input, permission, or a timer. |
| May this worker access that resource? | Access against the rules supplied by your application. |
| What was saved before the application restarted? | Stored work and progress that the application can inspect after reopening. |

Saved progress does not automatically restart a worker. Your application still controls how work is carried out and continued.

## Example: keeping a report on track

In a reporting application, the plan might be to gather data, analyze it, and write a report. Runtime holds that plan and the recorded progress. The worker supplies the analysis; your application decides which data it may use.

If a step needs a decision from you, the application can record a wait. After the input is resolved, the worker's next decision and the application's next action are checked separately. Receiving an answer does not silently start more work.

:::caution[What is available today]
The current Runtime library can save plans, accept work, and record supported results and decisions. It does not yet run the worker's code itself. The reporting example explains how the parts fit together, rather than demonstrating a complete running agent.
:::

## For developers

Runtime is a Python library for developers, also called a software development kit (SDK). It is currently available as an unreleased source preview. Its current native setup uses SQLite for saved state and local files for content. Your application supplies storage locations, access rules, and resource limits.

- Read [current capabilities](../../runtime/capabilities/) before planning an integration.
- Follow [Installation](../installation/) and the [first artifact tutorial](../../tutorials/native-runtime/) to try implemented SDK behavior.
- Explore [core concepts](../../runtime/concepts/) when you are ready for the technical details.

Runtime stores and checks the work you define. The application and worker still provide the plan, the code, and the decisions about whether the result meets your needs.
