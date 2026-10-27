---
title: Introduction
description: What AgentFabric is and how its components fit together.
---

AgentFabric is a platform for defining, running, coordinating, and hosting versioned AI workers that perform work for users.

Your application supplies agent behavior, requested outcomes, and permission policy. Runtime records goals and ordered tasks, enforces authority boundaries, and preserves progress. The agent supplies judgments about the results and what should happen next.

## Platform components

| Component | Responsibility |
| --- | --- |
| **Runtime** | Durable goals, tasks, decisions, waits, recovery, and enforcement of external access. |
| **AgentCLI** | Define workers and harness their reasoning, planning, and task execution from a command line. |
| **Fabric** | Coordinate workers, communication, and delegated work. |

These describe intended platform responsibilities. This documentation currently focuses on Runtime.

## Example: preparing a report

An application receives a request for a sales report. It declares a goal and tasks for reading data, analyzing it, and creating a document. The application grants access to the relevant source.

The agent supplies task behavior and assesses results. Runtime tracks progress and validates requests to continue, revise pending work, or wait for input. Sending the report through an email account requires the applicable external permission.

This is a product example, not an executable tutorial. Check [current capabilities](../../runtime/capabilities/) before planning an integration.

## Where to begin

Read [Runtime at a glance](../runtime-overview/), then learn the [core concepts](../../runtime/concepts/).
