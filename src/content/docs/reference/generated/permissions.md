---
title: Permission and admission models
description: Source-derived fields and signatures for the unreleased SDK preview.
---

> **Unreleased source preview.** Generated declarations describe types, not a promise that every contract has an executable implementation. Read the [behavioral API reference](../../overview/) and [capability matrix](../../../runtime/capabilities/) first.

Field defaults shown as `Field(...)` include validation metadata. A `Field(...)` without `default=` or `default_factory=` is required. Inherited fields from classes in the same source module are included. Cross-field invariants are explained in the concept and behavioral reference pages.

## `agentfabric_runtime.permissions.schemas`

### `AdmissionReadLimits`

Import: `agentfabric_runtime.permissions.schemas.AdmissionReadLimits`

Application-selected bound on a complete action-grant candidate query.

| Field | Type | Default / validation |
| --- | --- | --- |
| `max_candidate_grants` | `int` | `Field(ge=1, le=(1 << 63) - 2)` |

### `PermissionReadLimits`

Import: `agentfabric_runtime.permissions.schemas.PermissionReadLimits`

Application-selected bound on a complete origin-grant query.

| Field | Type | Default / validation |
| --- | --- | --- |
| `max_origin_grants` | `int` | `Field(ge=1, le=(1 << 63) - 2)` |

### `ExternalScope`

Import: `agentfabric_runtime.permissions.schemas.ExternalScope`

Exact HTTPS origin; raw web or one account/resource/action via a trusted adapter.

| Field | Type | Default / validation |
| --- | --- | --- |
| `origin` | `str` | `Field(max_length=2048)` |
| `route` | `Literal['web', 'adapter']` | `Required` |
| `account_id` | `Identifier \| None` | `None` |
| `resource` | `Identifier \| None` | `None` |
| `action` | `Identifier \| None` | `None` |

### `AdapterDefinition`

Import: `agentfabric_runtime.permissions.schemas.AdapterDefinition`

| Field | Type | Default / validation |
| --- | --- | --- |
| `implementation_digest` | `ContentDigest` | `Required` |
| `provider` | `Identifier` | `Required` |
| `origin` | `str` | `Required` |
| `actions` | `tuple[Identifier, ...]` | `Field(min_length=1, max_length=100)` |

### `Connection`

Import: `agentfabric_runtime.permissions.schemas.Connection`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `namespace` | `Namespace` | `Required` |
| `provider` | `Identifier` | `Required` |
| `account_id` | `Identifier` | `Required` |
| `origin` | `str` | `Required` |
| `credential_ref` | `Identifier` | `Required` |
| `credential_digest` | `ContentDigest` | `Required` |
| `version` | `Version` | `1` |
| `state` | `Literal['connected', 'disconnected']` | `'connected'` |
| `expires_at` | `UtcDatetime \| None` | `None` |

### `ConnectionDisconnect`

Import: `agentfabric_runtime.permissions.schemas.ConnectionDisconnect`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `expected_version` | `Version` | `Required` |

### `ContextLimits`

Import: `agentfabric_runtime.permissions.schemas.ContextLimits`

Optional exact applicability, never wildcard matching or inferred authority.

| Field | Type | Default / validation |
| --- | --- | --- |
| `agent_id` | `Identifier \| None` | `None` |
| `goal_id` | `Identifier \| None` | `None` |
| `task_id` | `Identifier \| None` | `None` |
| `execution_id` | `Identifier \| None` | `None` |
| `roles` | `tuple[ExecutionRole, ...]` | `Required` |

### `AuthorityConfig`

Import: `agentfabric_runtime.permissions.schemas.AuthorityConfig`

| Field | Type | Default / validation |
| --- | --- | --- |
| `namespace` | `Namespace` | `Required` |
| `version` | `Version` | `1` |
| `issuer_actor_ids` | `tuple[Identifier, ...]` | `Required` |
| `resolver_actor_ids` | `tuple[Identifier, ...]` | `Required` |
| `store` | `Literal['integrated', 'external']` | `Required` |
| `permit_lifetime_ms` | `int` | `Field(ge=1, le=(1 << 63) - 1)` |
| `identity_store` | `Literal['local', 'external']` | `Required` |

### `Grant`

Import: `agentfabric_runtime.permissions.schemas.Grant`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `issuer_actor_id` | `Identifier` | `Required` |
| `recipient` | `Identity` | `Required` |
| `scope` | `ExternalScope` | `Required` |
| `context` | `ContextLimits` | `Required` |
| `expires_at` | `UtcDatetime` | `Required` |
| `parent_id` | `Identifier \| None` | `None` |
| `delegable` | `bool` | `False` |
| `revoked` | `bool` | `False` |
| `version` | `Version` | `1` |

### `AuthorityBinding`

Import: `agentfabric_runtime.permissions.schemas.AuthorityBinding`

Trusted eligibility binding, not a grant copy for each task/execution.

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `namespace` | `Namespace` | `Required` |
| `actor_id` | `Identifier` | `Required` |
| `context` | `ContextLimits` | `Required` |
| `root_grant_ids` | `tuple[Identifier, ...]` | `Required` |
| `version` | `Version` | `Required` |
| `policy_version` | `Version` | `Required` |

