"""Declare and dispatch a goal without launching a physical handler.

Requires a compatible unreleased AgentFabric Runtime source installation.
The temporary tutorial state is removed when the example exits.
"""

import asyncio
from datetime import UTC, datetime, timedelta
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory

from agentfabric_runtime.artifacts.schemas import ArtifactLimits
from agentfabric_runtime.core.identity import VerifiedPrincipal
from agentfabric_runtime.core.schemas import (
    ContentReference, ExecutionOutputLimits, HandlerReference, Identity, Namespace,
)
from agentfabric_runtime.goals.schemas import AgentBinding, GoalLimits, GoalSpec, TaskSpec
from agentfabric_runtime.operations.schemas import OperationReadLimits
from agentfabric_runtime.permissions.schemas import (
    AdmissionReadLimits,
    AuthorityConfig,
    AuthorityPolicy,
    PermissionReadLimits,
)
from agentfabric_runtime.runtime import Runtime, SQLiteRuntimeSettings


async def declare_goal(runtime, credential, namespace, source, now):
    # Demonstration digests identify a declared example only. No handler is resolved.
    digest = "sha256:" + sha256(b"docs-declared-handler-v1").hexdigest()
    handler = HandlerReference(
        id="inspect-input", version=digest, deployment=digest,
        configuration=digest, environment="declared-example",
    )
    binding = AgentBinding(
        id="reporter", version=digest, task_handlers=(handler,),
        decision_actor=Identity(namespace=namespace, actor_id="application"),
        decision_mode="signals",
    )
    spec = GoalSpec(
        request_id="report-goal", namespace=namespace, agent=binding,
        description="Inspect the accepted input", input_ref=source,
        tasks=(TaskSpec(
            id="inspect", handler=handler, input_ref=source,
            expected_output="An inspection result",
        ),),
        limits=GoalLimits(max_tasks=1, max_executions=2, max_decisions=2, max_revisions=1),
        output_limits=ExecutionOutputLimits(
            max_outputs=0, max_output_bytes=0, max_return_bytes=4096,
        ),
        deadline=now + timedelta(minutes=5),
    )
    await runtime.goals.register(binding, credential=credential)
    goal_id = await runtime.goals.submit(spec, credential=credential)
    details = await runtime.goals.inspect(goal_id, credential=credential)
    execution_id = await runtime.goals.dispatch(
        goal_id, details.version, credential=credential,
    )
    outcome = await runtime.task_completions.inspect(execution_id, credential=credential)
    assert outcome.availability == "pending"
    return spec, goal_id, execution_id


def main() -> None:
    now = datetime.now(UTC)
    namespace = Namespace(application_id="docs-example", owner_id="local-owner")
    principal = VerifiedPrincipal(
        identity=Identity(namespace=namespace, actor_id="application"),
        role="management",
        expires_at=now + timedelta(hours=1),
    )
    policy = AuthorityPolicy(
        config=AuthorityConfig(
            namespace=namespace,
            issuer_actor_ids=("application",),
            resolver_actor_ids=("application",),
            store="integrated",
            identity_store="local",
            permit_lifetime_ms=1200,
        )
    )
    with TemporaryDirectory(prefix="agentfabric-tutorial-") as temporary:
        state = Path(temporary).resolve()
        state.chmod(0o700)
        artifacts = state / "artifacts"
        artifacts.mkdir(mode=0o700)
        settings = SQLiteRuntimeSettings(
            namespace=namespace,
            database_path=state / "runtime.db",
            artifact_directory=artifacts,
            busy_timeout_ms=1500,
            file_lock_timeout=1.5,
            artifact_limits=ArtifactLimits(max_ingest_bytes=1024, max_read_bytes=1024),
            permission_read_limits=PermissionReadLimits(max_origin_grants=256),
            admission_read_limits=AdmissionReadLimits(max_candidate_grants=256),
            operation_read_limits=OperationReadLimits(max_goal_operations=256),
        )
        with Runtime.open_sqlite(settings, policy=policy) as runtime:
            credential = runtime.identities.bootstrap_management(
                "management.json", "management", principal
            )
            published = asyncio.run(
                runtime.artifacts.put_bytes(
                    b"Hello, AgentFabric!",
                    request_id="hello",
                    expires_at=now + timedelta(minutes=10),
                    credential=credential,
                )
            )
            assert published.state == "published"
            print("Artifact published.")
            spec, goal_id, execution_id = asyncio.run(declare_goal(
                runtime, credential, namespace,
                ContentReference(id=published.id, digest=published.digest), now,
            ))
            print("Goal accepted; execution recorded. No handler was launched.")

        with Runtime.open_sqlite(settings, policy=policy) as runtime:
            credential = runtime.identities.bootstrap_management(
                "management.json", "management", principal
            )
            recovered = asyncio.run(
                runtime.artifacts.recover_publication("hello", credential=credential)
            )
            assert recovered.id == published.id
            payload = asyncio.run(
                runtime.artifacts.read(
                    ContentReference(id=recovered.id, digest=recovered.digest),
                    credential=credential,
                )
            )
            print("Artifact recovered after reopening.")
            print(payload.decode("utf-8"))
            details = asyncio.run(runtime.goals.inspect(goal_id, credential=credential))
            assert details.spec == spec
            assert details.current_execution_id == execution_id
            print("Accepted goal recovered after reopening.")


if __name__ == "__main__":
    main()
