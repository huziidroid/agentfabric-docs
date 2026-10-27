---
title: Scheduling development contracts
description: Source-derived fields and signatures for the unreleased SDK preview.
---

> **Unreleased source preview.** Generated declarations describe types, not a promise that every contract has an executable implementation. Read the [behavioral API reference](../../overview/) and [capability matrix](../../../runtime/capabilities/) first.

Field defaults shown as `Field(...)` include validation metadata. A `Field(...)` without `default=` or `default_factory=` is required. Inherited fields from classes in the same source module are included. Cross-field invariants are explained in the concept and behavioral reference pages.

:::caution[Extension contracts]
These declarations include future facades and experimental scheduling interfaces. They are not additional attributes on `Runtime` and do not qualify physical execution, isolation, or termination.
:::

## `agentfabric_runtime.execution.schemas`

### `ExecutionStatus`

```python
ExecutionStatus = Literal['accepted', 'starting', 'running', 'succeeded', 'failed', 'denied', 'expired', 'cancelled', 'interrupted', 'yielded']
```

### `TERMINAL_EXECUTION_STATUSES`

```python
TERMINAL_EXECUTION_STATUSES = frozenset({'succeeded', 'failed', 'denied', 'expired', 'cancelled', 'interrupted', 'yielded'})
```

### `AcceptanceRequest`

Import: `agentfabric_runtime.execution.schemas.AcceptanceRequest`

An already-authorized, resolved submission from the trusted runtime.

Identities name resolved deployment/profile/configuration, not mutable
aliases. Inputs must contain no credentials. Live ownership/source checks
remain the caller's responsibility on every acceptance, replay and read.
Schema validation does not authenticate the caller.

| Field | Type | Default / validation |
| --- | --- | --- |
| `request_id` | `Identifier` | `Required` |
| `agent` | `Identifier` | `Required` |
| `input` | `dict[str, JsonValue]` | `Required` |
| `deployment_id` | `Identifier` | `Required` |
| `environment_id` | `Identifier` | `Required` |
| `configuration_id` | `Identifier` | `Required` |
| `scheduling_deadline` | `AwareDatetime` | `Required` |
| `session_id` | `Identifier \| None` | `None` |

### `SessionRecord`

Import: `agentfabric_runtime.execution.schemas.SessionRecord`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `created_at` | `AwareDatetime` | `Required` |

### `ExecutionRecord`

Import: `agentfabric_runtime.execution.schemas.ExecutionRecord`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `session_id` | `Identifier` | `Required` |
| `request_id` | `Identifier` | `Required` |
| `agent` | `Identifier` | `Required` |
| `input_json` | `str` | `Required` |
| `deployment_id` | `Identifier` | `Required` |
| `environment_id` | `Identifier` | `Required` |
| `configuration_id` | `Identifier` | `Required` |
| `scheduling_deadline` | `AwareDatetime` | `Required` |
| `accepted_at` | `AwareDatetime` | `Required` |
| `status` | `ExecutionStatus` | `'accepted'` |
| `cancel_requested` | `bool` | `False` |

### `LaunchObligation`

Import: `agentfabric_runtime.execution.schemas.LaunchObligation`

| Field | Type | Default / validation |
| --- | --- | --- |
| `execution_id` | `Identifier` | `Required` |
| `scheduling_deadline` | `AwareDatetime` | `Required` |
| `status` | `Literal['pending', 'claimed', 'finished']` | `'pending'` |

### `ExecutionEvent`

Import: `agentfabric_runtime.execution.schemas.ExecutionEvent`

| Field | Type | Default / validation |
| --- | --- | --- |
| `execution_id` | `Identifier` | `Required` |
| `sequence` | `Annotated[int, Field(ge=1, le=(1 << 63) - 1)]` | `Required` |
| `occurred_at` | `AwareDatetime` | `Required` |
| `type` | `str` | `'execution.accepted'` |

## `agentfabric_runtime.execution.scheduling_schemas`

### `SchedulingSettings`

Import: `agentfabric_runtime.execution.scheduling_schemas.SchedulingSettings`

Caller-owned windows and capacity; no SDK operating preset is selected.

