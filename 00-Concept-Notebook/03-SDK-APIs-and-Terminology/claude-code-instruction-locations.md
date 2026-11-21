# Claude Code instruction locations and hierarchy

## Actual repository inventory — 22 November 2026

| Level | Path | Present? | Purpose |
| --- | --- | --- | --- |
| Workspace root | `C:\Users\RakeshPenugonda\Desktop\Blend360\Claude Certified Archiect Foundations Prep\CLAUDE.md` | No | Shared guidance for every lab, if later needed. |
| Project 1 | `...\01-Agentic-Architecture\CLAUDE.md` | No | Would apply to the agentic-architecture lab. |
| Project 2 | `...\02-Claude-Code\CLAUDE.md` | **Yes** | Shared Python, testing, workflow, and safety guidance for Project 2. |
| Project 3 | `...\03-Structured-Output\CLAUDE.md` | No | Would apply to the structured-extraction lab. |
| Project 4 | `...\04-MCP-Integration\CLAUDE.md` | No | Would apply to the MCP lab. |
| Project 5 | `...\05-Context-Reliability\CLAUDE.md` | No | Would apply to the reliability lab. |
| User level | `%USERPROFILE%\.claude\CLAUDE.md` | Not inspected | Optional personal instructions across local projects; do not commit it. |

Only the Project 2 file exists in this repository today. This table is an inventory, not evidence that a user-level file exists.

## Simple explanation

`CLAUDE.md` is persistent, human-written context for Claude Code. Project files capture team rules such as architecture, commands, and safety boundaries. A user-level file is for private preferences.

## How project discovery works

Claude Code can discover `CLAUDE.md` files from the working directory upward. A nested instruction file becomes relevant when working in that subtree. Use `/memory` in a Claude Code session to inspect loaded memory instead of guessing.

## Comparison

| Mechanism | Scope | Version controlled? | Appropriate use |
| --- | --- | --- | --- |
| Root `CLAUDE.md` | Whole repository | Usually yes | shared cross-project conventions |
| Project `CLAUDE.md` | One lab/subtree | Yes | commands and architecture unique to that lab |
| User `~/.claude/CLAUDE.md` | Personal local sessions | No | editor and personal workflow preferences |
| Prompt | Current request | No | task-specific outcome and constraints |

## Exam perspective

Clues such as “all contributors must follow this test command” indicate a project instruction file. “My preferred response style across repositories” indicates user-level configuration. Do not put credentials or secrets in either file.

## Self-check

1. Where should a command shared only by the MCP lab be recorded?  
2. Why is `/memory` more reliable than assuming an instruction file loaded?

### Answers

1. `04-MCP-Integration/CLAUDE.md` if the command is stable and shared by that lab.  
2. It reports what the active Claude Code session actually loaded.
