"""Local, mock-data MCP server for learning the host-client-server flow."""

from mcp.server import MCPServer

from mock_data import EMPLOYEES, LEAVE_POLICY

mcp = MCPServer(
    "mock-employee-assistant",
    instructions="Use employee tools only for mock data. Never claim a leave balance has been changed.",
)


def _employee_or_error(employee_id: str) -> dict:
    normalized = employee_id.strip().upper()
    if not normalized.startswith("EMP-"):
        raise ValueError("employee_id must use the format EMP-###")
    employee = EMPLOYEES.get(normalized)
    if employee is None:
        raise ValueError(f"No mock employee exists with id {normalized}")
    return employee


@mcp.tool()
def get_employee_details(employee_id: str) -> dict:
    """Look up non-sensitive mock employee details using an employee ID."""
    employee = _employee_or_error(employee_id)
    return {
        "employee_id": employee["employee_id"],
        "name": employee["name"],
        "department": employee["department"],
        "data_source": "mock",
    }


@mcp.tool()
def get_leave_balance(employee_id: str) -> dict:
    """Look up mock annual and sick leave balances; this is read-only."""
    employee = _employee_or_error(employee_id)
    return {"employee_id": employee["employee_id"], **employee["leave_balance"], "data_source": "mock"}


@mcp.resource("policy://leave")
def leave_policy() -> str:
    """Read the mock leave policy."""
    return LEAVE_POLICY


@mcp.prompt()
def prepare_leave_summary(employee_id: str) -> str:
    """Create a reusable workflow for a read-only leave summary."""
    return (
        f"Prepare a concise leave summary for {employee_id}. Call get_leave_balance first, "
        "read policy://leave if policy context is needed, state that results are mock data, "
        "and do not claim to approve or modify leave."
    )


if __name__ == "__main__":
    mcp.run()