| Field | Type | Default / validation |
| --- | --- | --- |
| `claim_seconds` | `Timeout` | `Required` |
| `provisioning_seconds` | `Timeout` | `Required` |
| `dispatch_seconds` | `Timeout` | `Required` |
| `capacity` | `int` | `Field(ge=1, le=(1 << 63) - 1)` |

### `Claim`

Import: `agentfabric_runtime.execution.scheduling_schemas.Claim`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `execution_id` | `Identifier` | `Required` |
| `worker_id` | `Identifier` | `Required` |
| `request_id` | `Identifier` | `Required` |
| `controller_version` | `int` | `Field(ge=1)` |
| `expires_at` | `AwareDatetime` | `Required` |

### `LaunchAttempt`

Import: `agentfabric_runtime.execution.scheduling_schemas.LaunchAttempt`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `execution_id` | `Identifier` | `Required` |
| `allocation_id` | `Identifier` | `Required` |
| `generation` | `int` | `Field(ge=1)` |
| `controller_version` | `int` | `Field(ge=1)` |
| `deployment_id` | `Identifier` | `Required` |
| `environment_id` | `Identifier` | `Required` |
| `configuration_id` | `Identifier` | `Required` |
| `provisioning_deadline` | `AwareDatetime` | `Required` |
| `state` | `Literal['reserved', 'ready', 'admitted', 'running', 'unknown', 'terminated', 'absent']` | `Required` |
| `capacity_reserved` | `bool` | `Required` |

### `LaunchPermit`

Import: `agentfabric_runtime.execution.scheduling_schemas.LaunchPermit`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `attempt_id` | `Identifier` | `Required` |
| `allocation_id` | `Identifier` | `Required` |
| `generation` | `int` | `Field(ge=1)` |
| `controller_version` | `int` | `Field(ge=1)` |
| `dispatch_deadline` | `AwareDatetime` | `Required` |

### `Rejection`

Import: `agentfabric_runtime.execution.scheduling_schemas.Rejection`

| Field | Type | Default / validation |
| --- | --- | --- |
| `execution_id` | `Identifier` | `Required` |
| `reason` | `Literal['denied', 'expired', 'cancelled', 'capacity', 'not_ready']` | `Required` |

### `LaunchObservation`

Import: `agentfabric_runtime.execution.scheduling_schemas.LaunchObservation`

| Field | Type | Default / validation |
| --- | --- | --- |
| `attempt_id` | `Identifier` | `Required` |
| `allocation_id` | `Identifier` | `Required` |
| `generation` | `int` | `Field(ge=1)` |
| `controller_version` | `int` | `Field(ge=1)` |
| `sequence` | `int` | `Field(ge=1)` |
| `state` | `Literal['ready', 'running', 'unknown', 'terminated', 'absent']` | `Required` |
| `controls_verified` | `bool` | `False` |
| `supervision_acknowledged` | `bool` | `False` |

### `TaskAttemptFacts`

Import: `agentfabric_runtime.execution.scheduling_schemas.TaskAttemptFacts`

| Field | Type | Default / validation |
| --- | --- | --- |
| `attempt` | `LaunchAttempt` | `Required` |
| `authority_version` | `int \| None` | `Required` |
| `permit_id` | `str \| None` | `Required` |
| `dispatch_deadline` | `datetime \| None` | `Required` |
| `observation_sequence` | `int` | `Required` |
| `launch_configuration_json` | `str \| None` | `None` |
| `launch_configuration_digest` | `str \| None` | `None` |
| `hard_deadline` | `datetime \| None` | `None` |
| `lease_expires_at` | `datetime \| None` | `None` |
| `lease_renewal_json` | `str \| None` | `None` |
| `observation_json` | `str \| None` | `None` |
| `launch_permit_json` | `str \| None` | `None` |

### `TaskResourceFacts`

Import: `agentfabric_runtime.execution.scheduling_schemas.TaskResourceFacts`

| Field | Type | Default / validation |
| --- | --- | --- |
| `namespace` | `Namespace` | `Required` |
| `execution` | `ExecutionRecord` | `Required` |
| `outcome_json` | `str \| None` | `Required` |
| `obligation` | `LaunchObligation` | `Required` |
| `obligation_controller_version` | `int` | `Required` |
| `obligation_claim_id` | `str \| None` | `Required` |
| `claim` | `Claim \| None` | `Required` |
| `attempt` | `TaskAttemptFacts \| None` | `Required` |
| `last_execution_event_sequence` | `int` | `Required` |
| `rejection_event` | `ExecutionEvent \| None` | `Required` |
| `initial_claim_expires_at` | `datetime \| None` | `None` |
| `claim_renewal_json` | `str \| None` | `None` |
| `control_claim_event` | `ExecutionEvent \| None` | `None` |

