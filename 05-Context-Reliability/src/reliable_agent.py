"""Offline-first reference implementation of context and task reliability."""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


IRREVERSIBLE_ACTIONS = {"delete_record", "send_message", "publish_report"}


@dataclass
class ContextWindow:
    summary: str
    recent_messages: list[str]
    trimmed: bool


def manage_context(messages: list[str], max_messages: int = 6) -> ContextWindow:
    """Keep explicit decisions/facts plus the newest conversation turns."""
    if len(messages) <= max_messages:
        return ContextWindow("", messages, False)
    preserved = [m for m in messages[:-max_messages] if m.startswith(("DECISION:", "FACT:", "APPROVAL:"))]
    summary = "Preserved history:\n" + "\n".join(preserved) if preserved else "Earlier conversation was summarized; no durable facts were marked."
    return ContextWindow(summary, messages[-max_messages:], True)


class TaskStore:
    def __init__(self, database_path: str | Path):
        self.connection = sqlite3.connect(database_path)
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS tasks (task_id TEXT PRIMARY KEY, status TEXT, payload TEXT, approval TEXT)"
        )
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS events (task_id TEXT, event TEXT)"
        )
        self.connection.commit()

    def create(self, task_id: str, payload: dict) -> None:
        self.connection.execute("INSERT INTO tasks VALUES (?, ?, ?, ?)", (task_id, "pending", json.dumps(payload), "none"))
        self.event(task_id, "created")
        self.connection.commit()

    def get(self, task_id: str) -> dict:
        row = self.connection.execute("SELECT status, payload, approval FROM tasks WHERE task_id = ?", (task_id,)).fetchone()
        if row is None:
            raise KeyError(task_id)
        return {"task_id": task_id, "status": row[0], "payload": json.loads(row[1]), "approval": row[2]}

    def update(self, task_id: str, status: str, approval: str | None = None) -> None:
        if approval is None:
            self.connection.execute("UPDATE tasks SET status = ? WHERE task_id = ?", (status, task_id))
        else:
            self.connection.execute("UPDATE tasks SET status = ?, approval = ? WHERE task_id = ?", (status, approval, task_id))
        self.connection.commit()

    def event(self, task_id: str, event: str) -> None:
        self.connection.execute("INSERT INTO events VALUES (?, ?)", (task_id, event))
        self.connection.commit()

    def events(self, task_id: str) -> list[str]:
        return [row[0] for row in self.connection.execute("SELECT event FROM events WHERE task_id = ?", (task_id,))]

    def close(self) -> None:
        """Release the database handle, especially important on Windows."""
        self.connection.close()


class ReliableAgent:
    def __init__(self, store: TaskStore, max_attempts: int = 3):
        self.store = store
        self.max_attempts = max_attempts

    def request_approval(self, task_id: str, action: str) -> None:
        if action not in IRREVERSIBLE_ACTIONS:
            raise ValueError(f"{action} does not require this approval workflow")
        self.store.update(task_id, "awaiting_approval", "requested")
        self.store.event(task_id, f"approval_requested:{action}")

    def approve(self, task_id: str) -> None:
        task = self.store.get(task_id)
        if task["status"] != "awaiting_approval":
            raise ValueError("No approval is pending")
        self.store.update(task_id, "approved", "approved")
        self.store.event(task_id, "approved_by_human")

    def run_action(self, task_id: str, action: str, operation: Callable[[], str]) -> str:
        task = self.store.get(task_id)
        if action in IRREVERSIBLE_ACTIONS and task["approval"] != "approved":
            self.store.event(task_id, f"blocked_without_approval:{action}")
            raise PermissionError("Human approval is required before this irreversible action")
        for attempt in range(1, self.max_attempts + 1):
            try:
                result = operation()
                self.store.update(task_id, "completed")
                self.store.event(task_id, f"completed_on_attempt:{attempt}")
                return result
            except RuntimeError as error:
                self.store.event(task_id, f"failed_attempt:{attempt}:{error}")
        self.store.update(task_id, "escalated")
        self.store.event(task_id, "escalated_after_bounded_retries")
        raise RuntimeError("Operation failed repeatedly; escalated for human review")
