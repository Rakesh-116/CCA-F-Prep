# Master CCA-F vocabulary and code terms

Last verified: 2026-11-23. This is the **single canonical glossary** for recurring English, architecture, configuration, CLI, SDK, API, MCP, validation, and reliability terms. The other notebook files provide deeper examples; this file is the place to look up what a term means.

## Architecture and control

| Term | Meaning | Exam signal / trap |
| --- | --- | --- |
| Deterministic | Same enforced rule gives the same outcome for matching inputs. | “Must never” needs code, authorization, or a blocking hook—not merely a prompt. |
| Probabilistic | Outcome is generated from likelihood, so it can vary. | An LLM instruction reduces risk; it does not guarantee prevention. |
| Least privilege | Give only the minimum required authority. | A helper that only reads should not inherit mutation tools. |
| Blast radius | Scope of damage if a change/action is wrong. | High-impact, broad change merits planning, review, or approval. |
| Observability | Ability to reconstruct behavior from logs, metrics, traces, and audit events. | Coordinator-mediated results are easier to inspect than hidden peer exchanges. |
| Fail closed / open | On guard failure, deny / allow the action. | Security-critical mutations favor carefully engineered fail-closed controls. |
| Hub-and-spoke | Coordinator routes tasks and merges worker results. | Prefer it when auditability and bounded responsibility matter. |
| Delegation | Handing a bounded task to another agent/component. | Delegate independent expertise; do not delegate trivial sequential edits. |
| Routing / misrouting | Selecting the right / wrong worker or tool. | Distinct descriptions and boundary conditions reduce misrouting. |
| Handoff | Passing task state and expectations to another actor. | Include goal, evidence, constraints, and remaining work. |
| Idempotency | Repeating an operation has the same net effect. | Needed before retrying a potentially completed payment/message mutation. |
| Irreversible side effect | External action not undone by changing chat/session history. | A session fork cannot reverse a refund, push, email, or deletion. |

## AI, context, and evaluation

| Term | Meaning | Exam signal / trap |
| --- | --- | --- |
| Calibration | Test whether stated confidence aligns with labeled-data accuracy. | Self-reported confidence is not a calibrated routing threshold. |
| Confirmation bias | Tendency to defend an earlier conclusion. | Independent review can catch errors an author misses. |
| Context rot / attention dilution | Quality degradation when irrelevant/noisy context dominates. | Larger context alone is not the fix; select, summarize, isolate. |
| Lossy | Compression drops detail. | Preserve IDs, versions, approvals, and entity links outside a summary. |
| Entity binding | Keep a value attached to the entity it belongs to. | `order_id → refund amount` must survive summarization. |
| Provenance | Evidence showing where a fact came from. | Preserve source quote/page/record so a reviewer can verify it. |
| Few-shot / multishot | Include representative input/output examples. | Useful for inconsistent formats; do not hardcode logic to examples. |
| Hallucination / fabrication | Plausible unsupported output. | Nullable fields and evidence prevent invented missing facts. |
| Over-triggering | Tool/agent activates when it should not. | Broad descriptions or aggressive instructions cause wasted actions. |
| Heuristic | Useful rule of thumb, not a guarantee. | Keyword-only security routing is brittle. |

## Data and reliability

| Term | Meaning | Exam signal / trap |
| --- | --- | --- |
| Syntactic validation | Checks shape/type/schema. | JSON Schema can accept a logically wrong total. |
| Semantic validation | Checks meaning/business truth. | Verify dates, totals, duplicates, policies, and evidence in code. |
| Normalization | Convert varied representations to a standard form. | Schema type alone does not normalize `$1,200` versus `1200 USD`. |
| Nullable | Field may explicitly be `null`. | Use for missing source facts instead of forcing fabrication. |
| Transient error | Temporary fault that may succeed later. | Retry with bounded backoff/jitter if safe. |
| Permanent error | Invalid input, denial, or unsupported request. | Retrying wastes cost; correct/escalate instead. |
| Empty result | Successful query with zero matches. | Do not confuse with a failed tool/transport. |
| Truncated | Output stopped due to token limit. | Check `stop_reason`; split work or increase output budget only when relevant. |
| Circuit breaker | Stops calls to a repeatedly failing dependency temporarily. | Protects capacity and enables graceful degradation. |
| Correlation ID | ID linking logs/events for one request or workflow. | Essential for tracing retries and human escalation. |

## Software and workflow

