---
title: Authority and admission API
description: Exact action permits, renewal, single-use consumption, and saved observations.
---

Use synchronous `runtime.authority`, conforming to `agentfabric_runtime.permissions.interfaces.AuthorityProvider`. All calls require `credential=SecretStr`. Admission, renewal, and consumption enforce current action/resource authority. Metadata inspection is separately authorized for namespace management or the original exact context; it can recover saved observations after the action stops or its former grant expires.

[Admission schemas](../generated/permissions/) define every request/permit field. [Client signatures](../generated/clients/) provide exact annotations.

## Methods

| Method | Preconditions / effect | Returns |
| --- | --- | --- |
| `admit(request, *, credential)` | Validate immutable intent, context, versions, scope, current grant lineage and resource control; save exact admission. | `AdmissionPermit`. |
| `renew(request, previous_permit_id, *, credential)` | Match exact accepted request and predecessor; recheck current authority and bounds. | Successor `AdmissionPermit`. |
| `inspect_admission(request_id, *, credential)` | Authorized observation of original request. | Saved `AdmissionPermit` or `None`. |
| `consume(permit, *, credential)` | Effective trusted executor; exact saved unexpired/current permit and resource control. Order single use against live revoke/expiry. | `AdmissionConsumption` with `new` or `already_consumed` disposition. |
| `inspect_consumption(request_id, *, credential)` | Authorized observation of original action consumption. | `AdmissionConsumption` or `None`. |

A valid credential alone is insufficient. Admission also validates current binding/policy, required complete grant observations, and applicable context. An adapter request needs complete connection/provider/version/implementation binding; raw web requests cannot carry those secret-selection fields.

## Replay and effects

Exact accepted request identities and renewal predecessors remain immutable. Conflicting reuse is rejected. Repeated consumption observes the same action rather than authorizing another remote invocation.

A permit or consumption receipt is not an external result. The host executor must avoid blindly resending a consumed operation with unknown result. Implemented complete-operation observations block unsafe progression; public operation execution/result recovery is unfinished.

## Limits and errors

Permit lifetime is bounded by explicit configured lifetime, action deadline, and current authority. `AdmissionReadLimits.max_candidate_grants` bounds a complete candidate query; overflow fails closed.

Validation, authorization, stale/conflicting identity, unavailable current evidence, and storage faults use [Errors and limits](../errors/). Resource-generation/controller mismatch is an authorization/freshness failure, not an invitation to rewrite accepted intent.

See [Admit an external action](../../guides/admission/) and [Operation contracts](../generated/operations/).
