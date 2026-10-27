---
title: Connections and provider credentials
description: Separate account metadata, stored secrets, permission, and trusted resolution.
---

## Connection metadata

A `Connection` binds a namespace, provider, account, origin, protected credential reference, credential digest, state, version, and optional expiry. It records the application's configured account binding. The record does not prove remote account ownership and does not grant permission to use the account.

For a reporting worker, an application might register sales-provider account metadata and separately authorize a read action. Both the connection and live authority must match before a provider credential is resolved.

## Secret material is separate

The optional native `FileCredentialSource` reads bounded private envelopes and verifies exact namespace/provider/account/origin/reference binding and fingerprint. It is an application-owned source, not an OAuth flow, secret writer, token refresh system, or filesystem reader for workloads.

`Runtime.open_sqlite(provider_source=...)` borrows the source. Without a source, `runtime.provider_credentials` is `None`. Close the source after Runtime and all underlying calls finish.

## Resolve at the trusted boundary

`provider_credentials.resolve()` requires a trusted executor and a saved, current, unconsumed adapter permit. The admission must match current connection version and configured adapter identity.

Reading the provider secret does not consume an action and does not prove that the remote action succeeded. Raw web grants cannot select provider secrets. Keep the returned `SecretStr` inside the trusted execution boundary.

## Connection changes

`put()` records metadata with a mutation ID. `disconnect()` uses an expected version and mutation ID. Current admission/resolution checks must observe the changed connection; keeping an old connection record does not preserve live access.

Use [Manage connections](../../guides/connections/) and the [Connection and credential API](../../reference/connections/).
