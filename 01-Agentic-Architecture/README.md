# Project 1 — Multi-Agent Research System

An offline-first lab for studying coordinator/subagent orchestration before connecting a live model provider.

## Architecture

```text
Research question
       |
  Coordinator -- parallel or sequential --> Technical specialist
       |                                  --> Business specialist
       v
validate + bounded retry + timeout
       |
Merged report, metrics, uncertainty, or human escalation
```

The coordinator owns control flow. Specialists return a small structured finding; they do not delegate further, which bounds the agent loop.

## Run the baseline

From this directory:

```powershell
python src/research_system.py
python -m unittest discover -s tests -t . -v
```

No dependency or API key is required. The demo deliberately uses mock findings and labels them as such; it must not be treated as real research.

## First experiments

1. Run the baseline and inspect the report's records.
2. Change `parallel=True` to `False` in `demo()` and compare latency.
3. Give one specialist `failure_mode="error"`, `"timeout"`, or `"malformed"`.
4. Explain why the coordinator escalates after a bounded number of attempts rather than retrying indefinitely.

## What this demonstrates

| Concern | Design choice |
| --- | --- |
| Independent work | `asyncio.gather` runs specialists concurrently. |
| Dependent work | `parallel=False` processes specialists in order. |
| Failure safety | Each call has a timeout and fixed retry budget. |
| Observability | Per-specialist status, attempt count, latency, and token estimate are recorded. |
| Uncertainty | Results and escalations retain uncertainty rather than inventing an answer. |

## Next increment

Replace `MockSpecialist` with a model-backed adapter only after this baseline is understood. The adapter should validate model JSON at the application boundary, capture provider usage from the response, and cite only retrieved sources.
