---
title: Artifact models and client
description: Source-derived fields and signatures for the unreleased SDK preview.
---

> **Unreleased source preview.** Generated declarations describe types, not a promise that every contract has an executable implementation. Read the [behavioral API reference](../../overview/) and [capability matrix](../../../runtime/capabilities/) first.

Field defaults shown as `Field(...)` include validation metadata. A `Field(...)` without `default=` or `default_factory=` is required. Inherited fields from classes in the same source module are included. Cross-field invariants are explained in the concept and behavioral reference pages.

## `agentfabric_runtime.artifacts.schemas`

### `ArtifactBytes`

```python
ArtifactBytes = Annotated[bytes, Field(strict=True)]
```

### `ArtifactLimits`

Import: `agentfabric_runtime.artifacts.schemas.ArtifactLimits`

Application-selected maximum byte payloads per client operation.

| Field | Type | Default / validation |
| --- | --- | --- |
| `max_ingest_bytes` | `int` | `Field(ge=1, le=(1 << 63) - 1)` |
| `max_read_bytes` | `int` | `Field(ge=1, le=(1 << 63) - 1)` |

### `ArtifactPublisher`

Import: `agentfabric_runtime.artifacts.schemas.ArtifactPublisher`

| Field | Type | Default / validation |
| --- | --- | --- |
| `execution_id` | `Identifier` | `Required` |
| `attempt_id` | `Identifier` | `Required` |
| `generation` | `Version` | `Required` |
| `controller_version` | `Version` | `Required` |
| `purpose` | `Literal['output', 'return']` | `Required` |

### `ArtifactReference`

Import: `agentfabric_runtime.artifacts.schemas.ArtifactReference`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `namespace` | `Namespace` | `Required` |
| `digest` | `ContentDigest` | `Required` |
| `size_bytes` | `int` | `Field(ge=0, le=(1 << 63) - 1)` |
| `state` | `Literal['publishing', 'published', 'deleting', 'expired', 'deleted']` | `Required` |
| `expires_at` | `UtcDatetime` | `Required` |
| `publisher` | `ArtifactPublisher \| None` | `None` |

## `agentfabric_runtime.artifacts.interfaces`

### `ArtifactClient`

Import: `agentfabric_runtime.artifacts.interfaces.ArtifactClient`

#### `ArtifactClient.put_bytes`

```python
async def put_bytes(self, data: ArtifactBytes, *, request_id: str, expires_at: UtcDatetime | None=None, credential: SecretStr) -> ArtifactReference:
    ...
```

Ingest bytes with an application-supplied expiry for every new request.

Omitting expires_at only replays an already saved request using its
original expiry. Replays cannot extend retention or resurrect content.

#### `ArtifactClient.read`

```python
async def read(self, source: ContentReference, *, credential: SecretStr) -> bytes:
    ...
```

#### `ArtifactClient.recover_publication`

```python
async def recover_publication(self, request_id: str, *, credential: SecretStr) -> ArtifactReference:
    ...
```

Resolve a saved request without requiring its caller to retain original bytes.

#### `ArtifactClient.publish`

```python
async def publish(self, source: ContentReference, *, request_id: str, credential: SecretStr) -> ArtifactReference:
    ...
```

Publish only verified bounded bytes before committing successful references.

#### `ArtifactClient.inspect`

```python
async def inspect(self, artifact_id: str, *, credential: SecretStr) -> ArtifactReference:
    ...
```

#### `ArtifactClient.delete`

```python
async def delete(self, artifact_id: str, *, credential: SecretStr) -> ArtifactReference:
    ...
```

## `agentfabric_runtime.services.artifact_service`

### `ArtifactService`

Import: `agentfabric_runtime.services.artifact_service.ArtifactService`

Borrow all components; await cancellation does not stop an accepted job.

The application waits for actual jobs before closing its components. This
facade does not close them or promise aggregate asynchronous draining.

#### `ArtifactService.__init__`

```python
def __init__(self, store: RuntimeStore, namespace: Namespace, verifier: IdentityVerifier, artifact_bytes: ArtifactByteStore, *, limits: ArtifactLimits, object_timeout: float, clock: Callable[[], datetime]=utc_now, retry: TransactionRetrySettings | None=None):
    ...
```

#### `ArtifactService.put_bytes`

```python
async def put_bytes(self, data: ArtifactBytes, *, request_id: str, expires_at: UtcDatetime | None=None, credential: SecretStr) -> ArtifactReference:
    ...
```

#### `ArtifactService.recover_publication`

```python
async def recover_publication(self, request_id: str, *, credential: SecretStr) -> ArtifactReference:
    ...
```

#### `ArtifactService.publish`

```python
async def publish(self, source: ContentReference, *, request_id: str, credential: SecretStr) -> ArtifactReference:
    ...
```

#### `ArtifactService.inspect`

```python
async def inspect(self, artifact_id: str, *, credential: SecretStr) -> ArtifactReference:
    ...
```

#### `ArtifactService.read`

```python
async def read(self, source: ContentReference, *, credential: SecretStr) -> bytes:
    ...
```

#### `ArtifactService.delete`

```python
async def delete(self, artifact_id: str, *, credential: SecretStr) -> ArtifactReference:
    ...
```

## `agentfabric_runtime.services.transactions`

### `TransactionRetrySettings`

Import: `agentfabric_runtime.services.transactions.TransactionRetrySettings`

Explicit bounds on starting retries; never interrupt an accepted transaction.

| Field | Type | Default / validation |
| --- | --- | --- |
| `max_attempts` | `int` | `Field(ge=1, le=(1 << 63) - 1)` |
| `max_elapsed_seconds` | `float` | `Required` |
