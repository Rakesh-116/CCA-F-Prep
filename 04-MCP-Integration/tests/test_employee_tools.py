import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "server"))

from employee_server import get_employee_details, get_leave_balance, leave_policy, prepare_leave_summary


class EmployeeToolTests(unittest.TestCase):
    def test_employee_details_uses_mock_data(self) -> None:
        result = get_employee_details("emp-101")
        self.assertEqual(result["name"], "Asha Rao")
        self.assertEqual(result["data_source"], "mock")

    def test_leave_balance_is_read_only_mock_data(self) -> None:
        result = get_leave_balance("EMP-102")
        self.assertEqual(result["annual_days"], 4)

    def test_invalid_id_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            get_employee_details("101")

    def test_resource_and_prompt_are_available_as_functions(self) -> None:
        self.assertIn("tracked separately", leave_policy())
        self.assertIn("EMP-101", prepare_leave_summary("EMP-101"))
