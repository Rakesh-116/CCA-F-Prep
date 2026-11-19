import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from extraction_pipeline import ExtractionPipeline, SequenceMockProvider


VALID_INVOICE = json.dumps({
    "document_type": "invoice",
    "invoice_number": "INV-1042",
    "vendor_name": "Northwind Office Supplies",
    "currency": "USD",
    "total_amount": "1250.00",
    "due_date": "2026-12-15",
    "evidence": [{"field_name": "invoice_number", "excerpt": "Invoice number: INV-1042", "location": "input text"}],
    "uncertainties": []
})


class ExtractionPipelineTests(unittest.TestCase):
    def test_valid_response_is_parsed_and_logged(self) -> None:
        result = ExtractionPipeline(SequenceMockProvider([VALID_INVOICE])).extract("invoice text")
        self.assertEqual(result.extraction.invoice_number, "INV-1042")
        self.assertTrue(result.attempts[0].valid)

    def test_invalid_then_valid_response_retries(self) -> None:
        invalid = '{"document_type": "invoice", "currency": "dollars"}'
        result = ExtractionPipeline(SequenceMockProvider([invalid, VALID_INVOICE]), max_attempts=2).extract("invoice text")
        self.assertIsNotNone(result.extraction)
        self.assertFalse(result.attempts[0].valid)
        self.assertTrue(result.attempts[1].valid)

    def test_failure_is_structured_after_bounded_retries(self) -> None:
        result = ExtractionPipeline(SequenceMockProvider(["not json", "also not json"]), max_attempts=2).extract("invoice text")
        self.assertIsNone(result.extraction)
        self.assertEqual(len(result.attempts), 2)
        self.assertIn("bounded retries", result.error)
