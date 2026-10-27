---
title: Runtime construction and settings
description: Native lifecycle, required configuration, owned resources, and close behavior.
---

## Imports and signatures

```python
from agentfabric_runtime.runtime import Runtime, SQLiteRuntimeSettings
```

[Exact settings and signatures](../generated/clients/) include all annotations/defaults for `open_sqlite`, `create_task_coordinator`, and `close`.

`Runtime.open_sqlite(settings, *, policy, clock=utc_now, legacy_policies=(), provider_source=None)` returns an open Runtime synchronously. Use it before entering the host event loop.

## Required settings

| Field | Meaning |
| --- | --- |
| `namespace` | Application/owner boundary shared with policy. |
| `database_path` | Absolute canonical SQLite file path with a prepared private parent. |
| `artifact_directory` | Existing absolute canonical private artifact directory. |
| `busy_timeout_ms` | Explicit database busy wait bound. |
| `file_lock_timeout` | Positive finite file-lock wait bound. |
| `artifact_limits` | Maximum ingest/read payload sizes. |
| `permission_read_limits` | Complete origin-grant observation bound. |
| `admission_read_limits` | Complete candidate-grant observation bound. |
| `operation_read_limits` | Complete goal-operation observation bound. |

All settings must be supplied. Read limits are completeness bounds, not partial-result preferences.

## Policy and paths

The supplied `AuthorityPolicy` must match the settings namespace, with `store="integrated"` and `identity_store="local"`. The clock must return timezone-aware timestamps. `legacy_policies` supplies explicit historical-policy interpretations; the default empty tuple supplies none.

Directories must be owned by the application user, mode `0700`, absolute, canonical, and free of symbolic-link aliases. Existing SQLite database/sidecar files must be owned regular files with mode `0600` and one hard link. Native construction validates ancestor safety as well as leaf paths.

## Side effects and resources

Opening may persist schema/storage setup and the supplied policy. Partial failure can leave committed setup. It issues no credentials/grants and starts no goals, handler, or background work.

Runtime owns its native clients. A supplied `FileCredentialSource` is borrowed and must belong to the same namespace with valid private storage. Without it, `provider_credentials` is `None`.

`close()` and context-manager exit release owned resources after calls quiesce. They do not undo durable state. Calls after close or across a host fork fail. Concurrent close/new work and aggregate asynchronous draining are unsupported.

## Errors and examples

Invalid settings, mismatched profiles, clocks, or paths raise validation errors/`ValueError`; authorization and storage failures retain their own categories. Do not assume a construction exception rolled back setup.

The [complete native tutorial](../../tutorials/native-runtime/) demonstrates valid paths, limits, policy, bootstrap, awaited operations, close, and reopen. Follow [Runtime lifecycle](../../guides/runtime-lifecycle/) for an application integration.