| Term | Meaning | Exam signal / trap |
| --- | --- | --- |
| Fixture / fixture factory | Reusable known test data / generator. | Enables repeatable tests without hand-building brittle objects. |
| Invariant | Fact/constraint that must remain true. | Save schema contracts and version constraints across long tasks. |
| Triage | Sort by risk/uncertainty for appropriate handling. | Human review focuses on borderline/high-impact cases. |
| Alert fatigue | Noisy warnings become ignored. | Disable or tune low-precision categories. |
| Barrel/wrapper module | Module re-exporting a public interface. | Read it before searching for exported aliases. |
| Precedence / shadowing | Which overlapping configuration/name wins. | Verify per-setting precedence; do not assume a universal override rule. |
| Stale read | Old file/context state after a change elsewhere. | Resume does not magically refresh prior file content. |
| Surgical edit | Minimal targeted change rather than full overwrite. | Reduces accidental loss and diff blast radius. |
| Synchronous / asynchronous | Wait now / submit and continue. | Interactive operator → sync; overnight backfill → batch/async. |
| SLA | Reliability or latency commitment. | No latency SLA means asynchronous completion may be acceptable. |

## Communication, software, and operations terms

| Term | Meaning | Exam signal / trap |
| --- | --- | --- |
| Rationale | The reason or justification for a decision. | An escalation should include rationale so a human does not repeat the investigation. |
| Prose | Ordinary sentences/paragraphs rather than bullets, tables, or code. | “Render as prose” is an output-format requirement, not a request for reasoning transparency. |
| Intermittent | Happens irregularly, not on every run. | Diagnose repeated conditions and probabilistic behavior; do not assume one passing run proves a fix. |
| Conventions | Team-agreed coding or workflow practices. | Put durable shared conventions in project instructions, not a private user file. |
| Module | A self-contained code file/package unit. | “Across 40 modules” means broad change scope and higher blast radius. |
| Prefix | Characters at the beginning of an identifier. | Validate an `ORD-` prefix in code/schema rules, not with a vague prompt alone. |
| Reconciliation | Compare and merge records into a consistent result. | Needed when multiple sources/agents may conflict. |
| Transcript | Full chronological record of a conversation or run. | Long raw transcripts cause context rot; preserve key decisions separately. |
| Verdict | Short final conclusion, such as pass/fail. | A verdict without evidence/provenance is weak for high-impact decisions. |
| Narrative | Story-like sequential explanation. | Do not confuse a narrative explanation with machine-verifiable structured output. |
| Isolation | Deliberate separation of context, files, tenants, or permissions. | State which boundary is isolated; context isolation alone does not isolate disk or external effects. |
| Blocking | Prevents later work until a check/action completes. | Use for a required safety gate; avoid for noncritical telemetry. |
| Fallback | Alternate option after primary option fails or is unavailable. | A fallback must still meet safety/quality requirements; it is not a silent bypass. |
| Backfill | Process historical backlog after a system/process changes. | Batch/asynchronous processing suits a large backfill. |
| Schema | Blueprint for allowed data fields and types. | Schema protects shape; semantic validation protects meaning. |
| Downstream | Component that receives an earlier component’s output. | Validate at the boundary before malformed data breaks a downstream parser. |
| Benchmark | Repeatable measurement of performance/cost/quality. | Compare architectures with the same workload and metrics. |
| Unhandled exception | Error that escapes normal error handling and crashes/fails a flow. | Return a structured tool error or escalate rather than letting the protocol loop collapse. |
| Drift | Gradual behavior change away from an intended baseline. | Detect with regression tests, fixtures, and monitored evaluations. |
| Diverge | Two environments or runs produce different outcomes. | Compare settings, instructions, dependencies, inputs, and permissions between local and CI. |
| Diagnostic | Investigation step for finding a cause. | First inspect actual loaded settings/context before changing architecture. |
| Telemetry | Automatically collected operational events, metrics, or traces. | Usually asynchronous; never use it as the only safety control. |
| Payload | Actual data body carried in a request/response/event. | Large noisy payloads should be trimmed or normalized before model context. |
| Crawl | Automated traversal of many files, links, or dependencies. | Bound scope/time; a full crawl may be unnecessary for a narrow question. |
| Ambiguity | More than one plausible interpretation. | Clarify or return uncertainty instead of choosing an unsupported meaning. |
| Escalation | Transfer to a human or higher-authority workflow. | Use after bounded retries, material uncertainty, or high-impact decisions. |
| Interoperability | Different systems work together through compatible interfaces/protocols. | MCP enables standardized host/client/server integration. |
| Boilerplate | Repetitive standard setup code. | Automate safely, but do not mistake repeated boilerplate for domain-specific logic. |
| Deprecate / deprecated | A feature is still available for now, but its use is discouraged and it may be removed later. | Do not design new systems around it; migrate to the documented replacement. Deprecated does **not** automatically mean broken today. |
| Deprecation | The lifecycle process of warning, migration, and eventual retirement of a feature. | Check version, announced replacement, and retirement date before answering migration questions. |
| Retired / removed | No longer supported or available. | Unlike deprecated behavior, existing code must be changed before it can rely on the feature. |
| Legacy | Older behavior/API retained for compatibility. | A legacy example may work but can be a poor choice for a new implementation. |

