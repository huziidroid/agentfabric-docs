---
title: Resolve waits and continue work
description: Resolve exact user/permission/timer dependencies without implicit progression.
---

## Prerequisites

A recorded current wait, a current goal snapshot, and configured resolver authority. User input must refer to the saved request; permission/timer resolution must satisfy verifiable service facts.

## Inspect and resolve

This contextual helper resolves a user wait with no content payload. It needs a real saved user wait and resolver credential; it cannot manufacture permission or timer evidence.

```python
from agentfabric_runtime.goals.schemas import WaitResolution

async def resolve_user_wait(runtime, goal_id, resolution_id, resolver_credential):
    current = await runtime.goals.inspect(goal_id, credential=resolver_credential)
    wait = await runtime.goals.inspect_wait(goal_id, credential=resolver_credential)
    if wait is None or wait.kind != "user":
        raise ValueError("A saved user wait is required")
    resolution = WaitResolution(
        id=resolution_id, goal_id=goal_id, goal_version=current.version,
        wait_id=wait.id, request_ref=wait.request_ref, outcome="resolved",
    )
    return await runtime.goals.resolve_wait(resolution, credential=resolver_credential)
```

Choose a stable `resolution_id` before the first attempt and retain the original full resolution for exact replay. Do not reconstruct an old resolution from newer goal versions after a lost reply.

For resolved input bytes, publish them under applicable authority and include the valid `result_ref`. Denied or expired outcomes are not successful input.

## Continue explicitly

Read the resulting decision request, have the agent issue matching Continue or Resume, then dispatch separately. A paused goal preserves paused intent after resolution; operator resume and agent continuation are distinct steps.

Permission approval alone neither resolves the goal wait nor authorizes a next task. Timer resolution must verify time instead of trusting a supplied status label.

See [Wait concepts](../../runtime/waits/), [Checkpoint continuation](../../runtime/checkpoints/), and [exact wait fields](../../reference/generated/decisions/).
