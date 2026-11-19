# ADR-001: Coordinator-owned orchestration with bounded retries

## Decision

Use one coordinator to dispatch two narrowly scoped specialists. The coordinator owns timeout, validation, retry, telemetry, merging, and escalation. Each specialist has no authority to create more agents.

## Why

This makes execution observable and finite. Parallel work reduces wall-clock latency when subtasks are independent, while sequential work remains available for real dependencies.

## Trade-offs

Multiple specialists can improve coverage or allow distinct expertise, but they add token cost, merge/conflict complexity, and more failure points. A single agent is usually preferable for a simple, coherent task that does not benefit from separation.

## Escalation rule

Escalate when retries are exhausted, required evidence is missing, specialist findings conflict on a material decision, or the action would have high impact and confidence is insufficient.
