---
title: Issue grants and bind eligible access
description: Configure a scoped grant and explicitly establish a worker eligibility binding.
---

## Prerequisites

The application is inside the trusted host. Runtime is open with `application` configured as issuer and resolver, and `credential` represents that current management principal. `namespace` is the Runtime namespace. The following contextual snippet changes local permission state; it performs no external request.

```python
from datetime import UTC, datetime, timedelta
from agentfabric_runtime.core.schemas import Identity
from agentfabric_runtime.permissions.schemas import (
    AuthorityBinding, ContextLimits, ExternalScope, Grant,
)

limits = ContextLimits(roles=("task",))
grant = Grant(
    id="reporter-web", issuer_actor_id="application",
    recipient=Identity(namespace=namespace, actor_id="reporter"),
    scope=ExternalScope(origin="https://example.com", route="web"),
    context=limits,
    expires_at=datetime.now(UTC) + timedelta(minutes=10),
)
runtime.permissions.issue(grant, "issue-reporter-web", credential=credential)
binding = AuthorityBinding(
    id="reporter-access", namespace=namespace, actor_id="reporter",
    context=limits, root_grant_ids=(grant.id,), version=1, policy_version=1,
)
runtime.permissions.bind(binding, credential=credential)
```

The configured policy version must match `policy_version`; use current trusted policy data in a real integration. A broad raw web route only restricts origin. Choose an adapter route with account/resource/action fields when that narrower promise is required.

## Request and resolve missing access

1. Supply an exact `AccessContext` represented by the current credential and allowed by the binding.
2. Submit `PermissionRequest` with its ID, scope, reason, and expiry through `request()`.
3. Have a configured management resolver inspect and decide the exact request using `PermissionDecision` and expected binding version.
4. Inspect the saved snapshot. A grant requires an explicit expiry within the requested deadline.
5. Resolve any separate goal permission wait, then obtain the appropriate agent continuation. Approval alone does not progress the goal.

## Narrow, revoke, and recover

Child grants require valid delegation and remain inside parent scope/context/lifetime. To revoke, read the saved version and call `revoke(grant_id, expected_version, mutation_id, credential=...)` as a resolver. Preserve mutation IDs across uncertain responses. Never treat read-limit overflow as a complete authority decision.

See [Permissions](../../runtime/permissions/) and the [Permission API](../../reference/permissions/).