## Reading strategy

For each long scenario, identify: **guarantee vs preference**, **who waits**, **whether there is a side effect**, **where state must survive**, and **whether evidence is required**.

## Claude Code files, scopes, and configuration

| Term / path | What it is | Scope / exam meaning |
| --- | --- | --- |
| `~/.claude.json` | Claude Code user/application state configuration. | User machine; not a shared project-policy file. Treat internal fields as version-sensitive. |
| `~/.claude/CLAUDE.md` | Personal persistent instructions. | User scope across projects; not committed. |
| `./CLAUDE.md` | Shared project instructions. | Project scope; commit stable team conventions, architecture, and test commands. |
| `./.claude/CLAUDE.md` | Alternative project instruction location. | Same project purpose; do not assume only root `CLAUDE.md` is loaded. |
| Nested `CLAUDE.md` | Instructions in a repository subtree. | Narrower file-area guidance; relevant when work enters that subtree. |
| `CLAUDE.local.md` | Personal project-specific instructions. | Local scope; add to `.gitignore`. |
| `@path/to/file.md` | Instruction-file import. | Reuse stable shared guidance without duplicating it. |
| `.claude/rules/*.md` | Focused instruction rules. | Use YAML `paths:` to scope a rule to matching files. |
| `.claude/settings.json` | Project settings. | Shared only when intentionally committed; use for team configuration. |
| `~/.claude/settings.json` | User settings. | Personal defaults; explicitly exclude from CI with `--setting-sources`. |
| `.mcp.json` | Project MCP server configuration. | Share server definitions through Git; never embed secrets. |
| User/local MCP config | Per-user or local server configuration. | Suitable for personal integrations; not portable team infrastructure. |
| Precedence / shadowing | Which overlapping setting or name takes effect. | Check the documented precedence for that exact setting—do not assume user always overrides project. |
| `--setting-sources` | CLI selector for settings sources. | Makes CI reproducible by selecting `project`, instead of inheriting personal settings. |
| Allowlist / denylist | Explicit allowed/disallowed tools. | Least privilege is safer than relying only on instructions. |

## Skills, commands, agents, and hooks

| Term | What it is | Exam signal / trap |
| --- | --- | --- |
| `.claude/commands/` | Project custom slash-command location. | Best for a user-invoked shortcut, not autonomous routing. |
| `~/.claude/commands/` | User custom commands. | Personal; can differ from team/CI behavior. |
| `.claude/skills/<name>/SKILL.md` | Reusable skill instructions/resources. | Use for repeatable workflow knowledge, not a one-line shortcut. |
| `description` | Explains when a skill/agent/tool should be selected. | Precise boundaries reduce over-triggering and misrouting. |
| `allowed-tools` | Skill-level tool permission declaration. | Limits capability; it does not validate business correctness. |
| `argument-hint` | UI hint for expected slash-command/skill arguments. | Usability metadata, not input validation. |
| `user-invocable` | Whether a user can invoke a skill directly. | Separate from whether a model may invoke it automatically. |
| `disable-model-invocation` | Version-sensitive metadata intended to prevent model-triggered use. | Verify installed-version support before relying on it. |
| `context: fork` | Version-sensitive metadata for an isolated skill context. | Use for noisy/independent work; pass required facts explicitly. |
| Main context | Current conversation context. | Choose when the workflow needs immediate shared state. |
| Subagent | Delegated agent with its own task/context boundary. | Great for independent work; not automatically a separate filesystem. |
| Standard subagent | Fresh delegated worker. | Use for focused exploration/review with least-privilege tools. |
| Forked session | Branch of a prior conversation. | Preserves prior conversational state but never reverses external effects. |
| Explore agent | Read-only discovery worker. | Give Read/Grep, not Edit or mutation tools. |
| `PreToolUse` | Hook before a tool runs. | Deterministic place to block/approve/alter safe input where supported. |
| `PostToolUse` | Hook after a successful tool run. | Audit or normalize output; cannot prevent an already-completed side effect. |
| `SessionStart` / `SessionEnd` | Session lifecycle hooks. | Load approved state / record audit completion. |
| `Stop` | Hook near completion. | Require a final verification step. |
| `SubagentStart` / `SubagentStop` | Delegation lifecycle hooks. | Capture work assignment and results for observability. |
| `Notification` | Hook event for a notification. | Route/log a notification; it is not a security boundary. |
| Matcher | Hook filter deciding which event/tool calls trigger. | Scope carefully to avoid blocking unrelated work. |
| `tool_name`, `tool_input`, `tool_response` | Hook event data. | Inspect tool identity, arguments, and post-run result. |
| `decision`, `reason` | Hook decision/control fields. | Event-specific; verify schema and explain denial clearly. |
| `updatedInput`, `updatedToolOutput` | Possible hook transformations. | Version/event-specific; validate exact support before using. |
| `async` | Hook can run without blocking the main flow. | Use for telemetry, not for a guard that must decide before execution. |
| `onFailure` | Hook failure behavior configuration. | Security guardrails often need deliberate fail-closed design. |
| `hookSpecificOutput` | Event-specific structured hook output. | Do not invent fields; check current hook reference. |

