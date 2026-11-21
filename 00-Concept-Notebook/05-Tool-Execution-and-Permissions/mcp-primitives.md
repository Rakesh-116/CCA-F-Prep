# MCP tools, resources, and prompts

## Simple explanation

MCP standardizes the connection between an AI host and external capabilities. The host application contains the MCP client; the server exposes tools, resources, and prompts.

| Primitive | Controlled by | Best use | Project 4 example |
| --- | --- | --- | --- |
| Tool | Model | Dynamic query/action with arguments | `get_leave_balance(employee_id)` |
| Resource | Application | Read-only contextual content | `policy://leave` |
| Prompt | User | Reusable guided workflow | `prepare_leave_summary` |

## Local flow

```text
Claude Code host → MCP client → stdio → mock employee server → mock data
```

For local servers, stdio keeps the server as a subprocess rather than exposing a network listener. Streamable HTTP is a deployment transport, not an automatic upgrade.

## Exam trap

A read-only policy document is a resource, not a tool. A lookup dependent on an employee ID is a tool, not a static resource.

## Self-check

1. Which component owns user interaction and may contain several MCP clients?  
2. Why validate a tool argument even when its schema appears in a client UI?

### Answers

1. The MCP host.  
2. Clients can be buggy or malicious; servers validate at their trust boundary.
