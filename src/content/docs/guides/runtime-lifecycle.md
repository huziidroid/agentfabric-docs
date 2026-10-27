---
title: Open and close Runtime
description: Prepare native storage, configure authority and limits, and manage service lifetime.
---

## Prerequisites

Use a compatible source installation on a POSIX host. The trusted application supplies the namespace, canonical private storage paths, all settings limits, and authority policy. The [complete tutorial](../../tutorials/native-runtime/) contains a runnable configuration.

## Prepare and open

1. Create the database parent and artifact directories with ownership by the application user and mode `0700`.
2. Resolve filesystem aliases before supplying paths. Existing database/sidecar files must satisfy the native file rules.
3. Build `SQLiteRuntimeSettings` with every required limit and timeout. Build a matching integrated/local `AuthorityPolicy`.
4. Call `Runtime.open_sqlite(settings, policy=policy)` synchronously before entering the host event loop.
5. Bootstrap trusted identity explicitly if needed. Opening does not grant authority or start work.

## Await and close

Use the returned service map and await asynchronous calls. Use context-manager exit or `close()` only after the actual underlying operations have finished. Cancelling an awaiting coroutine is not sufficient evidence that a file or SQL job quiesced.

Construct a new instance after a host fork. Do not race close against new calls. If a provider source was supplied, Runtime borrows it: close that source after its dependent work and Runtime finish.

## Recover a partial open

A construction exception can occur after schema/storage/policy setup was persisted. Correct the failure and retry the same explicit binding/policy; do not assume cleanup undid durable writes. Unsupported database schema is a compatibility issue, not permission to reset state.

See [Construction reference](../../reference/runtime/), [Durability](../../runtime/durability/), and [Troubleshooting](../../support/troubleshooting/).
