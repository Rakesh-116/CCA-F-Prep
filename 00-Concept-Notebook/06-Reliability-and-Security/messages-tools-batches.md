# Messages API, tool use, structured output, and batches

Last verified: 2026-11-22. Sources: [tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview), [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), and [batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing).

## Tool-use loop

`messages.create` receives `model`, `max_tokens`, and a conversation in `messages`. If Claude needs a client tool, the response has `stop_reason: "tool_use"` and one or more `tool_use` blocks. Execute each allowed tool, then return a `tool_result` that carries the matching `tool_use_id`.

```python
response = client.messages.create(model="MODEL", max_tokens=1024, tools=tools, messages=messages)
if response.stop_reason == "tool_use":
    calls = [block for block in response.content if block.type == "tool_use"]
    results = [run_safely(call) for call in calls]
    messages += [
        {"role": "assistant", "content": response.content},
        {"role": "user", "content": results},
    ]
else:
    final_response = response
```

Use `stop_reason`, not string matching in generated prose, to control the loop. A tool description helps selection; an `input_schema` shapes arguments; server-side validation protects the actual boundary.

| Choice | Meaning | Choose it when |
| --- | --- | --- |
| `tool_choice: auto` | model may call a tool or answer directly | normal conversational agent |
| `tool_choice: any` | model must choose an available tool | one of several retrieval paths is mandatory |
| Forced named tool | model must call one specific tool | required first lookup or authentication step |

Set `disable_parallel_tool_use` only when calls must serialize. After a forced first tool call, reset choice appropriately; leaving it forced can cause needless repeated calls.

## Structured and semantic validation

Use JSON Schema/strict structured output for syntax, field type, required fields, nullable values, enums, arrays, and nested objects. Use application validation for dates, totals, duplicate records, authorization, and factual evidence.

```json
{
  "type": "object",
  "properties": {
    "title": {"type": "string"},
    "date": {"type": ["string", "null"]},
    "location": {"type": ["string", "null"]},
    "attendees": {"type": "array", "items": {"type": "string"}}
  },
  "required": ["title", "date", "location", "attendees"],
  "additionalProperties": false
}
```

For an invitation with no stated date or location, return `null`, never a plausible invention. Schema-valid output still may be factually wrong; validate source evidence and business rules separately.

`is_error` on a tool result means the tool execution failed. An empty but valid search result is successful data, not an error. Transport/authentication failures happen outside the tool’s normal business-result contract.

## Messages versus batches

| API | Choose it when | Correlation rule |
| --- | --- | --- |
| Synchronous Messages API | user waits for a result or tool loop | response belongs to the current request |
| Message Batches API | large asynchronous workload, evaluation, lower-cost bulk processing | use each request’s unique `custom_id`, never result position |

Batches can return out of order and are not a streaming substitute. They suit overnight extraction, not an interactive operator. Batch requests are processed independently; record per-item errors and expiration/status separately.

## Remember this

Schema answers “is the shape usable?”; semantic validation answers “is the result safe and true enough to act on?”
