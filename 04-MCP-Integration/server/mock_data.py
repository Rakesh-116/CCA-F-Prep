EMPLOYEES = {
    "EMP-101": {
        "employee_id": "EMP-101",
        "name": "Asha Rao",
        "department": "Engineering",
        "manager_id": "EMP-001",
        "leave_balance": {"annual_days": 12, "sick_days": 7},
    },
    "EMP-102": {
        "employee_id": "EMP-102",
        "name": "Daniel Kim",
        "department": "Operations",
        "manager_id": "EMP-001",
        "leave_balance": {"annual_days": 4, "sick_days": 10},
    },
}

LEAVE_POLICY = """# Mock Leave Policy

Annual leave and sick leave are tracked separately. Balances are informational;
only the HR system can approve or alter a leave request.
"""
