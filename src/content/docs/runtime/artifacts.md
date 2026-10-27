---
title: Artifacts and storage
description: Content identity, publication, retention, executor provenance, and bounded access.
---

## Content identity

Artifacts hold input, output, checkpoint, and return bytes. `ArtifactReference` records identity, namespace, digest, size, state, expiry, and optional publisher provenance. `ContentReference` pins an accepted ID and digest for later use. Knowing a reference does not grant access.

For example, a report input can be published once, referenced by a task, and recovered after reopening the native database without changing the accepted content.

## Publication and retention

The lifecycle states are `publishing`, `published`, `deleting`, `expired`, and `deleted`. Publishing makes a verified durable reference available within the SDK; it does not make content public on the Internet.

`put_bytes()` ingests bytes with a request ID and application-supplied expiry. New requests require an expiry. Omitting expiry is only valid for replay of an existing request. Replay cannot extend retention or resurrect expired/deleted bytes.

`recover_publication()` retrieves a saved publication by request ID without requiring the caller to retain the original payload. `publish()` verifies bounded source bytes before committing a successful publication reference.

## Access and executor provenance

Management and exact executor contexts have different access rules. Ordinary nonmanagement artifact operations require executor authority; a workload credential alone is insufficient. Deletion is management-only. An execution reads declared sources, not arbitrary ancestor artifacts. Executor publications bind execution, attempt, generation, controller, and purpose (`output` or `return`).

`ArtifactLimits` bounds per-operation ingest/read bytes. `ExecutionOutputLimits` separately bounds the accepted number of outputs, ordinary output bytes, and canonical handler-return bytes. Increasing a host read limit does not expand an accepted execution's output budget.

## Integrity and availability

Integrity errors mean stored bytes or file identity do not match publication. Availability errors cover pending, expired, deleted, or otherwise unavailable content. Do not bypass either by reading native storage files directly.

Native storage uses SQLite state and private local artifact files. Advanced `ArtifactService` construction borrows supplied state, byte, and identity adapters; it does not close those components or promise aggregate asynchronous draining.

Follow [Store and recover an artifact](../../tutorials/native-runtime/) and [Manage artifacts](../../guides/artifacts/). See the [Artifact API](../../reference/artifacts/) for all six operations.
