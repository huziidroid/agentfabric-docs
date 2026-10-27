---
title: Native client method signatures
description: Source-derived fields and signatures for the unreleased SDK preview.
---

> **Unreleased source preview.** Generated declarations describe types, not a promise that every contract has an executable implementation. Read the [behavioral API reference](../../overview/) and [capability matrix](../../../runtime/capabilities/) first.

Field defaults shown as `Field(...)` include validation metadata. A `Field(...)` without `default=` or `default_factory=` is required. Inherited fields from classes in the same source module are included. Cross-field invariants are explained in the concept and behavioral reference pages.

## `agentfabric_runtime.runtime`

### `SQLiteRuntimeSettings`

Import: `agentfabric_runtime.runtime.SQLiteRuntimeSettings`

Existing application-owned paths and explicit native storage budgets.

| Field | Type | Default / validation |
| --- | --- | --- |
| `namespace` | `Namespace` | `Required` |
| `database_path` | `Path` | `Required` |
| `artifact_directory` | `Path` | `Required` |
| `busy_timeout_ms` | `int` | `Required` |
| `file_lock_timeout` | `float` | `Required` |
| `artifact_limits` | `ArtifactLimits` | `Required` |
| `permission_read_limits` | `PermissionReadLimits` | `Required` |
| `admission_read_limits` | `AdmissionReadLimits` | `Required` |
| `operation_read_limits` | `OperationReadLimits` | `Required` |

#### `SQLiteRuntimeSettings.valid_busy_timeout`

```python
def valid_busy_timeout(cls, value: int) -> int:
    ...
```

#### `SQLiteRuntimeSettings.valid_file_lock_timeout`

```python
def valid_file_lock_timeout(cls, value: float) -> float:
    ...
```

### `Runtime`

Import: `agentfabric_runtime.runtime.Runtime`

Owned synchronous native clients; not a workload context or a runner.

Use open_sqlite before entering the application's event loop. Before close,
quiesce every service call including underlying synchronous file/SQL jobs:
cancelling an awaiting coroutine alone does not prove its thread stopped.
Concurrent close/new calls and aggregate asynchronous draining are unsupported.
Existing artifact close retains descriptor safety for accepted file jobs.
Borrowed clocks and provider sources are never closed by this object.

#### `Runtime.create_task_coordinator`

```python
def create_task_coordinator(self, *, environment: Environment, coordinator_credential: Callable[[], SecretStr], worker_id: Identifier, claim_seconds: float, io_timeout: float) -> _TaskCoordinator:
    ...
```

#### `Runtime.open_sqlite`

```python
def open_sqlite(cls, settings: SQLiteRuntimeSettings, *, policy: AuthorityPolicy, clock: Callable[[], datetime]=utc_now, legacy_policies: tuple[LegacyPolicyInterpretation, ...]=(), provider_source: FileCredentialSource | None=None) -> Self:
    ...
```

Open the supported native clients, with no implicit bootstrap or runner.

A partial failure may retain committed setup. Retry the same explicit
storage binding/policy; do not assume cleanup undoes durable writes.

#### `Runtime.close`

```python
def close(self) -> None:
    ...
```

## `agentfabric_runtime.storage.repositories.credential_repo`

### `SQLCredentialStore`

Import: `agentfabric_runtime.storage.repositories.credential_repo.SQLCredentialStore`

#### `SQLCredentialStore.close`

```python
def close(self) -> None:
    ...
```

#### `SQLCredentialStore.issue`

```python
def issue(self, credential_id: Identifier, principal: VerifiedPrincipal) -> CredentialIssue:
    ...
```

#### `SQLCredentialStore.rotate`

```python
def rotate(self, old_id: Identifier, new_id: Identifier, principal: VerifiedPrincipal) -> CredentialIssue:
    ...
```

#### `SQLCredentialStore.inspect`

```python
def inspect(self, credential_id: Identifier) -> CredentialRecord:
    ...
```

#### `SQLCredentialStore.revoke`

```python
def revoke(self, credential_id: Identifier) -> None:
    ...
```

#### `SQLCredentialStore.verify`

```python
def verify(self, credential: SecretStr) -> VerifiedPrincipal:
    ...
```

#### `SQLCredentialStore.bootstrap_management`

```python
def bootstrap_management(self, filename: Identifier, credential_id: Identifier, principal: VerifiedPrincipal, *, rotation_from: Identifier | None=None) -> SecretStr:
    ...
```

## `agentfabric_runtime.permissions.interfaces`

### `ProviderCredentialSource`

Import: `agentfabric_runtime.permissions.interfaces.ProviderCredentialSource`

Application-owned bounded material source with exact connection binding.

Implementations must verify namespace/provider/account/origin/reference and
fingerprint against their own representation. This proves no remote identity.

#### `ProviderCredentialSource.namespace`

```python
def namespace(self) -> Namespace:
    ...
```

#### `ProviderCredentialSource.read`

```python
def read(self, record: Connection) -> SecretStr:
    ...
```

### `CredentialProvider`

Import: `agentfabric_runtime.permissions.interfaces.CredentialProvider`

