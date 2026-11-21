# Project 4 — Mock Employee MCP Server

This local lab demonstrates MCP without API keys or real employee data.

```text
Claude Code (host) → MCP client → stdio → employee_server.py → mock data
```

## What is exposed

- Tools: `get_employee_details(employee_id)`, `get_leave_balance(employee_id)`
- Resource: `policy://leave`
- Prompt: `prepare_leave_summary(employee_id)`

Tools are model-controlled actions/queries. Resources are read-only context. Prompts are user-selected workflows.

## Test the server logic

```powershell
python -m unittest discover -s tests -t . -v
```

## Inspect the real MCP protocol

From this directory, run:

```powershell
mcp dev server/employee_server.py
```

The Inspector opens a UI. List tools, call `get_leave_balance` with `EMP-101`, read `policy://leave`, then render the `prepare_leave_summary` prompt.

## Connect with Claude Code

Start Claude Code from this project and supply the config:

```powershell
claude.cmd --mcp-config client/.mcp.json
```

Ask: `What is the mock leave balance for EMP-101?` Approve the tool invocation only after confirming the tool name and arguments. If running from another working directory, make the server path in `.mcp.json` absolute.

## Experiments

1. Call each tool with a valid ID.
2. Try `EMP-999` and `101`; inspect the structured tool errors.
3. Stop the server and observe the host's unavailable-tool failure.
4. Compare the tool, resource, and prompt in Inspector.
5. Later, change `mcp.run()` to Streamable HTTP only after understanding why local stdio is the smaller security boundary.

## Revision notes

See [MCP tools, resources, and prompts](../00-Concept-Notebook/05-Tool-Execution-and-Permissions/mcp-primitives.md).
