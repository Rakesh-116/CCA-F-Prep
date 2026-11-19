# Experiment log

| Experiment | Change | Observe | Result |
| --- | --- | --- | --- |
| Baseline | Two healthy specialists, parallel | report-level `total_latency_ms`, findings, records | Passed: 53 ms per agent; total metric added for the next run |
| Sequential comparison | Set `parallel=False` | report-level `total_latency_ms` | Run completed; record total metric after the instrumentation update |
| Timeout | Set a specialist to `timeout` | retry count and escalation | Automated test passes |
| Malformed output | Set a specialist to `malformed` | validation failure and escalation | Automated test passes |
| Contradiction | Replace mock claims with incompatible claims | merge/escalation policy | Planned |
