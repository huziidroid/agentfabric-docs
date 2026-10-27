---
title: Continue a checkpoint or retry before start
description: Choose the correct continuation path and preserve accepted input and effects.
---

## Prerequisites

A real recorded technical outcome, its exact decision request, current agent authority, available inputs, remaining budgets, and complete operation observations. This guide does not provide a physical handler or launched-work recovery implementation.

## Continue a checkpoint

1. The trusted executor records the actual yielded return with its declared checkpoint and applicable wait.
2. Use V2 for a yielded checkpoint without a wait; retain V1's strict wait requirement for V1 records.
3. Reconcile until the actual stopped execution and return evidence support the decision request.
4. Resolve any saved `resume_task` wait with its exact request identity.
5. The agent supplies Resume with the matching checkpoint, task, outcome, request, goal version, and plan revision.
6. Dispatch separately. The new execution retains the same logical task and accepted continuation input.

Only the declared checkpoint and optional resolved input are exposed. A checkpoint operation ID does not give the new execution authority over the old action.

## Retry a before-start denial

Verify the recorded denial occurred before creation of a launch attempt. Supply an exact Retry signal for that unfinished task/outcome/request without a contribution assessment. Runtime rechecks stopped state, deadlines, budgets, inputs, and complete effect history. Then dispatch separately.

Retry retains original accepted input, including an earlier continuation. It does not rewrite the handler or reset accumulated budgets.

## Stop when results are uncertain

Unknown consumed external effects, incomplete operation observations, unavailable source data, or uncertain resource termination block safe progression. A generic failure or timeout is not proof of before-start denial. Retry after launched work and original external-action recovery remain unfinished.

See [Checkpoint concepts](../../runtime/checkpoints/), [Retry concepts](../../runtime/retry/), [Task completion API](../../reference/completions/), and [Troubleshooting](../../support/troubleshooting/).
