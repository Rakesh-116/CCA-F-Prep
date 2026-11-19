# Project 2 — Claude Code Development and CI/CD Automation

This lab configures a small Python repository so Claude Code has explicit team instructions, a reproducible test command, and safe automation boundaries.

## First exercise: project context

Start Claude Code from this folder:

```powershell
claude
```

In the interactive session, run `/memory` and confirm that `CLAUDE.md` is listed. Then ask:

```text
Describe this repository's architecture, mandatory test command, and actions that require approval. Do not modify files.
```

Claude Code should use the repository's `CLAUDE.md` as project context. Verify the answer against the file rather than assuming it loaded correctly.

## Baseline verification

```powershell
python -m unittest discover -s tests -t . -v
```

## Instruction scope

| Location | Scope | Appropriate content |
| --- | --- | --- |
| `./CLAUDE.md` | This repository and collaborators | architecture, test commands, team safety rules |
| `~/.claude/CLAUDE.md` | Your local Claude Code sessions | personal preferences that should not be committed |

Project instructions are version controlled and are the shared source of truth. User-level instructions are personal and must not override a repository's safety or delivery constraints.

## Next increments

1. Validate project context interactively.
2. Add a project slash command for a test-first plan.
3. Add a narrowly scoped validation hook.
4. Add a review-only GitHub Actions workflow with bounded agent turns and least privilege.
