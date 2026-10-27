---
title: Before-start Retry
description: Retry eligibility, immutable accepted input, and the limits of recovery.
---

## A narrow retry boundary

Implemented Retry applies to an unfinished task whose execution was denied before any launch attempt was created. The agent supplies the exact task, outcome, and decision context, without inventing a contribution assessment.

For example, admission may deny a queued invocation before work launches. After the blocking condition is addressed, the agent can request another attempt within the existing goal limits.

## What Runtime checks

Runtime verifies the actual denial, stopped work, input availability, deadlines, accumulated budgets, and complete effect history. Retry preserves accepted input exactly, including an earlier checkpoint continuation. It does not reinterpret the task or reset its budget counters.

The signal authorizes retry. A later dispatch creates the execution. Until that dispatch, no new execution has been accepted.

## Work that already launched

Retry after launched work requires additional reset and external-effect recovery support that remains unfinished. A failed or unknown remote result must not be treated as a before-start denial.

A storage timeout also does not establish that a launch or commit failed. Recover the original request/receipt before deciding whether replacement work is safe.

Follow [Continue a checkpoint or retry](../../guides/recovery/) and [Durability and recovery](../durability/). Read [current capabilities](../capabilities/) before building automated retry loops.
