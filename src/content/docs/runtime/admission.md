---
title: Action admission and effect safety
description: Permission approval, exact permits, single-use consumption, and uncertain external effects.
---

## From access to a specific action

A permission grant describes eligible access. `AdmissionRequest` binds one immutable operation intent to exact context, binding and policy versions, scope, deadline, resource generation, and controller version. Adapter requests also bind a complete connection/provider/version/implementation identity.

`runtime.authority.admit()` evaluates current authority and records an `AdmissionPermit`. The permit binds an exact attempt, allocation, claim, grant lineage/version set, and expiry. It cannot outlive the action deadline.

For example, permission to read sales data is broader than admission of one accepted read operation for one execution generation.

## Renewal and consumption

`renew()` names the exact previous permit. Renewal refreshes bounded authority for the accepted action; it does not rewrite immutable intent or retarget another allocation.

`consume()` orders single-use consumption against live expiry and revocation. Its `AdmissionConsumption` reports `new` or `already_consumed`. The latter is a replay observation, not permission to repeat an external side effect.

Credential resolution, consumption, dispatching a remote request, and recording the external result remain distinct responsibilities. No local receipt alone proves the remote provider's result.

## Unknown effects

A consumed action can have an unknown external result. In that case, starting replacement work can duplicate an effect. Progression checks therefore require complete operation observations across all goal executions, including untracked work and other execution roles.

`OperationReadLimits.max_goal_operations` bounds that complete observation. Overflow refuses progression rather than declaring the omitted history safe. Omitting an action from a checkpoint does not remove it from effect history.

## Operation contracts

`OperationRequest` names the requested action and input. `OperationIntent` pins accepted configuration, authority evidence, and resource generation. `OperationOutcome` distinguishes pending, succeeded, failed, and unknown. Success requires a saved result reference; failure requires a bounded error code.

Internal operation observations are implemented. `OperationClient.execute/inspect/reconcile` is a protocol; there is no `runtime.operations` facade or completed public external-operation runner/result recovery path.

Read [Admit an external action](../../guides/admission/) and the [Authority API](../../reference/authority/). The [operation declarations](../../reference/generated/operations/) describe extension contracts.