### `TaskControlClaimWrite`

Import: `agentfabric_runtime.execution.scheduling_schemas.TaskControlClaimWrite`

| Field | Type | Default / validation |
| --- | --- | --- |
| `expected` | `TaskResourceFacts` | `Required` |
| `claim` | `Claim` | `Required` |
| `event` | `ExecutionEvent` | `Required` |
| `initial_expires_at` | `datetime \| None` | `None` |
| `attempt_state` | `Literal['unknown'] \| None` | `None` |

### `ResourceObservationWrite`

Import: `agentfabric_runtime.execution.scheduling_schemas.ResourceObservationWrite`

| Field | Type | Default / validation |
| --- | --- | --- |
| `expected` | `TaskResourceFacts` | `Required` |
| `observation` | `LaunchObservation` | `Required` |
| `capacity_reserved` | `bool` | `Required` |
| `execution_status` | `ExecutionStatus` | `Required` |
| `obligation_status` | `Literal['pending', 'claimed', 'finished']` | `Required` |
| `event` | `ExecutionEvent \| None` | `Required` |

### `LaunchRejectionWrite`

Import: `agentfabric_runtime.execution.scheduling_schemas.LaunchRejectionWrite`

| Field | Type | Default / validation |
| --- | --- | --- |
| `expected` | `TaskResourceFacts` | `Required` |
| `execution_status` | `ExecutionStatus` | `Required` |
| `obligation_status` | `Literal['pending', 'claimed', 'finished']` | `Required` |
| `event` | `ExecutionEvent \| None` | `Required` |

### `SchedulingPoolConfiguration`

Import: `agentfabric_runtime.execution.scheduling_schemas.SchedulingPoolConfiguration`

One immutable host capacity contract shared across all store namespaces.

| Field | Type | Default / validation |
| --- | --- | --- |
| `claim_seconds` | `Timeout` | `Required` |
| `provisioning_seconds` | `Timeout` | `Required` |
| `dispatch_seconds` | `Timeout` | `Required` |
| `capacity` | `int` | `Field(ge=1, le=(1 << 63) - 1)` |
| `format` | `Literal['scheduling-pool-v1']` | `Required` |
| `host_profile_id` | `Identifier` | `Required` |
| `max_observation_age_seconds` | `Timeout` | `Required` |
| `observation_validity_seconds` | `Timeout` | `Required` |

### `SchedulingReadLimits`

Import: `agentfabric_runtime.execution.scheduling_schemas.SchedulingReadLimits`

| Field | Type | Default / validation |
| --- | --- | --- |
| `max_scan_candidates` | `int` | `Field(ge=1, le=(1 << 63) - 2)` |
| `max_configuration_bytes` | `int` | `Field(ge=1, le=(1 << 63) - 2)` |

### `SchedulingCursor`

Import: `agentfabric_runtime.execution.scheduling_schemas.SchedulingCursor`

| Field | Type | Default / validation |
| --- | --- | --- |
| `namespace` | `Namespace` | `Required` |
| `accepted_at` | `UtcDatetime` | `Required` |
| `execution_id` | `Identifier` | `Required` |

### `SchedulingCandidate`

Import: `agentfabric_runtime.execution.scheduling_schemas.SchedulingCandidate`

| Field | Type | Default / validation |
| --- | --- | --- |
| `execution_id` | `Identifier` | `Required` |
| `accepted_at` | `UtcDatetime` | `Required` |

### `SchedulingPage`

Import: `agentfabric_runtime.execution.scheduling_schemas.SchedulingPage`

| Field | Type | Default / validation |
| --- | --- | --- |
| `items` | `tuple[SchedulingCandidate, ...]` | `Required` |
| `next_cursor` | `SchedulingCursor \| None` | `Required` |
| `exhausted` | `bool` | `Required` |

### `SchedulingClaimResult`

