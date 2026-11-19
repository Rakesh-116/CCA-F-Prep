"""Provider-neutral extraction, validation, retry, and audit boundary."""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from typing import Protocol

from pydantic import ValidationError

from models import InvoiceExtraction

SYSTEM_PROMPT = """You extract document facts. Return only JSON matching the supplied schema.
Use null when a value is absent or ambiguous. Do not infer values. For every non-null
business value, include evidence with the exact source excerpt and location."""


class ExtractorProvider(Protocol):
    def extract(self, document_text: str, schema: dict, system_prompt: str) -> tuple[str, int]:
        """Return raw JSON text and provider-reported total token usage."""


@dataclass
class AttemptLog:
    attempt: int
    valid: bool
    latency_ms: int
    token_usage: int
    error: str | None = None


@dataclass
class ExtractionResult:
    extraction: InvoiceExtraction | None
    attempts: list[AttemptLog]
    error: str | None = None


class ExtractionPipeline:
    def __init__(self, provider: ExtractorProvider, max_attempts: int = 2):
        if max_attempts < 1:
            raise ValueError("max_attempts must be at least one")
        self.provider = provider
        self.max_attempts = max_attempts

    def extract(self, document_text: str) -> ExtractionResult:
        if not document_text.strip():
            return ExtractionResult(None, [], "Input document is empty")
        logs: list[AttemptLog] = []
        schema = InvoiceExtraction.model_json_schema()
        for attempt in range(1, self.max_attempts + 1):
            started = time.perf_counter()
            try:
                raw_json, tokens = self.provider.extract(document_text, schema, SYSTEM_PROMPT)
                model = InvoiceExtraction.model_validate_json(raw_json)
                logs.append(AttemptLog(attempt, True, int((time.perf_counter() - started) * 1000), tokens))
                return ExtractionResult(model, logs)
            except (json.JSONDecodeError, ValidationError, ValueError) as error:
                logs.append(AttemptLog(attempt, False, int((time.perf_counter() - started) * 1000), 0, str(error)))
        return ExtractionResult(None, logs, "Validation failed after bounded retries; route for review")


class SequenceMockProvider:
    """Returns supplied responses in sequence, for repeatable experiments and tests."""

    def __init__(self, responses: list[str], token_usage: int = 100):
        self.responses = iter(responses)
        self.token_usage = token_usage

    def extract(self, document_text: str, schema: dict, system_prompt: str) -> tuple[str, int]:
        return next(self.responses), self.token_usage
