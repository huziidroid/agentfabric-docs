---
title: Troubleshooting
description: Diagnose common setup, authority, publication, progression, and recovery failures.
---

| Symptom | Check | Safe next step |
| --- | --- | --- |
| `agentfabric_runtime.runtime` import missing | Installed source predates the preview. | Use a compatible checkout; package name/version alone is insufficient. |
| Native path validation fails | Absolute canonical paths, owner/modes, ancestor safety, symlinks, existing SQLite sidecars. | Prepare valid private paths; do not weaken checks. |
| `provider_credentials` is `None` | No source supplied at construction. | Provision and borrow an application-owned source before creating Runtime. |
| Credential unauthorized | Revocation/expiry, namespace, role, exact context, generation/controller. | Obtain current authority through trusted host flows. |
| Grant exists but action denied | Eligibility binding, policy version, context ceiling, restrictions, lineage, connection freshness. | Inspect complete current evidence; existence alone grants no action. |
| Publication reply lost | Stable request ID and original retention. | Use `recover_publication`; do not ingest under a new ID blindly. |
| Artifact unavailable | State/expiry/deletion/source authority. | Inspect and recover within existing authority; replay cannot resurrect bytes. |
| Artifact integrity failure | Digest, file identity, bounded content verification. | Stop trusting content and investigate storage; do not bypass verification. |
| Decision conflicts | Request, goal version, plan revision, exact outcome and task. | Read current state; preserve original IDs for exact replay. |
| Wait resolved but work did not run | Paused intent, pending agent decision, dispatch. | Complete the explicit control/decision/dispatch sequence. |
| Outcome remains pending | Pending reason and backend/storage/resource evidence. | Reconcile original work; pending is not success or safe replacement. |
| Resume/Retry blocked | Complete effects, inputs, budgets, actual stopped state, retry-before-launch eligibility. | Resolve uncertainty rather than omitting history or changing task identity. |
| `finish` rejected | Schema value exists but implementation is unfinished. | Use only implemented decision actions; do not relabel a report as completion. |
| Read limit reached | Query is a complete safety observation, not a user page. | Review application limits and complete trusted evidence; partial data cannot authorize progress. |
| Storage timeout or cancellation | Commit or underlying work may still be uncertain. | Recover original identity/receipt and quiesce actual work. |

## Reporting an issue

Record the SDK source baseline, operation name, bounded error class/code, and nonsecret request identifiers. Redact credentials, provider secret envelopes, artifact content, and sensitive account data. Do not paste full validation input containing secrets.

Consult [Errors and limits](../../reference/errors/), [capabilities](../../runtime/capabilities/), and [source compatibility](../compatibility/) before assuming unsupported execution behavior.
