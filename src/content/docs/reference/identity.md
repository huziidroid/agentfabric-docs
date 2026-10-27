---
title: Identity administration API
description: Trusted synchronous credential issuance, inspection, rotation, revocation, verification, and bootstrap.
---

Access this service as `runtime.identities`. Its native implementation is `agentfabric_runtime.storage.repositories.credential_repo.SQLCredentialStore`; use Runtime to construct it.

[Exact method signatures](../generated/clients/) and [identity schemas](../generated/core/) supply parameter types/defaults and response fields.

## Trusted-host requirement

These synchronous administration methods have **no `credential=` parameter**. The application must protect access to this service itself. They are not worker-callable permission endpoints.

| Operation | Preconditions and effect | Returns / replay |
| --- | --- | --- |
| `issue(credential_id, principal)` | Valid principal in the namespace; persist credential issuance. | `CredentialIssue`; bearer once on new issuance, `secret=None` on exact replay. |
| `rotate(old_id, new_id, principal)` | Preserve required identity/context binding; create successor and revoke old credential. | `CredentialIssue`; replay does not regenerate bearer. |
| `inspect(credential_id)` | Trusted host reads saved credential metadata. | `CredentialRecord` with principal, state, issue time, and optional rotation source. |
| `revoke(credential_id)` | Trusted host revokes the saved credential. | `None`; subsequent verification cannot treat it as active. |
| `verify(credential)` | Current valid bounded `SecretStr` bearer required. | `VerifiedPrincipal`; checks live issuance/revocation/expiry. |
| `bootstrap_management(filename, credential_id, principal, *, rotation_from=None)` | Management principal, private recoverable publication, exact bootstrap binding. | `SecretStr`; recover matching existing publication rather than reissue arbitrary authority. |

## Principal invariants

Management cannot carry workload context/generation claims. Workload/executor require exact execution context, matching identity, resource generation, and controller version. Execution roles `task`, `assessment`, and `check` belong to context, separately from authentication roles.

`CredentialRecord` states are pending, issued, or revoked. A known ID or successful token parse does not establish action eligibility; protected capability boundaries recheck current authority and resource state.

## Failure and recovery

Malformed input raises validation errors; conflicting ID/principal reuse raises `RequestConflictError`; missing records, authorization failures, and persistence faults use the categories in [Errors](../errors/). Bootstrap SQL/file publication is recoverable rather than one cross-resource transaction.

Keep new bearer material in trusted private storage. An issue replay cannot recover a bearer that was returned once and lost. Use [Bootstrap and rotate credentials](../../guides/credentials/) and the [native tutorial](../../tutorials/native-runtime/).
