---
title: Environment and execution contracts
description: Source-derived fields and signatures for the unreleased SDK preview.
---

> **Unreleased source preview.** Generated declarations describe types, not a promise that every contract has an executable implementation. Read the [behavioral API reference](../../overview/) and [capability matrix](../../../runtime/capabilities/) first.

Field defaults shown as `Field(...)` include validation metadata. A `Field(...)` without `default=` or `default_factory=` is required. Inherited fields from classes in the same source module are included. Cross-field invariants are explained in the concept and behavioral reference pages.

:::caution[Extension contracts]
These declarations include future facades and experimental scheduling interfaces. They are not additional attributes on `Runtime` and do not qualify physical execution, isolation, or termination.
:::

## `agentfabric_runtime.environments.schemas`

### `PositiveInteger`

```python
PositiveInteger = Annotated[int, Field(strict=True, gt=0)]
```

### `EnvironmentProfile`

Import: `agentfabric_runtime.environments.schemas.EnvironmentProfile`

Application-selected identity and explicit per-execution resource limits.

Declaring a host does not qualify a backend for that host. The selected
deployment must independently verify the gateway-only security boundary.

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `host` | `Identifier` | `Required` |
| `network` | `Literal['gateway-only']` | `'gateway-only'` |
| `cpu_count` | `PositiveInteger` | `Required` |
| `memory_mib` | `PositiveInteger` | `Required` |
| `workspace_mib` | `PositiveInteger` | `Required` |
| `process_limit` | `PositiveInteger` | `Required` |
| `lifetime_seconds` | `PositiveInteger` | `Required` |
| `lease_seconds` | `PositiveInteger` | `Required` |
| `stop_grace_seconds` | `PositiveInteger` | `Required` |
| `revocation_seconds` | `PositiveInteger` | `Required` |

### `LaunchRecipe`

Import: `agentfabric_runtime.environments.schemas.LaunchRecipe`

Complete application recipe; the configured backend validates its payload.

Its canonical bytes, including every backend setting, identify the accepted
handler configuration. Runtime does not prescribe a container implementation.

| Field | Type | Default / validation |
| --- | --- | --- |
| `format` | `Literal['launch-recipe-v1']` | `Required` |
| `handler_id` | `Identifier` | `Required` |
| `handler_version` | `ContentDigest` | `Required` |
| `deployment` | `ContentDigest` | `Required` |
| `environment` | `Identifier` | `Required` |
| `implementation` | `Identifier` | `Required` |
| `profile` | `EnvironmentProfile` | `Required` |
| `input_protocol` | `Identifier` | `Required` |
| `control_protocol` | `Identifier` | `Required` |
| `output_protocol` | `Identifier` | `Required` |
| `configuration` | `dict[str, JsonValue]` | `Required` |

### `EffectiveLaunchConfiguration`

Import: `agentfabric_runtime.environments.schemas.EffectiveLaunchConfiguration`

Immutable allocation content, separate from renewable control authority.

| Field | Type | Default / validation |
| --- | --- | --- |
| `format` | `Literal['effective-launch-v1']` | `Required` |
| `recipe_digest` | `ContentDigest` | `Required` |
| `namespace` | `Namespace` | `Required` |
| `execution_id` | `Identifier` | `Required` |
| `agent_id` | `Identifier` | `Required` |
| `deployment` | `ContentDigest` | `Required` |
| `environment` | `Identifier` | `Required` |
| `input_json` | `str` | `Field(min_length=1)` |
| `sources` | `tuple[ContentReference, ...]` | `Required` |
| `context` | `AccessContext` | `Required` |
| `output_limits` | `ExecutionOutputLimits` | `Required` |
| `attempt_id` | `Identifier` | `Required` |
| `allocation_id` | `Identifier` | `Required` |
| `generation` | `Version` | `Required` |
| `authorization_deadline` | `UtcDatetime` | `Required` |
| `scheduling_deadline` | `UtcDatetime` | `Required` |
| `hard_expires_at` | `UtcDatetime` | `Required` |

### `EnvironmentReadiness`

Import: `agentfabric_runtime.environments.schemas.EnvironmentReadiness`

Trusted backend observations, checked before workload dispatch in Stage 3/4.

| Field | Type | Default / validation |
| --- | --- | --- |
| `profile` | `Identifier` | `Required` |
| `allocation_id` | `Identifier` | `Required` |
| `generation` | `int` | `Field(ge=1)` |
| `controller_version` | `int` | `Field(ge=1)` |
| `valid_until` | `AwareDatetime` | `Required` |
| `isolation_verified` | `bool` | `Required` |
| `resource_limits_verified` | `bool` | `Required` |
| `storage_verified` | `bool` | `Required` |
| `supervision_verified` | `bool` | `Required` |
| `external_routes_verified` | `bool` | `Required` |

