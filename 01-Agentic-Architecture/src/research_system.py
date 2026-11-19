"""A small, observable coordinator/subagent research system.

It uses deterministic mock agents so the architecture can be exercised without
an API key. Replace ``MockSpecialist`` with a model-backed adapter later.
"""

from __future__ import annotations

import asyncio
import json
import time
from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Protocol


class AgentError(Exception):
    """A recoverable specialist failure."""


class Status(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    ESCALATED = "escalated"


@dataclass
class Finding:
    specialist: str
    claim: str
    sources: list[str]
    uncertainty: str


@dataclass
class ExecutionRecord:
    specialist: str
    status: Status
    attempts: int
    latency_ms: int
    token_estimate: int
    error: str | None = None


@dataclass
class ResearchReport:
    question: str
    findings: list[Finding]
    records: list[ExecutionRecord]
    status: Status
    total_latency_ms: int
    uncertainties: list[str] = field(default_factory=list)

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, default=str)


class Specialist(Protocol):
    name: str

    async def research(self, question: str) -> Finding:
        """Return a validated, structured finding or raise AgentError."""


class MockSpecialist:
    """Predictable specialist for demos and tests.

    failure_mode may be ``timeout``, ``error``, or ``malformed``.
    """

    def __init__(self, name: str, focus: str, failure_mode: str | None = None):
        self.name = name
        self.focus = focus
        self.failure_mode = failure_mode

    async def research(self, question: str) -> Finding:
        await asyncio.sleep(0.05)
        if self.failure_mode == "timeout":
            await asyncio.sleep(2)
        if self.failure_mode == "error":
            raise AgentError("simulated upstream API failure")
        if self.failure_mode == "malformed":
            raise AgentError("simulated malformed structured response")
        return Finding(
            specialist=self.name,
            claim=f"{self.focus} perspective on: {question}",
            sources=["Mock source — replace with cited retrieval results"],
            uncertainty="Mock data; no external research was performed.",
        )


class Coordinator:
    """Orchestrates independent tasks with timeout, retry, and escalation."""

    def __init__(self, specialists: list[Specialist], max_attempts: int = 2, timeout_s: float = 0.5):
        if max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")
        self.specialists = specialists
        self.max_attempts = max_attempts
        self.timeout_s = timeout_s

    async def _run_one(self, specialist: Specialist, question: str) -> tuple[Finding | None, ExecutionRecord]:
        started = time.perf_counter()
        last_error: str | None = None
        for attempt in range(1, self.max_attempts + 1):
            try:
                result = await asyncio.wait_for(specialist.research(question), timeout=self.timeout_s)
                if not result.claim or not result.sources:
                    raise AgentError("finding failed output validation")
                elapsed = int((time.perf_counter() - started) * 1000)
                return result, ExecutionRecord(specialist.name, Status.SUCCESS, attempt, elapsed, 150)
            except (AgentError, asyncio.TimeoutError) as error:
                last_error = "timeout" if isinstance(error, asyncio.TimeoutError) else str(error)
        elapsed = int((time.perf_counter() - started) * 1000)
        return None, ExecutionRecord(
            specialist.name, Status.ESCALATED, self.max_attempts, elapsed, 0, last_error
        )

    async def research(self, question: str, parallel: bool = True) -> ResearchReport:
        if not question.strip():
            raise ValueError("question cannot be empty")
        started = time.perf_counter()
        if parallel:
            results = await asyncio.gather(*(self._run_one(agent, question) for agent in self.specialists))
        else:
            results = []
            for agent in self.specialists:
                results.append(await self._run_one(agent, question))
        findings = [finding for finding, _ in results if finding]
        records = [record for _, record in results]
        failures = [r for r in records if r.status != Status.SUCCESS]
        return ResearchReport(
            question=question,
            findings=findings,
            records=records,
            status=Status.ESCALATED if failures else Status.SUCCESS,
            total_latency_ms=int((time.perf_counter() - started) * 1000),
            uncertainties=[f"{r.specialist}: {r.error}" for r in failures],
        )


async def demo() -> None:
    agents = [
        MockSpecialist("technical-researcher", "Technical"),
        MockSpecialist("business-analyst", "Business"),
    ]
    report = await Coordinator(agents).research(
        "Should a team adopt multi-agent research?",
        parallel=False,
    )
    print(report.to_json())


if __name__ == "__main__":
    asyncio.run(demo())
