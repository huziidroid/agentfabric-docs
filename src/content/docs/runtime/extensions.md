---
title: Extension contracts and execution boundaries
description: Understand supported adapters, future facades, simulated environments, and experimental scheduling.
---

## Native services and adapter boundaries

Native `Runtime.open_sqlite()` is the concrete construction path documented here. Shared service boundaries separate identity verification, state transactions, artifact bytes, authority, and provider credential sources. `ArtifactService` is an implemented advanced composition path that borrows its supplied components.

Implementing a protocol does not automatically provide production semantics. An adapter must preserve validation, authorization, transaction certainty, complete observations, bounded I/O, and current expiry/revocation behavior. Other extractions and complete adapter-based Runtime construction remain in progress.

## Future facades

`ExecutionClient`, `WorkspaceClient`, and `OperationClient` describe intended interfaces. `TaskHandler`, `AssessmentHandler`, and `CompletionCheckHandler` describe handler contracts. Their presence is not a completed public runner.

There is no `runtime.executions`, `runtime.workspace`, `runtime.operations`, or `runtime.scheduler` attribute. Use the actual [native service map](../../reference/overview/).

## Configuration and readiness

`EnvironmentProfile` declares explicit CPU, memory, workspace, process, lifetime, lease, stop-grace, revocation, and gateway-only network bounds. `LaunchRecipe` pins complete backend configuration. `EffectiveLaunchConfiguration` binds accepted input/sources/context/output limits to immutable allocation identity and hard expiry.

`EnvironmentReadiness.ready()` compares trusted observation identity, generation/controller, time window, and verification flags. Declaring a host or setting readiness flags is not independent backend qualification.

## Scheduling development preview

Existing Scheduler/DummyEnvironment behavior is simulated. New shared scheduling introduces claim identity, allocation/control identity, bounded cursor discovery, claim versus resource leases, same-controller renewal, fences, and immutable launch association. A renewable control lease does not extend the allocation's hard expiry.

Shared scheduling services and the corresponding new migration are experimental source candidates. They are not supported native Runtime construction or qualified physical infrastructure.

The [environment/execution declarations](../../reference/generated/environment/) and [scheduling declarations](../../reference/generated/scheduling/) are provided for contract inspection. Keep experimental adapters behind application-owned boundaries and do not infer isolation or termination guarantees from dummy tests.
