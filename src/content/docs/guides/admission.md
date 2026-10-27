---
title: Admit an external action safely
description: Bind immutable intent, resolve credentials, consume once, and preserve uncertain effects.
---

## Prerequisites

This is an integration guide for a trusted host/executor, not a complete external-operation runner. You need authoritative accepted execution/allocation/control facts, a current eligible authority binding, applicable grant lineage, and a declared exact operation intent. Fabricating those fields from worker input is unsafe.

## Admit the exact intent

1. Build `AdmissionRequest` with a stable request ID and operation ID, exact context, binding/policy versions, scope, intent digest, resource generation/controller, and deadline.
2. For adapter access, include the complete connection ID/provider/version/implementation binding. For raw web access, omit all secret-selection fields.
3. Call `runtime.authority.admit(request, credential=...)` under currently authorized context. It records the bounded permit for the exact resource/claim/attempt.
4. If the original reply is uncertain, use `inspect_admission()` and the original identity. Renewal must name the exact predecessor and accepted action.

## Resolve and consume

Resolve provider material only through the optional trusted resolver for a saved current unconsumed adapter permit. The effective executor then calls `consume()` under live authority before the external effect.

If consumption returns `already_consumed`, do not repeat the remote request. It identifies saved single use, not another permission to execute.

## Preserve uncertainty

A consumed operation can lack a known external result. Do not start replacement work merely because the caller timed out. Complete operation observations, including other roles and untracked executions, must prevent unsafe progression.

Public `OperationClient` execution/results and original-action recovery remain unfinished. Implemented admission and observations do not supply a complete external action transport.

See [Admission concepts](../../runtime/admission/) and [Authority reference](../../reference/authority/).
