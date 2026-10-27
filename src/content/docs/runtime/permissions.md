---
title: Permissions and authority
description: Application-owned grants, policy restrictions, exact context, and bounded inheritance.
---

## Authority is application-owned

The application selects trusted issuers and resolvers, policy versions, storage profile, and permit lifetime through `AuthorityConfig`. `AuthorityPolicy` adds restrictions, adapter definitions, and adapter-only origins. Native construction requires integrated authority and local identity storage.

A grant authorizes one recipient within a scope, context ceiling, and expiry. Opening Runtime or registering a worker never creates a grant implicitly.

## Scope and route

`ExternalScope` uses an exact canonical HTTPS origin, such as `https://example.com`. Paths, ports, embedded credentials, IP literals, queries, and fragments are rejected.

| Route | Meaning |
| --- | --- |
| `web` | Origin-level access. It cannot promise account, resource, or action restrictions. |
| `adapter` | Scoped access with an exact account, resource, and action, mediated by the declared adapter. |

`AdapterDefinition` pins provider, origin, actions, and an implementation digest. Adapter-only origins prevent bypassing scoped adapters through a raw web grant. Mixed routes for one origin are rejected by the applicable policy/grant validation.

## Eligibility and restrictions

`AuthorityBinding` identifies an actor's trusted eligible root grants, context, binding version, and policy version. An empty root set denies external access. It is not a fresh copy of all grants for every task.

`ContextLimits` names exact applicability and explicit execution roles. It does not use inferred wildcard authority. `AccessRestriction` applies a mandatory ceiling or denial; it never supplies authority that a grant lacks.

## Inheritance

A delegable parent grant may support child authority only within its scope, context, and lifetime. Parent revocation and expiry remain effective. A child cannot regain access merely by retaining a former parent ID.

For example, granting a worker access to one sales account does not authorize its child task to read another account or continue after the parent grant expires.

## Requests and decisions

`PermissionRequest` asks for access with a reason and deadline. A trusted resolver records a `PermissionDecision`; the snapshot becomes pending, granted, denied, or expired. A granted permission does not resume a goal or authorize its next task. Goal wait resolution and agent continuation are separate steps.

Read limits bound complete authority observations. Overflow fails closed; a partial grant list is not complete authorization evidence.

Use [Manage access](../../guides/permissions/) and the [Permission API](../../reference/permissions/). Exact field and scope requirements are in the [schema reference](../../reference/generated/permissions/).
