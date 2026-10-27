"""Open native Runtime, publish an artifact, and recover it after reopening.

Requires a compatible unreleased AgentFabric Runtime source installation.
The temporary tutorial state is removed when the example exits.
"""

import asyncio
from datetime import UTC, datetime, timedelta
from pathlib import Path
from tempfile import TemporaryDirectory

from agentfabric_runtime.artifacts.schemas import ArtifactLimits
from agentfabric_runtime.core.identity import VerifiedPrincipal
from agentfabric_runtime.core.schemas import ContentReference, Identity, Namespace
from agentfabric_runtime.operations.schemas import OperationReadLimits
from agentfabric_runtime.permissions.schemas import (
    AdmissionReadLimits,
    AuthorityConfig,
    AuthorityPolicy,
    PermissionReadLimits,
)
from agentfabric_runtime.runtime import Runtime, SQLiteRuntimeSettings


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


if __name__ == "__main__":
    main()