## Claude Code CLI and session terms

| Term / flag | What it is | When to choose it |
| --- | --- | --- |
| `claude` | Starts an interactive Claude Code session. | Human-supervised exploration and implementation. |
| `claude -p` / `--print` | Headless response then exit. | CI, scripts, and pipelines; use only trusted workspaces. |
| `--output-format json` | One JSON response envelope. | Machine consumption of result, metadata, and session information. |
| `--output-format stream-json` | Event stream in JSON. | Real-time progress/event consumers. |
| `--json-schema` | Schema-constrained structured output in print mode. | Downstream automation needs defined fields. |
| `result` | Human-oriented result field in a CLI JSON envelope. | Do not assume it is schema-constrained data. |
| `structured_output` | Structured payload when the relevant output-schema mode provides it. | Consume it rather than parsing prose; verify exact envelope fields for your version. |
| `--max-turns` | Limits agentic turns in headless mode. | Bound cost/loop length; not the same as retry count or token limit. |
| `maxTurns` | Likely SDK-style equivalent spelling. | Version-sensitive; verify language SDK documentation. |
| `--resume` | Resume a named/specific session. | Restore a known session; use explicit ID for tenant-sensitive work. |
| `--continue` | Resume the most recent local session. | Personal local continuation; avoid for multi-tenant exact-state restoration. |
| `--fork-session` | Resume into a new conversation ID. | Try alternative reasoning without overwriting the original session. |
| `--worktree` | Create/use separate Git working tree. | Parallel code changes without file conflicts. |
| Plan mode | Permission mode that plans rather than directly edits. | High-blast-radius or unclear changes. |
| Direct execution | Normal implementation behavior with approved permissions. | Small, clearly scoped, reversible work. |
| `/compact` | Summarizes/reduces session context. | Manage context; preserve IDs/invariants elsewhere because it is lossy. |
| `cwd` | Current working directory supplied to a session/SDK. | Defines local filesystem/project context. |
| `permissionMode` | SDK-style session permission control. | Version-sensitive spelling; principle is to choose least authority. |
| `allowedTools` / `disallowedTools` | SDK-style tool restrictions. | Prefer narrow allowlists for sensitive agents. |
| `session_id` | Durable identifier for a conversation/session. | Explicit resume, correlation, and tenant separation. |

## Messages API and tool-use terms

| Term | What it is | Exam signal / trap |
| --- | --- | --- |
| `messages.create` | Messages API call that generates the next assistant response. | Requires model, output limit, and conversation input. |
| `messages` | Ordered prior user/assistant turns. | Conversation state you explicitly send; not magic long-term memory. |
| `model` | Selected model identifier. | Choose capability/cost/latency fit; model availability is version/account dependent. |
| `max_tokens` | Maximum generated output tokens. | Does not increase input context capacity. |
| `stop_reason` | API reason the response stopped. | Use it to control loops, never a prose sentinel phrase. |
| `tool_use` | Assistant content block requesting a client tool call. | Run only allowed validated tools. |
| `tool_result` | Content block returned after tool execution. | Must match the requested call using `tool_use_id`. |
| `tool_use_id` | Identifier binding a result to a specific tool call. | Essential with parallel or repeated calls. |
| `tool_choice` | Policy controlling whether/how Claude selects tools. | `auto` optional; `any` requires some tool; forced requires one named tool. |
| `disable_parallel_tool_use` | Restricts parallel tool-call behavior. | Use only for genuine ordering/side-effect dependencies. |
| `input_schema` | JSON Schema describing tool arguments. | Shapes model arguments; server still validates inputs. |
| `strict: true` | Strict tool/schema conformance feature where supported. | Structural validity only, not truth/business validity. |
| `is_error` / `isError` | Error indicator naming varies by protocol/SDK object. | Check the specific API surface; do not assume casing transfers. |
| Forced tool selection | Require a specific initial tool. | Reset afterward or it may force needless future calls. |
| Sentinel phrase | Magic generated text used to end a loop. | Fragile anti-pattern; use `stop_reason`. |

