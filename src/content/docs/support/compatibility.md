---
title: Compatibility and source baseline
description: Understand the unreleased SDK baseline, source-derived reference, and compatibility boundaries.
---

## Documentation baseline

These docs describe the **unreleased working-tree SDK preview inspected on October 27, 2026**. Package version `0.1.0` is development metadata, not evidence that a matching public release exists.

The parent source commit is `cc77b8a58ca8a137a70e447155374a5e1a149bce`. Much of this preview is not part of that commit. Checking out the parent commit alone will not reproduce the APIs described here.

The documentation repository includes `sdk-reference-baseline.json`, which records SHA-256 hashes for the source modules used to generate field and signature reference pages. Those hashes identify the inspected declarations; they are not a release artifact or a claim of source availability.

## What is supported by these docs?

The [capability matrix](../../runtime/capabilities/) distinguishes native SDK behavior, implemented internal safety observations, contract-only extensions, and experimental scheduling work. Physical isolation and termination remain outside the qualified behavior.

A schema value can describe an action the runtime does not execute yet. For example, `finish` is part of `SignalAction`, but the current signal implementation rejects it with `NotImplementedError`. Handler-mode declarations and completion-check contracts likewise do not establish a working executable assessment pipeline.

## Data formats

Canonical records pin format names and digests. V1 and V2 task completion/outcome formats have distinct validation rules; do not relabel one format as another or discard unknown fields to make a record parse.

Legacy policy interpretation requires an operator-supplied mapping for an exact historical policy digest. It is not an automatic permissive migration.

## Versioned documentation

This site has one preview baseline. Separate versioned documentation should be introduced when distinct publicly usable releases require it. Until then, verify the source preview against the capability matrix and generated declarations before integrating.
