# CCA-F Concept Notebook

The numbered projects are runnable labs. This notebook is the single source of truth for reusable explanations, comparisons, exam traps, and links between labs.

## Learning map

| Topic | Primary note | Practical lab |
| --- | --- | --- |
| Delegation and orchestration | [Agent fundamentals](01-Agent-Fundamentals/orchestration.md) | [Project 1](../01-Agentic-Architecture/README.md) |
| Claude Code instructions | [Instruction locations](03-SDK-APIs-and-Terminology/claude-code-instruction-locations.md) | [Project 2](../02-Claude-Code/README.md) |
| Claude Code workflows | [Configuration, skills, and hooks](02-Claude-Code-Reference/configuration-skills-and-hooks.md) | [Project 2](../02-Claude-Code/README.md) |
| Agent SDK and headless CLI | [Agent SDK and CLI](03-SDK-APIs-and-Terminology/agent-sdk-and-cli.md) | [Projects 1–2](../01-Agentic-Architecture/README.md) |
| Schema validation and retries | [Validation boundary](06-Reliability-and-Security/validation-and-retries.md) | [Project 3](../03-Structured-Output/README.md) |
| Messages, tools, and batches | [Messages/tools/batches](06-Reliability-and-Security/messages-tools-batches.md) | [Project 3](../03-Structured-Output/README.md) |
| MCP primitives | [MCP tools, resources, prompts](05-Tool-Execution-and-Permissions/mcp-primitives.md) | [Project 4](../04-MCP-Integration/README.md) |
| MCP transport and security | [MCP architecture and security](05-Tool-Execution-and-Permissions/mcp-architecture-and-security.md) | [Project 4](../04-MCP-Integration/README.md) |
| Context and durable state | [Context vs persistence](04-Context-and-Sessions/context-vs-persistence.md) | [Project 5](../05-Context-Reliability/README.md) |
| Reliability and evaluation | [Prompt/context/evaluation](04-Context-and-Sessions/prompt-context-and-evaluation.md) | [Project 5](../05-Context-Reliability/README.md) |
| Exam recognition | [Comparisons and scenarios](07-Exam-Traps-and-Comparisons/comparisons-and-scenarios.md) | All projects |
| High-leverage terminology | [Vocabulary](08-Vocabulary-and-Mental-Models/high-leverage-vocabulary.md) | All projects |
| Session and filesystem isolation | [Conversation vs filesystem forks](08-Vocabulary-and-Mental-Models/conversation-vs-filesystem-forks.md) | Projects 1, 2, and 5 |

## How to add a learning item

1. Search this notebook and the relevant lab first.
2. Put implementation-specific learning next to its lab.
3. Put shared theory here and link back to the lab.
4. Record source-provided facts separately from verified documentation and your own inferences.

## Notebook rules

- One primary explanation per concept; link rather than duplicate.
- Include an exam clue, trade-off, and at least two self-check questions for meaningful concepts.
- Keep secrets, credentials, and private course material out of the notebook.
