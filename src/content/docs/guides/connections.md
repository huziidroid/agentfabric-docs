---
title: Manage connections and provider sources
description: Register exact connection metadata and resolve credentials only at the executor boundary.
---

## Prerequisites

A configured adapter definition, current management issuer authority, private provider-secret material provisioned by the application, and an exact namespace/provider/account/origin binding. This guide does not provide OAuth or secret-writing functionality.

## Register metadata

1. Open `FileCredentialSource` over the application-owned private directory and namespace.
2. Use its `digest(reference, provider=..., account_id=..., origin=...)` to verify and fingerprint the existing exact envelope. This returns a digest, not the secret.
3. Construct `Connection` with ID, namespace, provider, account, origin, private credential reference/digest, connected state, version 1, and optional expiry.
4. Call `runtime.connections.put(record, mutation_id, credential=issuer_credential)`.
5. Inspect with `inspect_connection()` under issuer authority. Metadata does not establish remote ownership or grant access.

When using provider resolution, supply the open source to `Runtime.open_sqlite(provider_source=source, ...)`. Runtime borrows it; the application closes it after dependent operations finish.

## Resolve for an admitted action

The trusted executor supplies a saved current unconsumed adapter permit to `runtime.provider_credentials.resolve(permit, credential=executor_credential)`. Check that this optional resolver exists before using it. Live policy, connection version, adapter binding, scope, and resource authority must still match.

Keep the resulting `SecretStr` inside trusted execution. Resolution is distinct from single-use consumption and recording the external result. A raw web permit cannot select provider secrets.

## Update or disconnect

Preserve provider/account/origin identity. A metadata update advances the saved version exactly one; use a new connection ID for a different identity. `disconnect()` needs the current expected version and a stable mutation ID. Recover exact mutation results after uncertainty rather than guessing the next version.

See [Connection concepts](../../runtime/connections/), [Connection API](../../reference/connections/), and [Admission](../../runtime/admission/).
