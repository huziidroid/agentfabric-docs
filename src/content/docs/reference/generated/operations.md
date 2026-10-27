---
title: Operation contracts
description: Source-derived fields and signatures for the unreleased SDK preview.
---

> **Unreleased source preview.** Generated declarations describe types, not a promise that every contract has an executable implementation. Read the [behavioral API reference](../../overview/) and [capability matrix](../../../runtime/capabilities/) first.

Field defaults shown as `Field(...)` include validation metadata. A `Field(...)` without `default=` or `default_factory=` is required. Inherited fields from classes in the same source module are included. Cross-field invariants are explained in the concept and behavioral reference pages.

:::caution[Extension contracts]
These declarations include future facades and experimental scheduling interfaces. They are not additional attributes on `Runtime` and do not qualify physical execution, isolation, or termination.
:::

## `agentfabric_runtime.operations.schemas`

### `OperationOutcome`

Import: `agentfabric_runtime.operations.schemas.OperationOutcome`

| Field | Type | Default / validation |
| --- | --- | --- |
| `operation_id` | `Identifier` | `Required` |
| `status` | `Literal['succeeded', 'pending', 'failed', 'unknown']` | `Required` |
| `result_ref` | `ContentReference \| None` | `None` |
| `error_code` | `ErrorCode \| None` | `None` |

### `OperationRequest`

Import: `agentfabric_runtime.operations.schemas.OperationRequest`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `connection_id` | `Identifier` | `Required` |
| `resource_id` | `Identifier` | `Required` |
| `action` | `Identifier` | `Required` |
| `input_ref` | `ContentReference` | `Required` |

### `OperationIntent`

Import: `agentfabric_runtime.operations.schemas.OperationIntent`

Trusted immutable resolved binding; refreshed grants never rewrite this intent.

| Field | Type | Default / validation |
| --- | --- | --- |
| `request` | `OperationRequest` | `Required` |
| `configuration` | `ContentDigest` | `Required` |
| `authority_evidence` | `ContentReference` | `Required` |
| `resource_generation` | `Version` | `Required` |

### `OperationReadLimits`

Import: `agentfabric_runtime.operations.schemas.OperationReadLimits`

Application-selected complete origin-query bound, not a workflow limit.

| Field | Type | Default / validation |
| --- | --- | --- |
| `max_goal_operations` | `int` | `Field(ge=1, le=(1 << 63) - 2)` |

## `agentfabric_runtime.operations.interfaces`

### `OperationClient`

Import: `agentfabric_runtime.operations.interfaces.OperationClient`

#### `OperationClient.execute`

```python
async def execute(self, request: OperationRequest, *, credential: SecretStr) -> OperationOutcome:
    ...
```

#### `OperationClient.inspect`

```python
async def inspect(self, operation_id: str, *, credential: SecretStr) -> OperationOutcome:
    ...
```

#### `OperationClient.reconcile`

```python
async def reconcile(self, operation_id: str, *, credential: SecretStr) -> OperationOutcome:
    ...
```

Observe original intent under explicit authority; never blindly resend.
