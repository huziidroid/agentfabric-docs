---
title: Permission API
description: Policy, grants, requests, decisions, eligibility bindings, revocation, and scoped reads.
---

Use synchronous `runtime.permissions`. The interface is `agentfabric_runtime.permissions.interfaces.PermissionService`. All calls require `credential=SecretStr`.

Consult [exact client signatures](../generated/clients/) and [permission schemas](../generated/permissions/) for parameter types, defaults, and constraints.

## Administration and resolution

| Method | Required authority | Durable effect / return |
| --- | --- | --- |
| `configure(policy, mutation_id, *, credential)` | Current configured management issuer. | Policy update preserves namespace/store and advances version exactly one; returns `AuthorityPolicy`. Identity profile changes need explicit administrative migration. |
| `issue(grant, mutation_id, *, credential)` | Root: configured management issuer. Child: management identity of parent recipient, with valid delegation. | Issuer matches authenticated actor; insert bounded live grant; return `Grant`. |
| `bind(binding, *, credential)` | Configured management resolver. | Record/version eligible root grants and context; return `AuthorityBinding`. Replay identity is binding ID/version. |
| `decide(decision, *, credential)` | Configured management resolver. | Resolve exact pending request and expected binding version; return `PermissionSnapshot`. A grant needs explicit expiry within request deadline. |
| `revoke(grant_id, expected_version, mutation_id, *, credential)` | Configured management resolver. | Revoke expected grant version; returns `None`. |

## Requests and reads

| Method | Required authority and return |
| --- | --- |
| `request(request, *, credential)` | Represent the exact requested context within its binding; return pending or replayed `PermissionSnapshot`. |
| `inspect(request_id, *, credential)` | Current authorized representation of the saved request context; return `PermissionSnapshot`. |
| `inspect_binding(binding_id, *, credential)` | Namespace management or matching own workload context; return `AuthorityBinding`. |
| `inspect_grant(grant_id, *, credential)` | Namespace management or matching recipient/workload context; return `Grant`. |

`AuthorityConfig` explicitly names issuer and resolver actor sets. Workload request/inspection is not authority to issue, approve, bind, or revoke grants.

## Invariants and replay

Exact scope, recipient, context, role, delegation lineage, expiry/revocation, policy version, and configured read-completeness bounds are enforced. Empty binding roots deny external access. Restrictions narrow authority and never supply grants.

Request/mutation identities bind original arguments. Exact replay returns saved results under current authorized entry; conflicting reuse or stale expected versions fail. Permission approval does not authorize a next goal task or resolve a goal wait automatically.

## Errors

Validation errors/`ValueError` cover malformed scope or context. `AuthorizationError` covers inapplicable authority; `RequestConflictError` covers stale/conflicting mutation. Missing or invalid stored evidence and storage failures retain their defined categories. Read overflow fails closed rather than authorizing from a partial grant set.

See [Permission concepts](../../runtime/permissions/) and [Manage access](../../guides/permissions/).
