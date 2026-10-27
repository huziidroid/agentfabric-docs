---
title: Artifact API
description: All six artifact operations, access, lifecycle, retention, replay, and errors.
---

Use `runtime.artifacts`. The structural interface is `agentfabric_runtime.artifacts.interfaces.ArtifactClient`; models and limits are in `agentfabric_runtime.artifacts.schemas`.

All operations are asynchronous and require `credential=SecretStr`. [Exact signatures and fields](../generated/artifacts/) include required and optional parameters.

## Operations

| Method | Parameters and result | State and replay |
| --- | --- | --- |
| `put_bytes(data, *, request_id, expires_at=None, credential)` | Strict bytes; returns `ArtifactReference`. | New request requires explicit expiry. Same request/payload replays saved publication; omitted expiry only recovers an existing request's retention. |
| `read(source, *, credential)` | Exact `ContentReference`; returns verified `bytes`. | Requires current source access and bounded readable content. No retention extension. |
| `recover_publication(request_id, *, credential)` | Returns saved `ArtifactReference` without original bytes. | Recovers uncertain publication, not a new ingest or resurrection. |
| `publish(source, *, request_id, credential)` | Exact source reference; returns `ArtifactReference`. | Verify bounded source bytes before committing publication. Does not publish to the Internet. |
| `inspect(artifact_id, *, credential)` | Returns authorized `ArtifactReference` metadata. | Metadata state does not imply bytes are still readable. |
| `delete(artifact_id, *, credential)` | Returns resulting `ArtifactReference`. | Management-only: records/coordinates deletion under current authority; deleted content is not resurrected by replay. |

## Access and limits

Management and exact executor credentials have scoped access. Ordinary nonmanagement calls require the executor role, not a workload token. Deletion requires namespace management. Executor publications require the applicable original execution/attempt/generation/controller and output/return purpose. Merely holding an artifact ID or an ancestor execution ID is insufficient.

`ArtifactLimits.max_ingest_bytes` and `max_read_bytes` are application-supplied positive bounded integers. Accepted `ExecutionOutputLimits` additionally constrain output count/bytes and canonical return bytes. States are publishing, published, deleting, expired, and deleted.

## Errors and lifetime

Expect strict validation/`ValueError`, `AuthorizationError`, `RequestConflictError`, `RecordNotFoundError`, `ArtifactIntegrityError`, `ArtifactUnavailableError`, or `StorageError` as applicable. Integrity failure is different from unavailable content; do not bypass verification by opening backing files.

Exact replay cannot extend expiry or grant new authority. An uncertain publication should be resolved with the original request ID. Cancellation does not prove accepted file/SQL work stopped; finish underlying operations before Runtime closes.

For advanced composition, `ArtifactService` in `agentfabric_runtime.services.artifact_service` borrows state, namespace, verifier, byte adapter, explicit limits, timeout, clock, and retry configuration. Ownership and adapter obligations are explained in [Extension contracts](../../runtime/extensions/).

See [Manage artifacts](../../guides/artifacts/) and the [runnable tutorial](../../tutorials/native-runtime/).

## Advanced transaction retry

`ArtifactService(..., retry=None)` accepts optional `TransactionRetrySettings(max_attempts, max_elapsed_seconds)` from `agentfabric_runtime.services.transactions`. Both fields are explicit: attempts are a positive bounded integer and elapsed seconds a positive finite wait timeout. Bounds control starting retries after confirmed transaction conflicts and do not interrupt accepted work. Unknown commits require recovery by original receipt identity. This does not implement goal Retry or external-effect retransmission. The [generated artifact reference](../generated/artifacts/) includes exact constructor and setting fields.
