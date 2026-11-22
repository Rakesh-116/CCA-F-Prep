# Prompt/context engineering, reliability, and evaluation

Last verified: 2026-11-22. Sources: [prompt engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables), [tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview), and [context management](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview).

## Solve the right layer

| Problem | Primary control |
| --- | --- |
| Ambiguous model task | clear system/user instructions, XML structure, few-shot examples |
| Untrusted input pretending to be instructions | isolate/label it as data; validate tool requests; do not grant it authority |
| Invalid JSON shape | structured output/schema |
| Invalid business fact or total | application semantic validation |
| Action must never happen | permission boundary or deterministic hook |
| Repeated transient outage | timeout, bounded retry, backoff, jitter |
| Long task loses important state | durable state plus selected summary |

Prompt caching reuses repeated prompt prefixes to reduce repeated processing cost. It does not shrink the context window or turn irrelevant history into useful context. Context compaction is lossy; preserve decisions, entity/value associations, and open work explicitly.

Example: do not summarize “two refunds exist.” Preserve `Order A-17 → $15 approved` and `Order B-22 → $15 pending`; losing the association can cause a harmful action even though the amount survives.

## Reliable execution

Retry only a transient, idempotent, or safely deduplicated operation. Use timeout, exponential backoff, jitter, a maximum attempt count, and correlation IDs. Do not blindly retry a charge, message send, or deletion: use an idempotency key or escalate. Circuit breakers and graceful degradation prevent a failing dependency from consuming all capacity.

## Evaluation

Use a labeled golden dataset and deterministic fixtures for regression. Measure the task-appropriate precision, recall, accuracy, false-positive and false-negative rates. LLM-as-judge can scale qualitative review but should be calibrated against human evaluation. A model’s self-reported confidence is not calibration evidence.

## Remember this

Put facts in durable state, repeated static context in a cache, and guardrails at deterministic boundaries.
