# Project 3 — Structured Data Extraction

An offline-first document extraction lab. The pipeline validates model-shaped JSON before downstream use and preserves evidence and uncertainty.

## Run

```powershell
python -m unittest discover -s tests -t . -v
```

## Architecture

```text
Document text/PDF adapter → extraction provider → JSON response
     → Pydantic validation → retry or structured failure → audit result
```

## Key files

- `src/models.py`: canonical Pydantic extraction model.
- `src/extraction_pipeline.py`: provider-neutral validation, retry, and logging boundary.
- `samples/invoice.txt`: mock document input.
- `tests/`: valid, invalid-then-valid, and retry-exhaustion cases.

## Revision notes

See [structured validation and retries](../00-Concept-Notebook/06-Reliability-and-Security/validation-and-retries.md). The practical schema is deliberately separate from a provider adapter so application validation remains enforceable.