## Structured output, batches, and context terms

| Term | What it is | Exam signal / trap |
| --- | --- | --- |
| JSON Schema | Machine-readable shape contract. | Controls valid fields/types, not factual accuracy. |
| Required field | Must be present. | Make missing source data nullable if absence is legitimate. |
| Optional field | May be omitted by schema. | Different from a required-but-nullable field. |
| Nullable field | Explicitly permits `null`, e.g. `"type": ["string", "null"]`. | Use when a document may not state the fact. |
| Enum | Finite allowed set of values. | Avoid options differing only in capitalization when provider behavior warns about casing. |
| Cross-field validation | Validates relationships across fields. | `sum(line_items) == total` is semantic, not just schema validation. |
| Validation-retry loop | Validate output, retry recoverable failure, then escalate. | Bound attempts to avoid runaway cost. |
| Message Batches API | Asynchronous bulk Messages processing. | Use for overnight/backfill/high volume, not immediate UI response. |
| `custom_id` | Developer-provided batch item correlation ID. | Match out-of-order results by ID, never position. |
| Batch status/result retrieval | Poll/obtain asynchronous batch outcomes. | Handle each item’s success/error independently. |
| Context window | Maximum model input/output capacity for a request. | Bigger window does not remove relevance/attention problems. |
| Token budget | Deliberate allocation of context/output/tool work. | Bound cost and ensure key facts fit. |
| Prompt caching / `cache_control` | Reuse stable prompt prefixes. | Reduces repeated processing cost; does not shrink context. |
| Context editing | Server/provider mechanism to manage accumulated context. | Different from cache reuse and application persistence. |
| Scratchpad | External file/state used to preserve exact facts. | Store invariants, IDs, and decisions across compaction. |

## MCP and production engineering terms

| Term | What it is | Exam signal / trap |
| --- | --- | --- |
| MCP host | User-facing application coordinating MCP clients. | Claude Code can be a host. |
| MCP client | Host component that speaks MCP to a server. | A host can have multiple clients/servers. |
| MCP server | Process exposing MCP capabilities. | Validate and authorize at this boundary. |
| MCP tool | Model-controlled dynamic operation. | `get_leave_balance(employee_id)` is a tool. |
| MCP resource | Application-controlled read-only context. | A static policy document is a resource. |
| MCP prompt | User-selected reusable workflow template. | Not a server-side action by itself. |
| stdio transport | Host launches local subprocess and exchanges protocol over standard streams. | Good local boundary; avoid printing protocol-corrupting data to stdout. |
| Streamable HTTP | Network HTTP transport for deployed/shared server. | Requires authentication, authorization, and network security. |
| Tool discovery | Client lists server tools/capabilities. | Descriptions/schemas affect usability and routing. |
| Pagination | Return large result sets in chunks. | Avoid context overload and preserve performance. |
| Tool annotation | Metadata describing tool behavior/risk. | Helpful context, not a substitute for authorization. |
| Roots / sampling | Historical MCP capabilities for workspace roots/client-model calls. | New MCP designs should verify current support; these are deprecated in the 2026-07-28 specification. |
| Elicitation | Server requests structured user input through a capable client. | Requires user interaction; not an invisible automation shortcut. |
| Timeout | Maximum wait before treating operation as failed. | Combine with safe retry/fallback policy. |
| Exponential backoff + jitter | Increasing delayed retries plus randomness. | Reduces retry storms for transient failures. |
| Graceful degradation | Provide a safe reduced service when dependency fails. | Better than hallucinating success or retrying forever. |

## Related deep-dive notes

- For the detailed distinction between conversation and filesystem forks, read [Conversation vs filesystem forks](conversation-vs-filesystem-forks.md).
- For scenario comparisons, read [How to recognize the correct architecture](../07-Exam-Traps-and-Comparisons/comparisons-and-scenarios.md).
- For exact current CLI syntax, use [Agent SDK and CLI](../03-SDK-APIs-and-Terminology/agent-sdk-and-cli.md).