#### `EnvironmentReadiness.ready`

```python
def ready(self, *, profile_id: Identifier, allocation_id: Identifier, generation: PositiveInteger, controller_version: PositiveInteger, now: AwareDatetime, max_validity_seconds: PositiveInteger) -> bool:
    ...
```

Match a trusted observation to its expected resource and validity window.

The caller supplies the maximum remaining validity horizon. This does
not establish when the backend originally measured the resource.

## `agentfabric_runtime.environments.client`

### `WorkspaceClient`

Import: `agentfabric_runtime.environments.client.WorkspaceClient`

Owner-checked workspace operations, not per-command external grant prompts.

The backend enforces allocation generation and lifetime. Network requests
originating inside any operation still go through external grant enforcement.

#### `WorkspaceClient.readiness`

```python
async def readiness(self, allocation_id: str, generation: Version, *, credential: SecretStr) -> EnvironmentReadiness:
    ...
```

#### `WorkspaceClient.invoke`

```python
async def invoke(self, allocation_id: str, generation: Version, handler: HandlerReference, input_ref: ContentReference, *, credential: SecretStr) -> ContentReference:
    ...
```

Return a recorded result envelope, not a goal decision or proof of cleanup.

#### `WorkspaceClient.command`

```python
async def command(self, allocation_id: str, generation: Version, argv: tuple[str, ...], deadline: UtcDatetime, *, credential: SecretStr) -> ContentReference:
    ...
```

Bounded process/output record; a lost reply never proves the process absent.

#### `WorkspaceClient.computer`

```python
async def computer(self, allocation_id: str, generation: Version, action: ContentReference, *, credential: SecretStr) -> ContentReference:
    ...
```

#### `WorkspaceClient.stop`

```python
async def stop(self, allocation_id: str, generation: Version, *, credential: SecretStr) -> None:
    ...
```

Request stop; inspect termination separately through the trusted backend.

## `agentfabric_runtime.execution.contracts`

### `ExecutionSpec`

Import: `agentfabric_runtime.execution.contracts.ExecutionSpec`

Immutable invocation; authority is verified separately on every admission.

| Field | Type | Default / validation |
| --- | --- | --- |
| `request_id` | `Identifier` | `Required` |
| `worker_id` | `Identifier` | `Required` |
| `handler` | `HandlerReference` | `Required` |
| `role` | `ExecutionRole` | `Required` |
| `goal_id` | `Identifier \| None` | `None` |
| `task_id` | `Identifier \| None` | `None` |
| `input_ref` | `ContentReference` | `Required` |
| `output_limits` | `ExecutionOutputLimits` | `Required` |
| `scheduling_deadline` | `AwareDatetime` | `Required` |

### `ExecutionOutcome`

Import: `agentfabric_runtime.execution.contracts.ExecutionOutcome`

| Field | Type | Default / validation |
| --- | --- | --- |
| `execution_id` | `Identifier` | `Required` |
| `status` | `Literal['succeeded', 'failed', 'denied', 'expired', 'cancelled', 'interrupted', 'yielded']` | `Required` |
| `result_ref` | `ContentReference \| None` | `None` |
| `checkpoint_ref` | `ContentReference \| None` | `None` |
| `error_code` | `ErrorCode \| None` | `None` |

### `ExecutionSnapshot`

Import: `agentfabric_runtime.execution.contracts.ExecutionSnapshot`

| Field | Type | Default / validation |
| --- | --- | --- |
| `execution_id` | `Identifier` | `Required` |
| `status` | `ExecutionStatus` | `Required` |
| `role` | `ExecutionRole` | `Required` |
| `cancel_requested` | `bool` | `Required` |
| `termination` | `Literal['unverified', 'verified']` | `Required` |

### `ExecutionClient`

Import: `agentfabric_runtime.execution.contracts.ExecutionClient`

Future facade contract only; implementation and current access checks are Stage 2.

#### `ExecutionClient.start`

```python
async def start(self, spec: ExecutionSpec, *, credential: SecretStr) -> ExecutionSnapshot:
    ...
```

#### `ExecutionClient.status`

```python
async def status(self, execution_id: str, *, credential: SecretStr) -> ExecutionSnapshot:
    ...
```

#### `ExecutionClient.result`

```python
async def result(self, execution_id: str, *, credential: SecretStr, timeout: Timeout) -> ExecutionOutcome:
    ...
```

#### `ExecutionClient.cancel`

```python
async def cancel(self, execution_id: str, *, credential: SecretStr) -> ExecutionSnapshot:
    ...
```

#### `ExecutionClient.events`

```python
async def events(self, execution_id: str, *, credential: SecretStr, after: EventCursor, limit: PageLimit) -> tuple[ExecutionEvent, ...]:
    ...
```
