---
title: Publish, recover, and delete artifacts
description: Use artifact request identity, exact content references, and explicit retention.
---

## Prerequisites

Use an open Runtime and a currently authorized management or exact executor credential. The following is an async helper for the trusted application; it is contextual code, not a standalone program. The [native tutorial](../../tutorials/native-runtime/) supplies a complete host.

```python
from datetime import UTC, datetime, timedelta
from agentfabric_runtime.core.schemas import ContentReference

async def artifact_round_trip(runtime, credential):
    saved = await runtime.artifacts.put_bytes(
        b"report input",
        request_id="report-input",
        expires_at=datetime.now(UTC) + timedelta(minutes=10),
        credential=credential,
    )
    recovered = await runtime.artifacts.recover_publication(
        "report-input", credential=credential
    )
    assert recovered.id == saved.id
    data = await runtime.artifacts.read(
        ContentReference(id=recovered.id, digest=recovered.digest),
        credential=credential,
    )
    assert data == b"report input"
    metadata = await runtime.artifacts.inspect(saved.id, credential=credential)
    return metadata
```

Choose stable request IDs for each logical publication. A new request needs explicit expiry. After an uncertain response, recover the same request rather than manufacture another publication.

## Publish an existing source

With a currently readable accepted `ContentReference`, call `publish(source, request_id=..., credential=...)`. This verifies bounded source bytes and records publication. It does not make an artifact publicly accessible on the Internet.

## Delete content

Under namespace management authority, after the application no longer needs a publication, call `delete(artifact_id, credential=...)` and inspect the resulting metadata. Retention/deletion cannot be undone by replaying a former ingest. Plan deletion around accepted tasks that still require the content.

Treat integrity and availability errors separately. Do not read backing files to bypass authority, digest, or size checks. Quiesce underlying work before close.

See [Artifacts](../../runtime/artifacts/) and [all six API methods](../../reference/artifacts/).
