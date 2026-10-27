---
title: Common values
description: Source-derived fields and signatures for the unreleased SDK preview.
---

> **Unreleased source preview.** Generated declarations describe types, not a promise that every contract has an executable implementation. Read the [behavioral API reference](../../overview/) and [capability matrix](../../../runtime/capabilities/) first.

Field defaults shown as `Field(...)` include validation metadata. A `Field(...)` without `default=` or `default_factory=` is required. Inherited fields from classes in the same source module are included. Cross-field invariants are explained in the concept and behavioral reference pages.

## `agentfabric_runtime.core.schemas`

### `MAX_IDENTIFIER_BYTES`

```python
MAX_IDENTIFIER_BYTES = 1024
```

### `Identifier`

```python
Identifier = Annotated[str, Field(strict=True, min_length=1), AfterValidator(_identifier_bytes)]
```

### `AccessBinding`

```python
AccessBinding = Annotated[str, Field(strict=True, min_length=1), AfterValidator(_binding_bytes)]
```

### `EventCursor`

```python
EventCursor = Annotated[int, Field(strict=True, ge=0, le=(1 << 63) - 1)]
```

### `PageLimit`

```python
PageLimit = Annotated[int, Field(strict=True, ge=1, le=1000)]
```

### `Timeout`

```python
Timeout = Annotated[float, Field(strict=True, gt=0, allow_inf_nan=False)]
```

### `ContentDigest`

```python
ContentDigest = Annotated[str, Field(strict=True, pattern='^sha256:[0-9a-f]{64}$')]
```

### `ErrorCode`

```python
ErrorCode = Annotated[str, Field(strict=True, pattern='^[a-z][a-z0-9_.]{0,63}$')]
```

### `Version`

```python
Version = Annotated[int, Field(strict=True, ge=1, le=(1 << 63) - 1)]
```

### `ExecutionRole`

```python
ExecutionRole = Literal['task', 'assessment', 'check']
```

### `UtcDatetime`

```python
UtcDatetime = Annotated[AwareDatetime, AfterValidator(_utc)]
```

### `RuntimeSchema`

Import: `agentfabric_runtime.core.schemas.RuntimeSchema`

Validated values with immutable fields and unknown-field rejection.

Nested inputs are revalidated at repository entry, including models created
with Pydantic's intentionally unchecked model_copy/model_construct APIs.

### `TechnicalOutcomeReference`

Import: `agentfabric_runtime.core.schemas.TechnicalOutcomeReference`

Immutable SQL-owned outcome identity, never an artifact or byte capability.

| Field | Type | Default / validation |
| --- | --- | --- |
| `execution_id` | `Identifier` | `Required` |
| `format` | `Literal['execution-outcome-v1', 'execution-outcome-v2']` | `Required` |
| `digest` | `ContentDigest` | `Required` |

### `ExecutionOutputLimits`

Import: `agentfabric_runtime.core.schemas.ExecutionOutputLimits`

Accepted ordinary output budgets and a separate canonical return budget.

| Field | Type | Default / validation |
| --- | --- | --- |
| `max_outputs` | `int` | `Field(ge=0, le=(1 << 63) - 1)` |
| `max_output_bytes` | `int` | `Field(ge=0, le=(1 << 63) - 1)` |
| `max_return_bytes` | `int` | `Field(ge=1, le=(1 << 63) - 1)` |

### `Namespace`

Import: `agentfabric_runtime.core.schemas.Namespace`

Application and owning account; neither identifier is authentication.

| Field | Type | Default / validation |
| --- | --- | --- |
| `application_id` | `Identifier` | `Required` |
| `owner_id` | `Identifier` | `Required` |

### `Identity`

Import: `agentfabric_runtime.core.schemas.Identity`

Verifier output shared as a value, never a substitute for verification.

| Field | Type | Default / validation |
| --- | --- | --- |
| `namespace` | `Namespace` | `Required` |
| `actor_id` | `Identifier` | `Required` |

