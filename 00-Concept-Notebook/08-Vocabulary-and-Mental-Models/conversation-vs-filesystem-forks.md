# Conversation forks versus filesystem isolation

Last verified: 2026-11-22. Sources: local `claude.cmd --help` (Claude Code 2.1.323) and [Claude Code cloud/session documentation](https://code.claude.com/docs/en/claude-code-on-the-web).

## The two meanings of “fork” solve different problems

| Concept | What is copied/branched | What is isolated | What is **not** isolated |
| --- | --- | --- | --- |
| Conversation/session fork | Conversation history branches into a new session ID. Local CLI: `--fork-session` with `--resume` or `--continue`. | Later chat turns and session identity. | Existing file edits, external API calls, sends, database writes, and repository state. |
| Filesystem isolation | A separate working directory, usually a Git worktree or isolated checkout. Local CLI: `--worktree`. | File changes, branch checkout, and many concurrent-edit conflicts. | External systems, shared credentials, remote APIs, and uncommitted work deliberately copied/shared by tooling. |
| Context-isolated subagent | Separate agent context window for a delegated task. | Its reasoning transcript and noisy exploration. | Shared filesystem unless you also give it a separate worktree; external effects from allowed tools. |

## Simple analogy

A conversation fork is a copied notebook: you can explore a different line of reasoning. A filesystem worktree is a separate desk with a separate copy of the project files. Neither is a time machine—an email sent or refund issued remains real.

## Execution patterns

```text
Resume + fork session:
  same prior conversation → new conversation branch → explore an alternative plan

Worktree:
  same repository → separate checkout/branch → implement concurrently without editing the same files

Both together:
  fork the reasoning AND use a worktree when the experiment will change files.
```

## When to choose each

| Need | Best choice |
| --- | --- |
| Try a different reasoning approach, no file changes | session fork |
| Run two code changes without overlapping files | separate worktrees |
| Investigate noisy logs without bloating main reasoning | context-isolated subagent |
| Separate two customers/tenants | explicit tenant-scoped state, authorization, and isolated storage—not merely a conversation fork |
| Test a risky irreversible integration | staging environment plus approval/idempotency controls |

## Common exam traps

- “Forking reverses previous changes.” False: it does not undo external side effects.
- “A subagent automatically gets a private filesystem.” False: context isolation and filesystem isolation are separate decisions.
- “`--continue` is safe for multi-tenant restoration.” Unsafe: use an explicit persisted session identifier and tenant authorization.
- “A larger context window removes the need for isolation.” False: isolation controls relevance and leakage boundaries, not just token capacity.

## Remember this

Fork conversation for alternate reasoning; isolate the filesystem for concurrent edits; use durable tenant state for security.
