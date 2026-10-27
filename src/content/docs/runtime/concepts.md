---
title: Core concepts and values
description: The shared value types, validation rules, and ownership boundaries behind the SDK.
---

## The ownership model

Your application defines work and authority. The agent supplies task behavior and business judgments. Runtime records accepted work and validates transitions. This separation lets an application recover durable progress without treating arbitrary agent text as authority.

For example, a reporting application declares a goal, pins a worker version and input, and allows access to a sales source. Runtime records the work; the agent decides whether the resulting report satisfies the request.

## Namespace and identity

`Namespace(application_id, owner_id)` identifies an application/owner boundary. `Identity(namespace, actor_id)` names an actor inside it. Both are values; authentication requires a verified credential. See [Identities and credentials](../identities/).

## Content and outcome references

`ContentReference(id, digest)` pins artifact content. A digest uses canonical `sha256:` followed by 64 lowercase hexadecimal digits. A reference is not a read capability.

`TechnicalOutcomeReference(execution_id, format, digest)` identifies immutable SQL-owned outcome metadata. Its bytes are not an ordinary artifact. An outcome can separately reference a handler-return artifact.

## Handler references and worker versions

`HandlerReference` pins handler ID, version digest, deployment digest, configuration digest, and environment. It describes accepted behavior; it is not a Python callable or import string. An `AgentBinding` registers those references with a decision actor and decision mode.

## Strict values

SDK models derive from frozen `RuntimeSchema` values. Inputs are strict, unknown fields and nonfinite values are rejected, and values are revalidated at boundaries. Supply timezone-aware timestamps; the SDK normalizes them to UTC.

Identifiers are nonempty bounded UTF-8 strings, with a maximum of 1,024 bytes. Versions are positive bounded integers. Event cursors are nonnegative. Page limits range from 1 to 1,000. Model fields can impose narrower constraints; consult [common values reference](../../reference/generated/core/).

## Requests and versions

A request or mutation ID identifies one accepted operation. Exact replay recovers that operation's saved response. Reusing the ID with different arguments causes a conflict. Optimistic versions identify the state you intend to change; they are not a substitute for credentials.

Read [Durability, budgets, and recovery](../durability/) and the [behavioral reference](../../reference/overview/) before choosing retry behavior.