Import: `agentfabric_runtime.execution.scheduling_schemas.SchedulingClaimResult`

| Field | Type | Default / validation |
| --- | --- | --- |
| `claim` | `Claim \| None` | `Required` |
| `next_cursor` | `SchedulingCursor \| None` | `Required` |
| `exhausted` | `bool` | `Required` |

### `AllocationCursor`

Import: `agentfabric_runtime.execution.scheduling_schemas.AllocationCursor`

| Field | Type | Default / validation |
| --- | --- | --- |
| `namespace` | `Namespace` | `Required` |
| `attempt_id` | `Identifier` | `Required` |
| `execution_id` | `Identifier` | `Required` |

### `AllocationCandidate`

Import: `agentfabric_runtime.execution.scheduling_schemas.AllocationCandidate`

| Field | Type | Default / validation |
| --- | --- | --- |
| `attempt_id` | `Identifier` | `Required` |
| `execution_id` | `Identifier` | `Required` |

### `AllocationPage`

Import: `agentfabric_runtime.execution.scheduling_schemas.AllocationPage`

| Field | Type | Default / validation |
| --- | --- | --- |
| `items` | `tuple[AllocationCandidate, ...]` | `Required` |
| `next_cursor` | `AllocationCursor \| None` | `Required` |
| `exhausted` | `bool` | `Required` |

### `LaunchAttemptV2`

Import: `agentfabric_runtime.execution.scheduling_schemas.LaunchAttemptV2`

Current control view of one immutable, genuinely configured allocation.

| Field | Type | Default / validation |
| --- | --- | --- |
| `format` | `Literal['launch-attempt-v2']` | `Required` |
| `namespace` | `Namespace` | `Required` |
| `id` | `Identifier` | `Required` |
| `execution_id` | `Identifier` | `Required` |
| `allocation_id` | `Identifier` | `Required` |
| `generation` | `Version` | `Required` |
| `controller_version` | `Version` | `Required` |
| `claim` | `Claim` | `Required` |
| `deployment_id` | `ContentDigest` | `Required` |
| `environment_id` | `Identifier` | `Required` |
| `configuration_id` | `ContentDigest` | `Required` |
| `pool_digest` | `ContentDigest` | `Required` |
| `recipe_json` | `str` | `Field(min_length=1)` |
| `launch_configuration_json` | `str` | `Field(min_length=1)` |
| `effective_digest` | `ContentDigest` | `Required` |
| `provisioning_deadline` | `UtcDatetime` | `Required` |
| `hard_expires_at` | `UtcDatetime` | `Required` |
| `lease_expires_at` | `UtcDatetime` | `Required` |
| `initial_lease_expires_at` | `UtcDatetime` | `Required` |
| `state` | `Literal['reserved', 'ready', 'admitted', 'running', 'unknown', 'terminated', 'absent']` | `Required` |
| `capacity_reserved` | `bool` | `Required` |

### `LaunchObservationV2`

Import: `agentfabric_runtime.execution.scheduling_schemas.LaunchObservationV2`

Actual bounded backend evidence; freshness is evaluated by common policy.

| Field | Type | Default / validation |
| --- | --- | --- |
| `format` | `Literal['launch-observation-v2']` | `Required` |
| `namespace` | `Namespace` | `Required` |
| `execution_id` | `Identifier` | `Required` |
| `attempt_id` | `Identifier` | `Required` |
| `allocation_id` | `Identifier` | `Required` |
| `generation` | `Version` | `Required` |
| `controller_version` | `Version` | `Required` |
| `pool_digest` | `ContentDigest` | `Required` |
| `configuration_id` | `ContentDigest` | `Required` |
| `effective_digest` | `ContentDigest` | `Required` |
| `hard_expires_at` | `UtcDatetime` | `Required` |
| `lease_expires_at` | `UtcDatetime` | `Required` |
| `observed_at` | `UtcDatetime` | `Required` |
| `valid_until` | `UtcDatetime` | `Required` |
| `sequence` | `Version` | `Required` |
| `state` | `Literal['ready', 'running', 'unknown', 'terminated', 'absent']` | `Required` |
| `controls_verified` | `bool` | `Required` |
| `supervision_acknowledged` | `bool` | `Required` |

### `LaunchPermitV2`

