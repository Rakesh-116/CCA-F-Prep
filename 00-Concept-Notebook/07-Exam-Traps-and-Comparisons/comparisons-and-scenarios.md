# How to recognize the correct architecture in a CCA-F scenario

Last verified: 2026-11-22. These are exam-oriented architectural interpretations, not official exam questions.

## Fast comparisons

| Confused concepts | Choose the first when | Choose the second when |
| --- | --- | --- |
| User vs project vs local config | preference spans projects | team policy / personal project override |
| `CLAUDE.md` vs rules vs skills vs commands | always-needed context | path rule / reusable workflow / manual shortcut |
| Skill vs subagent | reuse instructions in current work | independent delegated task needs isolation |
| Standard subagent vs forked session | independent task can start fresh | branch prior conversation without undoing effects |
| PreToolUse vs PostToolUse | action must be stopped first | completed result must be audited/annotated |
| Sync vs async hook | decision must control execution | telemetry can lag |
| Prompt vs hook vs validator | guide model behavior | enforce action / enforce data rule |
| Glob vs grep | select files by path | find text inside files |
| Read vs Edit vs Write | inspect / targeted modification / create-or-replace content | grant minimum needed capability |
| `auto` vs `any` vs forced tool | optional tool | some tool required / exact tool required |
| Strict schema vs semantic validation | shape must conform | facts and business relations must hold |
| Messages vs batches | immediate interactive result | high-volume asynchronous workload |
| `result` vs `structured_output` | human-oriented response envelope | schema-constrained payload |
| `tool_use` vs `end_turn` | execute and return a tool result | finish the loop |
| Empty result vs tool error | query succeeded but found nothing | operation failed or could not run |
| Retryable vs non-retryable error | transient timeout/rate fault | invalid input, denied permission, unsafe effect |
| stdio vs Streamable HTTP | local subprocess | deployed/network service |
| MCP tools vs resources vs prompts | dynamic model call | static context / user workflow |
| Context isolation vs compaction | separate sensitive/task context | shorten an overlong context |
| Prompt caching vs context editing | reuse stable prefix cost | remove/transform context state |

## Scenario-to-solution map

| Scenario clue | Best direction | Why alternatives fail |
| --- | --- | --- |
| Dangerous tool must never execute | `PreToolUse` or authorization boundary | a prompt can be ignored |
| Tool output needs normalization | `PostToolUse` transformation/validation | pre-hook cannot see the result |
| Helper must not access refunds | least-privilege tool allowlist | a broad prompt does not remove the tool |
| Restore exact multi-tenant state | explicit persisted ID and resume flow | summary alone is lossy |
| Thousands of documents overnight | Message Batches plus `custom_id` | sync calls cost more operationally and block users |
| Operator waits for extraction | synchronous Messages API | batch has no immediate completion guarantee |
| JSON must follow a contract | structured output/schema | prompt-only JSON is weaker |
| Missing value must not be invented | nullable field plus evidence/uncertainty | required string pressures invention |
| Totals must equal line items | semantic cross-field validation | schema checks only shape |
| Search finds no records | successful empty result | do not call it a transport failure |
| Backend temporarily unavailable | timeout + bounded retry + backoff | retry forever creates cost and load |
| Long task has excessive output | select/summarize context and persist state | increasing output limit does not expand input context |
| Team shares MCP server config | committed project `.mcp.json` | user config is not portable |
| CI must ignore personal preferences | explicit `--setting-sources project` | user settings make builds non-reproducible |
| Required first lookup | force named tool once, then reset policy | forcing it forever repeats it unnecessarily |
| Local developer MCP server | stdio | HTTP adds an unnecessary network boundary |
| Mutation may duplicate on retry | idempotency key or human escalation | blind retries can repeat side effects |

## Remember this

Read the requirement word: “never” implies enforcement, “immediate” implies synchronous, “bulk” implies batch, and “exact state” implies persistence.
