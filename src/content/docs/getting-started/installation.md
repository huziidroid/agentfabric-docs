---
title: Installation and compatibility
description: Install a compatible unreleased Runtime source checkout and verify the public SDK imports.
---

## Choose a compatible source preview

These docs describe the **unreleased SDK source preview**, not a published package release. The runtime's package metadata currently says `0.1.0`, but that alone does not identify the implemented API described here.

You need a Runtime source checkout containing `src/agentfabric_runtime/runtime.py` and the APIs in the [capability matrix](../../runtime/capabilities/). Current public repository HEAD may precede that preview. A package-index release and a downloadable qualified wheel have not been established by this documentation.

## Create an isolated Python environment

Use **Python 3.12 or newer**. The native implementation requires a POSIX host with application-owned private directories; the tutorial is intended for macOS or Linux.

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Replace `/path/to/agentfabric-runtime` below with the absolute path to your compatible source checkout, then install it:

```sh
python -m pip install /path/to/agentfabric-runtime
python -c "from agentfabric_runtime.runtime import Runtime, SQLiteRuntimeSettings; print('Runtime SDK import verified')"
```

Expected output from the import check:

```text
Runtime SDK import verified
```

The package declares SQLAlchemy, Pydantic, and Alembic dependencies. Let the source package resolve its declared versions; do not substitute an unrelated package with a similar name.

## Next step

Follow [Store and recover your first artifact](../../tutorials/native-runtime/). That tutorial exercises real native storage, credential bootstrap, and artifact publication. It does not require a physical execution backend.

See [Compatibility and source baseline](../../support/compatibility/) for the limitations of this preview and how these docs track it.