Import: `agentfabric_runtime.execution.scheduling_schemas.LaunchPermitV2`

Immutable original admission receipt, distinct from current authority.

| Field | Type | Default / validation |
| --- | --- | --- |
| `format` | `Literal['launch-permit-v2']` | `Required` |
| `namespace` | `Namespace` | `Required` |
| `id` | `Identifier` | `Required` |
| `execution_id` | `Identifier` | `Required` |
| `attempt_id` | `Identifier` | `Required` |
| `allocation_id` | `Identifier` | `Required` |
| `generation` | `Version` | `Required` |
| `controller_version` | `Version` | `Required` |
| `claim` | `Claim` | `Required` |
| `pool_digest` | `ContentDigest` | `Required` |
| `configuration_id` | `ContentDigest` | `Required` |
| `effective_digest` | `ContentDigest` | `Required` |
| `hard_expires_at` | `UtcDatetime` | `Required` |
| `lease_expires_at` | `UtcDatetime` | `Required` |
| `dispatch_deadline` | `UtcDatetime` | `Required` |
| `observation` | `LaunchObservationV2` | `Required` |

### `ResourceControlSnapshotV2`

Import: `agentfabric_runtime.execution.scheduling_schemas.ResourceControlSnapshotV2`

Scoped current metadata; this view grants no new resource authority.

| Field | Type | Default / validation |
| --- | --- | --- |
| `namespace` | `Namespace` | `Required` |
| `execution_id` | `Identifier` | `Required` |
| `observed_at` | `UtcDatetime` | `Required` |
| `claim` | `Claim \| None` | `Required` |
| `initial_claim_expires_at` | `UtcDatetime \| None` | `Required` |
| `claim_renewal_json` | `str \| None` | `Required` |
| `attempt` | `LaunchAttemptV2 \| None` | `Required` |
| `lease_renewal_json` | `str \| None` | `Required` |
| `legacy_attempt` | `LaunchAttempt \| None` | `None` |

## `agentfabric_runtime.execution.interfaces`

### `SchedulingRepository`

Import: `agentfabric_runtime.execution.interfaces.SchedulingRepository`

#### `SchedulingRepository.mark_unknown`

```python
def mark_unknown(self, claim: Claim) -> None:
    ...
```

#### `SchedulingRepository.claim_next`

```python
def claim_next(self, *, worker_id: str, request_id: str) -> Claim | None:
    ...
```

#### `SchedulingRepository.prepare_attempt`

```python
def prepare_attempt(self, claim: Claim) -> LaunchAttempt | Rejection:
    ...
```

#### `SchedulingRepository.admit_launch`

```python
def admit_launch(self, claim: Claim, attempt_id: str) -> LaunchPermit | Rejection:
    ...
```

#### `SchedulingRepository.record_observation`

```python
def record_observation(self, claim: Claim, observation: LaunchObservation) -> None:
    ...
```

#### `SchedulingRepository.get_attempt`

```python
def get_attempt(self, claim: Claim) -> LaunchAttempt:
    ...
```

#### `SchedulingRepository.recoverable`

```python
def recoverable(self, *, limit: int=10) -> list[str]:
    ...
```

#### `SchedulingRepository.claim_recovery`

```python
def claim_recovery(self, execution_id: str, *, worker_id: str, request_id: str) -> Claim | None:
    ...
```

### `ResourceScheduling`

Import: `agentfabric_runtime.execution.interfaces.ResourceScheduling`

Explicit async common scheduling capability; legacy repositories stay separate.

| Field | Type | Default / validation |
| --- | --- | --- |
| `namespace` | `Namespace` | `Required` |
| `environment` | `EnvironmentV2` | `Required` |
| `pool_configuration` | `SchedulingPoolConfiguration` | `Required` |
| `read_limits` | `SchedulingReadLimits` | `Required` |

#### `ResourceScheduling.claim_next`

```python
async def claim_next(self, *, worker_id: str, request_id: str, after: SchedulingCursor | None) -> SchedulingClaimResult:
    ...
```

#### `ResourceScheduling.active_allocations`

```python
async def active_allocations(self, *, after: AllocationCursor | None) -> AllocationPage:
    ...
```

#### `ResourceScheduling.claim_recovery`

