# Claude Agent SDK and Claude Code CLI

Last verified: 2026-11-22. CLI flags below were checked with local `claude.cmd --help` (Claude Code 2.1.323). API references must be rechecked against the installed Agent SDK version before use.

## CLI execution modes

| Mode | Command shape | Choose it when | Exam trap |
| --- | --- | --- | --- |
| Interactive | `claude` | human supervision and iterative work | not appropriate for unattended CI |
| Headless | `claude -p "..."` | scripts and CI | workspace-trust dialogue is skipped; use trusted directories only |
| JSON envelope | `-p --output-format json` | one machine-readable result envelope | `result` is not automatically schema-constrained |
| JSON stream | `-p --output-format stream-json` | event-by-event automation | consumer must handle several event types |
| Schema-constrained output | `-p --json-schema '<schema>'` | a defined output contract | schema validity is not semantic correctness |

Current CLI flags include `--setting-sources user,project,local`, `--resume`, `--continue`, `--fork-session`, `--max-turns`, `--permission-mode plan`, `--allowedTools`, `--disallowedTools`, `--mcp-config`, and `--strict-mcp-config`. In CI, explicitly choose setting sources and tool permissions so a developer’s personal configuration cannot silently change behavior.

```powershell
claude.cmd -p "Review only; do not edit files." `
  --setting-sources project `
  --allowedTools "Read,Grep,Bash(python -m unittest:*)" `
  --max-turns 5 `
  --output-format json
```

`/compact` or automatic compaction reduces conversation context; it does not enlarge the model context window. Raising output limits also does not cure input-context overflow.

## Custom agents and delegated work

The local CLI supports `--agents` with a JSON object whose minimal documented example has `description` and `prompt`. Descriptions matter because they tell the coordinator when an agent is appropriate.

```json
{
  "security-reviewer": {
    "description": "Reviews Python changes for unsafe file or network operations.",
    "prompt": "Review only. Do not edit. Report findings with file paths."
  }
}
```

| Agent role | Least-privilege tools | Why |
| --- | --- | --- |
| Explorer | read/search only | discover architecture without edits |
| Code generator | read/edit/test in a workspace | implement a bounded task |
| Documentation researcher | read/web fetch only | return cited findings |
| Security reviewer | read/search only | prevent review from becoming an unreviewed change |

Standard subagents should receive only task-relevant context and return a concise result to their coordinator. Forking a session creates a different conversation branch; it does **not** undo file writes, messages, or other external side effects. Parallel workers should use isolated worktrees or non-overlapping files to avoid filesystem conflicts.

## Version-sensitive Agent SDK names

The supplied material names `AgentDefinition`, `query()`, `ResultMessage`, `maxTurns`, `permissionMode`, `settingSources`, `forkSession`, and `disallowedTools`. These are plausible JavaScript/TypeScript SDK-style names, but they are not documented by the repository’s installed Python labs and the public Agent SDK overview did not expose a machine-readable API reference during this review. Treat exact casing and availability as **verify-before-use**. The stable design principles are: set a model and turn budget, limit tools, choose a working directory, persist a session ID when resumption is required, and isolate sensitive tenants.

## Remember this

Headless mode changes interaction, not safety: constrain settings, tools, turns, and output explicitly.
