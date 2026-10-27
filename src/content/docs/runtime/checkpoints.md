---
title: Checkpoints and same-task Resume
description: Pinned continuation input, versioned task returns, and safe source access.
---

## Why checkpoint?

A handler can yield partway through a task and preserve enough state for a later invocation. `Checkpoint` pins the logical task, source execution, handler version, original input, format, content reference, and unique operation IDs.

For a long report, the checkpoint could record completed analysis while waiting for a user choice. It must use the task's declared checkpoint format and accepted handler/input binding.

## Return format matters

`TaskCompletion` is the frozen V1 format. A yielded V1 response requires its wait. `TaskCompletionV2` permits a yielded checkpoint without a wait. Do not change a V1 format label to bypass its validation.

Runtime verifies the actual return and stopped execution before exposing the relevant agent request. A checkpoint artifact by itself does not authorize a continuation.

## Resume authorizes, dispatch starts acceptance

The agent sends an exact `resume` signal for the matching decision request. Any declared wait must have a verified resolution. A separate dispatch creates a new execution for the same logical task.

`TaskInvocation` preserves accepted task input. `TaskContinuation` ties the source technical outcome to its checkpoint and optional paired wait/resolution. The new executor receives the declared checkpoint and optional resolved input, not arbitrary prior artifacts.

## External effects remain part of history

An unused operation ID may survive in a checkpoint, but it conveys no authority to inspect, renew, consume, or resolve credentials for the old action. Complete operation observations cover all goal executions. A consumed action with an unknown external result blocks unsafe continuation even when the checkpoint omits it.

Operator `goals.resume()` restores paused intent and does not read checkpoint bytes. See [Continue a checkpoint or retry](../../guides/recovery/) and the [completion reference](../../reference/completions/).
