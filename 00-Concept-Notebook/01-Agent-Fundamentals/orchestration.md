# Coordinator and specialist orchestration

## Definition

A coordinator breaks a goal into bounded tasks, invokes specialists, validates their outputs, and decides whether to merge, retry, or escalate.

## Execution flow

```text
Question → decomposition → specialist calls → validation → merge / retry / escalate
```

Project 1 implements this with two mock specialists and a fixed retry limit.

## Parallel versus sequential

| Choice | Use when | Trade-off |
| --- | --- | --- |
| Parallel | Tasks are independent | Lower wall-clock latency; higher concurrent cost and merge complexity |
| Sequential | A later task needs an earlier result | Higher latency; preserves dependency order |
| Single agent | One coherent task needs no separated expertise | Lower cost and simpler coordination |
| Multiple agents | Distinct expertise or isolated workstreams add value | More tokens, failures, and contradiction handling |

## Exam trap

“Parallel is always faster” is incomplete. It is inappropriate when the business analysis must evaluate options first identified by technical research.

## Self-check

1. What control prevents an agent loop from continuing indefinitely?  
2. When should a coordinator escalate rather than retry?

### Answers

1. A maximum attempt/turn budget with a terminal outcome.  
2. After retries are exhausted, evidence conflicts materially, or a high-impact decision lacks sufficient confidence.
