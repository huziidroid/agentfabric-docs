---
title: Identities and credentials
description: Trusted host administration, principal roles, execution context, bootstrap, and rotation.
---

## Two kinds of role

A principal's authentication role is `management`, `workload`, or `executor`. An execution context's role is `task`, `assessment`, or `check`. These answer different questions: who may administer or perform work, and what kind of invocation that work belongs to.

`AccessContext` ties an identity and agent to optional goal, task, and execution identifiers. A task context requires a goal. Workload and executor principals require an exact execution context, matching identity, resource generation, and controller version. Management principals cannot carry workload context or generation claims.

For a reporting task, the application may hold a management credential while the worker and trusted executor hold separate exact-context credentials. Merely knowing the task ID does not confer either role.

## Trusted administration

`runtime.identities` exposes synchronous host administration: `issue`, `rotate`, `inspect`, `revoke`, `verify`, and `bootstrap_management`. These methods deliberately have no `credential=` parameter. They assume the caller is already inside the trusted host boundary. Do not expose this object directly to workers or unauthenticated HTTP callers.

`issue()` returns `CredentialIssue(record, secret)`. A new issuance returns the bearer once. Exact replay returns saved metadata with `secret=None`; replay does not regenerate a secret. Records have `pending`, `issued`, or `revoked` state.

## Bootstrap and rotation

`bootstrap_management()` publishes a management credential through private recoverable storage. The native tutorial uses this to retain the same bootstrap across reopening. File publication and SQL state are recoverable operations, rather than one atomic cross-resource write.

`rotate()` changes the credential while preserving required identity/context binding and revoking the old bearer. The host must preserve new secret material safely; an issuance replay cannot retrieve a lost bearer. Never print or store bearer values in public logs.

## Verification remains current

`verify()` returns a `VerifiedPrincipal`. Capability boundaries still validate current policy, eligibility, expiry, and resource generation/controller state. A token that parses successfully does not establish permission to perform an external action.

Follow [Bootstrap and rotate credentials](../../guides/credentials/) and see [Identity API behavior](../../reference/identity/) plus the [exact declarations](../../reference/generated/core/).
