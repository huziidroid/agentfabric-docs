---
title: Waits and verified input
description: Permission, user, and timer dependencies and their explicit resolution.
---

## A wait records a dependency

`WaitSpec` pins a wait ID, kind, request reference, continuation, and deadline. Kinds are `permission`, `user`, and `timer`. A continuation can lead to the next task or resume the same logical task.

A reporting task might wait for a user to choose a time range. A permission wait instead depends on verified access approval; a timer wait depends on the appropriate time condition.

## Resolution is separate from continuation

`inspect_wait()` returns the saved current wait. A trusted resolver submits `WaitResolution` naming the exact goal/version/wait/request and outcome. Permission and timer facts are verified by the service, not accepted just because the caller claims them.

Denial and expiry are not successful data. Optional resolved input is paired with the recorded resolution and remains subject to content authority checks.

A successful resolution makes the appropriate decision context available. It does not grant a next task automatically, launch an execution, or resume a paused goal. The agent still supplies the matching Continue or Resume signal, and dispatch is separate.

## Same-task waits

A yielding task may pair its checkpoint with a `resume_task` wait. The exact checkpoint, wait, and resolution must match. This prevents a response to one user question from being applied to another invocation.

See [Resolve waits and continue work](../../guides/waits/) and [Checkpoints and Resume](../checkpoints/). Exact kinds, fields, and resolution invariants are listed in the [decision model reference](../../reference/generated/decisions/).
