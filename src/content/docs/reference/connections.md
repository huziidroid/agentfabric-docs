---
title: Connections and credential resolution API
description: Connection metadata mutations and borrowed provider-secret sources.
---

Connection models live in `agentfabric_runtime.permissions.schemas`. Service protocols are in `agentfabric_runtime.permissions.interfaces`; the native source is `agentfabric_runtime.storage.provider_credentials.FileCredentialSource`.

Use [exact signatures](../generated/clients/) and [connection fields](../generated/permissions/) alongside this behavior reference.

## `runtime.connections`

All methods are synchronous, require `credential=SecretStr`, and require a configured management issuer.

| Method | Preconditions / effect | Return |
| --- | --- | --- |
| `put(record, mutation_id, *, credential)` | Registered provider/origin; connected nonexpired record. New records start at version 1; updates advance exactly one. Provider/account/origin identity is immutable. | Saved `Connection`. |
| `inspect_connection(connection_id, *, credential)` | Authorized issuer reads exact metadata. | `Connection`. |
| `disconnect(connection_id, expected_version, mutation_id, *, credential)` | Match current version; record disconnected state and next version. | Updated `Connection`. |

Exact mutation replay recovers saved output. Reusing an ID differently or using a stale version raises a conflict. A connection records configuration, not provider account ownership or action authority.

## `FileCredentialSource`

The application constructs the source over its private directory and namespace and supplies it to `open_sqlite`. Runtime borrows it. The source does not provide an OAuth authorization, credential writer, automatic refresh, or workload-facing cache.

`digest(reference, *, provider, account_id, origin)` computes a fingerprint only after exact private envelope binding checks. `read(record)` verifies the record's namespace/provider/account/origin/reference/fingerprint before returning `SecretStr`. Use the [exact source signatures](../generated/clients/) for construction and close details.

## `runtime.provider_credentials.resolve`

This optional service is `None` without a provider source. `resolve(permit, *, credential)` synchronously returns `SecretStr` only to an authorized trusted executor holding a saved current unconsumed adapter permit. Connection version, policy/adapter identity, scope, expiry, and live authority must still match.

Resolution does not consume the permit or prove the external result. Raw web permits cannot select provider credentials. Retain the secret only inside the trusted executor boundary.

## Failure and lifetime

Expect validation, authorization, stale-version/request conflicts, missing metadata, or storage errors. Invalid private envelopes and mismatched digests fail closed. Close a borrowed source only after Runtime and source-dependent work quiesce.

Follow [Manage connections](../../guides/connections/) and read [Action admission](../../runtime/admission/) before integrating secrets with remote effects.
