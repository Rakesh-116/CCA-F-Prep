# Context summarization versus durable task persistence

## Core distinction

Model context is the selected information sent with a model request. Durable persistence is application-managed state stored outside the model, such as SQLite task status and audit events.

| Concern | Context management | Durable persistence |
| --- | --- | --- |
| Purpose | Stay within a context budget | Resume reliably after interruption |
| Typical mechanism | trim and summarize | database/file/object store |
| Lossy? | Often yes | Should not be for required task state |
| Project 5 example | preserve `FACT:` and `DECISION:` messages | store task status and approval state in SQLite |

## Exam trap

Summarizing chat history does not make a task resumable. Recovery requires stored state, identifiers, and an audit trail.

## Self-check

1. Why should an approval state be persisted rather than left only in a conversation summary?  

### Answer

The process may restart or use a different model call; irreversible-action approval must remain auditable and enforceable.