#### `CredentialProvider.resolve`

```python
def resolve(self, permit: AdmissionPermit, *, credential: SecretStr) -> SecretStr:
    ...
```

Only trusted executors resolve a saved current unconsumed adapter permit.

### `ConnectionService`

Import: `agentfabric_runtime.permissions.interfaces.ConnectionService`

#### `ConnectionService.put`

```python
def put(self, record: Connection, mutation_id: Identifier, *, credential: SecretStr) -> Connection:
    ...
```

#### `ConnectionService.inspect_connection`

```python
def inspect_connection(self, connection_id: Identifier, *, credential: SecretStr) -> Connection:
    ...
```

#### `ConnectionService.disconnect`

```python
def disconnect(self, connection_id: Identifier, expected_version: Version, mutation_id: Identifier, *, credential: SecretStr) -> Connection:
    ...
```

### `PermissionService`

Import: `agentfabric_runtime.permissions.interfaces.PermissionService`

Request/decision API; verifies credential and ownership before every call.

#### `PermissionService.inspect_binding`

```python
def inspect_binding(self, binding_id: str, *, credential: SecretStr) -> AuthorityBinding:
    ...
```

#### `PermissionService.inspect_grant`

```python
def inspect_grant(self, grant_id: str, *, credential: SecretStr) -> Grant:
    ...
```

#### `PermissionService.configure`

```python
def configure(self, policy: AuthorityPolicy, mutation_id: Identifier, *, credential: SecretStr) -> AuthorityPolicy:
    ...
```

#### `PermissionService.issue`

```python
def issue(self, grant: Grant, mutation_id: Identifier, *, credential: SecretStr) -> Grant:
    ...
```

#### `PermissionService.request`

```python
def request(self, request: PermissionRequest, *, credential: SecretStr) -> PermissionSnapshot:
    ...
```

#### `PermissionService.inspect`

```python
def inspect(self, request_id: str, *, credential: SecretStr) -> PermissionSnapshot:
    ...
```

#### `PermissionService.decide`

```python
def decide(self, decision: PermissionDecision, *, credential: SecretStr) -> PermissionSnapshot:
    ...
```

#### `PermissionService.bind`

```python
def bind(self, binding: AuthorityBinding, *, credential: SecretStr) -> AuthorityBinding:
    ...
```

Authorize/version/audit eligibility mutation, serialized with local admission.

#### `PermissionService.revoke`

```python
def revoke(self, grant_id: str, expected_version: Version, mutation_id: str, *, credential: SecretStr) -> None:
    ...
```

### `AuthorityProvider`

Import: `agentfabric_runtime.permissions.interfaces.AuthorityProvider`

One authority of record, not a remote Boolean preflight plus a local allow copy.

#### `AuthorityProvider.admit`

```python
def admit(self, request: AdmissionRequest, *, credential: SecretStr) -> AdmissionPermit:
    ...
```

#### `AuthorityProvider.renew`

```python
def renew(self, request: AdmissionRequest, previous_permit_id: Identifier, *, credential: SecretStr) -> AdmissionPermit:
    ...
```

#### `AuthorityProvider.inspect_consumption`

```python
def inspect_consumption(self, request_id: str, *, credential: SecretStr) -> AdmissionConsumption | None:
    ...
```

#### `AuthorityProvider.inspect_admission`

```python
def inspect_admission(self, request_id: str, *, credential: SecretStr) -> AdmissionPermit | None:
    ...
```

#### `AuthorityProvider.consume`

```python
def consume(self, permit: AdmissionPermit, *, credential: SecretStr) -> AdmissionConsumption:
    ...
```

Effective executor orders single-use consumption against live revoke/expiry.

The integrated implementation shares the local intent transaction.
External implementations require their own qualified enforcement bound.

## `agentfabric_runtime.storage.provider_credentials`

### `FileCredentialSource`

Import: `agentfabric_runtime.storage.provider_credentials.FileCredentialSource`

#### `FileCredentialSource.__init__`

```python
def __init__(self, directory: Path, namespace: Namespace):
    ...
```

#### `FileCredentialSource.close`

```python
def close(self) -> None:
    ...
```

#### `FileCredentialSource.digest`

```python
def digest(self, reference: str, *, provider: str, account_id: str, origin: str) -> str:
    ...
```

Trusted configuration inspection; returns a fingerprint, never a secret.

#### `FileCredentialSource.read`

```python
def read(self, record: Connection) -> SecretStr:
    ...
```

## `agentfabric_runtime.services.goals`

### `SQLGoalClient`

Import: `agentfabric_runtime.services.goals.SQLGoalClient`

Native composition and lifecycle checks for the shared GoalService.

#### `SQLGoalClient.inspect_wait`

```python
async def inspect_wait(self, goal_id: Identifier, *, credential: SecretStr) -> WaitSpec | None:
    ...
```

#### `SQLGoalClient.resolve_wait`

```python
async def resolve_wait(self, resolution: WaitResolution, *, credential: SecretStr) -> GoalSnapshot:
    ...
```

