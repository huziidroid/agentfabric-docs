---
title: Bootstrap and rotate credentials
description: Operate trusted local credential administration without exposing it to workloads.
---

## Prerequisites

An open native Runtime and trusted host control over its identity administration. The tutorial's `principal` is a valid management `VerifiedPrincipal`; `runtime` refers to its open Runtime. This object must not be exposed to workers or unauthenticated callers.

## Bootstrap a management identity

This contextual call is used in the runnable tutorial:

```python
credential = runtime.identities.bootstrap_management(
    "management.json", "management", principal
)
```

The private publication is recoverable across reopening. Keep the secret inside the trusted host and never print it. A credential still needs applicable capability authority.

## Issue and rotate a credential

For host-administered issuance with a valid principal:

```python
issued = runtime.identities.issue("host-session-1", principal)
assert issued.secret is not None
replayed = runtime.identities.issue("host-session-1", principal)
assert replayed.secret is None
rotated = runtime.identities.rotate("host-session-1", "host-session-2", principal)
assert rotated.secret is not None
runtime.identities.revoke("host-session-2")
```

These synchronous methods require trusted administration rather than a `credential=` argument. New secrets appear only on new issuance; store them privately before discarding a response. Rotation preserves required identity/context claims and invalidates the predecessor.

## Workload and executor identities

Create workload/executor principals only from authoritative accepted execution/allocation facts. They require exact context, identity, generation, and controller version. A worker-supplied execution ID is not such evidence. Management and execution roles are different axes.

## Failure recovery

Conflicting issuance identity is rejected. Lost bearer material is not retrievable from an issue replay; recover private bootstrap publication or perform an explicit authorized rotation appropriate to the host. Revoked/expired credentials must not be reused.

See [Identity concepts](../../runtime/identities/) and [Identity reference](../../reference/identity/).
