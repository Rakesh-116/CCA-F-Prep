# MCP architecture and security

Last verified: 2026-11-22. Sources: [MCP Python SDK](https://py.sdk.modelcontextprotocol.io/) and [MCP specification changes](https://modelcontextprotocol.io/specification/draft/changelog).

An MCP host is the user-facing AI application. It owns one or more MCP clients. Each client connects to an MCP server exposing capabilities such as tools, resources, and prompts.

| Concern | Local stdio | Streamable HTTP |
| --- | --- | --- |
| Connection | host launches local subprocess | client connects over HTTP |
| Best fit | local developer integration | deployed/shared service |
| Main boundary | local process and inherited environment | network authentication, authorization, and transport security |
| Operational risk | stdout corruption or over-broad local permissions | exposed endpoint, tokens, headers, tenancy |

Use tool descriptions and input/output contracts for discoverability. Validate parameters server-side, paginate large responses, report progress where clients support it, and use idempotency/confirmation for effects. Separate read-only lookup tools from mutation tools and give each the least authority needed.

Version-sensitive correction: roots and sampling remain supported by some clients/SDKs but were deprecated by the 2026-07-28 MCP specification. New designs should prefer explicit tool parameters, resource URIs, server configuration, or direct provider calls. Do not build a new core workflow around a deprecated primitive without verifying client support.

Authentication and authorization belong to the transport/deployment design, not merely the tool description. A tool schema proves the input is shaped correctly; it does not prove the caller is entitled to use it.
