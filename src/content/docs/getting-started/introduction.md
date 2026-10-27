---
title: Meet AgentFabric
description: Build AI workers for useful tasks, with control over their work and access.
---

**Build AI workers that get work done.**

AgentFabric is a platform for building AI workers that carry out useful tasks, such as researching a topic, preparing a report, or processing documents.

An AI worker is software that uses AI to perform work on someone's behalf. With AgentFabric, you define what the worker should do and decide what information and tools it can access.

The platform is being developed to bring those workers, their work, and their progress together. These docs currently focus on its foundation: **AgentFabric Runtime**.

## One platform, distinct roles

| Part of AgentFabric | What it is for |
| --- | --- |
| **AgentFabric Runtime** | Keep a record of the work, track its steps and results, and check access. |
| **AgentCLI** | Define and work with AI workers through a command-line interface. |
| **Fabric** | Help multiple workers communicate and work together. |

These are the roles of the platform's parts, rather than a list of released products. See [current capabilities](../../runtime/capabilities/) for what is implemented today.

## Example: a sales report

Imagine asking a reporting worker to prepare this month's sales report. The work involves gathering sales data, analyzing it, and creating a document.

You decide which sales account the worker may access. Runtime keeps the plan and the recorded results. If the work needs your input or more access, that dependency can be recorded before the next step proceeds.

This illustrates the intended platform experience. A complete reporting worker that runs from start to finish is not supplied by the current Runtime library.

## Start with Runtime

Meet [AgentFabric Runtime](../runtime-overview/) to understand how it supports the work. If you are ready to try the developer tools, follow [Installation](../installation/) and the [first artifact tutorial](../../tutorials/native-runtime/).
