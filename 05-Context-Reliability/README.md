# Project 5 — Reliable Long-Running Agent

This offline lab separates three concerns:

```text
Conversation → context budgeting → selected prompt context
Task state + audit history → SQLite persistence → recovery after interruption
High-impact action → human approval gate → bounded execution/retry
```

## Run

```powershell
python -m unittest discover -s tests -t . -v
```

## What to learn

- Context trimming is lossy: preserve explicit decisions and facts, not every turn.
- SQLite state survives process failure; a model context window does not.
- Retry transient faults only a limited number of times. Escalate on repeated failures.
- Any irreversible action needs a human approval transition recorded in the audit history.

## Exercises

1. Add a durable fact without the `FACT:` prefix and observe that it is not preserved during trimming.
2. Change `max_attempts` and explain the cost/reliability trade-off.
3. Create a task, instantiate a new `TaskStore` with the same database path, and resume it.
4. Add `delete_record` to a scenario and verify it cannot run without approval.

## Revision notes

See [context summarization versus durable persistence](../00-Concept-Notebook/04-Context-and-Sessions/context-vs-persistence.md).