### `ContentReference`

Import: `agentfabric_runtime.core.schemas.ContentReference`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `digest` | `ContentDigest` | `Required` |

### `HandlerReference`

Import: `agentfabric_runtime.core.schemas.HandlerReference`

Trusted registered executable binding, without imports or live callables.

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `version` | `ContentDigest` | `Required` |
| `deployment` | `ContentDigest` | `Required` |
| `configuration` | `ContentDigest` | `Required` |
| `environment` | `Identifier` | `Required` |

## `agentfabric_runtime.core.identity`

### `AccessContext`

Import: `agentfabric_runtime.core.identity.AccessContext`

| Field | Type | Default / validation |
| --- | --- | --- |
| `identity` | `Identity` | `Required` |
| `agent_id` | `Identifier` | `Required` |
| `role` | `ExecutionRole` | `Required` |
| `goal_id` | `Identifier \| None` | `None` |
| `task_id` | `Identifier \| None` | `None` |
| `execution_id` | `Identifier \| None` | `None` |

### `VerifiedPrincipal`

Import: `agentfabric_runtime.core.identity.VerifiedPrincipal`

Fresh verifier output; application-supplied claims, never request-body authority.

| Field | Type | Default / validation |
| --- | --- | --- |
| `identity` | `Identity` | `Required` |
| `role` | `Literal['management', 'workload', 'executor']` | `Required` |
| `expires_at` | `UtcDatetime` | `Required` |
| `credential_id` | `Identifier \| None` | `None` |
| `context` | `AccessContext \| None` | `None` |
| `resource_generation` | `Version \| None` | `None` |
| `controller_version` | `Version \| None` | `None` |

### `IdentityVerifier`

Import: `agentfabric_runtime.core.identity.IdentityVerifier`

#### `IdentityVerifier.verify`

```python
def verify(self, credential: SecretStr) -> VerifiedPrincipal:
    ...
```

Verify current identity and exact role/context through application authority.

### `CredentialRecord`

Import: `agentfabric_runtime.core.identity.CredentialRecord`

| Field | Type | Default / validation |
| --- | --- | --- |
| `principal` | `VerifiedPrincipal` | `Required` |
| `state` | `Literal['pending', 'issued', 'revoked']` | `Required` |
| `issued_at` | `UtcDatetime` | `Required` |
| `rotation_from` | `Identifier \| None` | `None` |

### `CredentialIssue`

Import: `agentfabric_runtime.core.identity.CredentialIssue`

| Field | Type | Default / validation |
| --- | --- | --- |
| `record` | `CredentialRecord` | `Required` |
| `secret` | `SecretStr \| None` | `None` |

### `BootstrapCredential`

Import: `agentfabric_runtime.core.identity.BootstrapCredential`

Private publication envelope; never authority independently of its digest.

| Field | Type | Default / validation |
| --- | --- | --- |
| `credential_id` | `Identifier` | `Required` |
| `secret` | `SecretStr` | `Required` |

### `BootstrapPublication`

Import: `agentfabric_runtime.core.identity.BootstrapPublication`

#### `BootstrapPublication.read_current`

```python
def read_current(self) -> BootstrapCredential | None:
    ...
```

#### `BootstrapPublication.write_pending`

```python
def write_pending(self, credential_id: str, secret: SecretStr) -> None:
    ...
```

#### `BootstrapPublication.read_pending`

```python
def read_pending(self, credential_id: str) -> BootstrapCredential:
    ...
```

#### `BootstrapPublication.publish_pending`

```python
def publish_pending(self, credential_id: str) -> None:
    ...
```

### `BootstrapCredentialSource`

Import: `agentfabric_runtime.core.identity.BootstrapCredentialSource`

#### `BootstrapCredentialSource.object`

```python
def object(self, namespace: Namespace, name: str) -> AbstractContextManager[BootstrapPublication]:
    ...
```

Exclusive bounded publication; absence differs from corrupt/unreadable bytes.
