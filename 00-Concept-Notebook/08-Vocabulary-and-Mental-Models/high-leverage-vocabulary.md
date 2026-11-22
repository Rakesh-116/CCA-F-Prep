# High-leverage CCA-F vocabulary

Last verified: 2026-11-22. These definitions are exam-study explanations; use the linked implementation notes for version-specific API behavior.

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

## Reading strategy

For each long scenario, identify: **guarantee vs preference**, **who waits**, **whether there is a side effect**, **where state must survive**, and **whether evidence is required**.