#### `SQLGoalClient.register`

```python
async def register(self, binding: AgentBinding, *, credential: SecretStr) -> AgentBinding:
    ...
```

#### `SQLGoalClient.signal`

```python
async def signal(self, signal: AgentSignal, *, credential: SecretStr) -> DecisionReceipt:
    ...
```

#### `SQLGoalClient.decisions`

```python
async def decisions(self, goal_id: Identifier, after_version: EventCursor, limit: PageLimit, *, credential: SecretStr) -> tuple[GoalDecisionRecord, ...]:
    ...
```

#### `SQLGoalClient.pause`

```python
async def pause(self, goal_id: Identifier, version: Version, *, credential: SecretStr) -> GoalStatus:
    ...
```

#### `SQLGoalClient.resume`

```python
async def resume(self, goal_id: Identifier, version: Version, *, credential: SecretStr) -> GoalStatus:
    ...
```

#### `SQLGoalClient.cancel`

```python
async def cancel(self, goal_id: Identifier, version: Version, *, credential: SecretStr) -> GoalStatus:
    ...
```

#### `SQLGoalClient.submit`

```python
async def submit(self, spec: GoalSpec, *, credential: SecretStr) -> Identifier:
    ...
```

#### `SQLGoalClient.inspect`

```python
async def inspect(self, goal_id: Identifier, *, credential: SecretStr) -> GoalDetails:
    ...
```

#### `SQLGoalClient.status`

```python
async def status(self, goal_id: Identifier, *, credential: SecretStr) -> GoalStatus:
    ...
```

#### `SQLGoalClient.list`

```python
async def list(self, after: Identifier | None, limit: PageLimit, *, credential: SecretStr) -> GoalPage:
    ...
```

#### `SQLGoalClient.tasks`

```python
async def tasks(self, goal_id: Identifier, *, credential: SecretStr) -> tuple[TaskView, ...]:
    ...
```

#### `SQLGoalClient.pending_decision`

```python
async def pending_decision(self, goal_id: Identifier, *, credential: SecretStr) -> DecisionRequest | None:
    ...
```

#### `SQLGoalClient.events`

```python
async def events(self, goal_id: Identifier, after: EventCursor, limit: PageLimit, *, credential: SecretStr) -> tuple[GoalEvent, ...]:
    ...
```

#### `SQLGoalClient.dispatch`

```python
async def dispatch(self, goal_id: Identifier, version: Version, *, credential: SecretStr) -> Identifier:
    ...
```

#### `SQLGoalClient.executions`

```python
async def executions(self, goal_id: Identifier, task_id: Identifier, *, credential: SecretStr) -> tuple[Identifier, ...]:
    ...
```

## `agentfabric_runtime.goals.interfaces`

### `TaskHandler`

Import: `agentfabric_runtime.goals.interfaces.TaskHandler`

#### `TaskHandler.execute`

```python
async def execute(self, task: TaskSpec, checkpoint: ContentReference | None) -> TaskResponse:
    ...
```

Application behavior produces an outcome envelope, not a Runtime decision.

### `AssessmentHandler`

Import: `agentfabric_runtime.goals.interfaces.AssessmentHandler`

#### `AssessmentHandler.assess`

```python
async def assess(self, request: DecisionRequest) -> AgentSignal:
    ...
```

Return intent; do not wait for application of a signal while still executing.

### `CompletionCheckHandler`

Import: `agentfabric_runtime.goals.interfaces.CompletionCheckHandler`

#### `CompletionCheckHandler.check`

```python
async def check(self, request: CompletionCheckRequest) -> CompletionReport:
    ...
```

Assess exact saved evidence outside writes; Runtime verifies the returned binding.

### `TaskCompletionClient`

Import: `agentfabric_runtime.goals.interfaces.TaskCompletionClient`

Trusted executor return recording and current authorized outcome metadata.

#### `TaskCompletionClient.record`

```python
async def record(self, completion: TaskCompletion | TaskCompletionV2, *, expires_at: UtcDatetime | None=None, credential: SecretStr) -> TaskCompletionReceipt:
    ...
```

Require new expiry; exact receipt replay grants no new file/stop authority.

#### `TaskCompletionClient.inspect`

```python
async def inspect(self, execution_id: Identifier, *, credential: SecretStr) -> TaskOutcomeSnapshot:
    ...
```

Expose pending/recorded/legacy-unavailable facts without needing artifact bytes.

## `agentfabric_runtime.services.task_coordinator`

### `TaskCoordinator`

Import: `agentfabric_runtime.services.task_coordinator.TaskCoordinator`

One explicit reconciliation call; no agent reasoning or background loop.

Only a control claim acquired by this invocation permits backend control.
A configured worker label cannot adopt somebody else's live claim.

#### `TaskCoordinator.pending`

```python
async def pending(self, after: Identifier | None, limit: PageLimit) -> tuple[Identifier, ...]:
    ...
```

#### `TaskCoordinator.reconcile`

```python
async def reconcile(self, execution_id: Identifier) -> TaskOutcomeSnapshot:
    ...
```
