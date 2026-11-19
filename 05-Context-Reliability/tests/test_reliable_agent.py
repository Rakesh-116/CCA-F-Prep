import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from reliable_agent import ReliableAgent, TaskStore, manage_context


class ReliableAgentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.store = TaskStore(Path(self.temp.name) / "tasks.sqlite")
        self.store.create("task-1", {"goal": "publish mock report"})
        self.agent = ReliableAgent(self.store, max_attempts=2)

    def tearDown(self) -> None:
        self.store.close()
        self.temp.cleanup()

    def test_context_keeps_durable_information_when_trimmed(self) -> None:
        messages = ["FACT: Customer requires EU hosting", "small talk", "DECISION: Use mock data"] + [f"turn {n}" for n in range(7)]
        result = manage_context(messages, max_messages=3)
        self.assertTrue(result.trimmed)
        self.assertIn("EU hosting", result.summary)
        self.assertEqual(result.recent_messages, ["turn 4", "turn 5", "turn 6"])

    def test_irreversible_action_requires_approval(self) -> None:
        with self.assertRaises(PermissionError):
            self.agent.run_action("task-1", "publish_report", lambda: "published")
        self.assertIn("blocked_without_approval:publish_report", self.store.events("task-1"))

    def test_approved_task_can_complete(self) -> None:
        self.agent.request_approval("task-1", "publish_report")
        self.agent.approve("task-1")
        self.assertEqual(self.agent.run_action("task-1", "publish_report", lambda: "published"), "published")
        self.assertEqual(self.store.get("task-1")["status"], "completed")

    def test_repeated_failure_escalates(self) -> None:
        with self.assertRaises(RuntimeError):
            self.agent.run_action("task-1", "read_data", lambda: (_ for _ in ()).throw(RuntimeError("mock outage")))
        self.assertEqual(self.store.get("task-1")["status"], "escalated")
