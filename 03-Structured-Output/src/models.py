"""Application-level validation models.

The model schema is intentionally separate from the model provider. Structured
output reduces malformed JSON, while this layer protects downstream systems.
"""

from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Evidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    field_name: str
    excerpt: str = Field(min_length=1)
    location: str = Field(description="For example: page 1, or input text")


class InvoiceExtraction(BaseModel):
    model_config = ConfigDict(extra="forbid")

    document_type: Literal["invoice", "purchase_order", "unknown"]
    invoice_number: str | None = None
    vendor_name: str | None = None
    currency: str | None = Field(default=None, pattern=r"^[A-Z]{3}$")
    total_amount: Decimal | None = Field(default=None, ge=0)
    due_date: str | None = Field(default=None, description="ISO-8601 date when explicitly present")
    evidence: list[Evidence]
    uncertainties: list[str] = Field(default_factory=list)
