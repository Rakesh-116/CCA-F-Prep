# Claude Code configuration, skills, and hooks

Last verified: 2026-11-22. Official sources: [memory](https://code.claude.com/docs/en/memory) and [hooks](https://code.claude.com/docs/en/hooks).

## Scope: user, project, and local

| Item | Location | Scope / Git sharing | Choose it when | Exam trap |
| --- | --- | --- | --- | --- |
| User instructions | `~/.claude/CLAUDE.md` | all local projects / do not commit | personal conventions | not a team policy |
| Project instructions | `./CLAUDE.md` or `./.claude/CLAUDE.md` | repository / commit | stable team architecture and commands | it is not a secret store |
| Local instructions | `./CLAUDE.local.md` | one local checkout / gitignore | sandbox URL or local test data | not shared project guidance |
| Rules | `.claude/rules/*.md` | repository / commit | focused, optionally path-scoped rules | not a replacement for a task workflow |
| Project settings | `.claude/settings.json` | repository when intentionally shared | approved team configuration | do not assume user settings are present in CI |
| User settings | `~/.claude/settings.json` | one user / not committed | personal defaults | can make a local run differ from CI |
| MCP config | `.mcp.json` | project when committed | a shared server definition | never place a real secret in it |

`~/.claude.json` is an application-managed user configuration file, not the normal place to author shared repository policy. Treat its internal shape as implementation-managed unless the active Claude Code version documents the field you need.

### Rules and imports

Use `@relative/path.md` in a `CLAUDE.md` file to import stable, relevant instructions. Use `.claude/rules/*.md` when a rule only applies to a subset of files; YAML frontmatter can scope a rule with `paths:`. Keep project instructions concise—large always-loaded context competes with the task itself.

```yaml
---
paths:
  - "src/**/*.py"
---
Run the unit tests after changing Python behavior.
```

## Skills, commands, and subagents

| Mechanism | Best for | Trigger | Context |
| --- | --- | --- | --- |
| Command | a user-invoked shortcut | user selects `/name` | main session |
| Skill | reusable task knowledge/workflow | user or model, depending on metadata | main or forked context |
| Subagent | independent delegated work | coordinator/model | isolated agent context |

A skill lives at `.claude/skills/<name>/SKILL.md`; user skills live under `~/.claude/skills/`. A command is typically a lightweight user shortcut, while a skill carries instructions and supporting resources. Use a subagent when independent exploration benefits from isolation; use a main-context skill when the result must immediately share current task state.

Illustrative metadata—verify supported fields in the installed Claude Code version before copying:

```yaml
---
description: Review a Python change using the project test command.
allowed-tools: Read, Grep, Bash(python -m unittest:*)
argument-hint: "[file-or-feature]"
user-invocable: true
---
```

Fields such as `context: fork` and `disable-model-invocation` are version-specific skill metadata. The architectural lesson is stable: use a fork for isolated research, and expose a workflow to the model only when automatic invocation is safe and useful.

## Hooks: deterministic guardrails

Hooks run at lifecycle events and can inspect structured context. Prompt instructions influence behavior; hooks can enforce a decision.

| Event | Timing | Appropriate guardrail |
| --- | --- | --- |
| `SessionStart` / `SessionEnd` | session lifecycle | load environment context / audit completion |
| `PreToolUse` | before execution | block production mutations or rewrite safe input where supported |
| `PostToolUse` | after success | audit, validate, or annotate output |
| `PostToolUseFailure` | after tool failure | classify retryable failures |
| `Stop` | before completion | require final verification |
| `SubagentStart` / `SubagentStop` | delegated-work lifecycle | capture delegation audit data |
| `Notification` | notification emitted | route notifications |

For a tool invocation, a hook can receive fields such as `tool_name`, `tool_input`, and (post-execution) `tool_response`. Decision output is event-specific; fields such as `decision`, `reason`, `updatedInput`, `updatedToolOutput`, `async`, `onFailure`, and `hookSpecificOutput` must be checked against the installed hook schema before production use.

### Conceptual guardrails

```text
PreToolUse: if a database mutation targets production, deny with a reason.
PreToolUse: allow file edits only under the workspace root.
PostToolUse: log tool name, correlation ID, status, and latency.
PostToolUse: normalize a known noisy MCP response before later reasoning.
```

Run security checks synchronously when their result must control execution. Use asynchronous hooks for non-blocking telemetry. “Fail open” favors availability; “fail closed” is appropriate for a high-impact denied action only when the guardrail itself is reliable.

## Remember this

Instructions guide; hooks enforce; application code validates business correctness.
