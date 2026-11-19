import asyncio
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from research_system import Coordinator, MockSpecialist, Status


class CoordinatorTests(unittest.TestCase):
    def test_parallel_coordinator_merges_two_findings(self):
        agents = [MockSpecialist("technical", "Technical"), MockSpecialist("business", "Business")]
        report = asyncio.run(Coordinator(agents).research("Evaluate option A"))
        self.assertEqual(report.status, Status.SUCCESS)
        self.assertEqual(len(report.findings), 2)
        self.assertTrue(all(record.attempts == 1 for record in report.records))
        self.assertLess(report.total_latency_ms, 100)

    def test_timeout_is_retried_then_escalated(self):
        report = asyncio.run(
            Coordinator([MockSpecialist("slow", "Technical", "timeout")], max_attempts=2, timeout_s=0.01)
            .research("Evaluate option A")
        )
        self.assertEqual(report.status, Status.ESCALATED)
        self.assertEqual(report.records[0].attempts, 2)
        self.assertEqual(report.records[0].error, "timeout")

    def test_malformed_output_is_escalated(self):
        report = asyncio.run(
            Coordinator([MockSpecialist("broken", "Technical", "malformed")], max_attempts=1).research("Evaluate option A")
        )
        self.assertEqual(report.status, Status.ESCALATED)
        self.assertIn("malformed", report.uncertainties[0])