### `AccessRestriction`

Import: `agentfabric_runtime.permissions.schemas.AccessRestriction`

An applicable mandatory ceiling/deny, not an alternative source of grants.

| Field | Type | Default / validation |
| --- | --- | --- |
| `context` | `ContextLimits` | `Required` |
| `actor_id` | `Identifier \| None` | `None` |
| `allowed_scopes` | `tuple[ExternalScope, ...] \| None` | `None` |
| `denied_scopes` | `tuple[ExternalScope, ...]` | `()` |

### `AuthorityPolicy`

Import: `agentfabric_runtime.permissions.schemas.AuthorityPolicy`

| Field | Type | Default / validation |
| --- | --- | --- |
| `config` | `AuthorityConfig` | `Required` |
| `restrictions` | `tuple[AccessRestriction, ...]` | `Field(default=(), max_length=100)` |
| `adapters` | `tuple[AdapterDefinition, ...]` | `Field(default=(), max_length=100)` |
| `adapter_only_origins` | `tuple[str, ...]` | `Field(default=(), max_length=100)` |

### `LegacyPolicyInterpretation`

Import: `agentfabric_runtime.permissions.schemas.LegacyPolicyInterpretation`

Operator-supplied meaning for one exact historical policy JSON payload.

| Field | Type | Default / validation |
| --- | --- | --- |
| `payload_digest` | `ContentDigest` | `Required` |
| `policy` | `AuthorityPolicy` | `Required` |

### `PermissionRequest`

Import: `agentfabric_runtime.permissions.schemas.PermissionRequest`

| Field | Type | Default / validation |
| --- | --- | --- |
| `request_id` | `Identifier` | `Required` |
| `context` | `AccessContext` | `Required` |
| `binding_id` | `Identifier` | `Required` |
| `scope` | `ExternalScope` | `Required` |
| `reason` | `str` | `Field(min_length=1, max_length=2048)` |
| `expires_at` | `UtcDatetime` | `Required` |

### `PermissionDecision`

Import: `agentfabric_runtime.permissions.schemas.PermissionDecision`

Trusted resolution authorizes access, not goal continuation.

| Field | Type | Default / validation |
| --- | --- | --- |
| `request_id` | `Identifier` | `Required` |
| `decision_id` | `Identifier` | `Required` |
| `outcome` | `Literal['grant', 'deny']` | `Required` |
| `expected_binding_version` | `Version` | `Required` |
| `grant_expires_at` | `UtcDatetime \| None` | `None` |
| `grant_context` | `ContextLimits \| None` | `None` |

### `PermissionSnapshot`

Import: `agentfabric_runtime.permissions.schemas.PermissionSnapshot`

| Field | Type | Default / validation |
| --- | --- | --- |
| `request` | `PermissionRequest` | `Required` |
| `status` | `Literal['pending', 'granted', 'denied', 'expired']` | `Required` |
| `decision` | `PermissionDecision \| None` | `None` |
| `grant_id` | `Identifier \| None` | `None` |

### `AdmissionRequest`

Import: `agentfabric_runtime.permissions.schemas.AdmissionRequest`

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `operation_id` | `Identifier` | `Required` |
| `context` | `AccessContext` | `Required` |
| `binding_id` | `Identifier` | `Required` |
| `binding_version` | `Version` | `Required` |
| `policy_version` | `Version` | `Required` |
| `scope` | `ExternalScope` | `Required` |
| `connection_id` | `Identifier \| None` | `None` |
| `provider` | `Identifier \| None` | `None` |
| `connection_version` | `Version \| None` | `None` |
| `adapter_digest` | `ContentDigest \| None` | `None` |
| `intent_digest` | `ContentDigest` | `Required` |
| `resource_generation` | `Version` | `Required` |
| `controller_version` | `Version` | `Required` |
| `deadline` | `UtcDatetime` | `Required` |

### `AdmissionPermit`

Import: `agentfabric_runtime.permissions.schemas.AdmissionPermit`

Trusted exact bounded permit; single-use is enforced by the future executor.

| Field | Type | Default / validation |
| --- | --- | --- |
| `id` | `Identifier` | `Required` |
| `version` | `Version` | `Required` |
| `previous_permit_id` | `Identifier \| None` | `None` |
| `attempt_id` | `Identifier` | `Required` |
| `allocation_id` | `Identifier` | `Required` |
| `claim_id` | `Identifier` | `Required` |
| `request` | `AdmissionRequest` | `Required` |
| `grant_ids` | `tuple[Identifier, ...]` | `Required` |
| `grant_versions` | `tuple[Version, ...]` | `Required` |
| `expires_at` | `UtcDatetime` | `Required` |

### `AdmissionConsumption`

Import: `agentfabric_runtime.permissions.schemas.AdmissionConsumption`

| Field | Type | Default / validation |
| --- | --- | --- |
| `operation_id` | `Identifier` | `Required` |
| `permit_id` | `Identifier` | `Required` |
| `consumed_at` | `UtcDatetime` | `Required` |
| `disposition` | `Literal['new', 'already_consumed']` | `Required` |
