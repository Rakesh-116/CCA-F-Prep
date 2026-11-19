# Reliable agent experiment log

| Experiment | How to run | Expected observation |
| --- | --- | --- |
| Long context | Run the context unit test | Old durable facts survive; ordinary older turns are trimmed. |
| Interruption/recovery | Reopen `TaskStore` against the same SQLite file | Task status and audit events persist outside model context. |
| Approval rejection | Call `run_action` before `approve` | Irreversible action is blocked and audited. |
| Repeated failures | Use an operation that raises `RuntimeError` | Fixed retries then `escalated`; no infinite loop. |

## Design note

SQLite persistence is application state, not model memory. A later model call must receive a deliberately selected summary and recent messages.