```python
async def claim_recovery(self, execution_id: str, *, worker_id: str, request_id: str) -> Claim | None:
    ...
```

#### `ResourceScheduling.inspect_control`

```python
async def inspect_control(self, execution_id: str) -> ResourceControlSnapshotV2:
    ...
```

#### `ResourceScheduling.get_attempt`

```python
async def get_attempt(self, claim: Claim) -> LaunchAttemptV2:
    ...
```

#### `ResourceScheduling.prepare_attempt`

```python
async def prepare_attempt(self, claim: Claim) -> LaunchAttemptV2 | Rejection:
    ...
```

#### `ResourceScheduling.admit_launch`

```python
async def admit_launch(self, claim: Claim, attempt_id: str) -> LaunchPermitV2 | Rejection:
    ...
```

#### `ResourceScheduling.record_observation`

```python
async def record_observation(self, claim: Claim, observation: LaunchObservationV2) -> None:
    ...
```

#### `ResourceScheduling.mark_unknown`

```python
async def mark_unknown(self, claim: Claim) -> None:
    ...
```

#### `ResourceScheduling.renew_claim`

```python
async def renew_claim(self, command: ClaimRenewal) -> ClaimRenewalResult:
    ...
```

#### `ResourceScheduling.renew_lease`

```python
async def renew_lease(self, command: LeaseRenewal) -> LeaseRenewalResult:
    ...
```

## `agentfabric_runtime.environments.interface`

### `Environment`

Import: `agentfabric_runtime.environments.interface.Environment`

#### `Environment.prepare`

```python
async def prepare(self, attempt: LaunchAttempt) -> LaunchObservation:
    ...
```

#### `Environment.launch`

```python
async def launch(self, attempt: LaunchAttempt, permit: LaunchPermit) -> LaunchObservation:
    ...
```

#### `Environment.inspect`

```python
async def inspect(self, attempt: LaunchAttempt) -> LaunchObservation:
    ...
```

#### `Environment.fence`

```python
async def fence(self, attempt: LaunchAttempt) -> LaunchObservation:
    ...
```

#### `Environment.stop`

```python
async def stop(self, attempt: LaunchAttempt) -> LaunchObservation:
    ...
```

### `LaunchConfigurationSource`

Import: `agentfabric_runtime.environments.interface.LaunchConfigurationSource`

Borrowed bounded content source; the SDK independently checks its digest.

#### `LaunchConfigurationSource.read`

```python
def read(self, configuration: str, *, max_bytes: int) -> bytes:
    ...
```

### `ResourceAuthority`

Import: `agentfabric_runtime.environments.interface.ResourceAuthority`

Store-backed command gates checked at the actual backend effect boundary.

#### `ResourceAuthority.provision_allowed`

```python
async def provision_allowed(self, attempt: LaunchAttemptV2) -> None:
    ...
```

#### `ResourceAuthority.dispatch_allowed`

```python
async def dispatch_allowed(self, attempt: LaunchAttemptV2, permit: LaunchPermitV2) -> None:
    ...
```

#### `ResourceAuthority.lease_renewal_allowed`

```python
async def lease_renewal_allowed(self, command: LeaseRenewal) -> None:
    ...
```

### `EnvironmentV2`

Import: `agentfabric_runtime.environments.interface.EnvironmentV2`

Explicit configured backend; matching values alone do not attest containment.

#### `EnvironmentV2.prepare`

```python
async def prepare(self, attempt: LaunchAttemptV2) -> LaunchObservationV2:
    ...
```

#### `EnvironmentV2.launch`

```python
async def launch(self, attempt: LaunchAttemptV2, permit: LaunchPermitV2) -> LaunchObservationV2:
    ...
```

#### `EnvironmentV2.inspect`

```python
async def inspect(self, attempt: LaunchAttemptV2) -> LaunchObservationV2:
    ...
```

#### `EnvironmentV2.fence`

```python
async def fence(self, attempt: LaunchAttemptV2) -> LaunchObservationV2:
    ...
```

#### `EnvironmentV2.stop`

```python
async def stop(self, attempt: LaunchAttemptV2) -> LaunchObservationV2:
    ...
```

#### `EnvironmentV2.renew_lease`

```python
async def renew_lease(self, command: LeaseRenewal) -> LeaseAcknowledgement:
    ...
```
